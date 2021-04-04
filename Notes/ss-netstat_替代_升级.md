ss
Utility to investigate sockets

ss -apn | grep 5000

# 查找监听端口
udo ss -tlp | grep ":8118"


# ? debian10 
ss -nptl