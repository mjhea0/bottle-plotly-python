import os
from bottle import run, template, get, post, request, \
    route, run, static_file, template, view 
from plotly import plotly
import json

# grab username and key from config/data file
with open('data.json') as config_file:    
    config_data = json.load(config_file)
username = config_data["user"]
key = config_data["key"]

py = plotly(username, key)
 
@get('/plot')
def form():
    return template('starter', title='Plot.ly Graph')
 
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
    return template('starter', title='Plot.ly Graph', content=url)
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
