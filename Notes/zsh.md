当 Zsh 启动时，它会按照顺序依次读取下面的配置文件：

/etc/zsh/zshenv
该文件应该包含用来设置PATH 环境变量[ broken link: invalid section]以及其他一些环境变量的命令；不应该包含那些可以产生输出结果或者假设终端已经附着到 tty 上的命令。
~/.zshenv
该文件和 /etc/zsh/zshenv 相似，但是它是针对每个用户而言的。一般来说是用来设置一些有用的环境变量。
/etc/zsh/zprofile
这是一个全局的配置文件，在用户登录的时候加载。一般是用来在登录的时候执行一些命令。请注意，在 Arch Linux 里该文件默认包含一行配置，用来加载 /etc/profile 文件，详见 #全局配置文件。
/etc/profile
在登录时，该文件应该被所有和伯克利（Bourne）终端相兼容的终端加载：它在登录的的时候会加载应用相关的配置（/etc/profile.d/*.sh）。注意在 Arch Linux 里，Zsh 会默认加载该文件。
~/.zprofile
该文件一般用来在登录的时候自动执行一些用户脚本。
/etc/zsh/zshrc
当 Zsh 被作为交互式终端的时候，会加载这样一个全局配置文件。
~/.zshrc
当 Zsh 被作为交互式终端的时候，会加载这样一个用户配置文件。
/etc/zsh/zlogin
在登录完毕后加载的一个全局配置文件。
~/.zlogin
和 /etc/zsh/zlogin 相似，但是它是针对每个用户而言的。
/etc/zsh/zlogout
在注销的时候被加载的一个全局配置文件。
~/.zlogout
和 /etc/zsh/zlogout 相似，但是它是针对每个用户而言的.


# A plain old glob
print -l *.txt
print -l **/*.txt

# Show text files that end in a number from 1 to 10
print -l **/*<1-10>.txt

# Show text files that start with the letter a
print -l **/[a]*.txt

# Show text files that start with either ab or bc
print -l **/(ab|bc)*.txt

# Show text files that don't start with a lower or uppercase c
print -l **/[^cC]*.txt

# Show only directories
print -l **/*(/)

# Show only regular files
print -l **/*(.)

# Show empty files
print -l **/*(L0)

# Show files greater than 3 KB
print -l **/*(Lk+3)

# Show files modified in the last hour
print -l **/*(mh-1)

# Sort files from most to least recently modified and show the last 3
print -l **/*(om[1,3])

# `.` show files, `Lm-2` smaller than 2MB, `mh-1` modified in last hour,
# `om` sort by modification date, `[1,3]` only first 3 files
print -l **/*(.Lm-2mh-1om[1,3])

# Show every directory that contain directory `.git`
print -l **/*(e:'[[ -d $REPLY/.git ]]':)

# Return the file name (t stands for tail)
print -l *.txt(:t)

# Return the file name without the extension (r stands for remove_extension)
print -l *.txt(:t:r)

# Return the extension
print -l *.txt(:e)

# Return the parent folder of the file (h stands for head)
print -l *.txt(:h)

# Return the parent folder of the parent
print -l *.txt(:h:h)

# Return the parent folder of the first file
print -l *.txt([1]:h)

# Parameter expansion
files=(*.txt)          # store a glob in a variable
print -l $files
print -l $files(:h)    # this is the syntax we saw before
print -l ${files:h}
print -l ${files(:h)}  # don't mix the two, or you'll get an error
print -l ${files:u}    # the :u modifier makes the text uppercase

# :s modifier
variable="path/aaabcd"
echo ${variable:s/bc/BC/}    # path/aaaBCd
echo ${variable:s_bc_BC_}    # path/aaaBCd
echo ${variable:s/\//./}     # path.aaabcd (escaping the slash \/)
echo ${variable:s_/_._}      # path.aaabcd (slightly more readable)
echo ${variable:s/a/A/}      # pAth/aaabcd (only first A is replaced)
echo ${variable:gs/a/A/}     # pAth/AAAbcd (all A is replaced)

# Split the file name at each underscore
echo ${(s._.)file}

# Join expansion flag, opposite of the split flag.
array=(a b c d)
echo ${(j.-.)array} # a-b-c-d
