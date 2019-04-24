# 第一章 jsp概述

> jsp 页面在执行过程中会被转换为Servlet然后又服务器执行该Servlet.

# 第二章 jsp开发基础

## 1 java 语言基础
### 1.1 基本数据类型
byte  8位
short  16位
int  32位
long  64位
float  32位
double  64位
char  16位
boolean 8位

### 1.5 字符串处理
#### 1 字符串声明
String()

String(String name)

String(char[] value)
String str  = "abc";

...

### 1.6 数组的创建与使用
type name[] = new type[number];



#### 2 字符串类的常用方法
boolean equals(Stirng s)
boolean equalsIgnoreCase(String s)

int indexOf()
int length()
String replace(char oldChar, char newChar)
String substring()

char[] toCharArray()
toLowerCase   toUpperCase

### 1.8 集合类的应用
#### 1 ArrayList
add(int index,Object obj)
addAll(int ,Collection coll)
remove(int index)
set(int index, Object obj)
get(int index)
indexOf(Object obj)
lastIndexOf(Object obj)

List<String> list = new ArrayList<String>();

#### 2 Vector
Vector v = new Vector();

## JavaScript 脚本语言

### 3 JavaScript 的数据类型与运算符
vat variable = 11;

### 5 函数的定义和调用
#### 1 函数的定义
function functionName([parameter1,parameter2...])
{
​    statements
​    [return expression]
}

### 6 事件
####2 常用事件
onblur    失去焦点
onchange  获得焦点后内容改变
onclick   左键单击时
onfocus   获得焦点
onkeydown 键盘被按下时触发 
onload
onselect
onsumbit    点击提交按钮时,form 上触发
onunload    

### 7 JavaScript 常用对象的应用
#### 7.1 String 对象
lenght
split(separator,limit)
substr(start,length)
substr(from,to)
replace(searchValue, replaceValue)
CharAt(index)

#### 7.2 Date 对象
getFullYear()    返回用四位数表示的年份
getMonth()    返回月份(0~11)
getDate()     (1~31)
getDay()      (0~6)
getHours()    (0~23)
getMinutes()  (0~59)
getSeconds()  (0~59)
getTime()     毫秒表示
set* 

#### 7.3 window 对象
...

# 第三章 jsp 语法

## 3.1 了解jsp的基本构成

1. jsp 中的指令标识
2. HTML 标记语言
3. 嵌入的java代码
4. jsp表达式

## 3.2 jsp的指令表示

<%@ 指令名称 属性1="属性值" 属性2="属性值"%>

### 3.2.1 使用page 指令



### 3.2.2 使用include指令

该指令用于在当前jsp页面中,在当前使用该指令的位置嵌入其他的文件,如果被包含的文件中又可执行的代码,则显示代码执行后的结果.

### 3.2.3 taglib
## 3.3  JSP的脚本标识

### 3.3.1 JSP 表达式

<%=变量或可以返回值的方法或java表达式%>

转换为out.print() 方法

### 3.3.2 声明标识

<%! 声明变量或方法的代码%>

### 3.3.3 脚本程序

<% java代码 %>



## 3.5 动作标识
### 3.5.1 <jsp:include >

使用include指令被包含的文件,它的内容会原封不动地插入到包含页面中使用该指令的位置,然后JSP编译器再对这个合成的文件进行翻译.

### 3.5.2 <jsp:forward >

用来将请求转发到拎一个jsp,html或相关的资源文件中

当该标识被执行后,当前页面将不再被执行.

### 3.5.3 <jsp:useBean >

id 定义一个变量名

class 完整的类名

### 3.5.4 <jsp:setProperty >

这个标识通常情况下与 useBean标识一起使用,他将调用Bean中的setxxx()方法,将求情中的参数粗制为 useBean标识创建的JavaBean中对应的属性



property="*" 将request 请求中所有参数的值将被一一附给Bean中与参数具有相同姓名的属性

### 3.5.5 <jsp:getProperty >
### 3.5.6 <jsp:fallback >

plugin 的错误信息

### 3.5.7 <jsp:plugin >

### 3.5.8 <jsp:param >



# 第四章 JSP 内置对像

## 4.1 JSP内置对象概述

cookies 中的session id 

url 重写技术

## 4.2 request 对象

request 对象是从客户端向服务器发出的请求.

### 4.2.1 请求访问参数

String userName = request.getParameter("name")

### 4.2.2 在作用域中管理属性

设置转发数据

request.setAttribute("key",Object)



获取转发数据

request.getAttribute(String name)



转发

< jsp:forward page="error.jsp">

### 4.2.3 获取Cookie

```java
Cookie[] = request.getCookies();//从request 中huode Cookies 集

//初始化Cookie对象为空

Cookie cookie_response = null;

if(cookies!=null){cookie_response=cookies[1]}

if(cookie_respoinse!=null)

{
    cookie_response.getValue();
    cookie_response.setValue(new java.util.Date()toLocaleString());
}
//如果Cookies 集为空,创建cookie,并加入到response
if(cookies==null)
{
    cookie_respon se=new Cookie("AccessTime","");
    cookie_response.setValue(new java.util.Date()toLocaleString());
    response.addCookie(cookie_response)
}
```



