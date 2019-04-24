# dutc-rwatch

```python
import rwatch
from sys import getrwatch,setrwatch

def f(frame,obj):
    print("saw",obj,"in",frame)

x = 10

setrwatch({id(x):f})


x
```