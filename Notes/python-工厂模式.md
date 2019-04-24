```python
import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self,filepath):
        self.data = {}
        with open(filepath,mode='r',encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def data(self):
        return self._data




```