### 4.2.4 获取客户信息

request对象提供了一些用来获取客户信息的方法

getRemoteAddr()

getMethod()

getHeader(String name)

### 4.2.5 访问安全信息

request 对象:

isSecure() # htttp?

is...

### 4.2.6 访问国际化信息

java.util.Locale locale = request.getLocale();



local.equals(java.util.Locale.US)

## 4.3 response 对象

用于响应客户请求,向客户端输出信息.

### 4.3.1 重定向网页

response.sendRedirect("login_ok.jsp");

sendError(int number)

sendError(int number,String msg)

sendRedirect(String location)

### 4.3.2 设置HTTP响应报头

setDateHeader..

...

### 4.3.3 缓冲区配置

缓冲区可以更加有效地在服务器域客户之间传输内容.

...??



## 4.4 session 对象

但是在一定时间内,,若果没有应答对象就会自动消失.

### 4.4.1 创建及获取客户的会话

session.setAttribute(String anme,String value)

session.getAttribute(String name);

### 4.4.2 从会话中溢出指定对象

session.removeAttribute();

### 4.4.3 销毁session

session.invalidate()

### 4.4.4 会话超时的管理

getLastAccessedTIme()

getMaxInactiveInterval() ; 以秒为单位返回一个会话内两个请求的最大时间间隔.

setMaxInactiveInterval()



## 4.5 application 对象

application 对象用于保存所有应用程序中的共有数据,服务器启动并且自动创建application对象后,只要没有关闭服务器,application 对象将一直存在.

### 4.5.1 访问应用程序初始化参数

通过application对象调用ServletContext 对象踢狗了对应用程序环境属性的访问.

web.xml 在WEB-INF中



getInitParameter(String name);

getInitparameterNames();

### 4.5.2 管理应用程序环境属性

与session对象相同,也可以在application对象中设置书香.

removeAttribute(String name)

setAttribute...

getAttributeNames()



## 4.6 out对象

out.println..

## 4.7 其他内置对象
### 4.7.1 获取会话范围的pageContext 对象

相当于页面中所有其他对象功能的最大继承者,使用它可以访问到本页中所有其它对象.

### 4.7.2 读取web.xml配置信息的config

### 4.7.3 应答或请求的page对象
### 4.7.4 获取异常信息的exception对象


# 第五章 JavaBean 技术
## 5.1 JavaBean 概述
### 5.1.1
### 5.1.2
### 5.1.3
### 5.1.4
### 5.1.5
### 5.1.6
### 5.1.7
## 5.2
### 5.2.1
### 5.2.2
### 5.2.3
### 5.2.4
### 5.2.5
### 5.2.6
### 5.2.7
## 5.3
### 5.3.1
### 5.3.2
### 5.3.3
### 5.3.4
### 5.3.5
### 5.3.6
### 5.3.7
## 5.4
### 5.4.1
### 5.4.2
### 5.4.3
### 5.4.4
### 5.4.5
### 5.4.6
### 5.4.7
## 5.5
### 5.5.1
### 5.5.2
### 5.5.3
### 5.5.4
### 5.5.5
### 5.5.6
### 5.5.7
## 5.6
### 5.6.1
### 5.6.2
### 5.6.3
### 5.6.4
### 5.6.5
### 5.6.6
### 5.6.7
## 5.7
### 5.7.1
### 5.7.2
### 5.7.3
### 5.7.4
### 5.7.5
### 5.7.6
### 5.7.7
# 第六章 Servlet技术
## 6.1 Servlet基础
### 6.1.1
### 6.1.2
### 6.1.3
### 6.1.4 Servlet 的生命周期



### 6.1.5
### 6.1.6
### 6.1.7
## 6.2 Servlet API 编程常用接口
### 6.2.1 Servlet 接口

destory

...

### 6.2.2 HttpServlet 类

doDelete

doGet

doHead

doOptions

doPost

doPut

doTrace

getLastModified

### 6.2.3 ServletConfig 接口 
### 6.2.4 HttpServletRequest接口
### 6.2.5 HttpServletResponse接口
### 6.2.6 GenericServlet 类
### 6.2.7
## 6.3 Servlet 开发
### 6.3.1 Servlet的创建

继承HttpServlet抽象类

重载适当的方法

...

