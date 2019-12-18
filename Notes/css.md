# display 属性
block: 占整行
inline: 可在文字内
none: 隐藏,不占位置

# max-width


# 隐藏
display: none;

a:link
a:Visit
a:hover


# text-decoration下划线CSS单词值参数：
none : 　无装饰
blink : 　闪烁
underline : 　下划线
line-through : 　贯穿线
overline : 　上划线


# 整齐排列
float:left
> 或者是什么grid的,,不怎么用呢...
嗯,,clear: left;谨慎

# display 样式
inline
block
inline-block

# 字体
font-size:10px;
font-family
font-weight
font-height
# 字体大小
font-size

# 文本
text-align
text-indent
text-decoration
text-spacing
text-overflow
letter-spacing


# 边框属性
border-weight:10px;
border-style:[solid（默认实线），dotted（点线），dashed（虚线）];
border-color:red;
border:10px dotted red;...
## 阴影  圆角
border-radius:5px;
box-shadow: 2px 2px 5px #000;

transform: rotate(45deg); & transform-origin: 250px 150px;

# 颜色color的写法
单词：red，blue，yellow等；
十六进制：#000，#fff，#060606 等；
rgb形式：rgb(255,255,255)；
rgba形式：rgba(0,0,0,0.5) ，里面的a代表的是透明度，范围是`0~1`，数值越大越不透明；

# 隐藏和透明
透明（指的是元素不能被看见，但是位置依然被占据）
1.opacity:0~1：透明度，作用于整体，用得比较少；
2.visibility:hidden：元素可见度，表示该元素透明，位置依然占据；
3.background-color:rgba(0,0,0,0~1)：表示背景色的透明度，a的值为0时完全透明；
隐藏（指元素整体消失，并且不占据位置）
1.display:none：表示设置该元素消失，不占据位置也看不见；

# 线性变换

background: linear-gradient(217deg, rgba(255,0,0,.8), rgba(255,0,0,0) 70.71%),
            linear-gradient(127deg, rgba(0,255,0,.8), rgba(0,255,0,0) 70.71%),
            linear-gradient(336deg, rgba(0,0,255,.8), rgba(0,0,255,0) 70.71%);

从底向左,,度数增加
## inline css     (内联)

<p style="color:white">this is a example of inline css</p>

## embedded/internal css    (嵌入)

<style>p{color:white;}</style>



## external css    (外部)

<link rel="stylesheet" href="example.css">

> href:(**H**ypertext **REF**erence) (超文本参考)



## selector {property:value;[property:value; ...]}



## 注释

```css
/*这是注释*/
```


absolute 中的 absolute 相当于   revelate 呢






url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'\a     width='100' height='100' viewBox='0 0 100 100'%3E%3Cg \a     fill-rule='evenodd'%3E%3Cg \a     fill='%23d3c3db' fill-opacity='0.4'%3E%3Cpath opacity='.5'\a     d='M96 95h4v1h-4v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9zm-1 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9z'/%3E%3Cpath d='M6 5V0H5v5H0v1h5v94h1V6h94V5H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")



