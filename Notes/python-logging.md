import logging


logging.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=logging.DEBUG)

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warn('this is a warn message')
logging.error('this is a warn message')


# 多 输出(stdout ,file)
```python
import logging
logger = logging.getLogger()  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
# 使用FileHandler输出到文件
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)
logger.info('this is info message')
logger.warn('this is warn message')
```


# getLogger

# file config

# format handle ...

# cook book
https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
