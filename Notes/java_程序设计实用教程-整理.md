# 第一章 java概述
package 声明类所在包
lang 包默认导入
final 常量


# 第二章 java语言基础

## 标识符
以字母开头的字母数字序列
0~9,大小写字母,下划线(_)和符号$

## 注释
// 单行注释

/* 多行注释
*/

/** 文档注释
*/
## 基本数据类型
整数类型    字节数
byte 1
short 2
int 4
long 8
float 4
double 8

> 空语句?
> i = 1;;

## 数组
type[] name
name = new type[10]

type[] name  ={values}

> ArrayList

类的封装包含两层含义:
第一,将数据和对数据的操作包装成一个对象类型,使对象成为包含一组属性和操作的运行单位
第二,实现信息隐藏,类既要提供与外部联系的方法,又要尽可能地隐藏类中某些数据和实现细节,以约束外部的可见性

析构方法
public void finalize()

public static void main(String args[])

## 类的继承性
extends

## 类的多态
父实例(引用指针)(容器)能兼容子实例

在子类的实例成员方法中,可用super引用访问被子类隐藏的父类同名成员变量

沿着继承关系逐层向上

父类对象只能执行那些在父类中声明,被子类覆盖的子类方法,不能执行子类增加的成员方法

## 类的抽象性
public abstract class ColsedFigure
{
    public abstract double area();
}
> 构造方法,静态成员方法不能被声明为抽象方法
> 抽象类通常包含抽象方法,也可以不包含抽象方法,但是包含抽象方法的类必须被声明为抽象类


### 最终类
public final class Math extends Object


# 第三章 类的封装,继承和多态

## 3.2 类的封装性
类的封装包含两层含义,
第一,将数据和对数据的操作包装成一个对象类型,使对象成为包含一组属性和操作的运行单位
第二,实现信息隐藏,类既要提供与外部联系的方法,又要尽可能地隐藏类中某些数据和实现细节.

> 缺省权限 到当前包


### 3.3.2 继承原则及作用


### 3.5.2 抽象类
public abstract class ClosedFigure{
    public abstract double area();
}


# 第四章 接口,内部类和javaa pi基础

## 4.1 接口与实现接口的类
public interface Area{
    public abstract double area();
}

用 implements 声明一个类指定接口
一个类可以实现多个接口,多个接口之间用逗号隔开.

接口与抽象类的区别
抽象类为子类约定声明,抽象类可以给出部分实现包括构造方法等;抽象方法在多个子类中表象出多态性
类的单继承,是的一个类只能继承一个父类的约定和实现

接口为多个互不相关的类约定某一特性的方法声明,在类型层次中表达对象拥有的属性,接口没有实现部分
接口是多继承的.一个类实现多个接口,就具有多种特性,也是多继承的.

一个非抽象类如果声明多个接口,则必须实现(覆盖)所有指定接口中的所有抽象方法,
方法的参数列表必须相同;否则它必须声明为抽象类

## 4.2 内部类和内部接口
是声明在其他类或接口内部的内嵌类型.
> Pixel$Color.class 和 Pixel$ColorConstant.class

## 4.3 java api基础

### 4.3.1 java.lan 包中的基础类库

#### 1 object 类
string toString()
boolean queals(Object obj)
void finalize() throws Throable
final Class<?> getClass()

#### 2 Math 数学类
final double E
final double PI
static double abs(double a)
static double random()
static double pow(double a,double b)
static double sqrt(double a)
static double sin(double a)

最终类

#### 3 Comparable 可比较接口
public interfacce Comparable<T>{
    public abstract int compareTo(T cobj);
}

#### 4 基本数据类型的包装类
java 为每种基本数据类型声明了一个对应的类,称为基本数据类型的包装类.
Byte,Short,Integer,Long,Float,Doble,Character,Boolean
都是最终类?

##### Integer 最终类
parseInt() -> int i = Integer.parseInt("123");
intValue() -> int j = new Integer("123").intValue();

##### Double 浮点类 最终类
parseDouble(String s) throws NumberFormatException

##### Stirng 字符串类
isEmpty()
toUpperCase()
toLowerCase()
startsWith()
endsWith()
indexOf(int ch)
indexOf(String s)
lastIndexOf()
String[] split(String regex)

