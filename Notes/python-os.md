# about path see pathlib.Path
# basic
```py
from pathlib import Path
p = Path('./c')
p.resolve() # 解决符号连接

p / 'c.py'

p.glob(*.py)

...
```



# os.path.exists() ; os.mkdir()
```python
import os

if not os.path.exists('python-spyder-downloads'):
    os.mkdir('python-spyder-downloads')

newdir = os.path.join(dir_name,'this')

if not os.path.exists(newdir):
    os.mkdir(newdir)
```

# os.system
```python
os.system(r'C:\Users\14049\WordAndStudy\Projects\学校\大三上\数字图像处理\gif\giphy.gif')
```
os.popen()



# os.system()
sys shell command


# os.getcwd()



# os.chdir()



os.listdir()



os.mkdir()



os.mkdirs()



os.rmdir()



os.removedirs()



os.rename()



os.stat()



datetime.datetime.fromtimestamp()



os.walk()



os.environ



os.path.join()



os.path.basename()



os.path.dirname()



os.path.split()



os.path.exists()



os.path.isdir()



os.path.isfile()



os.path.splitext()