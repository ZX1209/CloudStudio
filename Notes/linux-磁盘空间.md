### **df**

df 命令意思是 “disk-free”，显示 Linux 系统上可用和已使用的磁盘空间。

df -h 以人类可读的格式显示磁盘空间。

df -a 显示文件系统的完整磁盘使用情况，即使 Available（可用） 字段为 0。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJI5DZMKKvRDdKNQElw7SticIaajOU8jTU13t9DE5bhQrytEEC7owl49Dg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

df -T 显示磁盘使用情况以及每个块的文件系统类型（例如，xfs、ext2、ext3、btrfs 等）。

df -i 显示已使用和未使用的 inode。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJIlzAU1JfeeibCGB5kVnpHKkSsjwXEckx0GMxxI9G0nD6VKOIhibSJyb8g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

###  

### **du**

du 显示文件，目录等的磁盘使用情况，默认情况下以 kb 为单位显示。

du -h 以人类可读的方式显示所有目录和子目录的磁盘使用情况。

du -a 显示所有文件的磁盘使用情况。

du -s 提供特定文件或目录使用的总磁盘空间。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJIUHj5pczk5ZMKNR0QktzXRRRiaz1NNkXxJq9ZTXmpWSQwRqw7ia7yoZDg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

###  

### **ls -al**

ls -al 列出了特定目录的全部内容及大小。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJIkIDUf4CnloVkg6ibZNZ1Vy9CRQTiaqlwIDiaQ7vKF33o6GZUicu4w9uMxg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

###  

### **stat**

stat <文件/目录>显示文件/目录或文件系统的大小和其他统计信息。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJIPVxKNwlc7RwLTYWda4EYZ7nxGxxOia1d9dO358tEv7jD1v7WVlMicjow/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

###  

### **fdisk -l**

fdisk -l 显示磁盘大小以及磁盘分区信息。

![img](https://mmbiz.qpic.cn/mmbiz_png/9aPYe0E1fb21PqupAo0m8n1EunuhKhJIDnKMZviaslJDjhrharIRibT2Z4m6F6XZQeCtcUK82YShPcPO0dnvP8BQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

这些是用于检查 Linux 文件空间的大多数内置实用程序。有许多类似的工具，如 Disks（GUI 工具），Ncdu 等，它们也显示磁盘空间的利用率。你有你最喜欢的工具而它不在这个列表上吗？请在评论中分享。

 