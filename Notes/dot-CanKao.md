# 命令行使用
dot -Tpdf filename.dot -o filename.pdf

# 基本
```graphviz
graph G{} //无向图
digraph G{} // 有向图

diagraph G
{
  subgraph cluster_0{} // 子图 必须用cluster_ 开头?
  subgraph cluster_1{}
}
```

# graphiz?
vscode 插件



























# 1.简介
dot是开源工具包Graphviz上用来画图的一门脚本语言。通过布局引擎解析脚本得到图像，然后可以将图像导出为各种格式以满足需求。主要用于编写脚本来画各种结构示意图和流程图。

Graphviz的文件后缀名是.gv。每个.gv文件代表一个图，可以通过dot -Tpng example.gv -o example.png命令生成图像，或者使用Graphviz提供的工具gvedit来编辑和运行脚本。

dot脚本的语法特别简单，官方doc只有8页。下面简单介绍下dot脚本的一些语法。

# 2.图的声明
使用digraph graphName可以申明一个图，具体实现代码用一对花括号包裹起来。

digraph graph1 {
  // statement
}
当图中某些内容同属一个类时，我们可以申明一个子图将其包含在齐齐。使用subgraph cluster_subgraphName可以申明一个子图^1。
****
subgraph cluster_subgraphName {
  // statement
}
来看一个具体的例子

digraph example1 {
  label = "this is a graph";
  a;b;

  subgraph cluster_subgraphName1 {
    label = "this is a  subgraph";
    bgcolor = greenyellow;
    c;d;
  }
}


# 3.结点和边的声明
dot里结点的申明非常简单，只需要键入结点名字nodeName；同时，结点默认的现实内容为结点名字。

当结点内容有空格时，我们可以将结点用一堆双引号包含起来，解析引擎会直接提取双引号里面的内容创建结点。

使用符号->就可以申明一条边，a -> b就代表由结点a连接到结点b的边^2。结点也可以连接到结点自身。

a;
b;
a -> b;


申明多条边的便捷语法:

a; b; c;
a -> b -> c -> c;
# 4.图的属性
图的属性可以写在graph[]里，也可以直接写在外面:

digraph graph1 {
  bgcolor = red;
  graph [bgcolor = red];
}
图的属性包括：

