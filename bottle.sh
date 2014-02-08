mkdir bottle
cd bottle
 
pip install virtualenv
virtualenv --no-site-packages testenv
source testenv/bin/activate
 
pip install bottle
pip freeze > requirements.txt
 
git init
git add .
git commit -m "initial commit"
 
cat >app.py <<EOF
import os
from bottle import route, run, template
 
index_html = '''My first web app! By {{ author }}'''
 
@route('/:anything')
def something(anything=''):
   return template(index_html, author=anything)
 
@route('/')
def index():
   return template(index_html, author='your name here')
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
EOF
 
chmod a+x app.py
 
git init
git add .
git commit -m "Updated"
