# pack 
首先我们先看看我们常用的pack(), 他会按照上下左右的方式排列.

tk.Label(window, text='1').pack(side='top')#上
tk.Label(window, text='1').pack(side='bottom')#下
tk.Label(window, text='1').pack(side='left')#左
tk.Label(window, text='1').pack(side='right')#右

pack(side=LEFT)

# grid 
接下里我们在看看grid(), grid 是方格, 所以所有的内容会被放在这些规律的方格中.

for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
以上的代码就是创建一个四行三列的表格，其实grid就是用表格的形式定位的。这里的参数 row为行，colum为列，padx就是单元格左右间距，pady就是单元格上下间距。

# place 
再接下来就是place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的（20,10），就是将这个部件放在坐标为（x，y）的这个位置 后面的参数anchor=nw就是前面所讲的锚定点是西北角。

tk.Label(window, text=1).place(x=20, y=10, anchor='nw')
 pack grid place 放置位置


```python
from tkinter import ttk
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # root.geometry("800x600+10+10")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

        self.input = tk.Entry(self)
        self.input['width'] = 100
        self.input.pack()

        self.button = tk.Button(self)
        self.button['text'] = "click me"
        self.button['command'] = self.show_text
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = "lavel me"
        self.button['command'] = self.add_label
        self.button.pack()

    def show_text(self):
        line = self.input.get()
        print(line)

    def say_hi(self):
        print("hi there, everyone!")
    def add_label(self):
        self.tmp = tk.Label(self)
        self.tmp['text'] = self.input.get()
        self.tmp.pack()
    def show_msg(self):
        tk.tkMessageBox('msg')

root = tk.Tk()

style = ttk.Style()
print(style.theme_names()) 
style.theme_use('clam') 

app = Application(root=root)
app.mainloop()

# class MyApplication(tk.frame):



# root = tk.Tk()
# root.geometry("800x600+10+10")

# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = tk.Listbox(root)          #  创建两个列表组件
# listb2 = tk.Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
 
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
 
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()                 # 进入消息循环

```


Tkinter 组件
Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。

目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:

控件  描述
Button  按钮控件；在程序中显示按钮。
Canvas  画布控件；显示图形元素如线条或文本
Checkbutton 多选框控件；用于在程序中提供多项选择框
Entry   输入控件；用于显示简单的文本内容
Frame   框架控件；在屏幕上显示一个矩形区域，多用来作为容器
Label   标签控件；可以显示文本和位图
Listbox 列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
Menubutton  菜单按钮控件，由于显示菜单项。
Menu    菜单控件；显示菜单栏,下拉菜单和弹出菜单
Message 消息控件；用来显示多行文本，与label比较类似
Radiobutton 单选按钮控件；显示一个单选的按钮状态
Scale   范围控件；显示一个数值刻度，为输出限定范围的数字区间
Scrollbar   滚动条控件，当内容超过可视化区域时使用，如列表框。.
Text    文本控件；用于显示多行文本
Toplevel    容器控件；用来提供一个单独的对话框，和Frame比较类似
Spinbox 输入控件；与Entry类似，但是可以指定输入范围值
PanedWindow PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
LabelFrame  labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
tkMessageBox    用于显示你应用程序的消息框。


标准属性
标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。

属性  描述
Dimension   控件大小；
Color   控件颜色；
Font    控件字体；
Anchor  锚点；
Relief  控件样式；
Bitmap  位图；
Cursor  光标；



几何管理
Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置

几何方法    描述
pack()  包装；
grid()  网格；
place() 位置；


