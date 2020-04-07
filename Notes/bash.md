# lsof
lsof


# 重定向输入输出
Example, redirecting standard out with >

For stderr redirection use 2>

redirect stderr to stdout 2>&1

## 如何分别输出(stdout)与错误(stderr)
重定向到不同文件

# 定义一个新函数
function myfunc() {
    # $1 代表第一个参数，$N 代表第 N 个参数
    # $# 代表参数个数
    # $0 代表被调用者自身的名字
    # $@ 代表所有参数，类型是个数组，想传递所有参数给其他命令用 cmd "$@" 
    # $* 空格链接起来的所有参数，类型是字符串
    {shell commands ...}
}



# 改变密码
## passwd username 
## passwd username -d
#$ passwd 

PS1+=

#
$()

## 显示上次程序的返回值
echo $?

# 参考
$1, $2, $3, ... are the positional parameters.
"$@" is an array-like construct of all positional parameters, {$1, $2, $3 ...}.
"$`*`" is the IFS expansion of all positional parameters, $1 $2 $3 ....
$# is the number of positional parameters.
$- current options set for the shell.
$$ pid of the current shell (not subshell).
$_ most recent parameter (or the abs path of the command to start the current shell immediately after startup).
$IFS is the (input) field separator.
$? is the most recent foreground pipeline exit status.
$! is the PID of the most recent background command.
$0 is the name of the shell or shell script.



# local varable

# use $CSP to use the value
# CSP= to change the value
CSP=`~`/CloudStudio

# set CSP to global varable
export CSP

# show all varables
set

# delet varable
unset variable

# show golbal varables
env



#create a soft link
ln -s fillename linkname

#remove link
rm -rf linkname

# show invisiable characters
cat -A filenaem

# get the 4th colume
ask '{print $4}' filename

#通过使用 <(some command) 可以将输出视为文件。例如，对比本地文件 /etc/hosts 和一个远程文件：
diff /etc/hosts <(ssh somehost cat /etc/hosts)


#使用括号扩展（{...}）来减少输入相似文本，并自动化文本组合。这在某些情况下会很有用，例如 mv foo.{txt,pdf} some-dir（同时移动两个文件），cp somefile{,.bak}（会被扩展成 cp somefile somefile.bak）或者 mkdir -p test-{a,b,c}/subtest-{1,2,3}（会被扩展成所有可能的组合，并创建一个目录树）。

# do something in current dir
(cd /some/other/dir && other-command)
# continue in original dir

# $1 代表第一个参数，$N 代表第 N 个参数
# $# 代表参数个数
# $0 代表被调用者自身的名字
# $@ 代表所有参数，类型是个数组，想传递所有参数给其他命令用 cmd "$@" 
# $* 空格链接起来的所有参数，类型是字符串




# 判断文件存在，且该文件是一个目录
-d file

# 判断文件存在，和 -a 等价
-e file

# 判断文件存在，且该文件是一个普通文件（非目录等)
-f file

# 判断文件存在，且可读
-r file

# 判断文件存在，且可写
-w file


# 文件1 比 文件2 新
file1 -nt file2 


# 文件1 比 文件2 旧
file1 -ot file2

num1 -eq num2             # 数字判断：num1 == num2
num1 -ne num2             # 数字判断：num1 != num2
num1 -lt num2             # 数字判断：num1 < num2
num1 -le num2             # 数字判断：num1 <= num2
num1 -gt num2             # 数字判断：num1 > num2
num1 -ge num2             # 数字判断：num1 >= num2









# To implement a for loop:
for file in *;
do 
    echo $file found;
done

# To implement a case command:
case "$1"
in
    0) echo "zero found";;
    1) echo "one found";;
    2) echo "two found";;
    3*) echo "something beginning with 3 found";;
esac

# Turn on debugging:
set -x

# Turn off debugging:
set +x

# Retrieve N-th piped command exit status
printf 'foo' | fgrep 'foo' | sed 's/foo/bar/'
echo ${PIPESTATUS[0]}  # replace 0 with N

# Lock file:
( set -o noclobber; echo > my.lock ) || echo 'Failed to create lock file'

#test this

#赋值等号与命令替换字符之间没有空格!!!!!!!!!!!
