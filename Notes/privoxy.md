
# gfwlist
gfwlist 是由 AutoProxy 官方维护，由众多网民收集整理的中国大陆防火长城的域名屏蔽列表；
因为这是 Firefox 浏览器直接使用的一种格式，要在 privoxy 上使用就需要进行相应的格式转换；
这里我提供一个 shell 转换脚本，除了正则语法无法自动处理外，其它的基本 OK，gfwlist2privoxy。

## 关于 gfwlist2privoxy 脚本
脚本依赖 base64、curl(支持 https)、perl5 v5.10.0+

## 获取 gfwlist2privoxy 脚本
curl -4sSkLO https://raw.github.com/zfl9/gfwlist2privoxy/master/gfwlist2privoxy

## 生成 gfwlist.action 文件
bash gfwlist2privoxy '127.0.0.1:1080'

## 检查 gfwlist.action 文件
more gfwlist.action # 一般有 5000+ 行

## 应用 gfwlist.action 文件
mv -f gfwlist.action /etc/privoxy
echo 'actionsfile gfwlist.action' >>/etc/privoxy/config # 不要和全局的配置写一块

## 启动 privoxy.service 服务
systemctl start privoxy.service
systemctl -l status privoxy.service


##环境变量
有两种方式可以实现全局代理，推荐使用 proxychains-ng，因为更彻底。

http_proxy和https_proxy环境变量：非强制性的环境变量，部分软件可能不遵守；
proxychains-ng 的LD_PRELOAD环境变量：强制性的环境变量，用来实现动态库替换。
但实际上，无论哪种方式，体验都不是很好，如果你愿意折腾，推荐使用 ss-redir 透明代理。

### http_proxy 方式：

### privoxy 默认监听端口为 8118
proxy="http://127.0.0.1:8118"
export http_proxy=$proxy
export https_proxy=$proxy
export no_proxy="localhost, 127.0.0.1, ::1"

# no_proxy 环境变量是指不经过 privoxy 代理的地址或域名
# 只能填写具体的 IP、域名后缀，多个条目之间使用 ',' 逗号隔开
# 比如: export no_proxy="localhost, 192.168.1.1, ip.cn, chinaz.com"
# 访问 localhost、192.168.1.1、ip.cn、*.ip.cn、chinaz.com、*.chinaz.com 将不使用代理







# 全局
全局模式是最简单最粗暴的，即：所有流量都走 ss-local，不区分什么国内国外。
所以请确定是否需要这种模式，如果不需要，请跳过此段，直接到 - gfwlist 模式。

## 添加 socks5 转发配置
echo 'forward-socks5 / 127.0.0.1:1080 .' >>/etc/privoxy/config

## 启动 privoxy.service
systemctl start privoxy.service
systemctl -l status privoxy.service






/etc/privoxy/config

转换为http代理
直接走socks代理有时未必是用户的期望，可使用privoxy等软件转化socks代理为http代理。可使用privoxy和squid等工具。 以Privoxy为例，编辑privoxy配置文件，添加socks5转发（不要漏下1080后面的点)：

 forward-socks5 / 127.0.0.1:1080 .
默认监听的是本机的8118端口，即localhost:8118，可更改为监听其他端口，如

 listen-address  127.0.0.1:8010

 使用systemd启动或重启privoxy.service服务，就可以使用了。假设转化后的http代理为127.0.0.1:8010，则在终端中启动（以启动chromium为例）：