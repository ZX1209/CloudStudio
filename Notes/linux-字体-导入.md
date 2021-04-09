> https://www.jianshu.com/p/fdcaab0a5230


执行 fc-list :lang=zh-cn 命令，查看Linux下是否包含要使用的中文字体。

复制字体
windows 的字体在 C:\Windows\Fonts 目录下
Linux 的字体一般在 /usr/share/fonts/ 目录下
可在/usr/share/fonts/ 下建立一个 winfonts 目录放要复制的windows 字体。

导入字体
复制完成后，命令行下依次执行下面三条命令（root用户无须加sudo）：

sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv

显示fc-cache:succeded说明安装成功


作者：ouyangan
链接：https://www.jianshu.com/p/fdcaab0a5230
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。