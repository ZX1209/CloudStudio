#使程序在ssh断开后继续运行 
nohup command &

# 关闭 nohup
ps -aux | grep command
kill -15/-19 pid 

#使用jobs查看任务,fg %n关闭  

/home/gl/nohup.out