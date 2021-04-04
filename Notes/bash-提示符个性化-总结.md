# bash 提示符 个性化 总结

## `~/.bashrc & ~/.bash_profile`

~/.bashrc 是非登陆式shell启动时会载入的个人配置文件,而~/.bash_profile,则是登陆式shell启动时会载入.

不过,想要有一致的体验的话,最好在其中一个里面写主要内容,另一个调用它.这样不管是哪种情况都能保证会运行我的配置.

比如我现在的东西都写在.bashrc 里 就在 .bash_profile中加上

```bash
if [ -f '.bashrc' ];then
	source .bashrc;
fi
```

若没有文件,直接新键即可.

## `PS1`

PS1 是bash 中的一个环境变量,用来设置提示符

比如,命令行中输入

```bash
PS1="bash_promot->"
export PS1
```

之后,

基本上就可以看到命令行提示符的改变了,不过这种改变只是一时的,想要使这种改变持续最好还是写在~/.bashrc或

~/.bash_profile 中



除了这些固定的字符外,还有其他内置的信息可以用(特殊转义符)

​    \d ：代表日期，格式为weekday month date，例如："Mon Aug 1"

​    \H ：完整的主机名称。例如：我的机器名称为：fc4.linux，则这个名称就是fc4.linux

​    \h ：仅取主机的第一个名字，如上例，则为fc4，**.**linux则被省略

​    \t ：显示时间为24小时格式，如：HH：MM：SS

​    \T ：显示时间为12小时格式

​    \A ：显示时间为24小时格式：HH：MM

​    \u ：当前用户的账号名称

​    \v ：BASH的版本信息

​    \w ：完整的工作目录名称。家目录会以 ~代替

​    \W ：利用basename取得工作目录名称，所以只会列出最后一个目录

​    \# ：下达的第几个命令

​    \$ ：提示字符，如果是root时，提示符为：# ，普通用户则为：$



稍微配置下的话,基本上格式,信息就令人比较满意了

```bash
PS1="# \u @ \h in \w \A Week:\d\n\$ "
```

不过,再加点颜色就更好了呢..



## `$() & tput`

> 在 bash shell 中，$( ) 与\`\`(反引号) 都是用来做命令替换用(commandsubstitution)的。
>
> 例如   version=$(uname -r)和version=\`uname -r\`都可以是version得到内核的版本号
>
> 各自的优缺点：
>
> 1. \` \` 基本上可用在全部的 unix shell 中使用，若写成 shell script ，其移植性比较高。但反单引号容易打错或看错。
> 2. $()并不是所有shell都支持。



[tput](https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x405.html)

 则是一个可以改变命令行颜色与光标的一个工具.不过介绍,直接看配置



```bash
tput sgr0; # reset colors
bold=$(tput bold);
reset=$(tput sgr0);
# Solarized colors, taken from http://git.io/solarized-colors.
black=$(tput setaf 0);
blue=$(tput setaf 27);
cyan=$(tput setaf 44);
green=$(tput setaf 46);
orange=$(tput setaf 208);
purple=$(tput setaf 93);
red=$(tput setaf 161);
violet=$(tput setaf 63);
white=$(tput setaf 15);
yellow=$(tput setaf 136);

PS1="${blue}# ${cyan}\u @ ${green}\h in ${blue}\w ${white}[\A Week:\d]\n${orange}\$ ${reset}"
```

> 其中,tput setaf 后的数字就代表了颜色,其值可以参考:[256color](https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg)



## `PS1+=`

前面的一个太长了,可以拆开来写



```bash
PS1="${blue}# "
PS1+="${cyan}\u "
PS1+="@ "
PS1+="${green}\h "
PS1+="in "
PS1+="${blue}\w "
PS1+="${white}[\A Week:\d]"
PS1+="\n"
PS1+="${orange}\$ ${reset}"

export PS1
```

这样基本显示效果就听不错了,,但是这边有个小坑呢..



## `\[ \]`

简单来说,要把特殊符号用`\[`,`\]`框起就行了..

```bash
PS1="\[${blue}\]# \[${reset}\]"
PS1+="\[${cyan}\]\u \[${reset}\]"
PS1+="@ "
PS1+="\[${green}\]\h \[${reset}\]"
PS1+="in "
PS1+="\[${blue}\]\w \[${reset}\]"
PS1+="\[${white}\][\A Week:\d]\[${reset}\]"
PS1+="\n"
PS1+="\[${orange}\]\$\[${reset}\] "

export PS1
```

完成,

## `dotfile`

github 上有个dotfile的项目一搜就有了,,可以去参考下别人的..

PS1

$()

tput



`\[ \]`



PS1+=



bashrc bash_profile



### Configuration files

See section "6.2 Bash Startup Files" in `/usr/share/doc/bash/bashref.html` ([online link](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)) and [GregsWiki:DotFiles](https://mywiki.wooledge.org/DotFiles) for a complete description.

| File               | Description                                                  | Login shells (see note) | Interactive, *non-login*shells |
| ------------------ | ------------------------------------------------------------ | ----------------------- | ------------------------------ |
| `/etc/profile`     | [Sources](https://wiki.archlinux.org/index.php/Source) application settings in `/etc/profile.d/*.sh` and `/etc/bash.bashrc`. | Yes                     | No                             |
| `~/.bash_profile`  | Per-user, after `/etc/profile`. If this file does not exist, `~/.bash_login` and `~/.profile` are checked in that order. The skeleton file `/etc/skel/.bash_profile` also sources `~/.bashrc`. | Yes                     | No                             |
| `~/.bash_logout`   | After exit of a login shell.                                 | Yes                     | No                             |
| `/etc/bash.bashrc` | Depends on the `-DSYS_BASHRC="/etc/bash.bashrc"` compilation flag. Sources `/usr/share/bash-completion/bash_completion`. | No                      | Yes                            |
| `~/.bashrc`        | Per-user, after `/etc/bash.bashrc`.                          | No                      | Yes                            |

Note:

- Login shells can be non-interactive when called with the `--login` argument.
- While interactive, *non-login* shells do **not** source `~/.bash_profile`, they still inherit the environment from their parent process (which may be a login shell). See [GregsWiki:ProcessManagement#On processes, environments and inheritance](https://mywiki.wooledge.org/ProcessManagement#On_processes.2C_environments_and_inheritance) for details.





## 参考

https://wiki.archlinux.org/index.php/Bash/Prompt_customization

https://www.youtube.com/watch?v=c5RZWDLqifA&index=10&list=PL-osiE80TeTvGhHkpvfmKWOiIPF8UVy6c

https://blog.csdn.net/x1269778817/article/details/46535729



http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/