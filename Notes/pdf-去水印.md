## pdf 图片分离
pdfimages -j sourcefile  imageroot(with file suffix)

## 多余图片分离
最多的还是pdf中图片合成的,,这个一般拆解pdf成图片
将多余图片分离即可
一般可以通过文件大小排除,
{ find ./ -size +833k ; find ./ -size -100k ; } | xargs  rm


## 通道分离
有些pdf中的水印,在某些通道中不存在(单色)?,就可以通过分离通道来去除水印
但还是挺少的呢.
convert image-003.jpg  -channel R -separate separate_red.jpg


## 文字分离
简单,方法多

## 图像学分离
有些是直接将书上盖印章,这个一般只能用图像学寻找图像并消除.有些麻烦
除非能通道分离,

## 图像裁剪
pdf 的话有个krop还不错