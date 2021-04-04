import pygame
#====窗口的相关操作====
# 创建一个窗口
screen = pygame.display.set_mode(width,hight)   
#width 窗口的宽  hight 窗口的高
# 设置窗口标题
pygame.display.set_caption("窗口标题")
# 加载资源图片，返回图片对象
image = pygame.image.load("图片的路径")
# 设置窗口图标
pygame.display.set_icon(image)
# 指定坐标，将图片绘制到窗口
window.blit(image, (0, 0))
# ----------图像相关操作-----------
# 加载图片文件，返回图片对象
image = pygame.image.load("图片
路径")
# 获得图片矩形对象 -> Rect(x, y, width, height)
# 默认情况下左上角的坐标是 (0, 0)
rect = image.get_rect(centerx=x, centery=y)
# 在原位置基础上，移动指定的偏移量 (x, y 增加)
rect.move_ip(num1, num2)
# 判断两个矩形是否相交，相交返回True，否则返回
Falseflag = pygame.Rect.colliderect(rect1, rect2)
# 将图片对象按指定宽高缩放，返回新的图片对象
trans_image = pygame.transform.scale(image, (WINDOWWIDTH, WINDOWHEIGHT))
# ----------事件相关操作和游戏的监听-----------
# 常见事件类型：
# QUIT　关闭窗口
# KEYDOWN　键盘按键
# 获得当前所有持续按键 bools_tuple
# 获得所有事件的列表
event_list = pygame.event.get()for event in event_list:   
# 1. 鼠标点击关闭窗口事件   
if event.type == pygame.QUIT:        print("关闭了窗口")        exit()   
# 2. 键盘按下事件   
if event.type == pygame.KEYDOWN:       
# 判断用户按下的键是否是a键       
if event.key == pygame.K_a:            print("按了 a ")        if event.key == pygame.K_UP:            print("按了 方向键上")
# 3. 获得当前键盘所有按键的状态(按下，没有按下)，返回bool元组
pressed_keys = pygame.key.get_pressed()if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:    print("按了 w 键，或者 方向键上")
# ----------音效相关操作-----------
# 加载背景音乐
pygame.mixer.music.load("./res/音乐文件名")
# 循环播放背景音乐
pygame.mixer.music.play(-1) # 参数表示重复播放几次,-1表示无限循环
# 停止背景音乐
pygame.mixer.music.stop()
# 加载音效
boom_sound = pygame.mixer.Sound("./res/音效名")
# 播放音效
boom_sound.play()
boom_sound.stop()
三基色：Red Green Blue0 ~ 255
# -------- 文字显示操作
font = pygame.font.SysFont('SimHei', 字体大小)
# render(text(文本内容), antialias(抗锯齿), color(RGB))，返回文字对象
textobj = font.render(text, 1, (200, 200, 200))
# 设置文字矩形对象位置
textrect = textobj.get_rect()textrect.move_ip(水平偏移量, 竖直偏移量)
# 在指定位置绘制指定文字对象
window.blit(textobj, textrect)
# 更新界面
pygame.display.update()

作者：会说话的乌鸦
链接：https://www.jianshu.com/p/68cc2255d83f
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。