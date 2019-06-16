# 图像混合?
```py
# Using the 'NOT' way
not_output = cv2.bitwise_not(images[i], not_output, mask=mask[i])
# Using the copyto way
np.copyto(copy_output, images[i], where=mask[i][:, :, None].astype(bool))
```

# np.copyto(dst,src,where=mask)
src to dst when cor mask is true


# np 会因为类型溢出
```python
o = np.random.randint(0,255,(5,5,3),dtype='uint8')
co = o+30 # 可能溢出呢..
```

# 线性代数 行列式
linalg是Linear Algebra的缩写
np.linalg
np.linalg.det()

# np.fill


# np.clip
d = np.clip(s,minv,maxv)

# np.hstack
将多个矩阵水平方向排列组合成一个

# nu.lookfor('create')

# ndarray[::2,[2,3,1],,]

# ndarray.reshape() & ndarray.ravel()

创建,
操作(加减乘除,)
矩阵运算

# numpy.array() & ndarray.tolist()


# np.cumsum
累计求和
numpy.cumsum(a, axis=None, dtype=None, out=None)

# ndarray attr
ndim, shape, size, dtype, itemsize, data

# shape
.shape = -1,2
# any cols 2 rows

# * & .dot()
* 各对应元素相乘

.dot() 内积.. 行 乘 列

# T
返回转置矩阵

# ufunc
all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

## np.sum()
轴上元素加,,元素形态一致,,可以加,,+
合并轴吧..加至1
```python
In [36]: test = np.ones((3,4,5))

In [37]: test
Out[37]:
array([[[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]]])

In [38]: np.sum(test)
Out[38]: 60.0

In [39]: np.sum(test,axis = 0)
Out[39]:
array([[3., 3., 3., 3., 3.],
       [3., 3., 3., 3., 3.],
       [3., 3., 3., 3., 3.],
       [3., 3., 3., 3., 3.]])

In [40]: a1 = np.sum(test,axis = 0)

In [41]: a2 = np.sum(a1,axis = 0)

In [42]: a2
Out[42]: array([12., 12., 12., 12., 12.])

In [43]: a3 = np.sum(a2,axis = 0)

In [44]: a3
Out[44]: 60.0
```

```python
import numpy as np

np.random.seed(324234)

np.random.randn(10)

np.random.random_sample((size))
```

# 创建 ndarray
```python
np.array([1,3,5,7,8])

np.zeros((3,4),dtype=np.int16)
np.ones((10,10))

# 值 随机..
np.empty((3,4))

# 可浮点数,但数量不保证
np.arange( 10, 30, 5 )

# 9 numbers from 0 to 2
np.linspace( 0, 2, 9 )

# 要禁用此行为并强制NumPy打印整个数组，你可以使用 set_printoptions 更改打印选项
np.set_printoptions(threshold=np.nan)

```

# 全元素迭代器
.flat

# 索引
ndarrayElement[:5,:2,...]   # 轴一 , 轴二

# 三角函数 逐元素
sin(),cos(),tan(),...

# 数学运算
方法  描述
add(x1, x2, /[, out, where, casting, order, …]) 按元素添加参数。
subtract(x1, x2, /[, out, where, casting, …])   从元素方面减去参数。
multiply(x1, x2, /[, out, where, casting, …])   按元素计算多个参数。     tips: 对应位置的元素相乘
divide(x1, x2, /[, out, where, casting, …]) 逐个元素方式返回输入的真正除法。
logaddexp(x1, x2, /[, out, where, casting, …])  输入的指数之和的对数。
logaddexp2(x1, x2, /[, out, where, casting, …]) 以-2为基的输入的指数和的对数。
true_divide(x1, x2, /[, out, where, …]) 以元素方式返回输入的真正除法。
floor_divide(x1, x2, /[, out, where, …])    返回小于或等于输入除法的最大整数。
negative(x, /[, out, where, casting, order, …]) 数字否定，元素方面。
positive(x, /[, out, where, casting, order, …]) 数字正面，元素方面。
power(x1, x2, /[, out, where, casting, …])  第一个数组元素从第二个数组提升到幂，逐个元素。
remainder(x1, x2, /[, out, where, casting, …])  返回除法元素的余数。
mod(x1, x2, /[, out, where, casting, order, …]) 返回除法元素的余数。
fmod(x1, x2, /[, out, where, casting, …])   返回除法的元素余数。
divmod(x1, x2[, out1, out2], / [[, out, …]) 同时返回逐元素的商和余数。
absolute(x, /[, out, where, casting, order, …]) 逐个元素地计算绝对值。
fabs(x, /[, out, where, casting, order, …]) 以元素方式计算绝对值。
rint(x, /[, out, where, casting, order, …]) 将数组的元素舍入为最接近的整数。
sign(x, /[, out, where, casting, order, …]) 返回数字符号的元素指示。
heaviside(x1, x2, /[, out, where, casting, …])  计算Heaviside阶跃函数。
conj(x, /[, out, where, casting, order, …]) 以元素方式返回复共轭。
exp(x, /[, out, where, casting, order, …])  计算输入数组中所有元素的指数。
exp2(x, /[, out, where, casting, order, …]) 计算输入数组中所有p的2**p。
log(x, /[, out, where, casting, order, …])  自然对数，元素方面。
log2(x, /[, out, where, casting, order, …]) x的基数为2的对数。
log10(x, /[, out, where, casting, order, …])    以元素方式返回输入数组的基数10对数。
expm1(x, /[, out, where, casting, order, …])    计算数组中所有元素的exp(x)-1。
log1p(x, /[, out, where, casting, order, …])    返回一个加上输入数组的自然对数，逐个元素。
sqrt(x, /[, out, where, casting, order, …]) 以元素方式返回数组的正平方根。
square(x, /[, out, where, casting, order, …])   返回输入的元素方块。
cbrt(x, /[, out, where, casting, order, …]) 以元素方式返回数组的立方根。
reciprocal(x, /[, out, where, casting, …])  以元素为单位返回参数的倒数。