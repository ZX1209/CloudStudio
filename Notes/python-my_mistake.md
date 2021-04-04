错误创建：myList = [[0] * 3] * 4

原因：*4只是把一维数组复制了四次引用。如果修改`mylist[0][1]`的值，`mylist[2][1]`、`mylist[3][1]`、`mylist[4][1]`的值都会变.*

# 更新引用和改变引用
```python
sets = [
{1,3,5,7,9,2},
{2,43,5,7,9,4},
{2,6,8,4,3,2}
]

# 这边两个变量其实是同一个引用
hard_set = sets[0]
easy_set = sets[0]

for tmpi in range(1,len(sets)):
    hard_set &= sets[tmpi]
    easy_set |= sets[tmpi]
print(hard_set)
print(easy_set)

# 这边的 &=,|= 都是改变了引用指向的值.
# 但是没有更改变量绑定的引用,所以两个其实改变一个东西
#
# 改成
#for tmpi in range(1,len(sets)):
#    hard_set = hard_set & sets[tmpi]
#    easy_set = easy_set | sets[tmpi]
# 可避免
#p = p + 1 重赋了引用
# 就好像变量重赋值了一样
```