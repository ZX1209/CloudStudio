> https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
also Fire 

argparse 是金典的定义是

dotopt则是将帮助文本解析称argpaser类似的来声明了参数等

click,则是根Fire有些像,通过标注函数来对应生成命令行,


My Recomendation
Now, to get this out of the way, my personal go-to library is click. I have been using it on large, multi-command, complex interfaces for the last year. (Credit goes to @kwbeam for introducing me to click). I prefer the decorator approach and think it lends a very clean, composable interface. That being said, let’s evaluate each option fairly.

Argparse

Arparse is the standard library (included with Python) for creating command-line utilities. For that fact alone, it is arguably the most used of the tools examined here. Argparse is also very simple to use as lots of magic (implicit work that happens behind the scenes) is used to construct the interface. For example, both arguments and options are defined using the add_arguments method and argparse figures out which is which behind the scenes.

Docopt

If you think writing documentation is great, docopt is for you! In addition docopt has implementations for many other languages - meaning you can learn one library and use it across many languages. The downside of docopt is that it is very structured in the way you have to define your command-line interface. (Some might say this is a good thing!)

Click

I’ve already said that I really like click and have been using it in production for over a year. I encourage you to read the very complete Why Click? documentation. In fact, that documentation is what inspired this blog post! The decorator style implementation of click is very simple to use and since you are decorating the function you want executed, it makes it very easy to read the code and figure out what is going to be executed. In addition, click supports advanced features like callbacks, command nesting, and more. Click is based on a fork of the now deprecated optparse library.

Invoke

Invoke surprised me in this comparison. I thought that a library designed for task execution might not be able to easily match full command-line libraries - but it did! That being said, I would not recommend using it for this type of work as you will certainly run into limitations for anything more complex than the example presented here.

Bonus: Packaging
Since not everyone is packaging up there python source with setuptools (or other solutions), we decided not to make this a core component of the article. In addition, we don’t want to cover packaging as a complete topic. If you want to learn more about packaging with setuptools go here or with conda go here or you can read my previous blog post on conda packaging. What we will cover here is how to use the entry_points option to make a command-line application an executable command on install.

Entry Point Basics
An entry_point is essentially a map to a single function in your code that will be given a command on your system PATH. An entry_point has the form - command = package.module:function

The best way to explain this is to just look at our click example and add an entry point.