### 6.3.2 Servlet的配置
### 6.3.3
### 6.3.4
### 6.3.5
### 6.3.6
### 6.3.7
## 6.4 Servlet 过滤器
### 6.4.1
### 6.4.2
### 6.4.3
### 6.4.4
### 6.4.5
### 6.4.6
### 6.4.7
## 6.5 Servlet 监听器
### 6.5.1
### 6.5.2
### 6.5.3
### 6.5.4
### 6.5.5
### 6.5.6
### 6.5.7
## 6.6 Servlet 的应用实例
### 6.6.1
### 6.6.2
### 6.6.3
### 6.6.4
### 6.6.5
### 6.6.6
### 6.6.7
## 6.7 第七章 JSP 实用组件
### 6.7.1
### 6.7.2
### 6.7.3
### 6.7.4
### 6.7.5
### 6.7.6
### 6.7.7
# 7
## 7.1
### 7.1.1
### 7.1.2
### 7.1.3
### 7.1.4
### 7.1.5
### 7.1.6
### 7.1.7
## 7.2
### 7.2.1
### 7.2.2
### 7.2.3
### 7.2.4
### 7.2.5
### 7.2.6
### 7.2.7
## 7.3
### 7.3.1
### 7.3.2
### 7.3.3
### 7.3.4
### 7.3.5
### 7.3.6
### 7.3.7
## 7.4
### 7.4.1
### 7.4.2
### 7.4.3
### 7.4.4
### 7.4.5
### 7.4.6
### 7.4.7
## 7.5
### 7.5.1
### 7.5.2
### 7.5.3
### 7.5.4
### 7.5.5
### 7.5.6
### 7.5.7
## 7.6
### 7.6.1
### 7.6.2
### 7.6.3
### 7.6.4
### 7.6.5
### 7.6.6
### 7.6.7
## 7.7
### 7.7.1
### 7.7.2
### 7.7.3
### 7.7.4
### 7.7.5
### 7.7.6
### 7.7.7
# 8
## 8.1
### 8.1.1
### 8.1.2
### 8.1.3
### 8.1.4
### 8.1.5
### 8.1.6
### 8.1.7
## 8.2
### 8.2.1
### 8.2.2
### 8.2.3
### 8.2.4
### 8.2.5
### 8.2.6
### 8.2.7
## 8.3
### 8.3.1
### 8.3.2
### 8.3.3
### 8.3.4
### 8.3.5
### 8.3.6
### 8.3.7
## 8.4
### 8.4.1
### 8.4.2
### 8.4.3
### 8.4.4
### 8.4.5
### 8.4.6
### 8.4.7
## 8.5
### 8.5.1
### 8.5.2
### 8.5.3
### 8.5.4
### 8.5.5
### 8.5.6
### 8.5.7
## 8.6
### 8.6.1
### 8.6.2
### 8.6.3
### 8.6.4
### 8.6.5
### 8.6.6
### 8.6.7
## 8.7
### 8.7.1
### 8.7.2
### 8.7.3
### 8.7.4
### 8.7.5
### 8.7.6
### 8.7.7
# 9
## 9.1
### 9.1.1
### 9.1.2
### 9.1.3
### 9.1.4
### 9.1.5
### 9.1.6
### 9.1.7
## 9.2
### 9.2.1
### 9.2.2
### 9.2.3
### 9.2.4
### 9.2.5
### 9.2.6
### 9.2.7
## 9.3
### 9.3.1
### 9.3.2
### 9.3.3
### 9.3.4
### 9.3.5
### 9.3.6
### 9.3.7
## 9.4
### 9.4.1
### 9.4.2
### 9.4.3
### 9.4.4
### 9.4.5
### 9.4.6
### 9.4.7
## 9.5
### 9.5.1
### 9.5.2
### 9.5.3
### 9.5.4
### 9.5.5
### 9.5.6
### 9.5.7
## 9.6
### 9.6.1
### 9.6.2
### 9.6.3
### 9.6.4
### 9.6.5
### 9.6.6
### 9.6.7
## 9.7
### 9.7.1
### 9.7.2
### 9.7.3
### 9.7.4
### 9.7.5
### 9.7.6
### 9.7.7
# 10
## 10.1
### 10.1.1
### 10.1.2
### 10.1.3
### 10.1.4
### 10.1.5
### 10.1.6
### 10.1.7
## 10.2
### 10.2.1
### 10.2.2
### 10.2.3
### 10.2.4
### 10.2.5
### 10.2.6
### 10.2.7
## 10.3
### 10.3.1
### 10.3.2
### 10.3.3
### 10.3.4
### 10.3.5
### 10.3.6
### 10.3.7
## 10.4
### 10.4.1
### 10.4.2
### 10.4.3
### 10.4.4
### 10.4.5
### 10.4.6
### 10.4.7
## 10.5
### 10.5.1
### 10.5.2
### 10.5.3
### 10.5.4
### 10.5.5
### 10.5.6
### 10.5.7
## 10.6
### 10.6.1
### 10.6.2
### 10.6.3
### 10.6.4
### 10.6.5
### 10.6.6
### 10.6.7
## 10.7
### 10.7.1
### 10.7.2
### 10.7.3
### 10.7.4
### 10.7.5
### 10.7.6
### 10.7.7

request

response

session

ArrrayList<Type>

html

js?
