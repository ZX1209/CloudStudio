#init virtual env
mkdir flaskdir
cd flaskdir
virtualenv venv

#active virtual env
. venv/bin/activate

#deactive vitual env
deactivate

#start flsak app
export FLASK_APP=explore.py
flask run --host=0.0.0.0

# dev mode (auto restart and load changed file)
export FALSK_ENV=development
export FLASK_DEBUG=1


# run on the internet rather locally
flask run --host=0.0.0.0


#run on python3 interpreter
app.run(debug=True,host='0.0.0.0',port='10001')


# 路由及变量
```python
# Converter types:

# string  (default) accepts any text without a slash
# int accepts positive integers
# float   accepts positive floating point values
# path    like string but also accepts slashes
# uuid    accepts UUID strings
@app.route('/user/<name>/<int:id>')
def some_func():
    pass

```

# 上下文
> current_app,g,request,session

# 请求钩子
before_first_request,before_request,after_request,teardown_request

# 响应
```python
@app.route('/')
def func():
    return "something",404 #[headers]?
```

# session
session['name'] = name
session.get('name')

# flask-moment



# 子域名
https://www.jianshu.com/p/1cfc3a7e5552