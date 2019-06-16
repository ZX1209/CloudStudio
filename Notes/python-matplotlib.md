# 坐标轴及网格线
```py
ax.axhline(0, color='red', lw=2)
ax.axhline(0, color='green', lw=2)

# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)

# Turn on the minor TICKS, which are required for the minor GRID
# ax.minorticks_on()
# don't work for scaling things

# Customize the major grid
ax.grid(which='major', linestyle='-', linewidth=0.5, color='red')
# Customize the minor grid
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# or
ax.grid(which='both')
```
or plt....
orginal is axes func

# axes vs axs vs figure...
https://matplotlib.org/faq/usage_faq.html#usage


# import path...

# (直接)显示开关
ion,ioff

# 基本思路
[subplot]
plot
设置
...
plt.show()
(一张图,,可以传多组数据,,多个曲线)

with plt.xkcd():

# 基本
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

# 图片数据
```py
fig=plt.figure()
plt.plot(x,y)
canvas=fig.canvas

buffer = io.BytesIO()
canvas.print_png(buffer)
data=buffer.getvalue()
buffer.close()
```
# fill

# 色调
autumn(),bone(),cool(),copper(),flag(),gray(),hot(),hsv(),inferno(),jet(),magna(),nipy_spectral(),pink(),plasma(),prism(),spectral(),spring(),viridis(),summer()

# 轴,标题
xlabel(),ylabel(),xlim(),ylim(),xticks(),yticks(),xscale(),yscale(),title()

# 交互模式
ion()
ioff()
是否需要show()

# 箱线图
```py
from matplotlib import pyplot as plt
a=range(1,10)
plt.boxplot((a,a),labels=('Mon','Tue'))
plt.show()
```

# 线图
plot()

# 图像
imshow()

# 矩阵图
pcolormesh()

# 等高图
contour()

# 直方图
hist()

# ploar()

# 散点图
scatter()

# 开启网格
plt.grid(True)

# streamplot()

# Axes3D

# 条形图
bar()

# 饼图
pie

# table

# Polar plots
polar()

# 图例
legends()

arrow()
axhline()
axhspan()
axvline()
axvspan()
colorbar()

figimage()
figtext()

table()
text()
subtitle()


# matplotlib.path
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Fixing random state for reproducibility
np.random.seed(19680801)


x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 + 500

plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
            label="Luck")
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc=2)
plt.show()
```

# 多图 subplot
```python
# 分成2x2，占用第一个，即第一行第一列的子图
plt.subplot(221)
# 分成2x2，占用第二个，即第一行第二列的子图
plt.subplot(222)
# 分成2x1，占用第二个，即第二行
plt.subplot(212)
plt.show()
```
## 另一种
```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
```

# fig,axes = plt.subplots()
## subplot & subplots
```python
fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
axes[0, 0].plot(x, y)
axes[1, 1].scatter(x, y)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
```


```python

# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


x = np.linspace(-10,10,50)
y1 = 2*x+1
y2 = x**2


# In[15]:



plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,'r--',label='down')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
'''
plt.yticks(
    [-2,-1.8,-1,1.22,3],
    ['really bad','bad','normal','good','really good']
)
'''

'''
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
'''

plt.show()


# In[17]:


plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,'r--',label='down')

# 图例
plt.legend()


# In[26]:


# plt.figure()
plt.plot(x,y1,label='up')

x0 = 1
y0 = 2*x0+1

plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,10],'k--')

plt.annotate('anotate',xy=(x0,y0))

plt.show()


# In[27]:


n=1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

T = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.show()


# In[28]:


'''
for x,y in zip(X,Y):
...pass
'''


# In[36]:


def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

X,Y = np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

#C = plt.contourf(X,Y,f(X,Y),8,colors='black',linewidth=0.5)
#plt.clabel(C,inline=True,fontsize=10)
plt.show()


# In[40]:


data = np.linspace(0,1,9)
a = data.reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar()


# In[42]:


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4  ,0.25)
X,Y = np.meshgrid(X,Y)

R = np.sqrt(X**2+Y**2)

Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='x',offset=-2,cmap='rainbow')

plt.show()


```













# 3d plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y,z) # each as (x,y,z) 对应的坐标点



```python
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
```


```python
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
t = np.linspace(0,100,1000)

x = np.cos(t)
y = 2*np.sin(t)

z = np.linspace(0,100,1000)

ax.plot(x, y, z, label='parametric curve')
ax.legend()
```