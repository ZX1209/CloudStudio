#start cron 
service cron start

> https://help.ubuntu.com/community/CronHowto#GUI_Applications

# GUI Applications
00 06 * * * env DISPLAY=:0 gui_appname


It is possible to run gui applications via cronjobs. This can be done by telling cron which display to use.

00 06 * * * env DISPLAY=:0 gui_appname
The env DISPLAY=:0 portion will tell cron to use the current display (desktop) for the program "gui_appname".

And if you have multiple monitors, don't forget to specify on which one the program is to be run. For example, to run it on the first screen (default screen) use :

00 06 * * * env DISPLAY=:0.0 gui_appname
The env DISPLAY=:0.0 portion will tell cron to use the first screen of the current display for the program "gui_appname".

Note: GUI users may prefer to use gnome-schedule (aka "Scheduled tasks") to configure GUI cron jobs. In gnome-schedule, when editing a GUI task, you have to select "X application" in a dropdown next to the command field.

Note: In Karmic(9.10), you have to enable X ACL for localhost to connect to for GUI applications to work.

 ~$ xhost +local:
non-network local connections being added to access control list
 ~$ xhost
access control enabled, only authorized clients can connect
LOCAL:
...

# 输出到终端
/dev/tty

usage: crontab [-u user] file
       crontab [ -u user] [ -i ] { -e | -l | -r }
               (default operation is replace, per 1003.2)
       -e      (edit user's crontab)
       -l      (list user's crontab)
       -r      (delete user's crontab)
       -i      (prompt before deleting user's crontab)

参数 说明 
-u user指定用户 
-e 编辑某个用户的计划任务文件，若不指定用户，默认编辑当前用户的计划任务文件 
-l 显示某个用户的计划任务文件，若不指定用户，默认显示当前用户的计划任务文件 
-r 删除某个用户的计划任务文件，若不指定用户，默认删除当前用户的计划任务文件 
-i 在删除之前推送确认提示 

crontab -u foo -e     #编辑用户 foo 的计划任务文件

crontab -e            #编辑当前用户的计划任务文件

crontab -u foo -l     #显示用户 foo 的计划任务文件

crontab -l            #显示当前用户的计划任务文件

crontab -r            #删除当前用户的计划任务文件


任务计划的语法格式如下：

m h dom mon dow   command
0-59 0-23 1-31 1-12 0-7  command

m: 表示分钟
h: 表示小时
dom: 表示日期
mon: 表示月份
dow: 表示星期
command: 预执行的命令
另外需要使用一些特殊符号实现灵活的配置：

* 代表所有值
/ 代表“每”
- 代表范围
, 分割数字





# set a shell
SHELL=/bin/bash

# crontab format
* * * * *  command_to_execute
- - - - -
| | | | |
| | | | +- day of week (0 - 7) (where sunday is 0 and 7)
| | | +--- month (1 - 12)
| | +----- day (1 - 31)
| +------- hour (0 - 23)
+--------- minute (0 - 59)

# example entries
# every 15 min
*/15 * * * * /home/user/command.sh

# every midnight
0 0 * * * /home/user/command.sh

# every Saturday at 8:05 AM
5 8 * * 6 /home/user/command.sh





copyed form http://lazybios.com/2015/11/about-crontab/



# Linux: 关于cron定时任务的一些心得

因为使用频率不高的原因，每次用cron的时候都会被语法格式纠结一下，今天的主题就来梳理一下cron语法和一些使用、调试技巧。

### 使用、调试技巧

- 命令执行之前，可以现在console里跑一下，首先保证命令本身没有问题，如果是一个程序，其实可以包到sh脚本里来跑
- 打开cron的运行日志，可以查看任务的运行情况，便于定位错误，后面会说怎么在ubuntu下开启日志功能
- 如果你跑的是一个完整的程序，最好能在程序中打下行为日志，这样除了能在cron.log中查看定时任务的运行情况之外，还能对程序本身的运行情况有个判断，可以避免cron正常，程序异常的问题。
- crontab里的任务一定要写绝对路径，像执行python、ruby这样的脚本，除了脚本要写绝对路径外，`python、ruby`解释器也要写绝对路径
- 确保你执行的任务所需资源的权限到位，这条可以通过在console中手动跑一遍命令试一试
- 必要的时候，在执行命令前`source`一下profile文件

### 开启cron日志功能

这里所涉及的命令均在ubuntu14.04下测试过，其它发行版，可以自行Google。没太多理论，直接贴代码了。最后的cron日志存放位置在`/var/log/cron.log`

```
cd /etc/rsyslog.d/

sudo vim 50-default.conf

#注释掉这行代码
#cron.*                         /var/log/cron.log

#重启rsyslog
sudo service rsyslog restart

# 重启cron
sudo service cron restart
```

### cron语法

跟我一样属于视觉学习型选手的同学有福了，一图胜千言，需要的就收藏起来吧。

![Cron](http://freshstu.qiniudn.com/crontab.png)

### 一些cron任务的例子

##### 实例1：每1分钟执行一次myCommand

```
* * * * * myCommand
```

##### 实例2：每小时的第3和第15分钟执行

```
3,15 * * * * myCommand
```

##### 实例3：在上午8点到11点的第3和第15分钟执行

```
3,15 8-11 * * * myCommand
```

##### 实例4：每隔两天的上午8点到11点的第3和第15分钟执行

```
3,15 8-11 */2  *  * myCommand
```

##### 实例5：每周一上午8点到11点的第3和第15分钟执行

```
3,15 8-11 * * 1 myCommand
```

##### 实例6：每晚的21:30重启smb

```
30 21 * * * /etc/init.d/smb restart
```

##### 实例7：每月1、10、22日的4 : 45重启smb

```
45 4 1,10,22 * * /etc/init.d/smb restart
```

##### 实例8：每周六、周日的1 : 10重启smb

```
10 1 * * 6,0 /etc/init.d/smb restart
```

##### 实例9：每天18 : 00至23 : 00之间每隔30分钟重启smb

```
0,30 18-23 * * * /etc/init.d/smb restart
```

##### 实例10：每星期六的晚上11 : 00 pm重启smb

```
0 23 * * 6 /etc/init.d/smb restart
```

##### 实例11：每一小时重启smb

```
* */1 * * * /etc/init.d/smb restart
```

##### 实例12：晚上11点到早上7点之间，每隔一小时重启smb

```
* 23-7/1 * * * /etc/init.d/smb restart
```

-完-

### 参考引用

- [http://dwz.cn/2d0eKi](http://lazybios.com/2015/11/about-crontab/)