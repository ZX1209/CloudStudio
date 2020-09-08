```py
import time
import datetime
import inspect


# Python code to merge dict using update() method
def dict_merge(dict1, dict2):
    return dict2.update(dict1)


def class_variable_to_dict_string(class_variable):
    """
    """
    return {
        key: str(value)
        for key, value in class_variable.__dict__.items()
        if not key.startswith("__") and not callable(key)
    }


def peewee_model_to_dict_string(class_variable):
    """
    """
    return {
        key: str(value)
        for key, value in class_variable.__dict__["__data__"].items()
        if not key.startswith("__") and not callable(key)
    }
```