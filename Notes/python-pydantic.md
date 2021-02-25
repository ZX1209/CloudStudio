> https://www.cnblogs.com/fengqiang626/p/13307771.html#:~:text=Pydantic%20%E6%98%AF%E4%B8%80%E4%B8%AA%E4%BD%BF%E7%94%A8Python,%E5%AF%B9%E5%85%B6%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%8B%93%E5%B1%95%E3%80%82


Pydantic 是一个使用Python类型提示来进行数据验证和设置管理的库。Pydantic定义数据应该如何使用纯Python规范用并进行验证。PEP 484 从Python3.5开始引入了类型提示的功能，PEP 526 使用Python3.6中的变量注释语法对其进行了拓展。Pydantic使用这些注释来验证不受信任的数据是否采用了您想要的形式。
示例：
from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
这里发生了什么：

id 是 int 类型；注释声明告诉pydantic该字段是必须的。如果可能，字符串、字节或浮点数将强制转换为int，否则将引发异常。
name 从默认值推断为其为 str 类型，该字段不是必须的，因为它有默认值。
signup_ts 是 datetime 类型，该字段不是必须的，默认值为 None。pydantic会将表示unix时间戳（例如1496498400）的 int 类型或表示时间和日期的字符串处理成 datetime 类型。
friends 使用Python的 typing 系统，该字段是必须的，并且必须是元素为整数的列表，默认值为一个空列表。
如果验证失败，pydantic会抛出一个错误，列出错误的原因：

from pydantic import ValidationError
try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())

"""
[
  {
    "loc": [
      "id"
    ],
    "msg": "field required",
    "type": "value_error.missing"
  },
  {
    "loc": [
      "signup_ts"
    ],
    "msg": "invalid datetime format",
    "type": "type_error.datetime"
  },
  {
    "loc": [
      "friends",
      2
    ],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
"""