bgcolor：设置图的背景颜色，可以使用rgb值，也可以用#rrggbb编码形式
label：设置图的描述。label会继承到子图，如果不想子图重复label需手动设置
rankdir：设置图的方向，包括：TB（top to bottom）、BT（bottom to top）、LR(left to Right）、RL（right to left）
rotate：设置图的旋转。如rotata = 90代表旋转90度，默认逆时针
ratio：设置图的长宽比，可以是一个浮点数，也可以是：fill、compress、auto
5.结点属性和边属性
结点和边的属性设置非常简单，只需要在结点或者边的声明后面加上方括号，然后在方括号里填写属性键值对即可。键值对之间使用逗号进行分割。

a [shape = egg, label = "this is node a"];
b [shape = circle, label = "this is node b"];
a -> b [style = dashed, label = "this is edge a to b"];


结点的常用属性：

shape：设置结点形状。包括：Mrecord（圆角矩形）、record（矩形）、circle（圆形）、box（矩形，和record略有区别，下面会讲到）、egg（蛋形）、doublecircle（双圆形）、plaintext（纯文本）、 ellipse（椭圆，默认）。
label：设置结点的显示内容，内容用双引号包含，可以使用转义字符。当结点内容!=结点名时使用
style：设置结点的样式。包括：filled(填充)、dotted（点状边框）、solid（普通边框）、dashed（虚线边框）、bold（边框加粗）、invis（隐形）。
color：设置边框颜色。可以使用单词形式或者#rrggbb形式。
fillcolor：设置填充颜色，仅style = filled时有效。
width：设置结点宽度。
height：设置结点高度。
perpheries：设置结点边框个数。
fontcolor：设置结点内容颜色。可以使用单词形式或者#rrggbb形式。
边的常用属性：
1.style：设置边的形状。包括：solid（实线）、dashed（虚线）、dotted（点线）、bold（加粗）、invis（隐形）。

label：设置边标签。内容用双引号包含，可以使用转义字符。
color：设置边颜色。可以使用单词形式或者#rrggbb形式。
arrowhead：设置结点箭头样式。包括：none、empty、odiamond等。
使用node[]和edge[]可以分别设置结点和边的全局设置：

digraph graph1{
node [shape = egg];
edge [style = dashed];
}


# 6.其他应用
使dot支持中文
Graphviz默认是不支持中文的，输入的中文在生成的图中显示为一个空方块。如果想要让其支持中文，可以尝试以下方法：

在命令行制定-Nfontname = xxx.ttf，在gv文件中输入utf-8编码的汉字
给graph、node、edge设置fontname = xxx.ttf然后设置label
使用record的label属性生成表格
前面提到record和box有所区别。原因就是：设置为record和Mrecord的结点的label属性可以很方便地生成单列的表格和UML图等。（类似于XAML里面的stack）

用一对双引号+一对花括号包含起来的就是表格内容，不同的格子之间用符号 | 隔开，尖括号里的内容表示一个锚点

example [shape = record, label = "{<head>cell1 | cell2 | cell3}"];


也可以生成空格只保留锚点：

label="{<b1>|<b2>|<b3>}"


使用html标签生成表格
如果record生成的表格不符合预期，还可以使用html标签生成表格。只需要将结点的label属性设置为相应的html代码即可。

table1 [label=<
<table>
  <tr>
    <td port="one">1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
  </tr>
</table>
>];
port属性可以给td增加一个锚点

表格锚点的应用
cell的锚点可以让使用者在cell之间划线

引用cell的锚点的语法为table: anchorName

示例代码

digraph example2 {
  node [shape = record];
  table1 [label = "{<head>cell1 | cell2 | cell3}"];
  table2 [label = "{<head>cell1 | cell2}"];

  table1: head -> table2: head
}


生成图形
可以使用结点的某些属性来生成图形，如

circle [label="", shape="circle", width=0.5, fixedsize=true, style=filled, color=black];
就生成了一个实心的黑色圆形。

命令行全局设置
不仅可以使用代码里的全局设置，还可以在命令行里进行全局设置，这样就可以根据不同要求来生成图形。

dot -Grankdir=LR -Nshape="plaintext" -Earrowhead="odiamond" -Tpng example.dot -o example.png
Grankdir: graph rankdir
Nshape: node shape
Earrowhead: edge arrowhead

其他一些属性也可以按照这种规则填写

添加注释
dot的注释使用//（单行）或者/* */（多行）

7.几个实例
(1) 复杂的标签

digraph structs{
  /* 把结点默认形状设置为矩形record,默认的是圆角矩形Mrecord */
  node [shape = record];

  struct1 [label = "left|middle|right"];
  struct2 [label = "one|two"];
  struct3 [label = "hello\nworld|{b|{c|d|e}|f}|g|h"];

  struct1 -> struct2;
  struct1 -> struct3;
}


graph picture {
//这幅图的名字
label = "I love you";

//图名字的位置在bottom，也可以是t
labelloc = b;

//图名字的位置在left，也可以是r
labeljust = l;

edge[decorate = true];

C -- D [label = "s1"];
C -- E [label = "s2"];
C -- F [label = "s3"];
D -- E [label = "s4"];
D -- F [label = "s5"];

edge[decorate = false, labelfontcolor = blue, fontcolor = red];
C1 -- D1 [headlabel = "c1",taillabel = "d1",label = "c1 - d1"];
}


(2) 行列对齐

digraph html {
rankdir = LR;
{
node[shape = plaintext];
1995 -> 1996 -> 1997 -> 1998 -> 1999 -> 2000 -> 2001;
}
{
node[shape = box, style = filled];
WAR3 -> Xhero -> Footman -> DOTA:
WAR3 -> Battleship;
}
{rank = same; 1996; WAR3;}
{rank = same; 1998; Xhero; Battleship;}
{rank = same; 1999; Footman;}
{rank = same; 2001; DOTA;}
}


(2)二叉树

digraph G {
label = "Binary search tree";
node [shape = record];

A [label = "<f0>|<f1>A|<f2>"];
B [label = "<f0>|<f1>B|<f2>"];
C [label = "<f0>|<f1>C|<f2>"];
D [label = "<f0>|<f1>D|<f2>"];
E [label = "<f0>|<f1>E|<f2>"];
F [label = "<f0>|<f1>F|<f2>"];
G [label = "<f0>|<f1>G|<f2>"];

A:f0 -> B:f1;
A:f2 -> C:f1;
B:f0 -> D:f1;
B:f2 -> E:f1;
C:f0 -> F:f1;
C:f2 -> G:f1;
}


(4)哈希表

digraph G{
nodesep = .05;
rankdir = LR;

node [shape = record,width = .1,height = .1];
node0 [label = "<f0>|<f1>|<f2>|<f3>|<f4>|<f5>|<f6>|",height = 2.5];

node [width = 1.5];
node1 [label = "{<n>n14|719|<p>}"];
node2 [label = "{<n>a1|805|<p>}"];
node3 [label = "{<n>i9|718|<p>}"];
node4 [label = "{<n>e5|989|<p>}"];
node5 [label = "{<n>t20|959|<p>}"];
node6 [label = "{<n>o15|794|<p>}"];
node7 [label = "{<n>s19|659|<p>}"];

node0:f0 -> node1:n;
node0:f1 -> node2:n;
node0:f2 -> node3:n;
node0:f5 -> node4:n;
node0:f6 -> node5:n;
node2:p -> node6:n;
node4:p -> node7:n;
}


(5)流程图

digraph G{
subgraph cluster0 {
node [style = filled,color = white];
style = filled;
color = lightgrey;
a0 -> a1 -> a2 -> a3;
label = "process #1";
}

subgraph cluster1 {
node [style = filled];
b0 -> b1 -> b2 -> b3;
label = "process #2";
color = blue;
}

start -> a0;
start -> b0;
a1 -> b3;
b2 -> a3;
a3 -> a0;
a3 -> end;
b3 -> end;
start [shape = Mdiamond];
end [shape = Msquare];
}


8.参考文献
啄木鸟社区关于GraphViz的文章：https://wiki.woodpecker.org.cn/moin/GraphViz
Cnblog上的一篇文章：http://www.cnblogs.com/CoolJie/archive/2012/07/17/graphviz.html
简书上的dot学习笔记：http://www.jianshu.com/p/e44885a777f0
dot官方文档：http://www.graphviz.org/pdf/dotguide.pdf
CSDN上关于python实现graphviz的文章：http://blog.csdn.net/a1368783069/article/details/52067404
文章作者: Monad Kai
文章链接: onlookerliu.github.io/2017/12/28/dot语法总结/
版权声明: 本博客所有文章除特别声明外，均采用 CC BY-NC-SA 4.0 许可协议。转载请注明来自 Code@浮生记！