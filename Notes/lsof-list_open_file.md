## 列出被进程号为1234的进程所打开的所有IPV4 network files
lsof -i 4 -a -p 1234

## 列出谁在使用某个端口
lsof -i :3306

## 通过某个进程号显示该进程打开的文件
lsof -p 11968

## 列出某个程序进程所打开的文件信息
lsof -c mysql

## 列出某个用户打开的文件信息
lsof -u username

## 查找某个文件相关的进程
lsof /bin/bash

# lsof
lsof（list open files）是一个查看当前系统文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。如传输控制协议 (TCP) 和用户数据报协议 (UDP) 套接字等，系统在后台都为该应用程序分配了一个文件描述符，该文件描述符提供了大量关于这个应用程序本身的信息。

3.1. 命令参数
-a 列出打开文件存在的进程
-c<进程名> 列出指定进程所打开的文件
-g 列出GID号进程详情
-d<文件号> 列出占用该文件号的进程
+d<目录> 列出目录下被打开的文件
+D<目录> 递归列出目录下被打开的文件
-n<目录> 列出使用NFS的文件
-i<条件> 列出符合条件的进程。（4、6、协议、:端口、 @ip ）
-p<进程号> 列出指定进程号所打开的文件
-u 列出UID号进程详情
-h 显示帮助信息
-v 显示版本信息

> Lists open files and the corresponding processes.
> Note: Root privileges (or sudo) is required to list files opened by others.

- Find the processes that have a given file open:

`lsof {{path/to/file}}`

- Find the process that opened a local internet port:

`lsof -i :{{port}}`

- Only output the process ID (PID):

`lsof -t {{path/to/file}}`

- List files opened by the given user:

`lsof -u {{username}}`

- List files opened by the given command or process:

`lsof -c {{process_or_command_name}}`

- List files opened by a specific process, given its PID:

`lsof -p {{PID}}`

- List open files in a directory:

`lsof +D {{path/to/directory}}`
