## 2.1 栈(stack)
栈(stack)时一种特殊的线性表,只能在某一段插入和删除.
它按照后进先出的原则存储数据,先进入的数据被压入栈底,最后的数据在栈顶,
需要读取数据的时候从栈顶开始弹出数据(最后一个数据被第一个读书来).栈也称为后进先出表

### 导入使用
```cpp
# include <stack>

stack<TYPE> StackName
```

### 成员函数
bool empty()
void pop()
void push(const TYPE &val)
TYPE &top()
size_type size()

### 示例
```cpp
stack<int> s;
s.push(1);
s.push(2);
s.push(3);

cout<<"Top: "<<s.top()<<endl;
cout<<"Size: "<<s.size()<<endl;
s.pop();
cout<<"Size: "<<s.size()<<endl;

if(s.empty()) cout<<"Is empyt"<<endl;
else cout<<"Is not empty"<<endl;

```

## 2.2 向量(vector)
STL容器向量(Vector)是一个动态数组,随机(任意)存取任何元素都能在常数时间完成
Vector是一个多功能的,能够操作多种数据结构和算法的模板类和函数库.
可以通过迭代器随机的存取,当向其中插入新的元素时,如果在结尾插入,执行效率会比较高,
而如果往中间某个位置插入,其插入位置之后的所有元素都要后移,因此效率就不那么高

Vector时一个线性顺序结构,相当于数组,可以不预想指定数组的大小,而却能自动扩展.在创建一个vector后,
他会自动在内存中分配一块连续的内存空间进行数据存储
这个大小即capacity()函数的返回值.但粗寸的数据差过分配的空间时,Vector会重新分配一块内存块.

### 导入使用
```cpp
# include <vector>
```

| 成员函数               | 功能                                                |
| ---------------------- | --------------------------------------------------- |
| vector<TYPE> c         | 产生一个空的Vector,其中没有任何元素                 |
| vector<TYPE> c1(c2)    | 产生另一个同型Vector的副本(所有元素都被复制)        |
| vector<TYPE> c(n)      | 利用元素的Default构造函数生成一个大小为 n  的Vector |
| vector<TYPE> c(n,leem) | 产生一个大小为 n 的Vector,每个元素都是 elem         |
| `c.~vector<TYPE>()`    | 销毁所有元素,并释放内存                             |



### 主要成员函数

| 函数                  | 功能                                                                 |
| --------------------- | -------------------------------------------------------------------- |
| c.pop_back()          | 删除最后一个数据                                                     |
| c.push_back(elem)     | 在尾部加入一个数据 elem                                              |
| c.empyt()             | 判断容器是否为空                                                     |
| c.clear()             | 移除容器中所有数据                                                   |
| c.insert(pos,elem)    | 在pos位置插入一个elem的副本,传回新数据的位置                         |
| c.insert(pos,n,elem)  | 在pos位置插入n个elem数据.无返回值                                    |
| c.insert(pos,beg,end) | 在 pos 位置插入在[beg,end)区间内的数据,无返回值 (另一个数组的区间吧) |
| c.erase(pos)          | 删除pos位置的数据,传回下一个数据的位置                               |
| c.erase(beg,end)      | 删除在[beg,end)区间内的数据,传回下一个数据的位置                     |
| c.size()              | 返回容器中实际数据的个数                                             |
| c.capacity()          | 返回已经分配的可以容纳的元素个数                                     |
| c.begin()             | 传回迭代器中的第一个数据地址                                         |
| c.end()               | 传回迭代器中的最后一个数据地址                                       |
| c.back()              | 传回最后一个数据,补减产这个数据是否存在?                             |
| c.assign(beg,end)     | 将[beg,end)区间内的数据复制并赋值给c                                 |
| c.assign(n,elem)      | 将n个elem的值复制并赋值给c                                           |
| c1.swap(c2)           | 将 c1 和 c2 元素互换                                                 |
| swap(c1,c2)           | 将 c1 和 c2 元素互换                                                 |

### 示例
```cpp
int n;
cin>>n;
vector<int> a(n);
for (int i = 0; i < n; ++i)
{
    cin>>a[i];
}
a.push_back(10)


for (int i = 0; i < n; ++i)
{
    cout<<a[i]<<" ";
}
cout<<a.size()<<endl;

# 迭代器
vector<int>::iterator p;
for(p=a.begin();p!=a.end();++p)
    cout<<*p<<" ";
cout<<endl;

```

