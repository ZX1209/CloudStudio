```py
x:int = 1
y: float = 1.0
z: bool = True
a: str = "test"
s: bytes = b'test'

child: bool
if age<18:
    child = True
else:
    child = False


```


copyed from   https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#d290117e243



## Legacy type syntax for docstrings

PyCharm supports legacy approach to specifying types in Python using docstrings. So doing, the supported formats are:

- [reStructuredText](http://docutils.sourceforge.net/rst.html)
- [epytext](http://folk.uio.no/inf3330/scripting/doc/python/epydoc/epytext.html)
- [NumPy](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_numpy.html)
- [Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html)

To choose the desired docstring format, use the [Python Integrated Tools](https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html) page of the Settings/Preferences dialog.

Type syntax in Python docstrings is not defined by any standard. Thus, PyCharm suggests the following notation:

| Syntax                      | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| `Foo`                       | Class Foo visible in the current scope                |
| `x.y.Bar`                   | Class Bar from x.y module                             |
| `Foo | Bar`                 | Foo or Bar                                            |
| `(Foo, Bar)`                | Tuple of Foo and Bar                                  |
| `list[Foo]`                 | List of Foo elements                                  |
| `dict[Foo, Bar]`            | Dict from Foo to Bar                                  |
| `T`                         | Generic type (T-Z are reserved for generics)          |
| `T <= Foo`                  | Generic type with upper bound Foo                     |
| `Foo[T]`                    | Foo parameterized with T                              |
| `(Foo, Bar) -> Baz`         | Function of Foo and Bar that returns Baz              |
| `list[dict[str, datetime]]` | List of dicts from str to datetime (nested arguments) |