## 使用代理

proxies={'http':'127.0.0.1:1080','https':'127.0.0.1:1080'}

requests.get('http://www.google.com',proxies=proxies)

// ok

# download file
```python
r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
```

# content?
>>> from PIL import Image
>>> from io import BytesIO

>>> i = Image.open(BytesIO(r.content))