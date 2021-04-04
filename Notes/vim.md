:set enc=utf8，i 到插入模式，Ctrl-V（或者MS下映射成Ctrl-Q）185，便可以输入¹；

:dig ^1 185，i 到插入模式，Ctrl-K 然后输入^1，便同样可以输入¹。 



#宏记录

#开始记录宏 并放在寄存器a中
qa
#结束宏记录
q
#调用寄存器a中的宏
@a




#全部替换
:%s/this/another/g


#搜索字符串
/search
#为命令、输入、导航都激活鼠标的使用
:set mouse = a

#窗口
##打开关闭命令
:sp[ lit] {file}     水平分屏
:new {file}         水平分屏
:sv[ iew] {file}     水平分屏，以只读方式打开
:vs[ plit] {file}    垂直分屏
:clo[ se]            关闭当前窗口

##打开关闭快捷键
Ctrl+w s        水平分割当前窗口
Ctrl+w v        垂直分割当前窗口
Ctrl+w q        关闭当前窗口
Ctrl+w n        打开一个新窗口（空文件）
Ctrl+w o        关闭出当前窗口之外的所有窗口
Ctrl+w T        当前窗口移动到新标签页

##切换窗口
Ctrl+w h        切换到左边窗口
Ctrl+w j        切换到下边窗口
Ctrl+w k        切换到上边窗口
Ctrl+w l        切换到右边窗口
Ctrl+w w        遍历切换窗口

##移动窗口
Ctrl+w H        向左移动当前窗口
Ctrl+w J        向下移动当前窗口
Ctrl+w K        向上移动当前窗口
Ctrl+w L        向右移动当前窗口

##调整大小
Ctrl+w +        增加窗口高度
Ctrl+w -        减小窗口高度
Ctrl+w =        统一窗口高度




# File management

:e              reload file
:q              quit
:q!             quit without saving changes
:w              write file
:w {file}       write new file
:x              write file and exit

# Movement

    k
  h   l         basic motion
    j

w               next start of word
W               next start of whitespace-delimited word
e               next end of word
E               next end of whitespace-delimited word
b               previous start of word
B               previous start of whitespace-delimited word
0               start of line
$               end of line
gg              go to first line in file
G               go to end of file
gk		move down one displayed line
gj		move up one displayed line

# Insertion
#   To exit from insert mode use Esc or Ctrl-C
#   Enter insertion mode and:

a               append after the cursor
A               append at the end of the line
i               insert before the cursor
I               insert at the beginning of the line
o               create a new line under the cursor
O               create a new line above the cursor
R               enter insert mode but replace instead of inserting chars
:r {file}       insert from file

# Editing

u               undo
yy              yank (copy) a line
y{motion}       yank text that {motion} moves over
p               paste after cursor
P               paste before cursor
<Del> or x      delete a character
dd              delete a line
d{motion}       delete text that {motion} moves over

# Search and replace with the `:substitute` (aka `:s`) command

:s/foo/bar/	replace the first match of 'foo' with 'bar' on the current line only
:s/foo/bar/g	replace all matches (`g` flag) of 'foo' with 'bar' on the current line only
:%s/foo/bar/g	replace all matches of 'foo' with 'bar' in the entire file (`:%s`)
:%s/foo/bar/gc	ask to manually confirm (`c` flag) each replacement 

# Preceding a motion or edition with a number repeats it 'n' times
# Examples:
50k         moves 50 lines up
2dw         deletes 2 words
5yy         copies 5 lines
42G         go to line 42
vim -v

