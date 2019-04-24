ALTER USER 'username'@'ip_address' IDENTIFIED WITH mysql_native_password BY 'password';



环境准备

MySQL8.0.11 Windows zip包下载地址：https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.11-winx64.zip 
系统环境：Windows 10

1.加压安装包到安装目录

 我的目录是：D:\programs\MySQL
1
2.配置文件 
解压后的目录不存在 my.ini 文件，自己创建并编辑如下内容 
注意：把 basedir 换成自己的mysql安装目录， datadir 同理

[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录
basedir=D:\programs\MySQL
# 设置mysql数据库的数据的存放目录
datadir=E:\database\MySQL\Data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
# 服务端使用的字符集默认为utf8mb4
character-set-server=utf8mb4
#使用–skip-external-locking MySQL选项以避免外部锁定。该选项默认开启
external-locking = FALSE
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB 
# 默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password

[mysqld_safe]
log-error=D:\programs\MySQL\mysql_oldboy.err
pid-file=D:\programs\MySQL\mysqld.pid
# 定义mysql应该支持的sql语法，数据校验
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8mb4
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8mb4

3.配置环境变量 
path 下配置 D:\programs\MySQL\bin 
4. 初始化数据库 
以管理员身份运行cmd, 执行如下命令：

mysqld --initialize --console
1
执行完成后，会打印 root 用户的初始默认密码，比如：

A temporary password is generated for root@localhost: APWCY5ws&hjQ
1
5.安装数据库服务： 
以管理员身份运行cmd, 执行如下命令：

# 服务名缺省值为 mysql 
mysqld --install [服务名]
1
2
若不是管理员身份运行cmd ,会有如下错误报出。。。

mysql Install/Remove of the Service Denied!
1
6.启动mysql数据库服务

net start [服务名]
1
7.修改初始化密码

# 登录
mysql -uroot -p 初始化密码
# 修改密码
 alter user 'root'@'localhost' identified by 'xxxxx';
1
2
3
4
—————- 2018-05-31 增加

# 停止服务
net stop mysql
# 卸载服务
mysqld -remove
1
2
3
4
至此，我们的mysql8.0.11 就安装完成啦。。。
--------------------- 
作者：痴乙 
来源：CSDN 
原文：https://blog.csdn.net/fxbin123/article/details/80220509 
版权声明：本文为博主原创文章，转载请附上博文链接！