## 2.3 映射(Map)(泛化字典)
映射(map) 和 多重映射(multimap)是基于某一类型Key的键集的存在,提供对TYPE类型的数据进行快速和高效的检索
对于map而言,键只是指存储在容器中的某一成员,multimap允许键值重复,但map不允许

map内部数据的组织是一颗红黑树,这棵树具有对数据自动排序的功能,,所以在map内部的所有数据Key都是有序的.
map容器中的一个元素,可以通过Pair封装一个结构对象.map容器将这个Pair对象插入到红黑树中,完成一个元素的添加
map提供一个仅使用键值比较的函数对象,??
### 导入使用
```cpp
# include <map>
```

构造与析构
| 成员函数          | 功能            |
| ----------------- | --------------- |
| map c             | 产生一个空的map |
| map c(op)         | none            |
| map c1(c2)        | none            |
| map c(beg,end)    | none            |
| map c(beg,end,op) | none            |
| `c.~map()`        | none            |


创建
| Map                       | 效果                                        |
| ------------------------- | ------------------------------------------- |
| Map<keytype,elem>         | 一个Map,以less<>(operator<) 为排序准则      |
| Map<keytype,elem,op>      | 一个Map,以op为排序准则                      |
| multimap<keytype,elem>    | 一个Multimap,以less<>(operator<) 为排序准则 |
| multimap<keytype,elem,op> | 一个Multimap,以op为排序准则                 |
keytype 为 键值类型,elem 为Value值的类型

### 成员函数

| 成员函数                                       | 功能                                                      |
| ---------------------------------------------- | --------------------------------------------------------- |
| iterator find(const keytype &key)              | 返回一个迭代器指向键值为key的元素,如果没有找到就返回end() |
| size_type count(const keytype &key)            | 返回键值等于key的元素的个数                               |
| size_type size()                               | 返回元素的数量                                            |
| void clear()                                   | 清空容器                                                  |
| bool empty()                                   | 为空返回true,否则返回false                                |
| iterator insert(pair<keytype,valuetype> &elem) | 插入一个Pair类型的元素,返回插入元素的位置?                |
| void insert(iterator start, iterator end)      | 插入[start,end) 之间的元素到容器                          |
| void erase(iterator loc)                       | 删除 loc 所指元素                                         |
| void erase(iterator start,iterator end)        | 删除[start,end) 之间的元素                                |
| size_type erase(constkeytype &key)             | 删除key值为value的元素,并返回被删除的个数                 |
| iterator begin()                               | 返回指向第一个元素的迭代器                                |
| iterator end()                                 | 返回指向末尾(最后一个元素之后)的迭代器                    |



### 示例
```cpp
map<string,float,less<string> > c;
c.insert(make_pair("cafe",7.75));
c.insert(make_pair("banana",1.72));
c.insert(make_pair("piza",30.69));

c['Wine'] = 15.66 # 像字典一样使用

map<string,float>::iterator pos;
for (pos = c.begin(); pos < c.end(); ++pos)
{
    cout<<pos->first<<" "<<pos->second<<endl;
}

c.clear()

```

<utilty> 中定义了make_pair()


## 2.4 列表(List)
列表(list)是一个线性表结构(double-linked list,双链表)

由于结构原因,List随机检索的性能非常不好,因为它不像Vector那样能直接找到元素的地址,而是要从头....

可以迅速地在任何节点进行插入和删除
### 导入使用
```cpp
# include <list>
```
构造和析构
| 成员函数              | 功能                                            |
| --------------------- | ----------------------------------------------- |
| list<TYPE> c          | 产生一个空 list,其中没有任何元素                |
| list<TYPE> c1(c2)     | 产生一个与c2同型的List(每个元素都被复制)        |
| list<TYPE> c(n)       | 产生拥有n个元素的List,都已default构造函数初始化 |
| list<TYPE> c(n,type)  | 产生拥有n个元素的List,每个元素都是type的副本    |
| list<TYPE> c(beg,end) | 产生一个List,并以[start,end) 区间为初试         |
| `c.~list<TYPE>()`     | 销毁所有元素,释放内存                           |



