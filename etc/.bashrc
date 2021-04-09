# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# cheat etc
export NOTES_MY='~/CloudStudio/Notes'
export DEFAULT_CHEAT_DIR=$NOTES_MY

export NOTES_OTHERS='~/CloudStudio/Notes/notes-others'
export CHEATPATH=$NOTES_MY:$NOTES_OTHERS

export CHEATCOLORS=true

export CHEAT_EDITOR=vim
# end cheat etc

#export DISPLAY=:0.0

# 太耗费启动时间了,还是换到crontab 中去吧
# (cd ~/CloudStudio && git add --all && git commit -m "auto commit by .bashrc" && git pull && git push)
#(cd ~/CloudStudio && git status && git pull)


#cheat path (win sub for linux proble)
export PATH=~/.local/bin:$PATH


# add python script file to syspath
export PATH=~/CloudStudio/bin/GLpackage:~/CloudStudio/bin:$PATH

# active autojump
. /usr/share/autojump/autojump.sh


# PS1 command line infomation
# use \[ and \] to close \e[0m(non print character) or it will have cursor proble
# i don't want to change it any more my eyes are about to bland fuck...
# PS1="\[\e[1;34m\]#\[\e[0m\] \[\e[36m\]\u\[\e[0m\] @ \[\e[32m\]\h\[\e[0m\] in \[\e[1;33m\]\w\[\e[0m\] [\[\e[4m\]\A\[\e[0m\] Week:\d] \[\e[0;31m\]  \[\e[0m\]\n\[\e[1;31m\]\$\[\e[0m\] "


# 放到你的配置文件中，给 man 增加漂亮的色彩高亮
export LESS_TERMCAP_mb=$'\E[1m\E[32m'
export LESS_TERMCAP_mh=$'\E[2m'
export LESS_TERMCAP_mr=$'\E[7m'
export LESS_TERMCAP_md=$'\E[1m\E[36m'
export LESS_TERMCAP_ZW=""
export LESS_TERMCAP_us=$'\E[4m\E[1m\E[37m'
export LESS_TERMCAP_me=$'\E(B\E[m'
export LESS_TERMCAP_ue=$'\E[24m\E(B\E[m'
export LESS_TERMCAP_ZO=""
export LESS_TERMCAP_ZN=""
export LESS_TERMCAP_se=$'\E[27m\E(B\E[m'
export LESS_TERMCAP_ZV=""
export LESS_TERMCAP_so=$'\E[1m\E[33m\E[44m'





ac(){
    git pull;
    git add --all && git commit -m "$1" && git push;
}


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
yellow=$(tput setaf 227);

PS1="\[${blue}\]# \[${reset}\]"
PS1+="\[${cyan}\]\u \[${reset}\]"
PS1+="@ "
PS1+="\[${green}\]\h \[${reset}\]"
PS1+="in "
PS1+="\[${white}\][\A Week:\d]\[${reset}\]"
PS1+="\n"
PS1+="\[${yellow}\]\w \[${reset}\]"
PS1+="\n"
PS1+="\[${red}\]\$\[${reset}\]"

export PS1




# added by Anaconda3 2018.12 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/home/gl/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/home/gl/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/gl/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/home/gl/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<


# cuda start
# export  PATH=/usr/local/cuda-9.0/bin:$PATH
# export  LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64$LD_LIBRARY_PATH

# cund end
PYTHONPATH=~/CloudStudio/bin/
export PYTHONPATH

# cli proxy start
# privoxy port
export http_proxy=http://127.0.0.1:8118/
export https_proxy=$http_proxy
export ftp_proxy=$http_proxy
export rsync_proxy=$http_proxy
export no_proxy="localhost, 127.0.0.1, ::1"
export ALL_PROXY=http://127.0.0.1:8118/
# cli proxy end

# flutter start
export FLUTTER_PATH=/home/gl/gl_home/archive/category-appdata/Linux/Flutter/flutter/bin/
export PATH=$PATH:$FLUTTER_PATH

export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

export PATH="$PATH":"$HOME/gl_home/archive/category-appData/Linux/Flutter/flutter/.pub-cache/bin"
export ENABLE_FLUTTER_DESKTOP=true

# flutter config --enable-web

# flutter end

# crontab start
## sublime
# export VISUAL=/home/gl/CloudStudio/bin/sublime-wait.sh
# export EDITOR=/home/gl/CloudStudio/bin/sublime-wait.sh

## vim
# export VISUAL=/usr/bin/vim
# export EDITOR=/usr/bin/vim

## vscode
export VISUAL=/home/gl/CloudStudio/bin/code-wait.sh
export EDITOR=/home/gl/CloudStudio/bin/code-wait.sh
# EDITOR

# crontab end

# andriod start
export ANDROID_HOME=/home/gl/gl_home/archive/category-appData/Linux/android-sdk/
export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
# andriod end

# java start
# export JAVA_HOME=/usr/lib/jdk1.8.0_212/
# export JRE_HOME=${JAVA_HOME}/jre
# export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
# export PATH=$PATH:${JAVA_HOME}/bin

# java end

# gradle?
# export GRADLE_OPTS='-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=1080'
# gradle end

# npm start
export PATH=~/.npm-global/bin:$PATH
# npm end

# func start

function applist(){
    echo $1 >> ~/CloudStudio/tmp/applist.txt 
    
}

function autorestart(){
    sudo rtcwake -m freeze -l -t $(date +%s -d "tomorrow 06:58")
}

function screen_off(){
    xset dpms force off
}

# func end

# alias start
alias python=python3
alias ipython=ipython3
alias py=python3
alias ipy=ipython3

alias ct='python /home/gl/gl_home/projects/play_ground/template-python/try/docopt_cli_parser.py'
alias copytemplate='python /home/gl/gl_home/projects/play_ground/template-python/try/docopt_cli_parser.py'

# alias end



xset r rate 200 20  


# shopt start
shopt -s huponexit
# shopt end