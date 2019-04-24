# 安装
pip install PyOpenGL_accelerate PyOpenGL
or
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl


# 移动,变换
glTranslatef

# 旋转
glRotatef

# 缩放
glScale


初始化窗口
11~17行基本也是固定的，
glutInit()是用glut来初始化OpenGL的，所有的问题都交给这个函数吧，基本不用管，虽说可以接受参数的，基本无用。
glutInitDisplayMode(MODE)非常重要，这里告诉系统我们需要一个怎样显示模式。至于其参数GLUT_RGBA就是使用(red,
green, blue)的颜色系统。有没有写错？这里有个A啊，不应该是(red, green, blue,
alpha)么？大概是历史原因，GLUT_RGBA和GLUT_RGB是其实是等价的（坑爹啊），要想实现Alpha还得用其他的参数。而GLUT_SINGLE意味着所有的绘图操作都直接在显示的窗口执行，相对的，我们还有一个双缓冲的窗口，对于动画来说非常合适。看看用Python和Pygame写游戏-从入门到精通（3）有些说明。
glutInitWindowSize(400,
400)这个函数很容易理解，设置出现的窗口的大小。实际上还有个glutInitWindowPosition()也很常用，用来设置窗口出现的位置。
glutCreateWindow(“First”)，一旦调用了，就出现一个窗口了，参数就是窗口的标题。
glutDisplayFunc(func)是glut非常讨人喜欢的一个功能，它注册了一个函数，用来绘制OpenGL窗口，这个函数里就写着很多OpenGL的绘图操作等命令，也就是我们主要要学习的东西。
glutMainLoop()，主循环，一旦调用了，我们的OpenGL就一直运行下去了。和很多程序中的主循环一样，不停的运行，画出即时的图像，处理输入等。
绘图
看看drawFunc里的几句话，这里是实际绘图的函数。
glClear(GL_COLOR_BUFFER_BIT)是把先前的画面给清除，这基本是定律，每次重绘之前都要把原来的画面擦除，否则叠加起来什么都看不出了。glClear一看就知道是OpenGL原生的命令，而参数就是指明要清除的buffer。大家一定会有疑问，我们清除，不就是清除屏幕上的画面么，为什么还要指定？OpenGL的博大精深这里就体现出来了，buffer不仅仅有我们看到的那个GL_COLOR_BUFFER_BIT，OpenGL中还有其他的buffer类型，我们会在后面的章节讲到。
glutWireTeapot(0.5)是glut提供的绘制犹他茶壶的工具函数，茶壶还是相当复杂的一个几何体，用这个函数一下子就画出来了，不过基本也就演示用用。这里是用的线模型，因为没有说光照和材质，如果glutSolidTeapot()画出来就成纸片儿了。
glFlush()似乎不用多说，画了那么多，自然要刷新一下显示。不过，这里的刷新不仅仅是屏幕上的更新，实际上，它是处理OpenGL的渲染流水线，让所有排队中的命令得到执行。OpenGL的渲染流水线是一个很重要的概念，不过这里暂时还不打算多说明，否则对初学者来说，未免有些麻烦了。但是这并不意味着可以无视这些基础，知道怎么做只能让你优秀，知道为什么这么做才能让你卓越。
小惊喜
现在你可以把注释的两个语句打开了，执行以下看到什么？旋转的茶壶！不得不说帅多了~
glutIdleFunc(Func)又是一个激动人心的函数，可以让OpenGL在闲暇之余，调用一下注册的函数，这是是产生动画的绝好方法。
glRotatef(1, 0, 1,
0)是一个我们以后会详细讲的函数，简单来说四个参数第一个是角度，后三个是一个向量，意义就是绕着这个向量旋转，这里是绕着Y轴旋转1°。这一度一度的累加，最后使得茶壶围绕Y轴不停的旋转。从这里我们也能看出来，我们指定了一个旋转的角度后，重新绘制并不会复位，而是在上一次旋转的结果上继续旋转。这是一个非常重要的概念，OpenGL是一个状态机，一旦你指定了某种状态，知道再指定位置，它会保持那种状态。不仅仅是旋转，包括以后的光照贴图等等，都遵循这样的规律。
好了，我们有了第一个PyOpenGL程序了，虽然离我们详细中的五光十色的立体世界还有些差距，不过毕竟画了点东西出来了（要知道，犹他茶壶在3D技术发展之初，是里程碑一般的作品）。慢慢的，我们会充实自己的知识，绘制出更靓丽的画面。

作者：红薯爱帅
链接：https://www.jianshu.com/p/21de4eb4d674
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


glViewport：指定了视口程序显示的范围，也就是OpenGL绘制的范围，这里使用(0, 0, w,
h)便是说明整个窗口，一般情况下总是如此，但是我们也是可以指定小于这个范围的ViewPort的。事实上我隐瞒了很多细节，这个函数必须和下面要讲的gluOrtho2D函数一起用才能出现正确的结果。
gluOrtho2D：这个函数派生于OpenGL的glOrtho，它创建了一个正交的视景体（View
Volume），我们所看到的物体，都处在这个体中，四个参数分别代表了(left, right, bottom,
top)，也就是竖直的左右边界和水平的下上边界；而近远则是默认的（-1，
1），glOrtho有六个参数可以设定。这个体越大，我们看到的东西就越小；反之看到的东西就越大。我知道这样很难理解，打个比方就是一个六边形的鱼缸，这个函数定出了一个鱼缸的大小，我们所看的东西呢，都在这个鱼缸里面。
上面说glViewport要和gluOrtho2D一起用才能正确显示是个什么意思呢？gluOrtho2D只管创建一个视体，而glViewport只管绘图的范围，如果视体是个正方体，而窗口是个长方体，直接绘制的结果会是什么呢？很明显，整个视体里的东西都被拉长了，而一般我们viewport都是指明了窗口大小，自然只能修改视体来适应各种不同的比例了。
修改代码，拉伸窗口，查看最终的结果会是怎样的。
glMatrixMode：这个函数非常难以理解，但是又极其重要！这关系到了OpenGL中的“矩阵”的概念。矩阵……你是说黑客帝国么？好像很有趣诶~~
嗯嗯没错，矩阵是个伟大的东西，通过它，3D世界的所有维度都蜷曲到内存中的一维数据里去了。这是一个有点儿抽象的概念但其实也没什么特别的，OpenGL里有如下几种矩阵：
GL_MODELVIEW：模型观察矩阵，表示物体的位置变化和观察点的改变；
GL_PROJECTION：投影矩阵，描述如何将一个物体投影到平面上； GL_TEXTURE：纹理矩阵，描述纹理坐标的动态变化 …
我不想搬出一堆数字和大括号来说明矩阵的基本运算和应用（好吧其实真实原因是我也不会：），也不会告诉你最后的ModelView矩阵是View矩阵与Model矩阵的乘积，更不会告诉你有glRotate和glTranslate之流的函数来改变矩阵！暂时这么理解就好了，矩阵就是我们走路的方向，我们现在朝南走，看到的南边的风景，然后说“向右拐”，现在看到西边的风景了，再说“向后转”，现在看到东边的风景了。就是通过这样可以累积的变换，我们把我们最初的一些数据变成了更复杂的东西表达了出来，转了几圈后也许有点糊涂了，用glLoadIdentity将当前指定的矩阵还原为最初的状态。

作者：红薯爱帅
链接：https://www.jianshu.com/p/21de4eb4d674
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


# demo
```py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.6, 1, 1, 1)
    glutWireTeapot(1)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
```