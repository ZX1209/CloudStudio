
# 边界
符号	描述	            例子	    能匹配	    不能匹配
^	行首或字符串开始	^yo	    yo	        ayo
$	行末或字符串结束	yo$	    yo	        yop
\b	单词边界	        \byo\b	mu yo mu	muyomu
\B	非单词边界	    \Byo\B	muyomu	    mu yo mu



# 匹配中文
[^\x00-\xff]




# python
python re 模块















( )([a-z]{1,4}\.{1})*[^\x00-\xff]{1}





[a-z] ([a-z]+\.)?[^\x00-\xff]
