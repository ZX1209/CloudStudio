## tcp client server template
> 一个 socket.socket 对象 来进行连接,发送  绑定,监听..

```python
#server.py

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

```python
# client.py
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
```

## udp广播,udp braodcast

```python
# client
# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(5)

server_address = ('255.255.255.255', 9434)

sock.sendto(data,address)
```

```python
# server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('', 9434)

sock.bind(server_address)

while True:
	data, address = sock.recvfrom(4096) # only recvfrom 
	data = str(data.decode('UTF-8'))

	if data == 'pfg_ip_broadcast_cl':
		#print('responding...')
		sent = sock.sendto(b"data", address)
		#print('Sent confirmation back')
```


## end




```py

def BytestoBin(bs):
    for i in bs:
        print(bin(i),end=" ")


def ana_head(q,n):
    list1 = []
    print (u'包长度%d'%len(q))
    print (u'标识为：%x%x'%(ord(q[0]),ord(q[1])))
    print (u'报文参数为：%x%x'%(ord(q[2]),ord(q[3])))
    print (u'问题数：%x%x'%(ord(q[4]),ord(q[5])))
    print (u'应答数：%x%x'%(ord(q[6]),ord(q[7])))
    print (u'授权机构数：%x%x'%(ord(q[8]),ord(q[9])))
    print (u'附加信息数：%x%x'%(ord(q[10]),ord(q[11])))
    for i in range(n+1):
        nu = 12+i
        list1.append('%d'%ord(q[nu]))
    str1 = ''.join(list1)
    print (u'查询信息为：%s'%str1)
    print (u'查询类型为：%x%x'%(ord(q[n+13]),ord(q[n+14])))
    print (u'查询类为：%x%x'%(ord(q[n+15]),ord(q[n+16])))
def ana_fin(c,x):
    times = ord(c[7])
    g = x+16
    for i in range(times):
        print ('*******************************************************')
        print (u'指针：%x%x'%(ord(c[g+1]),ord(c[g+2])))
        print (u'第%d个资源的响应类型：%x%x'%(i+1,ord(c[g+3]),ord(c[g+4])))
        print (u'第%d个资源的响应类：%x%x'%(i+1,ord(c[g+5]),ord(c[g+6])))
        print (u'第%d个资源的生存时间：%d%d%d%d秒'%(i+1,ord(c[g+7]),ord(c[g+8]),ord(c[g+9]),ord(c[g+10])))
        print (u'第%d个资源的数据长度：%x%x'%(i+1,ord(c[g+11]),ord(c[g+12])))
        print (u'返回的IP地址：%d.%d.%d.%d'%(ord(c[g+13]),ord(c[g+14]),ord(c[g+15]),ord(c[g+16])))
        g+=16
    print ('-----------------------------------------------------')



class dns():
    def _init_(self):
        pass
    def coding(self,second,first,root):
        len_root = '%s'%chr(len(root))
        l_root = len(root)
        len_first = '%s'%chr(len(first))
        l_first = len(first)
        if second:
            len_second ='%s'%chr(len(second))
            l_second = len(second)
            self.num = l_root+l_first+l_second+3
            q = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00%s%s%s%s%s%s\x00\x00\x01\x00\x01'%(len_second,second,len_first,first,len_root,root)
            return q
        else:
            q = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00%s%s%s%s\x00\x00\x01\x00\x01'%(len_first,first,len_root,root)
            self.num = l_root+l_first+2
            return q
    def send(self,q):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(q,('8.8.8.8',53))
        sock_recv = sock.recv(4096)
        return sock_recv
    def info(self,q):
        flag = '%x%x'%(ord(q[2]),ord(q[3]))
        if flag == '10':
            print ('-----------------------------------------------------')
            print (u'此为查询报文')
            ana_head(q,self.num)
        else:
            print ('-----------------------------------------------------')
            print (u'此为返回报文')
            ana_head(q,self.num)
            ana_fin(q,self.num)

```

# 测试端口联通性
```py
import socket


successPorts = []
for port in range(26737,50000):
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        client.settimeout(1)
        client.connect(('138.128.203.197',port))
        print("server port:{0} connect OK! ".format(port))
        successPorts.append(port)
    except Exception as e:
        print("server port:{0} can't connect ! error:{1}".format(port,e))

    print("below are success ports")
    for port in successPorts:
        print(port)

    client.close()

```



# byte code
bytes(str,encoding='utf-8')
str.decode('utf-8')
















socket(family=AF_INET, type=SOCK_STREAM, proto=0)

socket类型    描述
socket.AF_UNIX  用于同一台机器上的进程通信（既本机通信）
socket.AF_INET  用于服务器与服务器之间的网络通信(指定使用IPv4)
socket.AF_INET6 基于IPV6方式的服务器与服务器之间的网络通信
socket.SOCK_STREAM  基于TCP的流式socket通信
socket.SOCK_DGRAM   基于UDP的数据报式socket通信
socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次SOCK_RAW也可以处理特殊的IPV4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头
socket.SOCK_SEQPACKET   可靠的连续数据包服务

服务端Socket的方法

s.bind(address)
　 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
s.listen(backlog)
　　开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
s.setblocking(bool)
　　是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
s.accept()
　　接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
　　接收TCP 客户的连接（阻塞式）等待连接的到来

s.connect(address)
　　连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
s.connect_ex(address)
　　同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061

s.close()
　　关闭套接字
s.recv(bufsize[,flag])
　　接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
s.recvfrom(bufsize[.flag])
　　与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
s.send(string[,flag])
　　将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
s.sendall(string[,flag])
　　将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
   内部通过递归调用send，将所有内容发送出去。
s.sendto(string[,flag],address)
　　将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
s.settimeout(timeout)
　　设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）
s.getpeername()
　　返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
s.getsockname()
　　返回套接字自己的地址。通常是一个元组(ipaddr,port)
s.fileno()
　　套接字的文件描述符
s.setblocking(flag)
    如果flag为0，则将套接字设置为非阻塞模式，否则将套接字设置为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数  据，或send()调用无法立即发送数据，那么将引起socket.error异常。



服务端Socket的实现
伪代码

# 创建一个socket
s = socket()
# 绑定地址和端口，参数元组
s.bind()
# 监听
s.listen()
while True:
    # 阻塞式连接
    accept()


客户端Socket的实现
伪代码

cs = socket()
cs.connect()
while True:
    cs.send()
cs.close()