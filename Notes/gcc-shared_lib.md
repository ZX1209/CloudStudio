## 编译无约束位的代码

gcc -c -Wall -Werror -fpic foo.c

`-fpic`



## 生成共享库文件

gcc -shared -o libfoo.so foo.o

`-share`



## 将库放到标准位置并刷新缓存

cp /home/username/foo/libfoo.so /usr/lib

chmod 0755 /usr/lib/libfoo.so

ldconfig









copyed from https://www.cnblogs.com/ifantastic/p/3526237.html





# [在 Linux 使用 GCC 编译C语言共享库](https://www.cnblogs.com/ifantastic/p/3526237.html)

对任何程序员来说库都是必不可少的。所谓的库是指已经编译好的供你使用的代码。它们常常提供一些通用功能，例如链表和二叉树可以用来保存任何数据，或者是一个特定的功能例如一个数据库服务器的接口，就像MySQL。

 

大部分大型的软件项目都会包含若干组件，其中一些你发现可以用在其他项目中，又或者你仅仅出于组织目的将不同组件分离出来。当你有一套可复用的并且逻辑清晰的函数时，将其构建为一个库会十分有用，这样你就不将这些源代码拷贝到你的源代码中，而且每次都要再次编译它们。除此之外，你还可以保证你的程序各模块隔离，这样你修改其中一个模块时也不会影响到其他的模块。一旦你写好一个模块并且通过测试，你就可以无限次地安全地复用它，这可以节省大量时间和麻烦。

 

构建静态库太简单了，对此我们几乎不会遇到什么问题。我不想说明如何构建静态库。在此我只讨论共享库，因为对大多数人来说它更加难懂。

 

在我们正式开始前，让我们列一下纲要来了解从源代码到运行程序之间发生了什么：

1. 预处理：这个阶段处理所有预处理指令。基本上就是源代码中所有以#开始的行，例如#define和#include。
2. 编译：一旦源文件预处理完毕，接下来就是编译。因为许多人提到编译时都是指整个程序构建过程，因此本步骤也称作“compilation proper”。本步骤将.c文件转换为.o文件。
3. 连接：到这一步就该将你所有的对象文件和库串联起来使之成为最后的可运行程序。需要注意的是，静态库实际上已经植入到你的程序中，而共享库，只是在程序中包含了对它们的引用。现在你有了一个完整的程序，随时可以运行。当你从shell中启动它，它就被传递给了加载器。
4. 加载：本步骤发生在你的程序启动时。首先程序需要被扫描以便引用共享库。程序中所有被发现的引用都立即生效，对应的库也被映射到程序。

 

第3步和第4步就是共享库的奥秘所在。

现在，开始我们一个简单的示例。

 

 foo.h:

```c
#ifndef foo_h__
#define foo_h__

extern void foo(void);

#endif  // foo_h__
glonlinux@GL-PC-Win
```





foo.c:

```c
#include <stdio.h>


void foo(void)
{
    puts("Hello, I'm a shared library");
}
```



main.c:

```c
#include <stdio.h>
#include "foo.h"

int main(void)
{
    puts("This is a shared library test...");
    foo();
    return 0;
}

```



 

foo.h 定义了一个接口连接我们的库，一个简单的函数，foo()。foo.c包含了这个函数的实现，main.c是一个用到我们库的驱动程序。

为了更好的演示本例子，所有代码都放在/home/username/foo目录下。

 

**Step 1: 编译无约束位代码**

我们需要把我们库的源文件编译成无约束位代码。无约束位代码是存储在主内存中的机器码，执行的时候与绝对地址无关。

```
$ gcc -c -Wall -Werror -fpic foo.c
```

 

**Step 2: 从一个对象文件创建共享库**

现在让我们将对象文件变成共享库。我们将其命名为libfoo.so：

```
$ gcc -shared -o libfoo.so foo.o
```

 

**Step 3: 连接共享库**

