# 安装
pip install pyecharts

# Install data extensions:
pip install echarts-cities-pypkg

# Render to Local Html File
```python
from pyecharts import Bar

attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render()
```
Introduction
Echarts is an open source library from Baidu for data visualization in javascript. It has awesome demo pages so I started to look out for an interface library so that I could use it in Python. I ended up with echarts-python on github but it lacks of documentation and was not updated for a while. Just like many other Python projects, I started my own project, pyecharts, referencing echarts-python and another library pygal.

Installation
Python Compatibility
pyecharts works on Python2.7 and Python3.4+.

pyecharts handles all strings and files with unicode encoding and you MUST use unicode string on Python 2.

#coding=utf-8
from __future__ import unicode_literals
pyecharts
You can install it via pip

$ pip install pyecharts
or clone it and install it

$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
Please note: since version 0.3.2, NO LONGER pyecharts comes with any map files. Please read next section for more informations.

Geo Data extensions (0.5.7+)
From geonames.org, 138,398 cities of the world with a population of at least 1000 inhabitants: echarts-cities-pypkg

Install data extensions:

$ pip install echarts-cities-pypkg
Map extensions
Here is a list of map extensions from pyecharts dev team:

World countries include China map and World map: echarts-countries-pypkg (1.9MB)
Chinese provinces and regions: echarts-china-provinces-pypkg (730KB)
Chinese cities: echarts-china-cities-pypkg (3.8MB)
Chinese counties: echarts-china-counties-pypkg (4.1MB)
Custom Chinese regions: echarts-china-misc-pypkg (148KB)
United Kingdom map: echarts-united-kingdom-pypkg (1MB)
In order to install them, you can try one or all of them below:

$ pip install echarts-countries-pypkg
$ pip install echarts-china-provinces-pypkg
$ pip install echarts-china-cities-pypkg
$ pip install echarts-china-counties-pypkg
$ pip install echarts-china-misc-pypkg
$ pip install echarts-united-kingdom-pypkg
Basic Usage
Render to Local Html File
from pyecharts import Bar

attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render()
It will create a file named render.html in the root directory, open file with your borwser.



Export as Images or Pdf
pyecharts-snapshot is a command line utility and a library extension which renders the output of pyecharts as a svg, png, jpeg, gif image or a pdf file.

After you will have installed pyecharts-snapshot, you can modify previous example file slightly and get png output directly:

bar.render(path="render.png")
So please see installation instruction and other usage at that repository.

Platform Support
pyecharts exposes chart API and template API so that it can work on other python frameworks.

Integration with Jupyter Notebook/nteract
Notebook
In the Notebook cell, you can simply pass on chart instance itself to Jupyter, which will diplay the chart. Please note render_notebook function has been removed.

All chart classes in pyecharts implement the _repr_html_ interface about IPython Rich Display .

In the case of online jshost mode, you can also download as some file formats (ipynb/py/html/pdf) and run without jupyter notebook enviromnment.



nteract
Since pyecharts 0.5.5+, nteract is supported. Once the following two lines should added to your notebook, you could use pyecharts in nteract in the same way as in jupyter notebook.

from pyecharts import enable_nteract

enable_nteract()


However, when rendering output as image, the instructions are the same as jupyter notebook. Only default html(including js) output should call enable_nteract().

Integrate With Web Framework
With the help of pyecharts API, it is easy to integrate pyecharts to your web projects, such as Flask and Django.

Demo



Advanced Topics
Custom Template Files and Layout
pyecharts exposes engine API so that you can use your own template file and custom CSS.

In addition, pyecharts also ships a lot of jinja2 template functions used in template files.

Custom Map Libraries
All maps are developed and maintained by echarts-maps github organisation.

Documentation
中文文档
English Documentation
Examples
All examples is hosted on the repository pyecharts-users-cases.

Test
Unit Test
You should install the libraries in the requirements.txt files.

$ pip install -r test\requirements.txt
And run with the nose commands.

$ make
Quality Assurance
flake8, Codecov and pylint are used to improve the quality of code.

Continuous Integration
The project is developed with Travis CI and AppVeyor.

Author


License
pyecharts is released under the MIT License. See LICENSE for more information.