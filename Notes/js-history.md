History 对象
History 对象
History 对象包含用户（在浏览器窗口中）访问过的 URL。

History 对象是 window 对象的一部分，可通过 window.history 属性对其进行访问。

注释：没有应用于 History 对象的公开标准，不过所有浏览器都支持该对象。

# History 对象属性
属性  描述
length  返回浏览器历史列表中的 URL 数量。

# History 对象方法
方法  描述
back()  加载 history 列表中的前一个 URL。
forward()   加载 history 列表中的下一个 URL。
go()    加载 history 列表中的某个具体页面。
History 对象描述
History 对象最初设计来表示窗口的浏览历史。但出于隐私方面的原因，History 对象不再允许脚本访问已经访问过的实际 URL。唯一保持使用的功能只有 back()、forward() 和 go() 方法。

例子
下面一行代码执行的操作与单击后退按钮执行的操作一样：

history.back()
下面一行代码执行的操作与单击两次后退按钮执行的操作一样：

history.go(-2)