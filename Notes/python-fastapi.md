> https://fastapi.tiangolo.com/zh/tutorial/first-steps/

## installl
pip install fastapi[all]

## 第一步
```py
from fastapi import FastAPI # 导入

app = FastAPI() # 创建实例


@app.get("/") # 创建路径 get post put delete
async def root(): # async 也行
    return {"message": "Hello World"} # 自动转换json
```

`uvicorn main:app --reload`
uvicorn main:app --reload

### 交互式api文档
./docs 

./redoc

### 方法?
通常使用：

POST：创建数据。
GET：读取数据。
PUT：更新数据。
DELETE：删除数据。


##  路径参数

###   顺序很重要
在创建路径操作时，你会发现有些情况下路径是固定的。

比如 /users/me，我们假设它用来获取关于当前用户的数据.

然后，你还可以使用路径 /users/{user_id} 来通过用户 ID 获取关于特定用户的数据。

由于路径操作是按顺序依次运行的，你需要确保路径 /users/me 声明在路径 /users/{user_id}之前：

###   预设值
Enum

###   路径转换器
路径转换器¶
你可以使用直接来自 Starlette 的选项来声明一个包含路径的路径参数：


/files/{file_path:path}

##  查询参数
声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数

async def read_item(skip: int = 0, limit: int = 10):

查询字符串是键值对的集合，这些键值对位于 URL 的 ？ 之后，并以 & 符号分隔。

例如，在以下 url 中：


http://127.0.0.1:8000/items/?skip=0&limit=10

应用于路径参数的所有相同过程也适用于查询参数：

###   默认值
###   可选查询参数      
from typing import Optional

async def read_item(item_id: str, q: Optional[str] = None):

###   查询参数类型转换
bool 类型转换

###   多个路径和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):

###   必须查询参数
如果你不想添加一个特定的值，而只是想使该参数成为可选的，则将默认值设置为 None。

但当你想让一个查询参数成为必需的，不声明任何默认值就可以：


##  请求体 ,post
