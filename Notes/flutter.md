

# basic layout
see flutter-basic-layout-tutorial.md
> https://flutter.dev/docs/codelabs/layout-basics

#  交互 教程 指南
https://flutter.dev/docs/development/ui/interactive

# notes
In unbounded constraints, they try to fit their children in that direction. In this case, you cannot set flex on the children to anything other than 0 (the default). In the widget library, this means that you cannot use Expanded when the flex box is inside another flex box or inside a scrollable. If you do, you’ll get an exception message pointing you at this document.


# listView
会强制使子元素宽度为列宽
margin,padding等不限制

# stack & positioned

# List.generate


# mixin 
混合类,
应为只能单继承,这个东西太草了..
这个作为多继承打补充
虽然,不能有构造函数,但是可以有函数,所以也无所谓...就是要二次调用下...在新类中,,二次构造.对接





Flutter Widget采用现代响应式框架构建，这是从 React 中获得的灵感，中心思想是用widget构建你的UI。


widget的主要工作是实现一个build函数，用以构建自身。一个widget通常由一些较低级别widget组成。Flutter框架将依次构建这些widget，直到构建到最底层的子widget时，这些最低层的widget通常为RenderObject，它会计算并描述widget的几何形状。


Flutter有一套丰富、强大的基础widget，其中以下是很常用的：

Text：该 widget 可让创建一个带格式的文本。

Row、 Column： 这些具有弹性空间的布局类Widget可让您在水平（Row）和垂直（Column）方向上创建灵活的布局。其设计是基于web开发中的Flexbox布局模型。

Stack： 取代线性布局 (译者语：和Android中的LinearLayout相似)，Stack允许子 widget 堆叠， 你可以使用 Positioned 来定位他们相对于Stack的上下左右四条边的位置。Stacks是基于Web开发中的绝度定位（absolute positioning )布局模型设计的。

Container： Container 可让您创建矩形视觉元素。container 可以装饰为一个BoxDecoration, 如 background、一个边框、或者一个阴影。 Container 也可以具有边距（margins）、填充(padding)和应用于其大小的约束(constraints)。另外， Container可以使用矩阵在三维空间中对其进行变换。