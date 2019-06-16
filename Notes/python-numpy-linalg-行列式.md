# numpy.linalg or scipy.linalg
# linalg是Linear Algebra的缩写

# 秩
matix_rank

# 矩阵 幂次 值
matrix_power

# 求值
det
```py
>>> arr = np.array([[3, 2],[6, 4]])
>>> linalg.det(arr)
0.0
```

# 求逆 invertor 倒置
inv
```py
>>> arr = np.array([[1, 2], [3, 4]])
>>> iarr = linalg.inv(arr)
>>> iarr
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
```

# 求模 norm 范数?
norm
```py
>>>A = np.matrix(np.random.random((2, 2)))
>>>A
>>>linalg.norm(A)
>>>linalg.norm(A, 1)
>>>linalg.norm(A, np.inf)
```

# 解线性方程组
solve
```py
# 比较速度
import numpy as np
from scipy import linalg

m, n = 500, 50
A = np.random.rand(m, m)
B = np.random.rand(m, n)
X1 = linalg.solve(A, B)
X2 = np.dot(linalg.inv(A), B)
print(np.allclose(X1, X2))
%timeit linalg.solve(A, B)
%timeit np.dot(linalg.inv(A), B)
```

# 特征值与特征向量 eigenvalues
eig
```py
>>> A = np.array([[1, -0.3], [-0.1, 0.9]])
>>> evalues, evectors = linalg.eig(A)
```