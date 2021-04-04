```python
from string import Template
s = Template('$who likes $what')
s.substitute(who='tim', what='kung pao')
s.safe_substitute(who='tim', what='kung pao')
```