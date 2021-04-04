
#将python3 简写成py
alias py='python3'

#之后运行脚本什么的
py gltest.py
py

# 显示所有别名
alias


alias aliastest='echo "alias test ok"'

# Show a list of your current shell aliases
alias

# Map `ll` to `ls -l` (Can be used per session or put inside a shell config file)
alias ll='ls -l'


# alias

> Creates aliases -- words that are replaced by a command string.
> Aliases expire with the current shell session, unless they're defined in the shell's configuration file, e.g. `~/.bashrc`.

- Create a generic alias:

`alias {{word}}="{{command}}"`

- View the command associated to a given alias:

`alias {{word}}`

- Remove an aliased command:

`unalias {{word}}`

- List all aliased words:

`alias -p`

- Turn rm into an interactive command:

`alias {{rm}}="{{rm -i}}"`

- Create `la` as a shortcut for `ls -a`:

`alias {{la}}="{{ls -a}}"`
