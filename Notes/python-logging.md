import logging


logging.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=logging.DEBUG)
>The call to basicConfig() should come before any calls to debug(), info() etc. As it’s intended as a one-off simple configuration facility, only the first call will actually do anything: subsequent calls are effectively no-ops.
>一次性简单配置?

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
Warning The fileConfig() function takes a default parameter, disable_existing_loggers, which defaults to True for reasons of backward compatibility. This may or may not be what you want, since it will cause any non-root loggers existing before the fileConfig() call to be disabled unless they (or an ancestor) are explicitly named in the configuration. Please refer to the reference documentation for more information, and specify False for this parameter if you wish.
The dictionary passed to dictConfig() can also specify a Boolean value with key disable_existing_loggers, which if not specified explicitly in the dictionary also defaults to being interpreted as True. This leads to the logger-disabling behaviour described above, which may not be what you want - in which case, provide the key explicitly with a value of False.

# format handle ...
>If you are using {}-formatting (str.format()), you can use {attrname} as the placeholder in the format string. If you are using $-formatting (string.Template), use the form ${attrname}. In both cases, of course, replace attrname with the actual attribute name you want to use.
> 即 可使用 f string 等构建信息字符串.



| Attribute name  | Format              | Description                                                                                                                                                                                           |
|-----------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| args            | None                | The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).|                                  |
| asctime         | %(asctime)s         | Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).|                      |
| created         | %(created)f         | Time when the LogRecord was created (as returned by time.time()).|                                                                                                                                    |
| exc_info        | None                | Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.|                                                                                                                          |
| filename        | %(filename)s        | Filename portion of pathname.|                                                                                                                                                                        |
| funcName        | %(funcName)s        | Name of function containing the logging call.|                                                                                                                                                        |
| levelname       | %(levelname)s       | Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').|                                                                                                                |
| levelno         | %(levelno)s         | Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).|                                                                                                                       |
| lineno          | %(lineno)d          | Source line number where the logging call was issued (if available).|                                                                                                                                 |
| message         | %(message)s         | The logged message, computed as msg % args. This is set when Formatter.format() is invoked.|                                                                                                          |
| module          | %(module)s          | Module (name portion of filename).|                                                                                                                                                                   |
| msecs           | %(msecs)d           | Millisecond portion of the time when the LogRecord was created.|                                                                                                                                      |
| msg             | None                | The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).|                                        |
| name            | %(name)s            | Name of the logger used to log the call.|                                                                                                                                                             |
| pathname        | %(pathname)s        | Full pathname of the source file where the logging call was issued (if available).|                                                                                                                   |
| process         | %(process)d         | Process ID (if available).|                                                                                                                                                                           |
| processName     | %(processName)s     | Process name (if available).|                                                                                                                                                                         |
| relativeCreated | %(relativeCreated)d | Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.|                                                                                             |
| stack_info      | None                | Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.| |
| thread          | %(thread)d          | Thread ID (if available).|                                                                                                                                                                            |
| threadName      | %(threadName)s      | Thread name (if available).|                                                                                                                                                                          |
# cook book
https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
