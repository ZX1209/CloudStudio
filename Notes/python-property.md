```python
class Comic:
    def __init__(self,name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if type(value) == str and value != "":
            self._name = value
        else:
            raise ValueError('name must be non empty string')
            
    













```
