cat /etc/issue
uname -a
cat /proc/cpuinfo |grep "model name" && cat /proc/cpuinfo |grep "physical id"
cat /proc/meminfo |grep MemTotal
fdisk -l |grep Disk