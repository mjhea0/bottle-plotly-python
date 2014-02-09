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

We'll be building off of *app.py*. Open the file and "Save As" *cohort.py*.
   
1. Start by upgrading to the [Simple Template Engine](http://bottlepy.org/docs/dev/stpl.html), so we can add styles and Javascript files to our templates. Add a new folder called "views" then create a new file in that directory called *template.tpl*. Add the following code to that file:
  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>{{ title }}</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
      <style>
        body {
          padding: 60px 0px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Graph via Plot.ly</h1>
        <form role="form" method="post" action="/plot">
          <table>
              <td>
                <h3>2011</h3>
                <div class="form-group" "col-md-2">
                  <input type="number" name="Y01" class="form-control">
                  <input type="number" name="Y02" class="form-control">
                  <input type="number" name="Y03" class="form-control">
                  <input type="number" name="Y04" class="form-control">
                </div>
              </td>
              <td>
                <h3>2012</h3>
                <div class="form-group" "col-md-2">
                  <input type="number" name="Y11" class="form-control">
                  <input type="number" name="Y12" class="form-control">
                  <input type="number" name="Y13" class="form-control">
                  <input type="number" name="Y44" class="form-control">
                </div>
              </td>
              <td>
                <h3>2013</h3>
                <div class="form-group" "col-md-2">
                  <input type="number" name="Y21" class="form-control">
                  <input type="number" name="Y22" class="form-control">
                  <input type="number" name="Y23" class="form-control">
                  <input type="number" name="Y24" class="form-control">
                </div>
              </td>
              <td>
                <h3>2014</h3>
                <div class="form-group" "col-md-2">
                  <input type="number" name="Y31" class="form-control">
                  <input type="number" name="Y32" class="form-control">
                  <input type="number" name="Y33" class="form-control">
                  <input type="number" name="Y34" class="form-control">
                </div>
              </td>
            </tr>
          </table>
          <button type="submit" class="btn btn-default">Submit</button>
        </form>
        <br>
        <iframe id="igraph" src="" width="900" height="450" seamless="seamless" scrolling="no"></iframe>
      </div>
      <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
    </body>
  </html>
  ```

  As you can probably tell, this looks just like an HTML file. The difference is that we can pass Python variables to the file using the syntax - `{{ python_variable }}`. Also, did you notice the iframe? This will allow us to update the form then display the actual content/chart, with the update changes, below. Now, we do not have to leave the site to view the graph.

2. Update the imports:
  ```python
  import os
  from bottle import run, template, get, post, request, \
      route, run, static_file, template, view 
  from plotly import plotly
  import json
  ```

3. Create a *data.json* file and add your Plot.ly username and API key. You can view the sample file [here](https://github.com/mjhea0/bottle-plotly-python/blob/master/bottle/data_sample.json).

4. Add the following code to access the *data.json* file in order to add the values to make the API call:
  ```python
  # grab username and key from config/data file
  with open('data.json') as config_file:    
      config_data = json.load(config_file)
  username = config_data["user"]
  key = config_data["key"]

  py = plotly(username, key)
  ```

5. Next update the functions:
  ```python
  @get('/plot')
  def form():
      return template('template', title='Plot.ly Graph')
   
  @post('/plot')
  def submit():
      Y01 = request.forms.get('Y01')
      Y02 = request.forms.get('Y02')
      Y03 = request.forms.get('Y03')
      Y04 = request.forms.get('Y04')
   
      Y11 = request.forms.get('Y11')
      Y12 = request.forms.get('Y12')
      Y13 = request.forms.get('Y13')
      Y14 = request.forms.get('Y14')
   
      Y21 = request.forms.get('Y21')
      Y22 = request.forms.get('Y22')
      Y23 = request.forms.get('Y23')
      Y24 = request.forms.get('Y24')
   
      Y31 = request.forms.get('Y31')
      Y32 = request.forms.get('Y32')
      Y33 = request.forms.get('Y33')
      Y34 = request.forms.get('Y34')
   
      x0 = [1,2,3,4]; y0 = [Y01,Y02,Y03,Y04]
      x1 = [1,2,3,4]; y1 = [Y11,Y12,Y13,Y14] 
      x2 = [1,2,3,4]; y2 = [Y21,Y22,Y23,Y24]
      x3 = [1,2,3,4]; y3 = [Y31,Y32,Y33,Y34]
      response = py.plot(x0, y0, x1, y1, x2, y2, x3, y3, filename='same plot', fileopt='overwrite')
      url = response['url']
      filename = response['filename']
      return template('template', title='Plot.ly Graph')
  ```

  Notice the `return` statment. We're passing in the name of the template, plus any variables. Go back to the actual template. See how the variables match up.

  Also, take a look at the updated API call - `response = py.plot(x0, y0, x1, y1, x2, y2, x3, y3, filename='same plot', fileopt='overwrite')`. You can read more about what this call does [here](https://plot.ly/api/python/docs/add-append-extend).

6. Run it. Add values to the form. Just enter dummy data for now (all '1s' for example). Then submit. Navigate to [https://plot.ly/plot](https://plot.ly/plot). Grab the url of the latest graph. The name will be "same plot". Paste that URL into the template:
  ```html
  <iframe id="igraph" src="https://plot.ly/~realpython/19" width="900" height="450" seamless="seamless" scrolling="no"></iframe>
  ```

7. Kill the server. Fire it back up. Navigate to [http://localhost:8080/plot](http://localhost:8080/plot) and you should see the graph.

8. Now enter the real data. Submit. Your graph should now look like this:

  ![final](https://raw.github.com/mjhea0/bottle-plotly-python/master/images/final.png)

## Conclusion

Grab all the files from this [repo](https://github.com/mjhea0/bottle-plotly-python).

See you next time!
 

   
