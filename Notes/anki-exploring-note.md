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