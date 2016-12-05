#首先我们导入了 Flask 类。这个类的实例将会成为我们的 WSGI 应用
from flask import Flask

#所有Flask程序都必须创建一个程序实例。Web 服务器使用一种名为Web 服务器网关接口
#（Web Server Gateway Interface，WSGI）的协议，把接收自客户端的所有请求都转交给
#这个对象处理。程序实例是Flask 类的对象，
app=Flask(__name__)

#在Flask 程序中定义路由的最简便方式，是使用程序实例提供的app.route 修饰器，
#把修饰的函数注册为路由(习惯的用法是使用修饰器把函数注册为事件的处理程序)
@app.route('/')
#像index() 这样的函数称为视图函数（view function）。视图函数返回的响应可以是包含
#HTML 的简单字符串，也可以是复杂的表单
def index():
    return ('<h1>hello world<h1>')

#@app.route('/')
#def user(name):
#    return ('<h1>hello,%s!<h1>'%name)

#程序实例用run 方法启动Flask 集成的开发Web 服务器：
if __name__=='__main__':
    #运行服务器后，会发现只有你自己的电脑可以使用服务，
    #而网络中的其他电脑却不行。 缺省设置就是这样的，
    #因为在调试模式下该应用的用户可以执行你电脑中的任意 Python 代码。
    #app.run()

    #如果你关闭了 调试 或信任你网络中的用户，那么可以让服务器被公开访问。
    app.run(host='0.0.0.0')


#按 control-C 可以停止服务器。
