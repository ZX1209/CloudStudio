> https://www.91yun.co/archives/1690
> https://www.cnblogs.com/Dicky-Zhang/p/5904429.html

iptables > Tables > CHains > Rules 

## 规则、表和链

1.规则（rules）

规则（rules）其实就是网络管理员预定义的条件，规则一般的定义为“如果数据包头符合这样的条件，就这样处理这个数据包”。规则存储在内核空间的信息包过滤表中，这些规则分别指定了源地址、目的地址、传输协议（如TCP、UDP、ICMP）和服务类型（如HTTP、FTP和SMTP）等。当数据包与规则匹配时，iptables就根据规则所定义的方法来处理这些数据包，如放行（accept）、拒绝（reject）和丢弃（drop）等。配置防火墙的主要工作就是添加、修改和删除这些规则。

2.链（chains）

链（chains）是数据包传播的路径，每一条链其实就是众多规则中的一个检查清单，每一条链中可以有一条或数条规则。当一个数据包到达一个链时，iptables就会从链中第一条规则开始检查，看该数据包是否满足规则所定义的条件。如果满足，系统就会根据该条规则所定义的方法处理该数据包；否则iptables将继续检查下一条规则，如果该数据包不符合链中任一条规则，iptables就会根据该链预先定义的默认策略来处理数据包。

3.表（tables）
表（tables）提供特定的功能，iptables内置了4个表，即raw表、filter表、nat表和mangle表，分别用于实现包过滤，网络地址转换和包重构的功能。


 
（1）RAW表

只使用在PREROUTING链和OUTPUT链上,因为优先级最高，从而可以对收到的数据包在连接跟踪前进行处理。一但用户使用了RAW表,在 某个链上,RAW表处理完后,将跳过NAT表和 ip_conntrack处理,即不再做地址转换和数据包的链接跟踪处理了.

（2）filter表

主要用于过滤数据包，该表根据系统管理员预定义的一组规则过滤符合条件的数据包。对于防火墙而言，主要利用在filter表中指定的规则来实现对数据包的过滤。Filter表是默认的表，如果没有指定哪个表，iptables 就默认使用filter表来执行所有命令，filter表包含了INPUT链（处理进入的数据包），RORWARD链（处理转发的数据包），OUTPUT链（处理本地生成的数据包）在filter表中只能允许对数据包进行接受，丢弃的操作，而无法对数据包进行更改

（3）nat表

主要用于网络地址转换NAT，该表可以实现一对一，一对多，多对多等NAT 工作，iptables就是使用该表实现共享上网的，NAT表包含了PREROUTING链（修改即将到来的数据包），POSTROUTING链（修改即将出去的数据包），OUTPUT链（修改路由之前本地生成的数据包）

（4）mangle表

主要用于对指定数据包进行更改，在内核版本2.4.18 后的linux版本中该表包含的链为：INPUT链（处理进入的数据包），RORWARD链（处理转发的数据包），OUTPUT链（处理本地生成的数据包）POSTROUTING链（修改即将出去的数据包），PREROUTING链（修改即将到来的数据包）

3、规则表之间的优先顺序：

Raw——mangle——nat——filter

规则链之间的优先顺序（分三种情况）：


## 0x06 如何正确配置 iptables
a) 1. 删除现有规则

iptables -F

b) 2.   配置默认链策略

iptables -P INPUT DROP 
iptables -P FORWARD DROP 
iptables -P OUTPUT DROP 
c) 3. 允许远程主机进行 SSH 连接

iptables -A INPUT -i eth0 -p tcp  – dport 22 -m state  – state NEW,ESTABLISHED -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp  – sport 22 -m state  – state ESTABLISHED -j ACCEPT 
d) 4. 允许本地主机进行 SSH 连接

iptables -A OUTPUT -o eth0 -p tcp  – dport 22 -m state  – state NEW,ESTABLISHED -j ACCEPT 
iptables -A INPUT -i eth0 -p tcp  – sport 22 -m state  – state ESTABLISHED -j ACCEPT 
e) 5. 允许 HTTP 请求

iptables -A INPUT -i eth0 -p tcp  – dport 80 -m state  – state NEW,ESTABLISHED -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp  – sport 80 -m state  – state ESTABLISHED -j ACCEPT 


## 0x07 使用 iptables 抵抗常见攻击
1. 防止 syn 攻击
思路一：限制 syn 的请求速度（这个方式需要调节一个合理的速度值，不然会影响正常用户的请求）

iptables -N syn-flood 

iptables -A INPUT -p tcp --syn -j syn-flood 

iptables -A syn-flood -m limit --limit 1/s --limit-burst 4 -j RETURN 

iptables -A syn-flood -j DROP 
思路二：限制单个 ip 的最大 syn 连接数

iptables  – A INPUT  – i eth0  – p tcp --syn -m connlimit --connlimit-above 15 -j DROP 
2. 防止 DOS 攻击
利用 recent 模块抵御 DOS 攻击

iptables -I INPUT -p tcp -dport 22 -m connlimit --connlimit-above 3 -j DROP 
单个 IP 最多连接 3 个会话

iptables -I INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH    
只要是新的连接请求，就把它加入到 SSH 列表中

Iptables -I INPUT -p tcp --dport 22 -m state NEW -m recent --update --seconds 300 --hitcount 3 --name SSH -j DROP    
5 分钟内你的尝试次数达到 3 次，就拒绝提供 SSH 列表中的这个 IP 服务。被限制 5 分钟后即可恢复访问。

3. 防止单个 ip 访问量过大
iptables -I INPUT -p tcp --dport 80 -m connlimit --connlimit-above 30 -j DROP 
4. 木马反弹
iptables  – A OUTPUT  – m state --state NEW  – j DROP 
5. 防止 ping 攻击
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/m -j ACCEPT 
个人见解，不足之处求指正。