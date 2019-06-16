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
