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
