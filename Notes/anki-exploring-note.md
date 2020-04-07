# day 1 2019/12/24
成功下载anki仓库
可以安装python依赖(二进制包)
win10 sdk 下载
wsl 安装 ,使用 linux toolchains

尝试flutter;win10 desktop 构建失败;无法使用 desktop版本.


# day 2 2019/12/25
尝试 使用 wsl 环境构建;嗯,,;还是环境问题..毕竟qt是有窗口;wsl构建中的还是只能生成在wsl下运行的;/

# day 3 2019/12/26
准备转移到 debian 环境下


开始阅读原码
## anki start trace
aqt.run
  \_run
    mv = aqt.main.AnkiQt
      app with AnkiQt (main)

AnkiQt
  __init__
    setupUI
    setupAddon
    ...

# day 4 2019/12/27
faulthandler

aqt.mediasrv.MediaServer

aqt.forms.main.Ui_MainWindow

aqt.webview.AnkiWebView


anki/

anki/storage.py

找到了数据库与数据操作的相关文件夹anki
aqt是qt的界面实现代码文件夹


# day 5

# 2020-02-17

关于 flutter 中 类似树的设计暂时有两种构建策略

一是,直接用 canvas,custompaint,,绘制

二是用类似stack来模拟效果.

还是 直接绘制吧

# 2020-03-14

## 确定版本为2.1.9

## 开始了解第一层结构

anki/                         : anki 核心程序文件夹？
aqt/                          : anki qt 界面程序
designer/                     : qt 界面 源文件
tests/                        : 测试程序文件夹
web/                          : 疑似web 版程序源文件
.gitignore                    : git  忽略文件数据
.travix.yml                   : travix
runanki                       : anki       启动文件
tools/                        : 实用工具文件夹？
anki-explore-note-hard_link.md: 笔记硬链接文件
anki.1                        : man page usage?
anki.desktop                  : desktop (图标)文件
anki.png                      : anki 图标
anki.xml                      : ?
anki.xpm                      : ?
LINCENSE                      : 协议说明文件
LICENSE.logo                  : anki logo 协议文件
Makefile                      : anki make 配置 文件
pkgkey.asc                    : 公钥文件?
README.contributing           : 贡献指南
README.development            : 开发者使用说明
README.md                     : anki git repo 说明
requirements.txt              : python 依赖文件

## 确定主要关注文件
aqt/,anki/

# 2020-03-15 , 2020-03-16 , 2020-03-17 , 2020-03-18
## 了解 aqt/ 结构
`__pycache__`   : python 缓存文件
forms/          : qt ui 界面 构造 程序源码
`__init__.py`   : ?
about.py        : 菜单栏/帮助/关于
addcards.py     : 添加卡片页面
addons.py       : 标签管理界面控制器
browser.py      : 卡组中的卡片游览器
clayout.py      : ?
customstudy.py  : ?
deckbrowser.py  : ?
deckchooser.py  : ?
deckconf.py     : 卡组设置
downloader.py   : 下载插件相关
dyndeckconf.py  : ?
editcurrent.py  : ?
editor.py       : 内容(卡片)编辑器
errors.py       : 错误处理
exporting.py    : 导出界面?
fields.py       : 卡片中的各个域
importing.py    : dpkg 导入 | ?
main.py         : 主窗口构造程序, 组装部件 setupmainwindow
mediasrv.py     : 媒体服务器?
                :  something
                :
modelchooser.py : ?
models.py       : 卡片类型
overview.py     : ?
pinnedmodules.py: ?
preferences.py  : ?
profiles.py     : ?
progress.py     : ?
qt.py           : ?
reviewer.py     : ?
sound.py        : ?
stats.py        : 统计
studydeck.py    : ?
sync.py         : 远程同步 源码
tagedit.py      : 标签编辑 控制
taglimit.py     : 标签选择,限制 控制
toolbar.py      : 工具栏 构建代码
update.py       : 软件更新 
utils.py        : 常用的Anki界面 组件与工具
webview.py      : 网页试图 构建 QWebEnginePage
winpaths.py     : 检索 win 系统路径



