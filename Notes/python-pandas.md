```py
import numpy as np
import pandas as pd

# 创建一列数据,默认索引为0~len
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# 用字典创建多列数据
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
    })
# 用numpy 数组创建
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min
# use matplotlib.pyplot to show,with index x,and cols y
df.plot()
```


