Systemd 并不是一个命令，而是一组命令，涉及到系统管理的方方面面。

## 3.1 systemctl
systemctl是 Systemd 的主命令，用于管理系统。


### 重启系统
sudo systemctl reboot

### 关闭系统，切断电源
sudo systemctl poweroff

### CPU停止工作
sudo systemctl halt

### 暂停系统
sudo systemctl suspend

### 让系统进入冬眠状态
sudo systemctl hibernate

### 让系统进入交互式休眠状态
sudo systemctl hybrid-sleep

### 启动进入救援状态（单用户状态）
sudo systemctl rescue

## 3.2 systemd-analyze
systemd-analyze命令用于查看启动耗时。
### 查看启动耗时

systemd-analyze

### 查看每个服务的启动耗时
systemd-analyze blame

### 显示瀑布状的启动过程流
systemd-analyze critical-chain

### 显示指定服务的启动流
systemd-analyze critical-chain atd.service
## 3.3 hostnamectl
hostnamectl命令用于查看当前主机的信息。


### 显示当前主机的信息
hostnamectl

### 设置主机名。
sudo hostnamectl set-hostname rhel7

## 3.4 localectl
localectl命令用于查看本地化设置。


### 查看本地化设置
localectl

### 设置本地化参数。
sudo localectl set-locale LANG=en_GB.utf8
sudo localectl set-keymap en_GB

## 3.5 timedatectl
timedatectl命令用于查看当前时区设置。


### 查看当前时区设置
timedatectl

### 显示所有可用的时区
timedatectl list-timezones                                                                                   

### 设置当前时区
sudo timedatectl set-timezone America/New_York
sudo timedatectl set-time YYYY-MM-DD
sudo timedatectl set-time HH:MM:SS

## 3.6 loginctl
loginctl命令用于查看当前登录的用户。


### 列出当前session
loginctl list-sessions

### 列出当前登录用户
loginctl list-users

### 列出显示指定用户的信息
loginctl show-user ruanyf