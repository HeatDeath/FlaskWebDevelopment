from flask.ext.script import Manager
from flask import Flask
app=Flask(__name__)
manager=Manager(app)

@app.route('/')
def index():
    return '<h1> Hello world!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>'% name

if __name__=='__main__':
    manager.run()

'''
usage: 2.6Flask扩展.py [-?] {runserver,shell} ...

positional arguments:
  {runserver,shell}
    runserver        运行Flask开发服务器：app.run()
    shell            在Flask应用上下文中运行Python shell

optional arguments:
  -?, --help         show this help message and exit




  
'''
