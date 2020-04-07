# start (flask)
# 关于个模块的激活
model.init()
试试??

```html
<script src="{{url_for('static',filename='./layui/layui.all.js')}}"></script>

<link rel="stylesheet" href="{{url_for('static',filename='./layui/css/layui.css')}}">


function hello(){
      var layer = layui.layer;
      var form = layui.form;

      layer.msg('Hello World');
}
```

CSS内置公共基础类
类名（class）   说明
布局 / 容器
layui-main  用于设置一个宽度为 1140px 的水平居中块（无响应式）
layui-inline    用于将标签设为内联块状元素
layui-box   用于排除一些UI框架（如Bootstrap）强制将全部元素设为box-sizing: border-box所引发的尺寸偏差
layui-clear 用于消除浮动（一般不怎么常用，因为layui几乎没用到浮动）
layui-btn-container 用于定义按钮的父容器。（layui 2.2.5 新增）
layui-btn-fluid 用于定义流体按钮。即宽度最大化适应。（layui 2.2.5 新增）
辅助
layui-icon  用于图标
layui-elip  用于单行文本溢出省略
layui-unselect  用于屏蔽选中
layui-disabled  用于设置元素不可点击状态
layui-circle    用于设置元素为圆形
layui-show  用于显示块状元素
layui-hide  用于隐藏元素
文本
layui-text  定义一段文本区域（如文章），该区域内的特殊标签（如a、li、em等）将会进行相应处理
layui-word-aux  灰色标注性文字，左右会有间隔
背景色
layui-bg-red    用于设置元素赤色背景
layui-bg-orange 用于设置元素橙色背景
layui-bg-green  用于设置元素墨绿色背景（主色调）
layui-bg-cyan   用于设置元素藏青色背景
layui-bg-blue   用于设置元素蓝色背景
layui-bg-black  用于设置元素经典黑色背景
layui-bg-gray   用于设置元素经典灰色背景


# 栅格系统
layui-row
    layui-col-md* [layui-col-md-offset* |  layui-col-space5]
        div

一、栅格布局规则：

1.  采用 layui-row 来定义行，如：<div class="layui-row"></div>

2.  采用类似 layui-col-md* 这样的预设类来定义一组列（column），且放在行（row）内。其中：
变量md 代表的是不同屏幕下的标记（可选值见下文）
变量* 代表的是该列所占用的12等分数（如6/12），可选值为 1 - 12
如果多个列的“等分数值”总和等于12，则刚好满行排列。如果大于12，多余的列将自动另起一行。

3.  列可以同时出现最多四种不同的组合，分别是：xs（超小屏幕，如手机）、sm（小屏幕，如平板）、md（桌面中等屏幕）、lg（桌面大型屏幕），以呈现更加动态灵活的布局。

4.  可对列追加类似 layui-col-space5、 layui-col-md-offset3 这样的预设类来定义列的间距和偏移。

5.  最后，在列（column）元素中放入你自己的任意元素填充内容，完成布局！

不要放太大了..
xs 最好把..效果上

<div class="layui-row">
  <div class="layui-col-md3 layui-bg-orange">
    <div class="grid-demo">内容1</div>
  </div>
  <div class="layui-col-md6 layui-bg-blue">
    <div class="grid-demo">内容1</div>
  </div>
  <div class="layui-col-md3 layui-bg-black">
    <div class="grid-demo">内容1</div>
  </div>
</div>


四、布局容器：

将栅格放入一个带有 class="layui-container" 的特定的容器中，以便在小屏幕以上的设备中固定宽度，让列可控。

当然，你还可以不固定容器宽度。将栅格或其它元素放入一个带有 class="layui-fluid" 的容器中，那么宽度将不会固定，而是 100% 适应

五、列间距：

