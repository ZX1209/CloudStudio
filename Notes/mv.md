#重命名文件及文件夹
mv tldr-notes notes-others
//mv {文件或文件夹命} {你想要替换的名称}

# 移动文件夹
mv {源文件地址} {目标文件地址(父目录)}

# Move a file from one place to another
mv ~/Desktop/foo.txt ~/Documents/foo.txt

# Move a file from one place to another and automatically overwrite if the destination file exists
# (This will override any previous -i or -n args)
mv -f ~/Desktop/foo.txt ~/Documents/foo.txt

# Move a file from one place to another but ask before overwriting an existing file
# (This will override any previous -f or -n args)
mv -i ~/Desktop/foo.txt ~/Documents/foo.txt

# Move a file from one place to another but never overwrite anything
# (This will override any previous -f or -i args)
mv -n ~/Desktop/foo.txt ~/Documents/foo.txt


# mv

> Move or rename files and directories.

- Move files in arbitrary locations:

`mv {{source}} {{target}}`

- Do not prompt for confirmation before overwriting existing files:

`mv -f {{source}} {{target}}`

- Do not prompt for confirmation before overwriting existing files but write to standard error before overriding:

`mv -fi {{source}} {{target}}`

- Move files in verbose mode, showing files after they are moved:

`mv -v {{source}} {{target}}`
