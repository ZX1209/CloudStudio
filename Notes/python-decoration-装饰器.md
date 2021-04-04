```py
# 简
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw): # 相当于最终替换的函数
        print('start execute')
        func(*args, **kw)
        print('end execute')
    return wrapper


# 详
def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if arg and isinstance(arg, str):
                print('装饰器的参数：%s' % arg)
            print('start execute')
            func(*args, **kw)
            print('end execute')
        return wrapper
    if callable(arg):
        return decorator(arg)
    # TODO: 处理 arg
    return decorator

```
























##  返回函数的函数

再定义一个函数用来打印日志，并在其中执行原函数：

```python
def log(func):
    def wrapper():
        print('start execute')
        func()
        print('end execute')
    return wrapper


def time_ruler(func):
    import time
    def wrapper(*args,**kw):
        start = time.time()
        func(*args,**kw)
        print('run time is :',time.time()-start)
    return wrapper

# ipython %%time

```
顾顾
可以看到，`log`函数接收一个函数作为参数，并返回一个新的`wrapper`函数。

copyed from  https://www.jianshu.com/p/f51dbe1eaa4d

### 一、理解装饰器

通俗点说，当我们想给一个函数增强额外的功能，但又不想修改原函数的定义，同时新增的功能其它函数可能也需要使用，**装饰器**就是来解决这种需求的，将与原函数功能无关的代码提取出来，实现复用，在代码运行期间动态的给原函数增加功能，例如在函数执行前后插入日志、计算函数的执行时间等等

### 二、实践

#### 1、一个小需求

有一个需求，要在函数执行前后打印`start execute`、`end execute`，如果我们还不知道有装饰器存在可以怎么做呢？

首先定义原函数：

```
def my_func():
    print('Hello World')
```

再定义一个函数用来打印日志，并在其中执行原函数：

```python
def log(func):
    def wrapper():
        print('start execute')
        func()
        print('end execute')
    return wrapper
```

可以看到，`log`函数接收一个函数作为参数，并返回一个新的`wrapper`函数。

最后看执行结果：

```
my_func = log(my_func)
my_func()
```

![img](//upload-images.jianshu.io/upload_images/1633070-aef573dd9a949453.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/228)

0

我们将`my_func`函数作为参数传给`log`函数，并将返回的`wrapper`函数赋值给`my_func`变量，则`my_func`变量就是返回的`wrapper`函数，并不是之前定义的`my_func`函数，最后执行`my_func()`其实执行的是返回的`wrapper`函数。到这里已经实现了前边的小需求，其实装饰器的原理亦是如此。

#### 2、使用装饰器

如果使用装饰器怎么写呢？先不需要修改`log`函数，只对`my_func`函数做修改：

```
@log
def my_func():
    print('Hello World')
```

很明显吧，用Python的 **@** 语法实现装饰器，实现`log`函数对`my_func`函数的装饰。

再看执行结果：



![img](//upload-images.jianshu.io/upload_images/1633070-53302fdc8919e6a5.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/130)

1

其实装饰器相当于替我们执行了`my_func = log(my_func)`这一步。
 但是有个问题，按理`my_func`函数的`__name__`属性应该是`my_func`，但使用装饰器后变成了`wrapper`：

![img](//upload-images.jianshu.io/upload_images/1633070-803f7c218dcbc3be.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/173)

2

其实就是前边讲的赋值操作`my_func = log(my_func)`导致的，这当然不是我们想看到的，可以用Python内置`functools`模块的`wraps()`方法，修改我们的`log`函数：

```
def log(func):
    @functools.wraps(func)
    def wrapper():
        print('start execute')
        func()
        print('end execute')
    return wrapper
```

再执行结果：



![img](//upload-images.jianshu.io/upload_images/1633070-505178189cfd0ff4.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/190)

3

#### 3、带参数的被装饰函数

如果`my_func`函数有参数呢？像这样：

```
def my_func(a, b):
    print('a+b=%d' % (a + b))
```

当然还要修改`log`函数，怎么改呢，这样？？？给`wrapper`加两个参数？？？

```
def log(func):
    @functools.wraps(func)
    def wrapper(a, b):
        print('start execute')
        func(a, b)
        print('end execute')
    return wrapper
```

如果其它函数的参数个数、参数形式和`my_func`不同，也想使用`log`作为装饰器，那这样修改`log`肯定不行......，可以这样，让装饰器内嵌的`wrapper`函数支持可变参数以及关键字参数：

```
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('start execute')
        func(*args, **kw)
        print('end execute')
    return wrapper
```

这样其它函数也就能共用这个`log`函数了，要不然还搞啥装饰器。现在使用修改后的`log`函数：

```
@log
def my_func(a, b):
    print('a+b=%d' % (a + b))
```

再来一个`my_func1`函数：

```
@log
def my_func1(a, b, c, *, d):
    print('a+b+c+d=%d' % (a + b + c + d))
```

看下执行结果：



![img](//upload-images.jianshu.io/upload_images/1633070-62238e8196d81fb8.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/227)

4

以`my_func`为例，这时候使用装饰器执行`my_func(1, 2)`相当于执行了`log(my_func)(1, 2)`。

#### 4、带参数的装饰器函数

如果装饰器函数本身也需要参数呢？继续以`log`函数为例，现在需要接受一个字符串为参数，并在被装饰函数执行前打印，则可以给它在内嵌一层函数：

```
def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('装饰器的参数：%s' % arg)
            print('start execute')
            func(*args, **kw)
            print('end execute')
        return wrapper
    return decorator
```

这时再给`my_func`添加装饰器：

```
@log('Hello World')
def my_func(a, b):
    print('a+b=%d' % (a + b))
```

执行结果如下：



![img](//upload-images.jianshu.io/upload_images/1633070-ad1bf6edf02b680f.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/217)

5

此时相当于执行了`log('Hello World')(my_func)(1, 2)`

#### 5、参数可选的装饰器函数

我们继续扩展装饰器函数`log`的功能，使其既支持：

```
@log('Hello World')
def my_func(a, b):
    print('a+b=%d' % (a + b))
```

又要支持：

```
@log
def my_func(a, b):
    print('a+b=%d' % (a + b))
```

即参数可选，怎么修改呢？前边已经说过了，第一种情况执行`my_func(1, 2)`相当于`log('Hello World')(my_func)(1, 2)`，其中`log('Hello World')`先执行，返回接受`my_func`为参数的`decorator`函数，第二种情况执行相当于`log(my_func)(1, 2)`，其中`log(my_func)`先执行，返回的是接受`1、2`为参数的`wrapper`函数。所以我们让`log`函数在两种情况下分别返回不同的函数，即`log`函数的参数为函数时其返回`wrapper`函数，即`decorator(arg)`，`log`函数的参数为字符串时让其返回`decorator`函数，至于打印`log`的字符串参数，只需要判参数是字符串再打印即可：

```
def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if arg and isinstance(arg, str):
                print('装饰器的参数：%s' % arg)
            print('start execute')
            func(*args, **kw)
            print('end execute')
        return wrapper
    if callable(arg):
        return decorator(arg)
    return decorator
```

> 1、isinstance(arg, str)：判断arg是否为str类型
>  2、callable(arg)：判断arg是否可被调用，可被调用指的是能否使用()括号的方法调用。

测试结果如下：









