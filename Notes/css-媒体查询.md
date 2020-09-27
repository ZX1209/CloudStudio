@media screen and (min-width:480px) 手机

@media screen and (min-width:768px) 平板

@media screen and (min-width:992px) 桌面显示器

@media screen and (min-width: 1200px){ 选择器{ 属性：值; } }  大于1200px时


CSS样式分为：内联式css样式、嵌入式css样式、外部式css样式

### 媒体查询 @media

媒体设备：all所有设备 screen所有屏幕设备（PC+移动端） print打印机设备。
媒体条件：指定在什么样的条件下指定对应样式 。

**方式一**：****（嵌入式css样式------这种是不推荐的，这样会使得html页面代码太繁琐）：

<style type="text/css">
@media screen and (max-width:768px){

//当屏幕宽度小于768px时，加载这里的样式
}
@media screen and (min-width:368px){

//当屏幕宽度大于368px时，加载这里的样式
} 

@media screen and (min-width:300px) and (max-width:600px){

//当屏幕宽度大于300px且小于600px时，加载这里的样式

}

@media all and (-webkit-device-pixel-ratio:2){

//二倍屏

}

</style>

**方式二：**（外部式css样式）

<!DOCTYPE html>
<html>
<head>
<title>Home</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<link rel="stylesheet" type="text/css" href="./font_icons/fonts.css">
<link rel="stylesheet" type="text/css" href="./css/common.css">
<link rel="stylesheet" media="screen and (max-width:768px)" href="./css/phone.css" />
<link rel="stylesheet" media="screen and (min-width:768px)" href="./css/tablet.css" />
<link rel="stylesheet" media="screen and (min-width:1024px)" href="./css/desktop.css" />
<link rel="stylesheet" media="screen and (min-width:1200px)" href="./css/desktop_hd.css" />
</head>
注：书写顺序一定不能差

在真实项目中，设计师的设计稿一般是：640*1136 或 640*960 或 750*1334。

CSS3中的媒体查询，可以在不同分辨率下对元素重新设置样式（不只是尺寸），在不同屏幕下可以显示不同版式。

@media screen and (min-width:480px) 手机

@media screen and (min-width:768px) 平板

@media screen and (min-width:992px) 桌面显示器

@media screen and (min-width: 1200px){ 选择器{ 属性：值; } }  大于1200px时

这四个值是常用的，注意先后顺序，小的在前大的在后。