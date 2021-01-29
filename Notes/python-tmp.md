## 关于迭代器动态增加?
```python
nums = [1,2,3,4]

for i in range(len(nums)):
    print(nums.pop(0))
# 1
# 2
# 3
# 4


nums = [1,2,3,4]
for i in nums:
    if i == 1:
        nums.append(2)
    print(i)
# 1
# 2
# 3
# 4
# 2


```