如你所见，一切都很简单。我们现在有了一个共享库。现在我们编译我们的main.c并且将它连接到libfoo。我们将最终的运行程序命名为test。注意：-lfoo选项并不是搜寻foo.o，而是libfoo.so。GCC编译器会假定所有的库都是以lib开头，以.so或.a结尾（.so是指shared object共享对象或者shared libraries共享库，.a是指archive档案，或者静态连接库）。

```
$ gcc -Wall -o test main.c -lfoo
/usr/bin/ld: cannot find -lfoo
collect2: ld returned 1 exit status
```

 

**\*告诉GCC去哪找共享库***

Uh-oh!连接器不知道该去哪里找到libfoo。GCC有一个默认的搜索列表，但我们的目录并不在那个列表当中。我们需要告诉GCC去哪里找到libfoo.so。这就要用到-L选项。在本例中，我们将使用当前目录/home/username/foo：

```
$ gcc -L/home/username/foo -Wall -o test main.c -lfoo
```

 

**Step 4: 运行时使用库**

好的，没有异常。让我们运行一下程序：

```
$ ./test
./test: error while loading shared libraries: libfoo.so: cannot open shared object file: No such file or directory
```

 

Oh no! 加载器不能找到共享库。我们没有将它安装到标准位置，因此我们需要帮一帮加载器。我们有两个选项：使用环境变量LD_LIBRARY_PATH或者rpath。让我们先看看LD_LIBRARY_PATH：

 

**\*使用LD_LIBRARY_PATH***

```
$ echo $LD_LIBRARY_PATH
```

 

目前什么都没有。现在把我们的工作目录添加到LD_LIBRARY_PATH中：

```
$ LD_LIBRARY_PATH=/home/username/foo:$LD_LIBRARY_PATH
$ ./test
./test: error while loading shared libraries: libfoo.so: cannot open shared object file: No such file or directory
```

 

为什么还报错？虽然我们的目录在LD_LIBRARY_PATH，但是我们还没有导出它。在Linux中，如果你不将修改导出到一个环境变量，这些修改是不会被子进程继承的。加载器和我们的测试程序没有继承我们所做的修改，不过放心，要修复这个问题很简单：

```
$ export LD_LIBRARY_PATH=/home/username/foo:$LD_LIBRARY_PATH
$ ./test
This is a shared library test...
Hello, I'm a shared library
```

 

很好，运行正常！LD_LIBRARY_PATH很适合做快速测试，尤其是那些你没有管理员权限的系统。另一方面，导出LD_LIBRARY_PATH变量意味着可能会造成其他依赖LD_LIBRARY_PATH的程序出现问题，因此在做完测试后最好将LD_LIBRARY_PATH恢复成之前的样子。

 

**\*使用rpath***

现在让我们来试试rpath，首先需要清除LD_LIBRARY_PATH，确保我们是使用rpath来搜索库文件。Rpath，或者称为run path，是种可以将共享库位置嵌入程序中的方法，从而不用依赖于默认位置和环境变量。我们在连接环节使用rpath。注意“-Wl,-rpath=/home/username/foo”选项。-Wl会发送以逗号分隔的选项到连接器，因此我们通过它发送-rpath选项到连接器。（译者按：逗号分隔符后面没有空格，而是紧跟需要发送的选项。本例中为-rpath。一定注意"-Wl,-rpath"之间没有空格。）

```
$ unset LD_LIBRARY_PATH
$ gcc -L/home/username/foo -Wl,-rpath=/home/username/foo -Wall -o test main.c -lfoo
$ ./test
This is a shared library test...
Hello, I'm a shared library
```

 

非常好，奏效了。rpath方法非常棒，因为每个程序都可以单独罗列它自己的共享库位置，因此不同的程序不会再在错误的路径上搜索LD_LIBRARY_PATH。

 

**\*rpath和LD_LIBRARY_PATH***

rpath也存在一些反作用面。首先，它要求共享库必须安装在一个固定的位置，这样所有的用户才可以在同一个位置访问到库。这就意味着在系统配置中不够灵活。其次，如果库涉及NFS挂载或者其他网络驱动，你在启动程序时会遇到延时或者更糟的情况。

 

