```python
import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  fire.Fire(hello) # 暴露一个函数或对象
```
>https://github.com/google/python-fire/blob/master/docs/guide.md
>https://blog.csdn.net/qq_17550379/article/details/79943740

# auto help message
command -- --help

# command arguments
--title="this is title"
'"str"'
'{"key":"val"}'
copyed from https://github.com/google/python-fire

 
# 构造参数
```py3
import fire

class BrokenCalculator(object):

  def __init__(self, offset=1):
      self._offset = offset

  def add(self, x, y):
    return x + y + self._offset

  def multiply(self, x, y):
    return x * y + self._offset

if __name__ == '__main__':
  fire.Fire(BrokenCalculator)

# 当你使用BrokenCalculator时，你会得到错误的答案：

# $ python example.py add 10 20
# 31
# $ python example.py multiply 10 20
# 201

# 但你可以这样解决它：

# $ python example.py add 10 20 --offset=0
# 30
# $ python example.py multiply 10 20 --offset=0
# 200
```