import json

# 将json字符串变为python类型
json.loads()

# 读取文件并转换json类型
json.load()

# 将obj 转换为str 写到 fp 中
json.dump(obj,fp)

# 将
json.dumps(boj)
# return json str

python 原始类型向 json 类型的转化对照表：

Python	JSON
dict	object
list, tuple	array
str, unicode	string
int, long, float	number
True	true
False	false
None	null

Demjson?

note:
Keys in key/value pairs of JSON are always of the type str.
When a dictionary is converted into JSON, all the keys of the dictionary are coerced to strings. 
As a result of this, if a dictionary is converted into JSON and then back into a dictionary,
the dictionary may not equal the original one.
That is, loads(dumps(x)) != x if x has non-string keys.