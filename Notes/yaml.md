# 键值对
key: value
# 数组
- one
- two

数组也可以采用行内表示法。
animal: [Cat, Dog]

# 复合结构
对象和数组可以结合使用，形成复合结构。


languages:
 - Ruby
 - Perl
 - Python 
websites:
 YAML: yaml.org 
 Ruby: ruby-lang.org 
 Python: python.org 
 Perl: use.perl.org 

# 纯量
?

# 注释
用 #

# 多行字符串
字符串可以写成多行，从第二行开始，必须有一个单空格缩进。换行符会被转为空格。


str: 这是一段
  多行
  字符串
转为 JavaScript 如下。


{ str: '这是一段 多行 字符串' }
多行字符串可以使用|保留换行符，也可以使用>折叠换行。


this: |
  Foo
  Bar
that: >
  Foo
  Bar
转为 JavaScript 代码如下。


{ this: 'Foo\nBar\n', that: 'Foo Bar\n' }
+表示保留文字块末尾的换行，-表示删除字符串末尾的换行。


s1: |
  Foo

s2: |+
  Foo


s3: |-
  Foo
转为 JavaScript 代码如下。


{ s1: 'Foo\n', s2: 'Foo\n\n\n', s3: 'Foo' }
字符串之中可以插入 HTML 标记。


message: |

  <p style="color: red">
    段落
  </p>
转为 JavaScript 如下。


{ message: '\n<p style="color: red">\n  段落\n</p>\n' }