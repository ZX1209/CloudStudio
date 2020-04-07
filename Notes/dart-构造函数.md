定义
1. 默认构造函数
如果你定义了一个类，而没有定义构造函数，那么它将有一个默认的构造函数，这个构造函数 没有参数
如果这个类有父类，那么默认构造函数，还会调用父类的无参数构造函数。
2. 普通构造函数
这就是我们普通的构造函数，其样子和其它语言几乎一样
class Point {
  num x, y;

  Point(num x, num y) {
    // There's a better way to do this, stay tuned.
    this.x = x;
    this.y = y;
  }
}
复制代码上例中只有两个成员变量，如果有10个，岂不是麻烦死？所以Dart有语法糖给你哦：
class Point {
  num x, y;

  // Syntactic sugar for setting x and y
  // before the constructor body runs.
  Point(this.x, this.y);
}
复制代码它可以将x,y的赋值变得简单一些，就不用写构造函数的方法体了，记得括号后用分号哦。
3. 命名构造函数

class Point {
  num x, y;

  Point(this.x, this.y);

  // 命名构造函数，新增代码
  Point.origin() {
    x = 0;
    y = 0;
  }
}

复制代码请记住，命名构造函数不可继承，如果子类想要有 和父类一样的命名构造函数，那就写个同名的（通常也会在子类的命名构造函数里，调用父类的同名命名构造函数）

作者：Realank Liu
链接：https://juejin.im/post/5d3fda64e51d4561cc25efa5
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。