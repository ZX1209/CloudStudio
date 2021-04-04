```py
import yaml

yamlstr = """
this is something:
    _str: something
    a: a
    b: b
str: some
this is another key: [1,2,3,4]
"""

yamlo = yaml.load(yamlstr)

yamlo

yamlstr2 = """
anima:
    - 1
    - 2
    - 3
    - 4


something: what

"""
yamlo2 = yaml.load(yamlstr2)

yamlo2
```