import os
from bottle import run, template, get, post, request

import plotly.plotly as py
from plotly.graph_objs import *

# add your username and api key
py.sign_in(username, apiKey)


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
    # grab data from form
    name1 = request.forms.get('name1')
    age1 = request.forms.get('age1')
    name2 = request.forms.get('name2')
    age2 = request.forms.get('age2')
    name3 = request.forms.get('name3')
    age3 = request.forms.get('age3')

    data = Data([
        Bar(
            x=[name1, name2, name3],
            y=[age1, age2, age3]
        )
    ])

    # make api call
    response = py.plot(data, filename='basic-bar')

    if response:
        return template(
            '''<h1>Congrats!</h1>
            <div>
              View your graph here: <a href="{{response}}"</a>{{response}}
            </div>
            ''',
            response=response
        )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
