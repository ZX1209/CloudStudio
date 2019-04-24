## 存档
```
# frpc.ini
[common]
server_addr = 159.89.155.162
server_port = 17000

auth_token = 172

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 16000


[web]
type = http
local_ip = 127.0.0.1
local_port = 5000
custom_domains = hardtoname.me
```
./frpc -c frpc.ini


```
# frps.ini
[common]
bind_addr = 0.0.0.0
bind_port = 17000
auth_token = 172
vhost_http_port = 10080

[ssh]
listen_port = 16000



[web]
type = http


# frp 控制面板
dashboard_port = 17500
dashboard_user = admin
dashboard_pwd = admininin
```
/.frps -c frps.ini
