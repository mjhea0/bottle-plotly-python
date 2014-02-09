# Developing with Bottle - part 2 (plot.ly API)

**Updated on 02/08/2014!**

In this next post in the *Developing with Bottle* series, we'll be looking at both GET and POST requests as well as HTML forms. I'll also show you how to consume data from the [plot.ly](https://plot.ly/api) API. You'll also get to see how to create a cool graph showing the results of a cohort analysis study. (Click [here](http://mherman.org/blog/2012/11/16/the-benefits-of-performing-a-cohort-analysis-in-determining-engagement-over-time/) if you are unfamiliar with cohort analysis.)

> Did you miss the first part? Check it out here [here](http://www.realpython.com/blog/python/developing-with-bottle-part-1/).

## Basic Setup

1. Start by downloading this [Gist](https://gist.github.com/mjhea0/5784132) from Part 1, and then run it using the following command:
  ```sh
  $ bash bottle.sh
  ```

  This will create a basic project structure:

  ```sh
  ├── app.py
  ├── requirements.txt
  └── testenv
  ```
    
2. Activate the virtualenv:
  ```sh
  $ cd bottle
  $ source testenv/bin/activate
  ```
    
3. Install the requirements:
  ```sh
  $ pip install -r requirements.txt
  ```
       
4. Navigate to [https://www.plot.ly/api](https://www.plot.ly/api), sign up for a new account, sign in, and then create a new API key:

  ![plotly_api](https://raw.github.com/mjhea0/bottle-plotly-python/master/images/plotly.png)

  Copy that key.
    
5. Install plot.ly:
  ```sh
  $ pip install plotly
  ```
 
6. Next update the code in *app.py*:
  ```python
  import os
  from bottle import run, template, get, post, request
  from plotly import plotly

  # add your username and api key
  py = plotly("realpython", "5q9mp6exnd")

  @get('/plot')
  def form():
      return '''<h2>Graph via Plot.ly</h2>
                <form method="POST" action="/plot">
                  Name: <input name="name1" type="text" />
                  Age: <input name="age1" type="text" /><br/>
                  Name: <input name="name2" type="text" />
                  Age: <input name="age2" type="text" /><br/>
                  Name: <input name="name3" type="text" />
                  Age: <input name="age3" type="text" /><br/>                
                  <input type="submit" />
                </form>'''

  @post('/plot')
  def submit():
      name1   = request.forms.get('name1')
      age1    = request.forms.get('age1')
      name2   = request.forms.get('name2')
      age2    = request.forms.get('age2')
      name3   = request.forms.get('name3')
      age3    = request.forms.get('age3')

      x0 = [name1, name2, name3];
      y0 = [age1, age2, age3];
      data = {'x': x0, 'y': y0, 'type': 'bar'}
      response = py.plot([data])
      url = response['url']
      filename = response['filename']
      return template('<h1>Congrats!</h1><div>View your graph here: \
          <a href="{{url}}"</a>{{url}}</div>', url=url)

  if __name__ == '__main__':
      port = int(os.environ.get('PORT', 8080))
      run(host='0.0.0.0', port=port, debug=True)
  ```
    
  ### What's going on here?

  The first function, `form()`, creates an HTML form for capturing the data we need to make a simple bar graph. Meanwhile, the second function, `submit()`, grabs the form inputs, assigns them to variables, then calls the plot.ly (passing our credentials as well as the data) API to generate a new chart. *Make sure you replace my username and API key with your own credentials. DO NOT use mine. It will not work.*
    
7. Run your app locally, `python app.py`, and point your browser to [http://localhost:8080/plot](http://localhost:8080/plot).

8. Enter the names of three people and their respective ages. Press submit, and  then if all is well you should see a congrats message and a URL. Click the URL to view your graph:

    ![ages](https://raw.github.com/mjhea0/bottle-plotly-python/master/images/ages.png)
    
## Cohort Analysis

Next, let's a more complicated graph to create a graph for the following cohort analysis stats:
 
    Cohort | 2011 | 2012 | 2013 | 2014
    ------ | ---- | ---- | ---- | ----
       0   |  310 |  348 | 228  | 250 
       1   |  55  |  157 | 73   | 105
       2   |  18  |  37  | 33   |  34
       3   |  2   |  4   | 4    |  3
    




## Conclusion

See you next time!
 

   