trim() 返回当前串删除所有空格后的字符串

##### StringBuffer 字符串缓冲区类


##### 7 Class 和 Package 类
public final class Class<T> implements java.io.Serializable,...{
    public String getName()
    public Class<? super T> getSuperclass()
    public Package getPackage()

}

public class Package extends Object ...{
    public String getName();
}

##### 8 System 系统类
public final class System extends Object{
    ...
    getProperties()
    getProperty()
    currentTimeMillis()
    exit(int status)
    in,out,err
}

##### 9 Runtime 运行时类
public class Runtime extends Object{
    public static Runtime getRuntime()
    public long totalMemory()
    public long freeMemory()
}

### 4.3.2 java.util 包中的工具类库
#### 1 日期类
##### Data 类
public Date();//构造方法,获得系统当前日期时间

##### Calendar 类
Calendar 时抽象类,调用getInstance() 方法创建一个子类实例后,在调用get() 方法通过常量参数获得或时间的指定部分
YEAR,MONTH,DATE,HOUR,MINUTE,SECOND,DAY_OF_WEEK

#### 2. Comparator 比较器接口
equals
compare

#### 3. Arrays 数组类
Arrays 类的所有方法都是静态方法,都提供多种基本数据类型及Object类行参数的重载方法
sort(int a[])
sort(Object a[])
<T> void sort(T a[],Comparator<?superT> c)

binarySearch(int a[],int key)
binarySearch(Object a[],Object key)
..Comparator

## 4.4 泛型
? extends T //?表示T及其任意一种子类型 上界
? super T //?表示T及其任意一种父类型   下界



# 第五章 异常处理
### 5.1.2 错误和异常
1. 错误
值程序运行时遇到的硬件错误,或操作系统,虚拟机等系统软件错误,或操作错误.
程序本身不能处理错误,只能依靠外界干预.

java.lang.Eroor 是错误类
当运行没有main() 方法的类时,则产生NoClassDefFOundError类
new 申请分配内存时,如果没有可用内存,则产生OutOfMeoryError 内存溢出错误

2. 异常
java.lan.Exception 异常类

3. RuntimeException 运行异常类
ArithmeticException 算术异常
NullPointerException 空对象异常
ClassCaseException 类型强制转换异常
NegativeArraySizeException 负数组长度异常
ArrayIndexOutOfBoundsException 数组下标越界异常
StringindexOutOfBOundsException 字符串序号越级异常
NumberFormatException 数值格式异常

try
catch(Exception ex)
finally

throw

ex.toString()

# 第六章 图像用户界面
## 6.1 AWT 组件及其属性类
### 6.1.1 AWT 组件
#### 1. 组件
组件(component)是构成图形用户界面的基本成分和核心元素,组件是具有以下特征的对象:
运行时可见,具有坐标位置,尺寸,字体,颜色等书香,可以拥有并管理其他组件,可以获得输入焦点,可以响应事件.
Component 是所有组件类构成树层次结构的根类,实际使用的组件都是Component的子类.
public abstract class Component implements ImageObserver,MenuContainer,Serializable
{
    getWidth()
    getHeight()
    setSize()
    getX()
    getY()
    setLocation(int x,int y)
    setBounds(int x,int y,int width,int height)
    getForeground() //获取组件的文本颜色
    setForeground()
    getBackground()
    setBackground()
    getFont()
    setFont()
    setVisible() //可见
    setEnabled() //设置是否有效状态
}

#### 2 容器
容器(Container) 是一种特殊组件,它能容纳其他组件,在其可视区域内显示这些组件.容器中各组件的大小和位置由容器的布局管理器进行控制
一个容器中可以放置其他容器.

public class Container extends Component
{
    setLayout(LayoutManager mgr)
    add(Component comp)
    remove(int i) //删除容器中第i个组件
}

#### 3 窗口和面板
Container 容器类的子类有:Window 窗口类和Panel 面板类
窗口有标题懒和关闭控制按钮,有边框,可以添加菜单栏;窗口可以独立存在,运行是可以被移动,被改变大小.
窗口时顶层容器,窗口不能包含在其他容器中,
public class Window extends Container immplements Accessible
{
    //设置窗口相对于组件comp 的位置,若comp为null,则将窗口置于屏幕中央
    setLocationRelativeTo(Component comp)
}

