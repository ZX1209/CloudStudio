# 知识结构网格图
## n维向量
### 运算
加法,数乘,内积,schmidt(斯密特正交化)
### 线性表示
#### 概念
$如果\beta = k_1 \alpha_1+\cdots+k_s \alpha_s$ 
$称\beta 可由\alpha_1,\cdots, \alpha_s 线性表出$ 
#### 判定
- 方程组 $x_1 \alpha_1+x_2 \alpha_2+\cdots+x_s \alpha_s = \beta$  有解
- $r(\alpha_1,\cdots,\alpha_s) = r(\alpha_1,\cdots,\alpha_s,\beta)$ 
- $\alpha_1,\cdots,\alpha_s无关 = \alpha_1,\cdots,\alpha_s,\beta 相关$ 
#### 等价
?
### 线性相关
#### 概念
#### 判定
### 线性无关
### 极大线性无关组
### 向量组的秩
### 向量空间(仅数学一)


# 基本内容与重要结论
## 基础知识
n个数 $\alpha_1,\alpha_1,\cdots,\alpha_n$ 所组成的有序数组
$\alpha = [\alpha_1,\alpha_1,\cdots,\alpha_n]^T或\alpha = [\alpha_1,\alpha_1,\cdots,\alpha_n]$ 
称为n维向量,前一个表示列向量,后者称为行向量
分量,坐标

---
设n维向量 $\alpha =[ a_1,a_2,\cdots,a_n]^T,\beta = [ b_1,b_2,\cdots,b_n]^T$ ,则
### 向量加法
$\alpha+\beta = [a_1+b_1,a_2+b_2,\cdots,a_n+b_n]^T$ 
### 数乘向量
$k \alpha = [ k a_1,k a_2,\cdots,k a_n]^T$ 

### 向量内积 :star:
$(\alpha,\beta) =\alpha^T \beta = \beta^T \alpha = a_1 b_1+a_2 b_2+\cdots+a_n b_n$ 
> 向量 $\alpha = [ a_1,a_2,\cdots,a_n]^T$的长度 $||a|| = \sqrt{\alpha^T \alpha} = \sqrt{a_1^2,a_2^2,\cdots,a_n^2}$  
> $\alpha^T \alpha = 0 \leftrightarrow \alpha=O$ 
> $若(\alpha,\beta) = 0,称\alpha 与 \beta 正交,记为A \perp B$ 

定义3.1 : 
$设 a_1,a_2,\cdots,a_n 是n维向量, k_1,k_2,\cdots,k_n 是一组实数,$
$称 k_1 a_1+k_2 a_2+\cdots+k_n a_n 是 a_1,a_2,\cdots,a_n 的线性组合$ 

定义3.2 : 
$对n维向量 a_1,a_2,\cdots,a_n,和\beta ,若存在实数 k_1,k_2,\cdots,k_n,$
$使得 k_1 a_1+k_2 a_2+\cdots+k_n a_n =\beta$ 
$称 \beta 是 a_1,a_2,\cdots,a_n 的线性组合,或者说可有其线性表出$ 

定义 3.3 :
对与n维向量a,如果存在不全为零的数使得其去k的向量内积为零,
则乘向量组a线性相关(分量可由其他分量表示)
否则,称向量组a线性无关

定义 3.4 : 
设有两个n维向量组a,b;
如果a中**每个向量**都可由b中向量线性表出,则称a可由b线性表出
如果两个向量组可以互相线性表出,则称两个向量组等价

定义 3.5 :
极大线性无关组 

定义 3.6 :
极大线性无关组所含向量个数r称为这个向量组的秩

> 向量可以用该基下的坐标表示，这样一组就构成了向量组了。矩阵用来表示不同线性空间的基之间的线性映射

## 重要定理
定理 3.1 :
$
向量\beta 可由 向量组 a_1,a_2,\cdots,a_n, 线性表出 \\
\leftrightarrow  非齐次线性方程 a x = \beta 有解 \\
\leftrightarrow 秩r(a) = r(a,\beta)
$ 

定理 3.2 :
$
向量组 a_1,a_2,\cdots,a_n, 线性相关 \\
\leftrightarrow  齐次线性方程 a x = 0 有非零解解 \\
\leftrightarrow 向量组的秩r(a) < n
$ 

推论1: n个n维向量线性相关的充分必要条件是对应行列式值为0

推论2: n+1各n维行列式一定线性相关

推论3:  部分组相关 -> 整体组相关; 整体组无关,部分组无关;

定理 3.3 :
如果向来组线性相关,则其中必有一个向量可用其余向量线性表出,反之亦然

定理 3.4 : 如果 a 线性无关,a,\beta 线性相关,则\beta 可由a线性表出,且标示法唯一

定理 3.5 :
如果 向量组$a_1, a_2,\cdots,a_s$,可由向量组 $b_1, b_2,\cdots,b_t$线性表示,且s>t,
那么$a_1, a_2,\cdots,a_s$线性相关.
即如果多数向量能用少数向量线性表出,那么多数向量一定线性相关

推论 : 如果 向量组$a_1, a_2,\cdots,a_s$线性无关,且可由$b_1, b_2,\cdots,b_t$线性表示线性表出,则 $s \leq t$ 

定理 3.6 : 
设$a_1, a_2,\cdots,a_s$,可由向量组 $b_1, b_2,\cdots,b_t$线性表示,则$r(a_1, a_2,\cdots,a_s) \leq r(b_1, b_2,\cdots,b_t)$
推论: 两个等价的向量组秩也等价

定理 3.7 : 
如果r(A)=n,则A中有n各线性无关的列向量,


## 主要公式
# 典型例题