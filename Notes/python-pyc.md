# 生成单个pyc文件
对于py文件，可以执行下面命令来生成pyc文件。

python -m foo.py
另外一种方式是通过代码来生成pyc文件。

import py_compile
py_compile.compile('/path/to/foo.py')

# 批量生成pyc文件
针对一个目录下所有的py文件进行编译。python提供了一个模块叫compileall，具体请看下面代码：

import compileall
compileall.compile_dir(r'/path')
这个函数的格式如下：

compile_dir(dir[, maxlevels[, ddir[, force[, rx[, quiet]]]]])

命令行为：

python -m compileall <dir>