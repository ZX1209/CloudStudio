# sources update tuna
echo "
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
" >> /etc/apt/sources.list

# update
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade


# git
sudo apt-get install git

# fsearch
sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
sudo apt update 
sudo apt install fsearch-trunk

# shadowsocks
sudo apt install shadowsocks-libev 

# sslocal
# https://wiki.archlinux.org/index.php/Shadowsocks_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
# #!/bin/bash
# ss-local -vc /home/gl/Projects/shadowsocks/shadowsocks2.json  > /tmp/sslocal.log 2>&1


## firefos or google-chrome

# google-chrome
# wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
# sudo apt-get update
# sudo apt-get install google-chrome-stable


# flameshot
sudo apt install flameshot


# zeal
sudo apt install zeal

# guake termianl
sudo apt install guake
sudo apt install gir1.2-wnck-3.0


# sublime text 3
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

sudo apt-get install apt-transport-https

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt-get update
sudo apt-get install sublime-text





# on debian
# $ sudo apt install git build-essential automake autoconf libtool pkg-config intltool autoconf-archive libpcre3-dev libglib2.0-dev libgtk-3-dev libxml2-utils
# $ git clone https://github.com/cboxdoerfer/fsearch.git
# $ cd fsearch
# $ ./autogen.sh
# $ ./configure
# $ make && sudo make install

# Is because other exception raised so given org.guake3.RemoteContro: no such name exception.

# At the last line, it shows that it didn't find Wnck:

#   File "/usr/lib64/python3.7/site-packages/gi/__init__.py", line 129, in require_version
#     raise ValueError('Namespace %s not available' % namespace)
# ValueError: Namespace Wnck not available
# As @freefcw mention, install gir1.2-wnck-3.0 can solve this problem.


# file struct APT



## unable to apt install software

# wps

# freefilesync or sync?

# albert

# crow translate


