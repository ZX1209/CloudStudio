# Data classes (3.7+)
Python 3 introduces data classes which do not have many restrictions and can be used to reduce boilerplate code because the decorator auto-generates special methods, such as __init__() and __repr()__. From the official proposal, they are described as “mutable named tuples with defaults”.
```py
class Armor:

    def __init__(self, armor: float, description: str, level: int = 1):
        self.armor = armor
        self.level = level
        self.description = description

    def power(self) -> float:
        return self.armor * self.level

armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)
# <__main__.Armor object at 0x7fc4800e2cf8>
```

The same implementation of Armor using data classes.
```py
from dataclasses import dataclass

@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1


    def power(self) -> float:
        return self.armor * self.level

armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4

print(armor)
# Armor(armor=5.2, description='Common armor.', level=2)
```

https://datawhatnow.com/things-you-are-probably-not-using-in-python-3-but-should/