面板没有标题,没有边框,不可添加菜单栏;面包那不能独立存在,必须包含在替他容器中,
窗口可以包含多个面板,一个面板可以包含另一个面板.
public class Panel extends Container implements Accessible
{
    public Panel() //默认FlowLayout布局
    public Panel(LayoutManage layout)
}

#### 4 框架和对象
Window 窗口类的子类有:Frame框架和Dialog对话框.
Frame框架时一种窗口,用做Java Application应用程序的主窗口,Frame 带有最大化和最小化控制按钮
public class Frame extends Window implements MenuContainer
{
    public Frame() // 默认BorderLayout 布局
    public Frame(String title) //title 指定框架标题
    public String getTitle()
    public setTitle()
    public setResizable(boolean)
}
对话框也是一种窗口,但不能作为应用程序的主窗口,它通常依附于一个框架,当框架关闭时对话框也关闭
.对话框界面比框架简单,没有最大化和最小化按钮.
对话框可以被设置为模式(modal)窗口,特点时总在最前面,如果不关闭模式对话框,这不能对其他窗口进行操作
public class Dialog extends Window
{
    public Dialog(Frame owner)
    public Dialog(Frame owner,String title)
    public Dialog(Frame owner,boolean modal) // model 指定模式窗口,默认为flase
    public Dialog(Frame owner, String title ,boolean modal)
}

#### 5 标签
标签组件用于显示字符串,标签只能显示星系,不能用于输入,
public class label extends Component implements Accessible
{
    public static final int LEFT=0,CENTER=1,RIGHT=2;//对其方式常量
    public Label()
    public Label(String text) //text 指定字符床,默认左对齐
    public Label(String text,int alignment) //alignment 指定对其方式
    public Stirng getText()
public void setText(String text)
}

#### 6 文本行
文本行是一个单行文本编辑框,用于输入一行文字
public class TextField extends TextComponent{
    public TextField()
    TextField(String text)
    TextField(int columns)
    TextField(String text,int columns)
    getText()
    setText()
}

#### 7 按钮
按钮用于显示操作命令,执行一种特定操作
public class Button extends Component implements Accessibl{
    public Button(String text)
}
图形界面的应用程序运行时所产生的错误和异常,分别由Java.awt. 包 中的 AETError 和 AWTException处理

#### 例 6.1
```java
import java.awt.*
public class LoginFrame extends Frame
{
    public LoginFrame(){
        super("User Login");
        this.setSize(200,130);
        this.setLocation(300,240);
        this.setBackground(Color.lightGray);
        this.setLayout(new FlowLayout());

        this.add(new Label("userid"));
        this.add(new TextField("user1",10))
        this.add(new label("password"));
        this.add(new TextField(10));
        this.add(new Button("OK"));
        this.add(new Button("Cancel"));

        this.setVisible(true);
    }
    public static void main(String arg[]){
        new LoginFrame()
    }
}

```

### 6.1.2 布局管理器
#### 1. 流布局管理器
FlowLayout 布局管理器提供按行不知组件方式,将组建按从左至右顺序,一行一样排列,当这一行放满时再放置下一行.组件保持自己的尺寸,容器中一行的宽度随容器的宽度而变化.当改变容器大小时,组件的相对位置随容器大小而改变,将呈现一样或多行
public class FlowLayout implements LayoutManager,java.io.Serialiable{
    public static final int LEFT=0,CENTER =1,RIGHT=2;
    public FlowLayout();
    public FlowLayout(int align);
    public FlowLayout(int align,int hgap,int vgap) //hgap,vgap 指定逐渐减的水平和垂直间距
}

#### 2 边布局管理器
BorderLayout 管理器将容器划分为5个区域,东,南,西,北四条边和中间.组件占满一条边或中间部分.
当改变容器大小时,四边组件的长度或宽度不变,中间组件的长度和宽度都随容器大小而变化.
public class BorderLayout implements LayoutManager2 ,java.io.serializable{
    public static final String North="North",SOUTH="South",EAST="East",WEST="West",CENTER="Center";
    public BorderLayout()
    public BorderLayout(int hgap,oint vgap)
    public void add (Component comp ,Object constraints) // constrains 参数指定组件添加BorderLayout 布局位置,
    //取值为BorderLayout 常量
}

