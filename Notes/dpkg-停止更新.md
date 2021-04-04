sudo dpkg -i {{ package_name }}
sudo apt --fix-broken install

# 停止更新
设置firefox包的状态为 hold；

echo " firefox hold" | dpkg --set-selections

如果想恢复可以更新的状态(install)，执行下面的命令；

echo "firefox install" | dpkg --set-selections

查询所有包的状态；

sudo dpkg --get-selections | more  

查询状态为hold的所有包;

sudo dpkg --get-selections | grep hold


# dpkg

> Debian package manager.

- List package contents:
 List files 'owned' by package(s).
`dpkg -L {{package_name}}`




- Install a package:

`dpkg -i {{/path/to/file}}`

- Remove a package:

`dpkg -r {{package_name}}`

- List installed packages:

`dpkg -l {{pattern}}`


- Find out which package owns a file:

`dpkg -S {{file_name}}`
