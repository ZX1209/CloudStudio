> http://www.freeoa.net/scheme/manual/fonts-ttcfo_3395.html

三者都是字体文件格式，跟我们的工作生活都息息相关，以至于我们感觉不到它们的存在，本文对它们做一个简单的说明和对比。

TTF(TrueType Font)是Apple公司和Microsoft公司共同推出的字体文件格式，随着windows的流行，它已经变成最常用的一种字体文件表示方式，TrueType 会逐渐被OpenType 取代；OTF(OpenType Font)是 TTF 的升级版，它采用的是 PostScript 曲线，支持 OpenType 高级特性的更高级字体。


TTC全称是TrueType Collection，它是TrueType字体集成文件(.ttc文件)，是在一单独文件结构中包含多种字体，以便更有效地共享轮廓数据，当多种字体共享同一笔画时，TTC技术可有效地减小字体文件的大小。TTC的字体只有一些常用的汉字，而许多不常用的汉字就没有(选择字体以后依然以宋体显示)。TTC就是几个TTF合成的字库，安装后字体列表中会看到两个以上的字体。两个字体中大部分字都一样时，可以将两种字体做成一个TTC文件，常见的TTC字体，因为共享笔划数据，所以大多这个集合中的字体区别只是字符宽度不一样，以便适应不同的版面排版要求；而TTF字体则只包含一种字型。

虽然都是字体文件，但.ttc是microsoft开发的新一代字体格式标准，可以使多种truetype字体共享同一笔划信息，有效地节省了字体文件所占空间，增加了共享性。但是有些软件缺乏对这种格式字体的识别，使得ttc字体的编辑产生困难。

TTF 扩展名的 O 图标的表示 OpenType - TrueType 字体，采用的是 TrueType 曲线，不过支持 OpenType 的高级特性。

TTF 扩展名的 T 图标的表示 TrueType 字体，采用的是 TrueType 曲线，不支持 OpenType 特性。

OTF 扩展名的 O 图标的表示 OpenType - PostScript 字体，采用的是 PostScript 曲线，支持 OpenType 高级特性。

OTF主要优点：
1)增强的跨平台功能
2)更好的支持Unicode标准定义的国际字符集
3)支持高级印刷控制能力
4)生成的文件尺寸更小
5)支持在字符集中加入数字签名，保证文件的集成功能

OTF 格式是目前相对先进，TTF 格式也是目前相对主流，TTC 则是一系列 OTF 或者 TTF 字体的集合体。

OpenType 是 Microsoft 与 Adobe 共同制定的标准字体格式，在此之前有两大字体格式: TrueType 和 Type 1，两家合作制定出的 OpenType 将之前的两大格式都包含了进去，TrueType 进化成 OpenType - TrueType，在原有基础上增加了 OpenType 高级特性支持，扩展名不变 (TTF)，图标由 T 变为 O; Type 1 进化成 OpenType - PostScript，在原有基础上增加了 OpenType 高级特性支持，扩展名定位 OTF，图标为 O。

OpenType也叫Type 2字体，它也是一种轮廓字体，比TrueType更为强大，最明显的一个好处就是可以在把PostScript字体嵌入到TrueType的软件中。并且还支持多个平台，支持很大的字符集，还有版权保护，可以说它是Type 1和ueType的超集。这类字体的文件扩展名有.otf、.ttf、.ttc，类型代码是OTTO，现行标准为OpenType 1.8.2。OpenType最初发表于1996年，并在2000年之后出现大量字体。它源于微软公司的TrueType Open字体，TrueType Open字体又源于TrueType字体。OpenType font包括了Adobe CID-Keyed font技术；Adobe公司已经在2002年末将其字体库全部改用OpenType格式。到2005年大概有一万多种OpenType字体，Adobe产品占了三分之一。OpenType于2016年发布了1.8版规范，引入了“可变字体”的功能，支持通过调节一定的参数来自由改变文字的形状。

现在微软和 Adobe 都在努力干掉以往的 TrueType 和 Type 1 字体，比如 Windows 的系统字体在 Vista 以后全都由 TT 转换为 OT-TT (或许是向 OT-PS 的过渡)，而 Adobe 则大力推广 OT-PS 字体。

True Type是由美国Apple公司和Microsoft公司联合提出的一种新型数字化字形描述技术。这是一种彩色数字函数描述字体轮廓外形的一套内容丰富的指令集合，这些指令中包括字型构造、颜色填充、数字描述函数、流程条件控制、栅格处理器控制，附加提示信息控制等指令。采用了几何学中的二次B样条曲线及直线来描述字体的外形轮廓，二次B样条曲线具有一阶连续性和正切连续性。抛物线可由二次B样条曲线来精确表示，更为复杂的字体外形可用B样长曲线的数学特性以数条相接的二次B样条曲线及直线来表示。描述该类型字体的文件(内含字体描述信息、指令集、各种标记表格等)，可通用于MAC和PC平台。

2006、07年开始OT全面普及，到现在很多字体设计师与字体厂商已经不提供TTF版本的作品了，市面上的TT都是历史遗留产。adobe在2002年就把旗下产品全部换成OTF。