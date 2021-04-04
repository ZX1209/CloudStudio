vim /etc/shadowsocks-python/config.json

{
    "server":"0.0.0.0",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password": {
        "8080": "8080pc8080",
        "8081": "8081ph8081",
        "8082":"8082tmp8082"
    },
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":true
}


