pip3 install bs4

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_string)

# css 选择器器语法,,~~不怎么好用~~ 真香
r = soup.select("")
r[0].text
r.span.attrs['style'] = "..."

# attrs

# decode

# node.node.node
quote.span.attrs
tag.tag.attrs
上面的只能找到第一个

find_all 是找到所有的

# 另一种,还行.. 
r2 = soup.find_all('div',id="search")


```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-


# /home/gl/python-smtp

import requests
from bs4 import BeautifulSoup
import sqlite3
import logging as log

log.basicConfig(format='%(levelname)s: %(message)s\n',level=log.DEBUG)

connect = sqlite3.connect('quotescom')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE QUOTES(ID INTEGER PRIMARY KEY NOT NULL,QUOTE VARCHAR(2000));''')

# 
for i in range(1,100):
    response = requests.get('http://quotes.toscrape.com/page/'+str(i))
    html = response.text
    soup = BeautifulSoup(html,features="html.parser")
    quotes = soup.select('div.quote')


    for quote in quotes:
        quote.attrs['style'] = "padding: 10px;margin-bottom: 30px;border: 1px solid #333333;border-radius: 5px;box-shadow: 2px 2px 3px #333333;"
        quote.small.attrs['style'] ="font-weight: bold;color: #3677E8;"
        quote.span.attrs['style'] = "display: block;margin-bottom: 5px;font-size: large;font-style: italic;"
        tags = quote.select('a.tag')
        for tag in tags:
            tag.attrs['style'] = "padding: 2px 5px;border-radius: 5px;color: white;font-size: small;background-color: #7CA3E6;"
        
        atags = quote.select('a')
        for atag in atags:
            atag.attrs['href'] = 'http://quotes.toscrape.com' + atag.attrs['href']




        quote = '<body style="margin-bottom: 60px;">'+quote.decode()+'</body>'
        cursor.execute("insert into QUOTES(QUOTE) values(?)", (quote,))
    connect.commit()

    log.debug(str(i)+' success')

    next = soup.select('li.next')
    if next == []:
        break

connect.close()
log.debug('finished')
```