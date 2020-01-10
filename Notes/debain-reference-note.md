# 那么你能够用 Ctrl-Alt-F1进入登录提示符，同时你可以通过Alt-F7回到GUI环境

系统以保存在 "/etc/motd" 中的欢迎信息（Message Of The Day）来开始，同时显示一个命令提示符。

在默认的 Debian 系统中，有6个可切换的类VT100字符控制台，可以直接在 Linux 主机上启动 shell。除非你处于 GUI 环境下，否则你可以同时按下左 Alt 键和F1—F6之一的键在虚拟控制台间切换。每一个字符控制台都允许独立登陆账户并提供多用户环境。这个多用户环境是伟大的 Unix 的特性，很容易上瘾。

# user things
adduser fish
deluser --remove-home fish

# /etc/sudoers

# mount unmount

# 一些重要目录

目录	目录用途
/	根目录
/etc/	系统范围的配置文件
/var/log/	系统日志文件
/home/	所有非特权用户的用户目录
/dev 硬件设备挂载点

# 权限
chown
chgrp
chomd
umask

# 命名管道?
mkfifo

# 套接字

ss -nptl

# 特殊设备文件
设备文件	操作	响应描述
/dev/null	读取	返回“文件结尾字符（EOF）“
/dev/null	写入	无返回（一个无底的数据转存深渊）
/dev/zero	读取	返回"\0空字符"（与ASCII中的数字0不同）
/dev/random	读取	从真随机数产生器返回一个随机字符，供应真熵（缓慢）
/dev/urandom	读取	从能够安全加密的伪随机数产生器返回一个随机字符
/dev/full	写入	返回磁盘已满（ENOSPC）错误


# procfs 和 sysfs
## /proc

目录"/proc"为每个正在运行的进程提供了一个子目录，目录的名字就是进程标识符（PID）。需要读取进程信息的系统工具，如ps()，可以从这个目录结构获得信息。


## /sys
"/sys"以下的目录包含了内核输出的数据结构，它们的属性，以及它们之间的链接。它同时也包含了改变某些内核运行时参数的接口。


参考"proc.txt(.gz)"，"sysfs.txt(.gz)"，以及其他相关的Linux内核文档（"/usr/share/doc/linux-doc-*/Documentat参考"proc.txt(.gz)"，"sysfs.txt(.gz)"，以及其他相关的Linux内核文档（"/usr/share/doc/linux-doc-*/Documentation/filesystems/*"），这些文件由linux-doc-*软件包提供。ion/filesystems/*"），这些文件由linux-doc-*软件包提供。

# tmpfs?

# shell  通配符
1.5.6. Shell 通配符
经常有这种情况你期望命令成串自动执行而不需要挨个输入，将文件名扩展为 glob，(有时候被称为 通配符)，以此来满足这方面的需求。

表 1.20. Shell glob 模式

shell glob 模式	匹配规则描述
*	不以 "." 开头的文件名(段)
.*	以 "." 开头的文件名(段)
?	精确字符
[…]	包含在括号中的任意字符都可以作为精确字符
[a-z]	"a" 到 "z" 之间的任意一个字符都可以作为精确字符
[^…]	除了包含在括号中的任意字符 ( " 1^ 2"除外 )，其它字符都可以作为精确字符

# 命令的返回值
$?


# jobs fg bg kill

# type

# bug 追踪
你应该阅读优良的官方文档。第一个阅读的文档是 Debian 特定的 “/usr/share/doc/<package_name>/README.Debian”。同时也应该查询 “/usr/share/doc/<package_name>/” 中的其它文档。如果你设置 shell 为第 1.4.2 节 “定制bash”，输入下列命令。

$ cd <package_name>
$ pager README.Debian
$ mc
你可能需要安装以 “-doc” 后缀命名的对应文档软件包来获取详细的信息。

如果你在使用一个特定的软件包时出现了问题，一定要首先检查 Debian bug 跟踪系统（BTS） 网站。

表 2.5. 解决特定软件包问题的主要网站

网站	命令
Debian bug 跟踪系统（BTS） 的主页	sensible-browser "http://bugs.debian.org/"
软件包名称已知的 bug 报告	sensible-browser "http://bugs.debian.org/<package_name>"
bug 编号已知的 bug 报告	sensible-browser "http://bugs.debian.org/<bug_number>"

使用 Google 搜索，在关键字中包含 “site:debian.org”，“site:wiki.debian.org”，“site:lists.debian.org” 等等。

当你要发送一份 bug 报告时，请使用 reportbug(1) 命令。

# apt apt-get/apt-cache aptitute

建议用户使用新的 apt(8) 命令用于 交互式的使用场景，而在 shell 脚本中使用 apt-get(8) 和apt-cache(8) 命令

# 软件包活动日志
你可以在日志文件里查询到软件包活动历史。

表 2.12. 软件包活动日志文件

文件	内容
/var/log/dpkg.log	dpkg 级的软件包活动日志
/var/log/apt/term.log	通用 APT 活动日志
/var/log/aptitude	aptitude 命令活动日志


"apt-get -s dist-upgrade" 命令来评估升级造成的影响。

/var/lib/dpkg

