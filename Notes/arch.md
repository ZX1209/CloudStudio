# 设置DNS server
/etc/resolv.conf

# OpenNIC IPv4 nameservers (US)
nameserver 107.170.95.180
nameserver 75.127.14.107

# Google IPv4nameservers
nameserver 8.8.8.8
nameserver 8.8.4.4

# Google IPv6 nameservers
nameserver 2001:4860:4860::8888
nameserver 2001:4860:4860::8844

https://wiki.archlinux.org/index.php/Resolv.conf_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E9.80.89.E6.8B.A9.E5.85.B6.E5.AE.83_DNS_.E6.9C.8D.E5.8A.A1.E5.99.A8

# 设置静态ip
```bash
ip link set eth0 up
ip addr add 192.168.1.2/24 dev eth0
ip route add default via 192.168.1.1
```


lsblk & fdisk -l
n,d,p

vim /etc/pacman.d/mirrorlist

Server = http://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = http://mirrors.zju.edu.cn/archlinux/$repo/os/$arch

arch-chroot 

mount??