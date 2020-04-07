# ssh config
```
Host tvps
  HostName 129.211.86.00
  User ubuntu
  Port 22
  IdentityFile /home/gl/Tmp/Download/tencentkey
```
Port 22 要注意,不能写在地址后面
Host,HostName意义很迷啊



`make sure that ~/.ssh/config is right (no port after ip) `


# 使用指南
（1）远程主机收到用户的登录请求，把自己的公钥发给用户。（2）用户使用这个公钥，将登录密码加密后，发送回来。（3）远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录。



# 常用参数
-p 222
指定 222 端口



# ssh

> Secure Shell is a protocol used to securely log onto remote systems.
> It can be used for logging or executing commands on a remote server.

- Connect to a remote server:

`ssh {{username}}@{{remote_host}}`

- Connect to a remote server with a specific identity (private key):

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- Connect to a remote server using a specific port:

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- Run a command on a remote server:

`ssh {{remote_host}} {{command -with -flags}}`

- SSH tunneling: Dynamic port forwarding (SOCKS proxy on localhost:9999):

`ssh -D {{9999}} -C {{username}}@{{remote_host}}`

- SSH tunneling: Forward a specific port (localhost:9999 to slashdot.org:80):

`ssh -L {{9999}}:slashdot.org:80 {{username}}@{{remote_host}}`

- Enable the option to forward the authentication information to the remote machine (see `man ssh_config` for available options):

`ssh -o "ForwardAgent=yes" {{username}}@{{remote_host}}`
