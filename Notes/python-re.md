# re.match(pattern, string, flags=0)
Try to apply the pattern at the start of the string, returning
a Match object, or None if no match was found.
```python
import re
m = re.match('\d*','12sadf')
m.group()
```

# re.search(pattern, string, flags=0)
Scan through string looking for a match to the pattern, returning
a Match object, or None if no match was found.

>>> m = re.match('foo', 'seafood') # 匹配失败
>>> if m is not None: m.group()

>>> m = re.search('foo', 'seafood') # 使用 search() 代替
>>> if m is not None: m.group()

# re.compile()
re.compile(pattern, flags=0)
Docstring: Compile a regular expression pattern, returning a Pattern object.

# Match.group()
>>> m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
>>> m.group() # 完整匹配
'abc-123'
>>> m.group(1) # 子组 1
'abc'
>>> m.group(2) # 子组 2
'123'
>>> m.groups() # 全部子组
('abc', '123')


# ^ & $
start & end

# re.sub re.subn
re.sub(pattern, repl, string, count=0, flags=0)
> replace

Return the string obtained by replacing the leftmost
non-overlapping occurrences of the pattern in string by the
replacement repl.  repl can be either a string or a callable;
if a string, backslash escapes in it are processed.  If it is
a callable, it's passed the Match object and must return
a replacement string to be used.

# re.split()

# 通常情况下，在正则表达式中使用原始字符串是个好主意

# 表 1-1 常见正则表达式符号和特殊字符
表 示 法 描 述 正则表达式示例
符号
literal 匹配文本字符串的字面值 literal foo
re1|re2 匹配正则表达式 re1 或者 re2 foo|bar
. 匹配任何字符（除了\n 之外） b.b
^ 匹配字符串起始部分 ^Dear
$ 匹配字符串终止部分 /bin/*sh$
* 匹配 0 次或者多次前面出现的正则表达式 [A-Za-z0-9]*
+ 匹配 1 次或者多次前面出现的正则表达式 [a-z]+\.com
? 匹配 0 次或者 1 次前面出现的正则表达式 goo?
{N} 匹配 N 次前面出现的正则表达式 [0-9]{3}
{M,N} 匹配 M～N 次前面出现的正则表达式 [0-9]{5,9}
[…] 匹配来自字符集的任意单一字符 [aeiou]
[..x−y..] 匹配 x ～ y 范围中的任意单一字符 [0-9], [A-Za-z]
[^…] 不匹配此字符集中出现的任何一个字符，包括某一范围的字符（如果在此字符集中出现） [^aeiou], [^A-Za-z0-9]
(* |+|?|{})? 用于匹配上面频繁出现/重复出现符号的非贪婪版本（*、+、?、{}） .*?[a-z]
(…) 匹配封闭的正则表达式，然后另存为子组 ([0-9]{3})?,f(oo|u)bar

# 表 示 法 描 述 正则表达式示例
特殊字符
\d
匹配任何十进制数字，与[0-9]一致（\D 与\d 相反，不匹配任何非数值型的数字）
data\d+.txt
\w
匹配任何字母数字字符，与[A-Za-z0-9_]相同（\W 与之相反）
[A-Za-z_]\w+
\s
匹配任何空格字符，与[\n\t\r\v\f]相同（\S 与之相反）
of\sthe
\b
匹配任何单词边界（\B 与之相反）
\bThe\b
\N
匹配已保存的子组 N（参见上面的(…))
price: \16
\c
逐字匹配任何特殊字符 c（即，仅按照字面意义匹配，不匹配特殊含义）
\., \\, \*
\A(\Z)
匹配字符串的起始（结束）（另见上面介绍的^和$）
\ADear
