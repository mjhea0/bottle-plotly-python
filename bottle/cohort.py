import os
from bottle import run, template, get, post, request
from plotly import plotly
 
# add your username and api key
py = plotly("realpython", "5q9mp6exnd")
 
@get('/plot')
def form():
    return '''<h2>Graph via Plot.ly</h2>
              <form method="POST" action="/plot">
              <table>
                <tr>
                <td>
                <h3><center>Year 1</center></h3>
                Cohort 0: <input name="Y01" type="number"/><br/>
                Cohort 1: <input name="Y02" type="number"/><br/>
                Cohort 2: <input name="Y03" type="number"/><br/>
                Cohort 3: <input name="Y04" type="number"/><br/>
                </td>
                <td>
                <h3>Year 2</h3>                
                <input name="Y11" type="number"/><br/>
                <input name="Y12" type="number"/><br/>
                <input name="Y13" type="number"/><br/>
                <input name="Y14" type="number"/><br/>
                </td> 
                <td>
                <h3>Year 3</h3>                
                <input name="Y21" type="number"/><br/>
                <input name="Y22" type="number"/><br/>
                <input name="Y23" type="number"/><br/>
                <input name="Y24" type="number"/><br/>
                </td>
                <td>
                <h3>Year 4</h3>                
                <input name="Y31" type="number"/><br/>
                <input name="Y32" type="number"/><br/>
                <input name="Y33" type="number"/><br/>
                <input name="Y34" type="number"/><br/>
                </td>
                <td>
                </td>  
                </tr>
              </table>  
               <input type="submit"/>                        
              </form>'''
 
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
    response = py.plot(x0, y0, x1, y1, x2, y2, x3, y3)
    url = response['url']
    filename = response['filename']
    return template('<h1>Congrats!</h1><div>View your chart here: \
        <a href="{{url}}">{{url}}</a>!</div>', url=url)
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
