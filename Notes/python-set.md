>>> x = set('spam')  
>>> y = set(['h','a','m'])  
>>> x, y  
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))  
 

x & y # 交集 
set(['a', 'm'])  

 
x | y # 并集  
set(['a', 'p', 's', 'h', 'm'])  
  
x - y # 差集  
set(['p', 's'])  

基本操作：  
  
t.add('x')            # 添加一项  
  
s.update([10,37,42])  # 在s中添加多项  
  
   
  
使用remove()可以删除一项：  
  
t.remove('H')  
  
   
  
len(s)  
set 的长度  
  
x in s  
测试 x 是否是 s 的成员  
  
x not in s  
测试 x 是否不是 s 的成员   

s.issubset(t)  
s <= t  
测试是否 s 中的每一个元素都在 t 中  
  
s.issuperset(t)  
s >= t  
测试是否 t 中的每一个元素都在 s 中  
 
运算符（voperator）  
等价于  
运算结果  
  
s.update(t)  
s |= t  
返回增加了 set “t”中元素后的 set “s”  
  
s.intersection_update(t)  
s &= t  
返回只保留含有 set “t”中元素的 set “s”  
  
s.difference_update(t)  
s -= t  
返回删除了 set “t”中含有的元素后的 set “s”  
  
s.symmetric_difference_update(t)  
s ^= t  
返回含有 set “t”或者 set “s”中有而不是两者都有的元素的 set “s”  

s.add(x)  
  
向 set “s”中增加元素 x  
  
s.remove(x)  
  
从 set “s”中删除元素 x, 如果不存在则引发 KeyError  
  
s.discard(x)  
  
如果在 set “s”中存在元素 x, 则删除  
  
s.pop()  
  
删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError  
  
s.clear()  
  
删除 set “s”中的所有元素  
  
  
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.  
  
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。  
  
