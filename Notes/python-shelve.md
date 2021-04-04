Creating a new Shelf
The simplest way to use shelve is via the DbfilenameShelf class. It uses anydbm to store the data. You can use the class directly, or simply call shelve.open():
```py
import shelve
s = shelve.open('test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
finally:
    s.close()
```
To access the data again, open the shelf and use it like a dictionary:
```py
import shelve

s = shelve.open('test_shelf.db')
try:
    existing = s['key1']
finally:
    s.close()

print existing
```
If you run both sample scripts, you should see:
```bash
$ python shelve_create.py
$ python shelve_existing.py

{'int': 10, 'float': 9.5, 'string': 'Sample data'}
```

## auto write back
s = shelve.open('test_shelf.db', writeback=True)


