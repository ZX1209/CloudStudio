iptables-tutorial.md 

## 命令参考
iptables [-t 表名] 命令选项 [ 链名 ] [ 条件匹配 ] [ -j 目标动作或跳转 ]

### 1. 表名
表名： Filter, NAT, Mangle, Raw

起包过滤功能的为表 Filter ，可以不填，不填默认为 Filter

### 2. 命令选项
| 选项名       | 功能及特点                                                              |
| ------------ | ----------------------------------------------------------------------- |
| -P           | 设置指定链的默认策略（ –policy ）                                       |
| -A           | 在指定链的末尾添加（ –append ）一条新的规则                             |
| -D           | 删除（ –delete ）指定链中的某一条规则，按规则序号或内容确定要删除的规则 |
| -I           | 在指定链中插入（ –insert ）一条新的规则，默认在链的开头插入             |
| -L           | 列出（ –list ）指定链中的所有的规则进行查看，默认列出表中所有链的内容   |
| -R           | 修改、替换（ –replace ）指定链中的一条规则，按规则序号或内容确定        |
| -F           | 清空（ –flush ）指定链中的所有规则，默认清空表中所有链的内容            |
| -N           | 新建（ –new-chain ）一条用户自己定义的规则链                            |
| -X           | 删除指定表中用户自定义的规则链（ –delete-chain ）                       |
| -n           | 用数字形式（ –numeric ）显示输出结果，若显示主机的 IP 地址而不是主机名  |
| -v           | 查看规则列表时显示详细（ –verbose ）的信息                              |
| -V           | 查看 iptables 命令工具的版本（ –Version ）信息                          |
| -h           | 查看命令帮助信息（ –help ）                                             |
| –line-number | 查看规则列表时，同时显示规则在链中的顺序号                              |

### 3. 链名
可以根据数据流向来确定具体使用哪个链，在 Filter 中的使用情况如下：
| 链名       | 解释                               |
| ---------- | ---------------------------------- |
| INPUT 链   | 处理来自外部的数据。               |
| OUTPUT 链  | 处理向外发送的数据。               |
| FORWARD 链 | 将数据转发到本机的其他网卡设备上。 |

### 4. 条件匹配
条件匹配分为基本匹配和扩展匹配，拓展匹配又分为隐式扩展和显示扩展。
#### 基本匹配

| 匹配参数 | 说明                                                             |
| -------- | ---------------------------------------------------------------- |
| -p       | 指定规则协议,如 tcp, udp,icmp 等,<br>可以使用 all 来指定所有协议 |
| -s       | 指定数据包的源地址参数，可以使 IP 地址、网络地址、主机名         |
| -d       | 指定目的地址                                                     |
| -i       | 输入接口                                                         |
| -o       | 输出接口                                                         |

#### 扩展匹配
...

### 5. 目标值
数据包控制方式包括四种为：

| ACCEPT | 允许数据包通过。                                                         |
| ------ | ------------------------------------------------------------------------ |
| DROP   | 直接丢弃数据包，不给出任何回应信息。                                     |
| REJECT | 拒绝数据包通过，必须时会给数据发送端一个响应信息。                       |
| LOG    | 在 /var/log/messages  文件中记录日志信息，然后将数据包传递给下一条规则。 |
| QUEUE  | 防火墙将数据包移交到用户空间                                             |
| RETURN | 防火墙停止执行当前链中的后续 Rules ，并返回到调用链 (the calling chain)  |

## 常用命令
### 查看 iptables 规则
iptables  – L （ iptables  – L  – v -n ）  


### 允许远程主机进行 SSH 连接

iptables -A INPUT -i eth0 -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT 

### 允许 HTTP
iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT 
iptables -A OUTPUT -o eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT 

### 允许 ping
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT

# iptables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.

- See chains and rules for specific table:

`sudo iptables -t {{table_name}} -vnL`

- Set chain policy rule:

`sudo iptables -p {{chain}} {{rule}}`

- Append rule to chain policy for IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Append rule to chain policy for IP considering protocol and port:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Delete chain rule:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Save iptables configuration:

`sudo iptables-save > {{path/to/iptables_file}}`