**\*使用ldconfig修改ld.so***

如果我们想让系统上所有用户都可以使用我的库时该怎么办？对此，你需要管理员权限。缘由有二：首先，将库放到标准位置，很可能是/usr/lib或者/usr/local/lib，这些地方普通用户是没有写的权限。其次，你需要修改ld.so配置文件并缓存。以root身份做一下操作：

```
$ cp /home/username/foo/libfoo.so /usr/lib
$ chmod 0755 /usr/lib/libfoo.so
```

 

现在文件在标准位置，对所有人都可读。我们现在需要告诉加载器库文件可用，因此让我们更新一下缓存：

```
$ ldconfig
```

 

这将创建一个链接到我们的共享库，并且更新缓存以便它可立即生效。让我们再核实一下：

```
$ ldconfig -p | grep foo
libfoo.so (libc6) => /usr/lib/libfoo.so
```

 

现在我们的库安装好了，在我们开始测试它之前，我们一定要先清理一下其他东西：

以防万一，先清理一下LD_LIBRARY_PATH：

```
$ unset LD_LIBRARY_PATH
```

 

重新连接我们的可执行程序。注意：我们不需要-L选项，因为我们的库保存在默认位置，我们可以不用rpath选项：

```
$ gcc -Wall -o test main.c -lfoo
```

 

让我们确认一下我们将使用/usr/lib中我们库的实例，使用ldd命令：

```
$ ldd test | grep foo
libfoo.so => /usr/lib/libfoo.so (0x00a42000)
```

 

很好，现在运行一下程序吧：

```
$ ./test
This is a shared library test...
Hello, I'm a shared library
```

 

以上就是所有内容。我们讲述了如何构建一个共享库，如何连接，如果解决最常见的共享库加载问题，还有各种方法的优劣性。

 

 

附：

\1. Shared Libraries（共享库） 和 Static Libraries（静态库）区别

共享库是以.so（Windows平台为.dll，OS X平台为.dylib）作为后缀的文件。所有和库有关的代码都在这一个文件中，程序在运行时引用它。使用共享库的程序只会引用共享库中它要用到的那段代码。

静态库是以.a（Windows平台为.lib）作为后缀的文件。所有和库有关的代码都在这一个文件中，静态库在编译时就被直接链接到了程序中。使用静态库的程序从静态库拷贝它要使用的代码到自身当中。（Windows还有一种.lib文件是用来引用.dll文件，但其实它们和第一种情况是一样的。）

 

两种库各有千秋。

 

使用共享库可以减少程序中重复代码的数量，让程序体积更小。而且让你可以用一个功能相同的对象来替换共享对象，这样可以在增加性能的同时不用重新编译那些使用到该库的程序。但是使用共享库会小额增加函数的执行的成本，同样还会增加运行时的加载成本，因为共享库中的符号需要关联到它们使用的东西上。共享库可以在运行时加载到程序中，这是二进制插件系统最通用的一种实现机制。

 

静态库总体上增加了程序体积，但它也意味着你无需随时随地都携带一份要用到的库的拷贝。因为代码在编译时就已经被关联在一起，因此在运行时没有额外的消耗。

 

\2. GCC首先在/usr/local/lib搜索库文件，其次在/usr/lib，然后搜索-L参数指定路径，搜索顺序和-L参数给出路径的顺序一致。

 

\3. 默认的GNU加载器ld.so，按以下顺序搜索库文件：

1. 首先搜索程序中DT_RPATH区域，除非还有DT_RUNPATH区域。
2. 其次搜索LD_LIBRARY_PATH。如果程序是setuid/setgid，出于安全考虑会跳过这步。
3. 搜索DT_RUNPATH区域，除非程序是setuid/setgid。
4. 搜索缓存文件/etc/ld/so/cache（停用该步请使用'-z nodeflib'加载器参数）
5. 搜索默认目录/lib，然后/usr/lib（停用该步请使用'-z nodeflib'加载器参数）