通过“列间距”的预设类，来设定列之间的间距。且一行中最左的列不会出现左边距，最右的列不会出现右边距。列间距在保证排版美观的同时，还可以进一步保证分列的宽度精细程度。我们结合网页常用的边距，预设了 12 种不同尺寸的边距，分别是：
layui-col-space1    列之间间隔 1px
layui-col-space3    列之间间隔 3px
layui-col-space5    列之间间隔 5px
layui-col-space8    列之间间隔 8px
layui-col-space10   列之间间隔 10px
layui-col-space12   列之间间隔 12px
layui-col-space15   列之间间隔 15px
layui-col-space18   列之间间隔 18px
layui-col-space20   列之间间隔 20px
layui-col-space22   列之间间隔 22px
layui-col-space28   列之间间隔 28px
layui-col-space30   列之间间隔 30px


六、列偏移：

对列追加 类似 layui-col-md-offset* 的预设类，从而让列向右偏移。其中 * 号代表的是偏移占据的列数，可选中为 1 - 12。
如：layui-col-md-offset3，即代表在“中型桌面屏幕”下，让该列向右偏移3个列宽度

下面是一个采用“列偏移”机制让两个列左右对齐的实例

七、栅格嵌套：

理论上，你可以对栅格进行无穷层次的嵌套，这更加增强了栅格的表现能力。而嵌套的使用非常简单。在列元素（layui-col-md`*`）中插入一个行元素（layui-row），即可完成嵌套。下面是一个简单的例子


八、让IE8/9兼容栅格
事实上IE8和IE9并不支持媒体查询（Media Queries），但你可以使用下面的补丁完美兼容！该补丁来自于开源社区：

codelayui.code
<!-- 让IE8/9支持媒体查询，从而兼容栅格 -->
<!--[if lt IE 9]>
  <script src="https://cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <script src="https://cdn.staticfile.org/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->

将上述代码放入你页面 <body> 标签内的任意位置


# 颜色
常用主色 #009688 通常用于按钮、及任何修饰元素 #5FB878 一般用于选中状态 #393D49 通常用于导航 #1E9FFF 比较适合一些鲜艳色系的页面
layui 主要是以象征包容的墨绿作为主色调，由于它给人以深沉感，所以通常会以浅黑色的作为其陪衬，又会以蓝色这种比较鲜艳的色调来弥补它的色觉疲劳，整体让人清新自然，愈发耐看。【取色意义】：我们执着于务实，不盲目攀比，又始终不忘绽放活力。这正是 layui 所追求的价值。

场景色
#FFB800 暖色系，一般用于提示性元素 #FF5722 比较引人注意的颜色 #01AAED 用于文字着色，如链接文本 #2F4056
侧边或底部普遍采用的颜色

事实上，layui 并非不敢去尝试一些亮丽的颜色，但许多情况下一个它可能并不是那么合适，所以我们把这些颜色归为“场景色”，即按照实际场景来呈现对应的颜色，比如你想给人以警觉感，可以尝试用上面的红色。他们一般会出现在 layui 的按钮、提示和修饰性元素，以及一些侧边元素上。

极简中性色
他们一般用于背景、边框等

#F0F0F0 #f2f2f2 #eeeeee #e2e2e2 #dddddd #d2d2d2 #c2c2c2
layui 认为灰色系代表极简，因为这是一种神奇的颜色，几乎可以与任何元素搭配，不易形成视觉疲劳，且永远不会过时。低调而优雅！

内置的背景色CSS类
layui 内置了七种背景色，以便你用于各种元素中，如：徽章、分割线、导航等等

赤色：class="layui-bg-red"
橙色：class="layui-bg-orange"
墨绿：class="layui-bg-green"
藏青：class="layui-bg-cyan"
蓝色：class="layui-bg-blue"
雅黑：class="layui-bg-black"
银灰：class="layui-bg-gray"
结语
“不热衷于视觉设计的程序猿不是一个好作家！” ——贤心


