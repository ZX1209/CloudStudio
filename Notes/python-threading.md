threading.Thread() # 创建

Thread.start() # 开始线程

Thread.join([timeout=None]) # 等待线程结束

threading.current_thread() # 返回当前线程




`class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`


```python
import threading 

def f(i):
    print(i,threading.current_thread().name)


t=threading.Thread(target=f,args=(1))

t.start()

t.join()
```


# Timer
class threading.Timer(interval, function, args=[], kwargs={})

创建一个timer，在interval秒过去之后，它将以参数args和关键字参数kwargs运行function 。
调用该函数回返回一个定时器的句柄，同时也获得了一个定时器实例。

但是这时，定时器只是被创建，被没有启动，需要调用实例里面的

start（）方法启动定时器。如果在定时过程中想要取消该定时器，需要使用cancel()函数。

https://zhuanlan.zhihu.com/p/32094690