#### 3 网格布局管理器
GridLayout 布局管理器将容器划分为大小相等的若干行乘若干列的网格,组件大小随容器大小而变化.
public class GridLayout implements LayoutManager,java.io.Serializable{
    public GridLayout(int rows,int cols);
    public GridLayout(int rows,int cols,int hgap,ing vgap);
}
GirdLayout 布局的组件放置次序时行优先,从第一行开始,从左至右一次放置,一行放满后自动转入下一行.
每个组件占满一格,如果组件数超过网格数.这布局管理器会自动增加网格数,增加的原则时保持行数不变;反之,一些网格将空置

#### 4 网格包布局
GirdBagLayout 网格包布局时一种灵活的布局管理器.

### 6.1.3 颜色和字体
#### 1. 颜色
Color 颜色类表示24位真彩色.
Color 类声明white,black,red,yellow,green,blue,pink,orange,magenta,cyan,gray,lightGray,darkGray等颜色常量
public class Color implements Paint,java.io.Serializable
{
    public Color(int red,int green,int blue)
    puglic Color(int rgb)
    public int getRed()
    public int getBlue()
    public int getGreen()
    public int getRGB()
    public Color brighter() //颜色变浅
    public Color darker() //颜色变深
}


#### 2. 字体
Font 字体类声明如下,一种字体由字体名,字形,字号等属性组成.
public class Font implements java.io.Serializable
{
    public static final int PLAIN=0,BOLD=1,ITALIC=2;
    public Font(String name,int style,int size)
    public String getName()
    public int getSize()
    public int getStyle()
    public boolean isBold()
    public boolean isItalic()

}


## 6.2 事件处理
### 6.2.1 委托事件模型
#### 1. 事件和事件源
事件(event) 是指一个状态的改变,或者一个活动的发生.产生事件的组件成为事件源(event source)

#### 2. 事件类和事件监听接口
Java 将事件封装成事件类,并为每个事件类定义一个事件监听器接口(listener interfacce)
约定事件处理方法,指定产生事件时执行的操作

例如ActionListener 是动作事件监听接口,声明actionPerformed()方法如下

public interface ActionListener extends EventListener
{
    public abstract void actionPerformed(ActionEvent ev);
}

WindowListener 是窗口事件监听器接口,声明多个窗口事件的处理方法如下
public interface WindowListener extends EventListener
{
    public abstract boid windowOpened(WindowEvent ev);
    public abstract void windowClosing(WindowEvent ev);
}

一个描述图像用户揭秘那的类声明实现一个事件监听器接口,意味着该类将响应指定事件并提供事件处理方法,



#### 3. 组件注册事件监听器对象
一个组件如果注册了一个事件监听器对象,表明该组件声明要响应指定事件.
button.addActionListener(this)
frame.addWindowListener(this)

this.addWindowListener(new WinClose())
class WinClosing(WindowEvent ev){
    windowOpened(WinddowEvent ev){}
    windowActivated(WinddowEvent ev){}
    windowClosed(WinddowEvent ev){}
    windowIconified(WinddowEvent ev){}
    ...
}
程序运行时,button按钮和frame框架被监听,单击button按钮时,执行this对象实现的actionPerformend()方法;
单击frame框架窗口的关闭按钮时,执行this对象实现的windowClosing()方法



### 6.2.2 AWT 事件类和事件监听器端口
#### 1. AWT 事件类
java.util.EventObject 是 Java事件类树的根类,即所有事件类的祖先类,部分声明如下:
public class EventObject implements java.io.Serializable
{
    public Object getSource();
}

java.awt.AWTEvent extends java.awt.AWTEvent
{
    public String getActionCommand()
}

#### 2. AWT 事件监听器接口

### 6.3 Swing 组件及事件

```java
import javax.swing.*

```
# 第七章 多线程
class Runnable

class Thread

# 第八章 输入/输出流和文件操作

# 第九章 网络通信

# 第十章 数据库应用

# 第十一章 Web应用

# 第十二章 综合应用设计