# 图标
i.layui-icon layui-icon-face-smile{[&#xe60c;]}

通过对一个内联元素（一般推荐用 i标签）设定 class="layui-icon"，来定义一个图标，然后对元素加上图标对应的 font-class（注意：layui 2.3.0 之前只支持采用 unicode 字符)，即可显示出你想要的图标，譬如：

codelayui.code
从 layui 2.3.0 开始，支持 font-class 的形式定义图标：
<i class="layui-icon layui-icon-face-smile"></i>

codelayui.code
注意：在 layui 2.3.0 之前的版本，只能设置 unicode 来定义图标
<i class="layui-icon">&#xe60c;</i>
其中的 &#xe60c; 即是图标对应的 unicode 字符


你可以去定义它的颜色或者大小，如：
<i class="layui-icon layui-icon-face-smile" style="font-size: 30px; color: #1E9FFF;"></i>


# 动画
div.lauui-anim layui-anim-*

动画的使用非常简单，直接对元素赋值动画特定的 class 类名即可。如：

codelayui.code
其中 layui-anim 是必须的，后面跟着的即是不同的动画类
<div class="layui-anim layui-anim-up"></div>

循环动画，追加：layui-anim-loop
<div class="layui-anim layui-anim-up layui-anim-loop"></div>

从最底部往上滑入
layui-anim-up

微微往上滑入
layui-anim-upbit

平滑放大
layui-anim-scale

弹簧式放大
layui-anim-scaleSpring

渐现
layui-anim-fadein

渐隐
layui-anim-fadeout

360度旋转
layui-anim-rotate

循环动画
追加：layui-anim-loop



# 按钮
.layui-btn layui-btn-lg layui-btn-radius layui-btn-normal

.layui-container

.layui-btn-group


用法
codelayui.code
<button class="layui-btn">一个标准的按钮</button>
<a href="http://www.layui.com" class="layui-btn">一个可跳转的按钮</a>

主题
原始  class="layui-btn layui-btn-primary"
默认  class="layui-btn"
百搭  class="layui-btn layui-btn-normal"
暖色  class="layui-btn layui-btn-warm"
警告  class="layui-btn layui-btn-danger"
禁用  class="layui-btn layui-btn-disabled"

尺寸  组合
大型  class="layui-btn layui-btn-lg"
默认  class="layui-btn"
小型  class="layui-btn layui-btn-sm"
迷你  class="layui-btn layui-btn-xs"

大型百搭    class="layui-btn layui-btn-lg layui-btn-normal"
正常暖色    class="layui-btn layui-btn-warm"
小型警告    class="layui-btn layui-btn-sm layui-btn-danger"
迷你禁用    class="layui-btn layui-btn-xs layui-btn-disabled"

<button class="layui-btn layui-btn-fluid">流体按钮（最大化适应）</button>

圆角
原始  class="layui-btn layui-btn-radius layui-btn-primary"
默认  class="layui-btn layui-btn-radius"
百搭  class="layui-btn layui-btn-radius layui-btn-normal"
暖色  class="layui-btn layui-btn-radius layui-btn-warm"
警告  class="layui-btn layui-btn-radius layui-btn-danger"
禁用  class="layui-btn layui-btn-radius layui-btn-disabled"

尺寸  组合
大型百搭    class="layui-btn layui-btn-lg layui-btn-radius layui-btn-normal"
小型警告    class="layui-btn layui-btn-sm layui-btn-radius layui-btn-danger"
迷你禁用    class="layui-btn layui-btn-xs layui-btn-radius layui-btn-disabled"


将按钮放入一个class="layui-btn-group"元素中，即可形成按钮组，按钮本身仍然可以随意搭配
<div class="layui-btn-group">
  <button class="layui-btn">增加</button>
  <button class="layui-btn">编辑</button>
  <button class="layui-btn">删除</button>
</div>

按钮容器
尽管按钮在同节点并排时会自动拉开间距，但在按钮太多的情况，效果并不是很美好。因为你需要用到按钮容器
<div class="layui-btn-container">
  <button class="layui-btn">按钮一</button>
  <button class="layui-btn">按钮二</button>
  <button class="layui-btn">按钮三</button>
</div>

# tab 页面
layui-tab
    layui-tab-title
        li[.layui-this]
    layui-tab-content
        layui-tab-item [layui-show]
        ...

<div class="layui-tab">
  <ul class="layui-tab-title">
    <li class="layui-this">网站设置</li>
    <li>用户管理</li>
    <li>权限分配</li>
    <li>商品管理</li>
    <li>订单管理</li>
  </ul>
  <div class="layui-tab-content">
    <div class="layui-tab-item layui-show">内容1</div>
    <div class="layui-tab-item">内容2</div>
    <div class="layui-tab-item">内容3</div>
    <div class="layui-tab-item">内容4</div>
    <div class="layui-tab-item">内容5</div>
  </div>
</div>

带删除的Tab
你可以对父层容器设置属性 lay-allowClose="true" 来允许Tab选项卡被删除

通过追加class：layui-tab-card来设定卡片风格

通过追加class：layui-tab-brief 来设定简洁风格。

提示
无论是导航、还是Tab，都需依赖 element模块，大部分行为都是在加载完该模块后自动完成的，但一些交互操作，如Tab事件监听等，需按照场景选择性使用。你可以移步文档左侧【内置组件 - 基本元素操作 element】了解详情

同样的还有增加选项卡和删除选项卡，都需要用到 lay-id，更多动态操作请阅读：element模块


# 进度条
div.layui-progress.layu-progress-big[lay-showPercent="true"]>div.layui-progress-bar[lay-percent="10%"]

<div class="layui-progress layui-progress-big " lay-showPercent="true">
  <div class="layui-progress-bar" lay-percent="10%"></div>
</div>

# 表格
layui-table
    colgroup
        col[width="100px"]
    thead
        tr
            th
    tbody
        tr
            td
            ...
        ...

table.layui-table>(colgroup>(col[width="100px"]{定义表格大小等})*3+(thead>tr>th*3)+(tbody>(tr>td*3)*3))

属性名 属性值 备注
lay-even    无   用于开启 隔行 背景，可与其它属性一起使用
lay-skin="属性值"  line （行边框风格）
row （列边框风格）
nob （无边框风格） 若使用默认风格不设置该属性即可
lay-size="属性值"  sm （小尺寸）
lg （大尺寸）    若使用默认尺寸不设置该属

<table class="layui-table" lay-skin="line">
  行边框表格（内部结构参见右侧目录“常规用法”）
</table>

<table class="layui-table" lay-skin="row">
  列边框表格（内部结构参见右侧目录“常规用法”）
</table>

<table class="layui-table" lay-even lay-skin="nob">
  无边框表格（内部结构参见右侧目录“常规用法”）
</table>

# 徽章?
<span class="layui-badge-rim">6</span>
layui-badge-dot 圆点
layui-badge  椭圆体
layui-badge-rim  边框体

# 时间线
ul.layui-timeline
    li.layui-timeline-item
        li.layui-icon layui-timeline-axis
        div.layui-timeline-content layui-text
        .layui-timeline-title
        p.main
```emment
ul.layui-timeline>((lilayui-timeline-item>(li.layui-icon.layui-timeline-axis{&#xe63f;}+div.layui-timeline-content.layui-text>(h3.layui-timeline-title+p{内容}))))*2
```

form.layui-form>(div.layui-form-item>(label.layui-form-label{输入框}+div.layui-input-block>input))

<form class="layui-form" action="">
  <div class="layui-form-item">
    <label class="layui-form-label">输入框</label>
    <div class="layui-input-block">
      <input type="text" name="title" required  lay-verify="required" placeholder="请输入标题" autocomplete="off" class="layui-input">
    </div>
  </div>
</form>

在一个容器中设定 class="layui-form" 来标识一个表单元素块，通过规范好的HTML结构及CSS类，来组装成各式各样的表单元素，并通过内置的 form模块 来完成各种交互。
依赖加载模块：form （请注意：如果不加载form模块，select、checkbox、radio等将无法显示，并且无法使用form相关功能）
form.render()
最后用..

.layui-input-block {
    /* margin-left: 110px; */
    min-height: 36px;
    float: left;
}