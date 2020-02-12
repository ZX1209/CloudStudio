There are two cases:

the application you want to use handles SOCKS5 proxies (for example Firefox), then you just have to configure it to use the proxy.
the application you want to use does not handle SOCKS proxies, then you can try to use tsocks or proxychains-ng.
In Firefox, you can use the SOCKS proxy in the menu Preferences > Network > Settings. Choose Manual Proxy Configuration, and set the SOCKS Host (and only this one, make sure the other fields, such as HTTP Proxy or SSL Proxy are left empty). For example, if a SOCKS5 proxy is running on localhost port 8080, put 127.0.0.1 in the SOCKS Host field, 8080 in the Port field, and validate.

If using proxychains-ng, the configuration takes place in /etc/proxychains.conf. You may have to uncomment the last line (set by default to use Tor), and replace it with the parameters of the SOCKS proxy. For example, if you are using the same SOCKS5 proxy as above, you will have to replace the last line by:

socks5 127.0.0.1 8080