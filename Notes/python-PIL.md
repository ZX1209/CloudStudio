from PIL import Image

bmpFile = Image.open(r'bmp/FLAG_B24.BMP')
bmpFile.close()
`
['BITFIELDS', 'COMPRESSIONS', 'JPEG', 'PNG', 'RAW', 'RLE4', 'RLE8', '_Image__transformer', '__array_interface__', '__class__', '__copy__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bitmap', '_close_exclusive_fp_after_loading', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_expand', '_min_frame', '_new', '_open', '_repr_png_', '_seek_check', 'alpha_composite', 'category', 'close', 'convert', 'copy', 'crop', 'decoderconfig', 'decodermaxblock', 'draft', 'effect_spread', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'fromstring', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'height', 'histogram', 'im', 'info', 'load', 'load_end', 'load_prepare', 'mode', 'offset', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'pyaccess', 'quantize', 'readonly', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'tostring', 'transform', 'transpose', 'verify', 'width']
`
bmpFile.format, bmpFile.size, bmpFile.mode
bmpFile.width,bmpFile.height

bmpFile.show()

bmpFile.getpixel((x,y))

# 点集操作
out = bmpFile.point(lambda i:i//2)
out.show()

# 颜色模式转换
#"1",“L”, “RGB” and “CMYK.”
out = bmpFile.convert("L")
out.show()

# resize
out = bmpFile.resize((500,500))
out.show()

# 图像旋转
out = bmpFile.rotate(45)
out.show()

# 分离与合并通道
r, g, b = bmpFile.split()
im = Image.merge("RGB", (b, g, r))


# 剪切粘贴和合并图像
Image类包含维护图像里区块的方法。为了从图像里抽取一个子矩形，使用crop()方法。

复制一个子矩形
box = (100, 100, 400, 400)
region = im.crop(box)
使用包含4个元素的元组来定义区块，相匹配的坐标是（左上右下）。PIL使用一个坐标系统，原点位于左上角。坐标系统使用像素来引用位置，所以上例中的区块大小是300x300像素。

现在这个区块可以以某种方式处理和粘贴了。

处理子矩形并粘贴
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
当粘贴回的时候，区块大小必须精确匹配已给的区块大小。另外，这个区块不能扩展到外部图像。但是，原始图像的模式必须和区块的模式匹配。如果他们比匹配，区块会提前动转换为匹配的模式。


Image是pillow库中一个非常重要的模块，提供了大量用于图像处理的方法。使用该模块时，首先需要导入。
>>> from PIL import Image
接下来，我们通过几个示例来简单演示一下这个模块的用法。
（1）打开图像文件
>>> im = Image.open('sample.jpg')
（2）显示图像
>>> im.show()
（3）查看图像信息
>>> im.format  #查看图像格式
'JPEG'
>>> im.size  #查看图像大小，格式为（宽度, 高度）
(200, 100)
>>> im.height #查看图像高度
100
>>> im.width  #查看图像宽度
200
（4）查看图像直方图
>>> im.histogram() #如果图像包含多个通道，则返回所有通道的直方图
>>> im.histogram()[:256] #查看第一个通道的直方图
（5）读取像素值
>>> im.getpixel((150, 80)) #参数必须是元组，两个元素分别表示x和y坐标
(255, 248, 220) #返回值分别表示红、绿、蓝三原色分量的值
（6）设置像素值，通过读取和修改图像像素值可以实现图像点运算
>>> im.putpixel((100,50), (128,30,120))  #第二个参数用来指定目标像素的颜色值
小提示：在使用时应注意图像文件的格式，这里演示的是24位颜色深度的图像，如果是256色的图像文件，那么getpixel()的返回值只是一个数字，而putpixel()的第二个参数也只需要一个数字就可以了。
（7）保存图像文件
>>> im.save('sample1.jpg')  #可以把图像保存为另一个文件
>>> im.save('sample.bmp')    #通过该方法也可以进行格式转换
>>> def img2jpg(imgFile):   #转换图像文件格式
     if type(imgFile)==str and imgFile.endswith(('.bmp', '.gif', '.png')):
          with Image.open(imgFile) as im:
              im.convert('RGB').save(imgFile[:-3]+'jpg')
>>> img2jpg('1.gif')
>>> img2jpg('1.bmp')
>>> img2jpg('1.png')
（8）图像缩放
>>> im = im.resize((100,100))  #参数表示图像的新尺寸，分别表示宽度和高度
（9）旋转图像，rotate()方法支持任意角度的旋转，而transpose()方法支持部分特殊角度的旋转，如90、180、270度旋转以及水平、垂直翻转等等。
>>> im = im.rotate(90)   #逆时针旋转90度
>>> im = im.transpose(Image.ROTATE_180)  #逆时针旋转180度
>>> im = im.transpose(Image.FLIP_LEFT_RIGHT)   #水平翻转
>>> im = im.transpose(Image.FLIP_TOP_BOTTOM)  #垂直翻转
（10）图像裁剪与粘贴
>>> box = (120, 194, 220, 294)  #定义裁剪区域
>>> region = im.crop(box)  #裁剪
>>> region = region.transpose(Image.ROTATE_180)
>>> im.paste(region,box)  #粘贴
（11）图像通道分离与合并
>>> r, g, b = im.split()  #将彩色图像分离为同样大小的红、绿、蓝三分量子图
>>> imNew = Image.merge(im.mode, (r,g,b))
（12）创建缩略图
>>> im.thumbnail((50, 20)) #参数为缩略图尺寸
>>> im.save('2.jpg')  #保存缩略图
（13）屏幕截图
>>> from PIL import ImageGrab
>>> im = ImageGrab.grab((0,0,800,200)) #截取屏幕指定区域的图像
>>> im = ImageGrab.grab()   #不带参数表示全屏幕截图
（14）图像增强
>>> from PIL import ImageFilter
>>> im = im.filter(ImageFilter.DETAIL)   #创建滤波器，使用不同的卷积核
>>> im = im.filter(ImageFilter.EDGE_ENHANCE) #边缘增强
>>> im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)  #边缘增强
（15）图像模糊
>>> im = im.filter(ImageFilter.BLUR)
>>> im = im.filter(ImageFilter.GaussianBlur)  #高斯模糊
>>> im.filter(ImageFilter.MedianFilter) #中值滤波
（16）图像边缘提取
>>> im = im.filter(ImageFilter.FIND_EDGES)
（17）图像点运算
>>> im = im.point(lambda i:i*1.3)  #整体变亮
>>> im = im.point(lambda i:i*0.7)  #整体变暗
>>> im = im.point(lambda i: i*1.8 if i<100 else i*0.7) #自定义调整图像明暗度
也使用图像增强模块来实现上面类似的功能，例如
>>> from PIL import ImageEnhance
>>> enh = ImageEnhance.Brightness(im)
>>> enh.enhance(1.3).show()
（18）图像冷暖色调整
>>> r, g, b = im.split()   #分离图像
>>> r = r.point(lambda i:i*1.3)  #红色分量变为原来的1.3倍
>>> g = g.point(lambda i:i*0.9) #绿色分量变为原来的0.9
>>> b = b.point(lambda i:0) #把蓝色分量变为0
>>> im = Image.merge(im.mode,(r,g,b)) #合并图像
>>> im.show()
（19）图像对比度增强
>>> from PIL import ImageEnhance
>>> im = ImageEnhance.Contrast(im)
>>> im = im.enhance(1.3) #对比度增强为原来的1.3倍