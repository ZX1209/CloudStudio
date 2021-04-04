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

# about arguments type
Argument Parsing
The types of the arguments are determined by their values, rather than by the function signature where they're used. You can pass any Python literal from the command line: numbers, strings, tuples, lists, dictionaries, (sets are only supported in some versions of Python). You can also nest the collections arbitrarily as long as they only contain literals.

To demonstrate this, we'll make a small example program that tells us the type of any argument we give it:

import fire
fire.Fire(lambda obj: type(obj).__name__)
And we'll use it like so:

$ python example.py 10
int
$ python example.py 10.0
float
$ python example.py hello
str
$ python example.py '(1,2)'
tuple
$ python example.py [1,2]
list
$ python example.py True
bool
$ python example.py {name: David}
dict
You'll notice in that last example that bare-words are automatically replaced with strings.

Be careful with your quotes! If you want to pass the string "10", rather than the int 10, you'll need to either escape or quote your quotes. Otherwise Bash will eat your quotes and pass an unquoted 10 to your Python program, where Fire will interpret it as a number.

$ python example.py 10
int
$ python example.py "10"
int
$ python example.py '"10"'
str
$ python example.py "'10'"
str
$ python example.py \"10\"
str
Be careful with your quotes! Remember that Bash processes your arguments first, and then Fire parses the result of that. If you wanted to pass the dict {"name": "David Bieber"} to your program, you might try this:

$ python example.py '{"name": "David Bieber"}'  # Good! Do this.
dict
$ python example.py {"name":'"David Bieber"'}  # Okay.
dict
$ python example.py {"name":"David Bieber"}  # Wrong. This is parsed as a string.
str
$ python example.py {"name": "David Bieber"}  # Wrong. This isn't even treated as a single argument.
<error>
$ python example.py '{"name": "Justin Bieber"}'  # Wrong. This is not the Bieber you're looking for. (The syntax is fine though :))
dict
Boolean Arguments
The tokens True and False are parsed as boolean values.

You may also specify booleans via flag syntax --name and --noname, which set name to True and False respectively.

Continuing the previous example, we could run any of the following:

$ python example.py --obj=True
bool
$ python example.py --obj=False
bool
$ python example.py --obj
bool
$ python example.py --noobj
bool
Be careful with boolean flags! If a token other than another flag immediately follows a flag that's supposed to be a boolean, the flag will take on the value of the token rather than the boolean value. You can resolve this: by putting a separator after your last flag, by explicitly stating the value of the boolean flag (as in --obj=True), or by making sure there's another flag after any boolean flag argument.