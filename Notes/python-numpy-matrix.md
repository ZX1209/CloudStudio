矩阵运算  |  array对象| matrix对象 |   备注
---|---|---|---|
转置 | A.T或A.transpose() |  C.T | 采用相同方式
求逆 | np.linalg.inv(A)   | C.I或C**-1 |
乘积 | np.dot（A,B）| C*D  | C和D均为矩阵|
共轭转置|--- | C.H
求迹 |  np.trace(A) | --- |


# mat utility
```py
In [50]: np.mat("4,3,1;1,-2,3")
Out[50]:
matrix([[ 4,  3,  1],
        [ 1, -2,  3]])
```


# 临时转化
np.mat()   


# 乘积
@
(python3.7)