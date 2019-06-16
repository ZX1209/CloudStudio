# 获取开始时间 epoch
time.gmtime(0)

# 获取秒数
time.time()

# 获取当地时间 str
```py
from time import time, ctime
t = time()
ctime(t)
'Mon Feb 25 19:11:59 2019'
```

# 闲置
time.sleep()
