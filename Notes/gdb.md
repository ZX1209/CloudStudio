# gdb

## 命令,效果
###   开始和停止
quit
run
kill

###   断点
break multstore ,在函数multstore入口出设置断点
break * 0x400540,在地址0x400540出设置断点

delete 1,删除断点1
delete,删除所有断点
###   执行
stepi,执行1条指令
stepi 4,执行4条指令
nexti,以函数调用为单位执行
continue,继续执行
finish,运行到当前函数返回
###   检查代码
dissas,反汇编当前函数
dissas multstore,反汇编 multstore 函数
dissas 0x400544,反汇编位于地址附近的函数
dissas 0x400540,0x40054d ,反汇编指定地址范围内的代码
print /x $rip, 以十六进制输出程序计数器的值

###   检查数据
print $rax,十进制输出内容
print /x $rax ,十六进制
print /t $rax,二进制
print 0x100,十进制
print /x 555,十六进制
print /x ($rsp+8) ,以十六进制输出rsp的内容加上8
print *(long *) 0x7fffffffe8181 ,输出位于地址的长整数
print *(long *)($rsp+8),输出位于地址处的长整型
x/2g 0x7fffffffe818 ,  检查从地址开始的双字节
x/20b multstore , 检查函数multstore的前20个字节

###   有用的信息
info frame,有关当前栈帧的信息
info registers,所有寄存器的值
help,获取有关gdb的信息
> The GNU Debugger.

- Debug an executable:

`gdb {{executable}}`

- Attach a process to gdb:

`gdb -p {{procID}}`

- Execute given GDB commands upon start:

`gdb -ex "{{commands}}" {{executable}}`

- Start gdb and pass arguments:

`gdb --args {{executable}} {{argument1}} {{argument2}}`
