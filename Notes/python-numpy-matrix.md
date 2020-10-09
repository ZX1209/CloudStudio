# 构造
## arange+reshape

## linspace+resize

## 常用
np.ones((3, 2))
np.zeros((2, 3))
np.eye(3)#3维单位矩阵
y = np.array([4, 5, 6])
np.diag(y)#以y为主对角线创建矩阵
np.random.randint(0, 10, (4,3))

## resiz reshape
    reshape：有返回值，所谓有返回值，即不对原始多维数组进行修改；
    resize：无返回值，所谓有返回值，即会对原始多维数组进行修改；


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