## tools/build_ui.sh
`从designer/*.ui 生成对应的 aqt/forms/*.py `
pyuic5 生成 中间 py 源码文件
perl 正则替换 指定特殊对象?

designer/ 中基本上只有架子,没有内容.毕竟qt主语言还是是C啊,跟python的集成才刚起步

## forms/
界面构建模板 文件夹


恩,这个构造挺像MVC的,
designer/: model
aqt/     : control
anki     : view

designer/,aqt/forms,与aqt/中的文件关联性强,不重复叙述,了解大概即可.

# 2020-03-21 
## 开始聚焦于 anki/
cards.py     : ?
collection.py: 数据读取,更新 封装?
consts.py    : 常量定义
db.py        : 数据库封装
decks.py     : ?
errors.py    : ?
exporting.py : ?
find.py      : ?
hooks.py     : ?
__init__.py  : 检测python版本与字符编码
lang.py      : ?
latex.py     : ?
media.py     : ?
models.py    : ?
mpv.py       : mpv 链接与控制 subprocess
notes.py     : ?
sched.py     : ?
schedv2.py   : ?
sound.py     : ?
statsbg.py   : ?
stats.py     : ?
stdmodels.py : ?
storage.py   : 创建数据库与数据表
sync.py      : ?
tags.py      : 标签管理
utils.py     : ?
importing/ : ?
template/ : ?


# 2020-03-22
## 卡片选取
"select * from cards where id = ?",self.id

## data folder
anki/profiles 282
~/.local/share/Anki2

## create db
anki/storage.py 206

## db 
- col : collection
  - id : 
  - crt : Call Request Time,呼叫请求时间
  - mod : modify time
  - scm : schema modify time
  - ver : scheduler version, 调度器版本, not use?
  - dty : nolonger use
  - usn : Update Sequence Number ,更新序号
  - ls : last sync time
  - conf :text json
  - models :text json
    - model id :
    - ...
  - decks  :text json
    - deckid
      - collapsed
      - conf
      - desc
      - dyn
      - extendNew
      - extendRev
      - id
      - lrnToday
      - mod
      - name
      - newToday
      - revtoday
      - timeToday
      - usn
  - dconf  :text json ,deck options or conf
  - tags :text json
  - 
- notes
  - id
  - guid
  - mid : model id
  - mod
  - usn
  - tags text 标签段
  - flds 整个域段
  - sfld 卡片标题
  - csum
  - flags
  - data
- cards
  - id : card id
  - nid       : note_id
  - did       : deck id
  - ord       : ?
  - mod : modify time?
  - usn : ...
  - type :
  - queue : 
  - due : 到期时间?
  - ivl
  - factor
  - reps
  - lapses
  - left
  - odue : original due
  - odid : original deck id
  - flags
  - data
  - 
- revlog
  - id
  - cid
  - usn
  - ease
  - ivl
  - lastIvl
  - factor
  - time
  - type
- graves
  - usn
  - oid
  - type


### index


# 2020-04-01 
## 尝试对Decks 展示页面进行修改


# trash
学习方面主要如下：
1. Anki 源码
由于是开源软件，可以方便的找到开发的源码。版本为比较新的2.1版本。
该程序主要由Python编写，Sqlite为数据库核心，涉及到写QT的知识。
同时通过学习也希望将其中关于间隔重复思想的算法与数据操作部分提取出来，使其能更加广泛的使用。
2.程序间通信技术
数据操作的独立带来的另一个问题就是如何实现程序间的通信来调用操作，实现外接应用的效果。虽然实现方法很多，但是需要研究的是哪种手段面对多样的需求有足够好的效果。
改进存在如下方面：
1.界面部分
基本上Anki的界面还是挺简洁的，这方面还是以了解为主。
2.联系的概念
Anki本身对于间隔重复的概念还是很好的实现了，但我认为，其对于联系的形式局限在反转卡片的形式上并不是很好。可以考虑多增加点形式以起到强化联系的作用。

