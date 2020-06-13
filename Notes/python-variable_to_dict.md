```py
{key:value for key, value in A.__dict__.items() if not key.startswith('__') and not callable(key)}
```