### 成员函数
| 函数                                                              | 功能                                                                  |
| ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| TYPE &back()                                                      | 返回对最后一个元素的引用                                              |
| TYPE &front                                                       | 返回对第一个元素的引用                                                |
| iterator begin()                                                  | 返回指向第一个元素的迭代器                                            |
| iterator end()                                                    | 返回指向末尾(最后一个元素之后)的迭代器                                |
| void clear()                                                      | 清空列表                                                              |
| bool empty()                                                      | 列表为空返回true,否在为false                                          |
| iterator erase(iterator pos)                                      | 删除pos所指元素并返回下一个元素的迭代器                               |
| iterator erase(iterator start,iterator end)                       | 删除[start,end)之间的元素并返回最后一个被删除元素的下一个元素的迭代器 |
| iterator insert(iterator pos,const TYPE &val)                     | 插入一个值为value的元素在pos位置并返回器迭代器,                       |
| iterator insert(iterator pos,,size_type num,const TYPE &val)      | 插入num个值为value的元素在pos位置                                     |
| void insert(iterator pos,input_iterator start,input_iterator end> | 插入[start,end)之间的元素到pos位置                                    |
| void merge(list &lst)                                             | 将列表List有序的合并到原列表中,默认使用小于号进行比较插入             |
| void merge(list &lst,bool Cmpfunc)                                | ..                                                                    |
| void pop_back()                                                   | 删除最后一个元素                                                      |
| void pop_front()                                                  | 删除第一个元素                                                        |
| void push_back(const TYPE &val)                                   | 将value连接到列表后面                                                 |
| void push_front(const TYPE &val)                                  | 将value连接到列表前面                                                 |
| void remove(const TYPE &val)                                      | 删除列表中所有值为val的元素                                           |
| void remove_if(bool testfunc)                                     | 用testfunc一元函数判断是否删除函数                                    |
| bool testfunc(TYPE &val)                                          | ...                                                                   |
| size_type size()                                                  | 返回list中元素的数量                                                  |
| void reverse()                                                    | 将列表的所有元素反转                                                  |
| void sort()                                                       | 默认使用<排序                                                         |
| void sort(Comp compfunc)                                          | 使用compfunc排序                                                      |
| void swap(list &list)                                             | 交换两列表的元素                                                      |
| void unique()                                                     | 去除列表中的重复元素                                                  |



### 示例
```cpp
list<int> mylist(5,100);
mylist.push_front(-13);
mylist.push_back(300);

list<int>::iterator p  = mylist.begin();
mylist.erase(p)

for (p = mylist.begin(); p !=mylist.end(); ++p)
{
    cout<<*p<<" ";
}
cout<<endl;
cout<<mylist.size()<<endl;
mylist.clear();


```

## 2.5 集合
集合(set)是一个容器,它其中所包含的元素的值是唯一的.集合中的元素按一定的顺序排列,并被作为集合中的实例.
对这个序列可以进行查找,插入或者删除序列中的任意一个元素,而完成这个操作的时间同这个序列中元素的个数的对数成比例

一个集合通过一个链表老祖师,其具体实现采用了红黑树的平衡二叉树的数据结构.在插入操作和删除操作上比向量快
但添加和查找末尾元素时回有些慢
多集multiset中可以出项副本键,同一值可以出现多次

### 导入使用
```cpp
# include <set>

```

构造和析构函数
| 成员函数          | 功能                                                     |
| ----------------- | -------------------------------------------------------- |
| set c             | 产生一个空的set/multiset,其中不含任何元素                |
| set c(op)         | 以op为排序准则,差生一个空的set/multiset                  |
| set c(beg,end)    | 以区间[beg,end]内的元素产生一个set/multiset              |
| set c(beg,end,op) | 以op为排序准则,利用[beg,end]内的元素产生一个set/multiset |
| `c.~set()`        | 销毁元素,释放内存                                        |

set可选形式
| Set               | 效果                                       |
| ----------------- | ------------------------------------------ |
| set<TYPE>         | 一个set,以less<>(operator<)为排序准则      |
| set<TYPE,op>      | 一个set,以op为排序准则                     |
| multiset<TYPE>    | 一个multiset,以less<>(operator<)为排序准则 |
| multiset<TYPE,op> | 一个multiset,以op为排序准则                |

### 成员函数
| 函数                                                           | 功能                                                                            |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| iterator begin()                                               | 返回指向第一个元素的迭代器                                                      |
| iterator end()                                                 | 返回指向末尾(最后一个元素之后)的迭代器                                          |
| void clear()                                                   | 清空set容器                                                                     |
| bool empty()                                                   | 如果为空返回true,否则返回false                                                  |
| iterator insert(TYPE &val)                                     | 插入一个元素,返回新元素的位置                                                   |
| iterator insert(iterator pos,TYPE &val)                        | 插入一个元素,返回新元素的位置(pos 是一个提示,指出插入操作的起点,提示得当可加速) |
| iterator insert(iterator pos,input_iterator end)               | 插入[start,end)之间的元素                                                       |
| void erase(iterator pos)                                       | 删除pos所指元素                                                                 |
| void erase(iterator start,iterator end)                        | 删除[start,end)之间的元素                                                       |
| size_type erase(const TYPE &val)                               | 删除值为val的元素,并返回被删除的元素个数                                        |
| pair<iterator start,iterator end> equal_range(const TYPE &val) | 查找multiset中键值等于val的所有元素返回指示范围的两个迭代器,以pair返回          |
| size_type count(const TYPE &val)                               | 查找容器中值为val的元素的个数                                                   |
| iterator find(const TYPE &val)                                 | 返回一个迭代器指向键值为value的元素                                             |
| size_type size()                                               | 返回元素的数量                                                                  |
| void swap(set &obj)                                            | 交换两个链表的元素                                                              |

### 示例
```cpp
set<string> str;
str.insert("apple");
str.insert("orange");
str.insert("banana");
str.insert("grapes");
set<string>::iterator pos;
for (pos = str.begin(); pos < str.end(); pos++)
{
    cout<<*pos<<" ";
}
cout<<endl;
str.clear()
```

## 2.6 队列(queue)
队列(queue)是一种特殊的线性表,它只允许在表的前端(Front)进行删除操作,而在表的后端(Rear)进行插入操作

### 导入使用
```cpp
# include <queue>

```

### 成员函数
| 函数                       | 功能                                |
| -------------------------- | ----------------------------------- |
| bool empty()               | 队列为空返回true                    |
| void pop()                 | 删除队列的一个元素                  |
| void push(const TYPE &val) | 将val元素加入队列                   |
| size_type size()           | 返回当前队列的元素数目              |
| TYPE &back()               | 返回一个引用,指向队列的最后一个元素 |
| TYPE &front()              | 返回队列第一个元素的引用            |

### 示例
```cpp
queue<int> q;
q.push(1);
q.push(3);
q.push(2);
q.push(9);

cout<<q.size()<<endl;
cout<<q.empty()<<endl;
cout<<q.front()<<endl;
cout<<q.back()<<endl;

while(q.empty()!=true)
{
    cout<<q.front()<<" ";
    q.pop();
}


```
## 2.7 优先队列(priority queue)
优先队列(priority queue)容器,与队列一样,只能从队尾插入元素,从队首删除元素.
但是它有一个特性,就是队列中最大的元素总是位于队首,所以出队时,并非按照先进先出的原则进行
而是将但钱队列中最大元素出队.

元素比较规则默认按元素值 由大到小排序,可以重载<操作符来重新定义比较规则
如果时系统提供的能够使用小于号比较的元素类型就可以只写元素类型;
如果想用系统提供的大于号进行比较,则还需给出储存容器和比较谓词;如果使用自定义的struct/class,这需要重载小于号运算符

### 导入使用
```cpp
# include <queue>

```

### 成员函数
| 函数                       | 功能                              |
| -------------------------- | --------------------------------- |
| bool empty()               | 队列为空返回true                  |
| void pop()                 | 删除队列的一个元素                |
| void push(const TYPE &val) | 将val元素加入队列                 |
| size_type size()           | 返回当前队列的元素数目            |
| TYPE &top()                | 返回一个引用,指向最高优先级的元素 |

### 示例
priority_queue<TYPE,Containter,Functional>
```cpp
struct info
{
    string name;
    float score;
    bool operator<(const info &a) const
    {
        return a.score<score;
    }
}

priority_queue<info> pq;
info in;
in.name = "Jack";
in.score = 68.5;
pq.push(in);
in.name = "Bomi";
in.score = 18.5;
pq.push(in);
in.name = "Peti";
in.score = 90;
pq.push(in);


while(!pq.empty())
{
    cout<<pq.top().name<<": "<<pq.top().score<<endl;
    pq.pop();
}
```
# contianer

vector

map?

set?

sort?

make_pair & pair


# algorithm

sort

find
min
max

push_heap
pop_heap
..
## doc
Non-modifying sequence operations:
all_of 
Test condition on all elements in range (function template )
any_of 
Test if any element in range fulfills condition (function template )
none_of 
Test if no elements fulfill condition (function template )
for_each
Apply function to range (function template )
find
Find value in range (function template )
find_if
Find element in range (function template )
find_if_not 
Find element in range (negative condition) (function template )
find_end
Find last subsequence in range (function template )
find_first_of
Find element from set in range (function template )
adjacent_find
Find equal adjacent elements in range (function template )
count
Count appearances of value in range (function template )
count_if
Return number of elements in range satisfying condition (function template )
mismatch
Return first position where two ranges differ (function template )
equal
Test whether the elements in two ranges are equal (function template )
is_permutation 
Test whether range is permutation of another (function template )
search
Search range for subsequence (function template )
search_n
Search range for elements (function template )

Modifying sequence operations:
copy
Copy range of elements (function template )
copy_n 
Copy elements (function template )
copy_if 
Copy certain elements of range (function template )
copy_backward
Copy range of elements backward (function template )
move 
Move range of elements (function template )
move_backward 
Move range of elements backward (function template )
swap
Exchange values of two objects (function template )
swap_ranges
Exchange values of two ranges (function template )
iter_swap
Exchange values of objects pointed to by two iterators (function template )
transform
Transform range (function template )
replace
Replace value in range (function template )
replace_if
Replace values in range (function template )
replace_copy
Copy range replacing value (function template )
replace_copy_if
Copy range replacing value (function template )
fill
Fill range with value (function template )
fill_n
Fill sequence with value (function template )
generate
Generate values for range with function (function template )
generate_n
Generate values for sequence with function (function template )
remove
Remove value from range (function template )
remove_if
Remove elements from range (function template )
remove_copy
Copy range removing value (function template )
remove_copy_if
Copy range removing values (function template )
unique
Remove consecutive duplicates in range (function template )
unique_copy
Copy range removing duplicates (function template )
reverse
Reverse range (function template )
reverse_copy
Copy range reversed (function template )
rotate
Rotate left the elements in range (function template )
rotate_copy
Copy range rotated left (function template )
random_shuffle
Randomly rearrange elements in range (function template )
shuffle 
Randomly rearrange elements in range using generator (function template )

Partitions:
is_partitioned 
Test whether range is partitioned (function template )
partition
Partition range in two (function template )
stable_partition
Partition range in two - stable ordering (function template )
partition_copy 
Partition range into two (function template )
partition_point 
Get partition point (function template )

Sorting:
sort
Sort elements in range (function template )
stable_sort
Sort elements preserving order of equivalents (function template )
partial_sort
Partially sort elements in range (function template )
partial_sort_copy
Copy and partially sort range (function template )
is_sorted 
Check whether range is sorted (function template )
is_sorted_until 
Find first unsorted element in range (function template )
nth_element
Sort element in range (function template )

Binary search (operating on partitioned/sorted ranges):
lower_bound
Return iterator to lower bound (function template )
upper_bound
Return iterator to upper bound (function template )
equal_range
Get subrange of equal elements (function template )
binary_search
Test if value exists in sorted sequence (function template )

Merge (operating on sorted ranges):
merge
Merge sorted ranges (function template )
inplace_merge
Merge consecutive sorted ranges (function template )
includes
Test whether sorted range includes another sorted range (function template )
set_union
Union of two sorted ranges (function template )
set_intersection
Intersection of two sorted ranges (function template )
set_difference
Difference of two sorted ranges (function template )
set_symmetric_difference
Symmetric difference of two sorted ranges (function template )

Heap:
push_heap
Push element into heap range (function template )
pop_heap
Pop element from heap range (function template )
make_heap
Make heap from range (function template )
sort_heap
Sort elements of heap (function template )
is_heap 
Test if range is heap (function template )
is_heap_until 
Find first element not in heap order (function template )

Min/max:
min
Return the smallest (function template )
max
Return the largest (function template )
minmax 
Return smallest and largest elements (function template )
min_element
Return smallest element in range (function template )
max_element
Return largest element in range (function template )
minmax_element 
Return smallest and largest elements in range (function template )

Other:
lexicographical_compare
Lexicographical less-than comparison (function template )
next_permutation
Transform range to next permutation (function template )
prev_permutation
Transform range to previous permutation (function template )
# iterator?
