/etc/shadowsocks.json

sudo ssserver -c /etc/shadowsocks.json -d restart


{
"server":"0.0.0.0″,
"local_address": "127.0.0.1",
"local_port":1080,
"port_password": {
"443": "main443main",
"444":"tmp444tmp"
},
"timeout":300,
"method":"aes-256-cfb",
"fast_open": false
}