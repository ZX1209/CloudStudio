python-sys.md

# 模块检索路径
sys.path


# settrace()
sys.settrace(tracefunc)
Set the system’s trace function, which allows you to implement a Python source code debugger in Python. The function is thread-specific; for a debugger to support multiple threads, it must be registered using settrace() for each thread being debugged.