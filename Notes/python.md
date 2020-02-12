# virtual shebangs
```
#!/usr/bin/env python3
```





# 顺时针旋转矩阵
zip( * matrix)

# python format string
f"statistics and {variable}"


# 显示数据的hex格式?
see python-struct.md


# todo 在数组中绘制图像
cairo
cv2
gen points
https://stackoverflow.com/questions/10031580/how-to-write-simple-geometric-shapes-into-numpy-arrays


# 闭包函数 closure
函数外自由变量,非全局
```py
def print_msg():
    # print_msg 是外围函数
    msg = "zen of python"
    def printer():
        # printer 是嵌套函数
        print(msg)
    return printer

another = print_msg()
# 输出 zen of python
another()
```
在计算机科学中，闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。

# timeit
python3.6 -m timeit "import typing"

<!-- todo: clean this to a index -->
# 时间日期
datetime

# python

> Python language interpreter.

- Call a Python interactive shell (REPL):

`python`

- Execute script in a given Python file:

`python {{script.py}}`

- Execute Python language single command:

`python -c {{command}}`

- Run library module as a script (terminates option list):

`python -m {{module}} {{arguments}}`


# 传递任意数量参数

# context management
```py
from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


@contextmanager #这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
上述代码执行结果为：

<h1>
hello
world
</h1>
```


# 函数内改变全局变量
加上 global 修饰

在生成器表达式中, in 子句在声明时执行, 而条件子句则是在运行时执行

https://github.com/leisurelicht/wtfpython-cn

# exec
动态执行python语法

# sort
sorted(s,key=lambda x:100 * x[1]-x[0])
This idiom works because tuples are compared lexicographically; the first items are compared; if they are the same then the second items are compared, and so on.

# [4:8] 可以超越长度 (应该做了处理呢.)

# 列表生成式
```python
for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]

# 注意，这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样
```
# pythonpath
Python搜索模块的路径：
1)、程序的主目录
2)、PTYHONPATH目录（如果已经进行了设置）
3)、标准连接库目录（一般在/usr/local/lib/python2.X/）
4)、任何的.pth文件的内容（如果存在的话）.新功能，允许用户把有效果的目录添加到模块搜索路径中去
.pth后缀的文本文件中一行一行的地列出目录。
这四个组建组合起来就变成了sys.path了，

>>> import sys
>>> sys.path
导入时，Python会自动由左到右搜索这个列表中每个目录。

模块路径
系统变量
# 设置python 导入模块的用户目录
```bash
export  PYTHONPATH=~/CloudStudio/bin
```

# decoding problem
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <= | not =<

# command line
# 交互式载入
python -i <file>

# 使用模块
python -m <model_name>

# byte code
bytes(str,encoding='utf-8')
str.decode('utf-8')

# // 整除符号

# 限制反转
# 这样可能不是高效的,,但是,,思维模型上比较好
n = 137
bin(n)[-1:1:-1]
===
变量作用域（scope）在Python中是一个容易掉坑的地方。
Python的作用域一共有4中，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

Python除了def/class/lambda 外，其他如: if/elif/else/ try/except for/while并不能改变其作用域。定义在他们之内的变量，外部还是可以访问。
===

# str to list
list & sorted

# chr() & ord()

# all() & any()

# getattr() 通过字符串获取对象..

# exec() & eval()
compile()

# if elif ... else

#int & format
int('00100',2)


```python
s = "0123456789"

# [1,3) like range
s[1:3]Z
```

```python
a = sets[0]
b= sets[0]
a is b
# 注意,不要用,很麻烦

p += 1
# 直接修改了p的引用的内容

p = p + 1
# 改变了p的引用
```

## sorted
```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
# 升序
```

