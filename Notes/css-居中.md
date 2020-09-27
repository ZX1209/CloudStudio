水平居中
1) 若是行内元素, 给其父元素设置 text-align:center,即可实现行内元素水平居中.

2) 若是块级元素, 该元素设置 margin:0 auto即可.

3) 若子元素包含 float:left 属性, 为了让子元素水平居中, 则可让父元素宽度设置为fit-content,并且配合margin, 作如下设置:

.parent{
      width: -moz-fit-content;
    width: -webkit-fit-content;
    width:fit-content;
    margin:0 auto;
}
注意是父元素,再上级就不行了

fit-content是CSS3中给width属性新加的一个属性值,它配合margin可以轻松实现水平居中, 目前只支持Chrome 和 Firefox浏览器.

4) 使用flex 2012年版本布局, 可以轻松的实现水平居中, 子元素设置如下:

.son{
    display: flex;
    justify-content: center;
}

>https://louiszhai.github.io/2016/03/12/css-center/