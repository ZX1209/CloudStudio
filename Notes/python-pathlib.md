```py
f.absolute() = (f.anchor/f.drive) + f.parent+f.name(f.stem+f.suffix)

f.as_uri()

list(f.parents)

f.parts

f.suffixes

list(f.glob('*.csv'))

list(f.iterdir())

# rename
f.rename('something.csv')

# convert to proper string
str(f)

# get modified and created time of a file
import time
time.ctime(f.stat().st_mtime())
time.ctime(f.stat().st_ctime())

f.stat().st_size()


# test
f.is_dir()
f.is_file()
f.exists()

Path.cwd()
Path.home()
```

# 参考 https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf



# basic
```py
from pathlib import Path
cwdPath = Path('.').resolve()
homePath = cwdPath.home()

p = Path('./c')
p.resolve() # 解决符号连接

p / 'c.py'

p.glob(*.py)

...
```

# resolve
将符号路径转换成绝对路径

# p.rglob
迭代遍历

cwd

# suffix or suffixes
后缀
``` py
# iter existing suffix
PurePath.suffix
The file extension of the final component, if any:

>>>
>>> PurePosixPath('my/library/setup.py').suffix
'.py'
>>> PurePosixPath('my/library.tar.gz').suffix
'.gz'
>>> PurePosixPath('my/library').suffix
''
PurePath.suffixes
A list of the path’s file extensions:

>>>
>>> PurePosixPath('my/library.tar.gar').suffixes
['.tar', '.gar']
>>> PurePosixPath('my/library.tar.gz').suffixes
['.tar', '.gz']
>>> PurePosixPath('my/library').suffixes
[]

# add suffix
PurePath.with_suffix(suffix)
Return a new path with the suffix changed. If the original path doesn’t have a suffix, the new suffix is appended instead. If the suffix is an empty string, the original suffix is removed:

>>>
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_suffix('.bz2')
PureWindowsPath('c:/Downloads/pathlib.tar.bz2')
>>> p = PureWindowsPath('README')
>>> p.with_suffix('.txt')
PureWindowsPath('README.txt')
>>> p = PureWindowsPath('README.txt')
>>> p.with_suffix('')
PureWindowsPath('README')
```



basename = Path(r'D:\储存，安装\14049\Music')



// test ok...

fullname = =basename /  '\"Lana Del Rey - Love.mp3\"'



os and os.path  pathlib
os.path.abspath()   Path.resolve()
os.chmod()  Path.chmod()
os.mkdir()  Path.mkdir()
os.rename() Path.rename()
os.replace()    Path.replace()
os.rmdir()  Path.rmdir()
os.remove(), os.unlink()    Path.unlink()
os.getcwd() Path.cwd()
os.path.exists()    Path.exists()
os.path.expanduser()    Path.expanduser() and Path.home()
os.path.isdir() Path.is_dir()
os.path.isfile()    Path.is_file()
os.path.islink()    Path.is_symlink()
os.stat()   Path.stat(), Path.owner(), Path.group()
os.path.isabs() PurePath.is_absolute()
os.path.join()  PurePath.joinpath()
os.path.basename()  PurePath.name
os.path.dirname()   PurePath.parent
os.path.samefile()  Path.samefile()
os.path.splitext()  PurePath.suffix