js.md

js-dom

js-window
window, navigator, screen, history, location

js-$special

js-synatx

# JavaScript 对象
JS Array
JS Boolean
JS Date
JS Math
JS Number
JS String
JS RegExp
JS Functions
JS Events

# js dom 顶层对象
对象  描述
Window  JavaScript 层级中的顶层对象。Window 对象表示浏览器窗口。每当 <body> 或者 <frameset> 标签出现，Window 对象就会被自动创建。
Navigator   包含客户端浏览器的信息。
Screen  包含客户端显示屏的信息。
History 包含了浏览器窗口访问过的 URL。
Location    包含了当前URL的信息。


window.location.href

# 获取与修改文本框的值(id)
document.getElementByID('ids').value  = ""
document.getElementByID('ids').onkeypress  = "command();"

# d
function some(){
	
}

# 
var i  = 0


domElement.sytle.background
# 标签 style 中 标明的.

# .style
m = documnet.getElementByClassName('main')
m[0].style.
一、使用obj.className来修改样式表的类名
从下面的代码可以看出ob.style.cssTest是如何来btnB的样式的。
```jsb
 function changeStyle1() {
            var obj = document.getElementById("btnB");
            obj.style.backgroundColor= "black";

  }
```
该段代码修改btB的文字的颜色，在浏览器中打开调试工具，可以发现btB标签中多了一个属性【style="background-color:black"】，从而改变btB的样式。

缺陷：
在修改btB的背景色之后用鼠标放到btB上可以发现，btB的伪类hover里面的css根本不起作用。原来是当你修改了这个这样样式之后。在btB的内联样式中多了background-color属性了，在css的应用中也是有级别的，嵌入式>内联式>外联式。而btB的hove伪类的background-color样式写在内联式中，所以嵌入式的background-color覆盖了伪类中，这就使得鼠标放入btB上感觉不到背景颜色的变化。

二、使用obj.style.cssTest来修改嵌入式的css
直接上JavaScript代码：

 function changeStyle2() {
            var obj = document.getElementById("btnB");
            obj.style.cssText = "background-color:black; display:block;color:White; 

}

该段代码和【一】中的效果是一样的，缺陷也是一样。

三、使用obj.className来修改样式表的类名
使用代码来修改btB引用样式的类名，如下段代码：

  function changeStyle3() {
            var obj = document.getElementById("btnB");
            //obj.className = "style2";
            obj.setAttribute("class", "style2");
    }

通过更改btB的css的类名的方式来更改样式，更改样式类名有两种方式。1、obj.className = "style2";  2、 obj.setAttribute("class", "style2");都是一样的效果。

用这种方式来修改css比上面的效果要好很多。

四、使用更改外联的css文件，从而改变元素的css

通过更改外联的css文件引用从而来更改btB的样式，操作很简单。代码如下：

首先得引用外联的css文件，代码如下：

<link href="css1.css" rel="stylesheet" type="text/css"  id="css"/>

function changeStyle4() {
            var obj = document.getElementById("css");
            obj.setAttribute("href","css2.css");
   }

这样也能方便的更改btB的样式，个人觉得这种方式是最好用的。是实现整体页面换肤的最佳方案。



===
# innerHTML
innerHTML与outerHTML的区别？
DOM元素的innerHTML, outerHTML, innerText, outerText属性的区别也经常被面试官问到， 比如对于这样一个HTML元素：
<div>content<br/></div>。

innerHTML：内部HTML，content<br/>；
outerHTML：外部HTML，<div>content<br/></div>；
innerText：内部文本，content ；
outerText：内部文本，content ；
上述四个属性不仅可以读取，还可以赋值。outerText和innerText的区别在于outerText赋值时会把标签一起赋值掉，另外xxText赋值时HTML特殊字符会被转义。 下图来源于：http://walsh.iteye.com/blog/261966

DOM content

jQuery的html()与innerHTML的区别？
jQuery的.html()会调用.innerHTML来操作，但同时也会catch异常，然后用.empty(), .append()来重新操作。 这是因为IE8中有些元素的.innerHTML是只读的。见：http://stackoverflow.com/questions/3563107/jquery-html-vs-innerhtml