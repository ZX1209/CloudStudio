#install
sudo apt-get install cron

# ubuntu?
/etc/init.d/cron status
. . . . 

#
service crond start //启动服务

service crond stop //关闭服务

service crond restart //重启服务

service crond reload //重新载入配置

service crond status //查看配置
#if it is work
pgrep cron

#use manage
crontab
