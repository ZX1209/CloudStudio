# free and install
pip install -r requirement.txt
pip freeze > requirement.txt


# pip 安装编译不了?
试试下载 whl文件
https://www.lfd.uci.edu/~gohlke/pythonlibs/

# update source list for china
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

## tmp use
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

# Search for packages
pip search SomePackage

# Install some packages
pip install SomePackage

# Install some package in user space
pip install --user SomePackage

# Upgrade some package
pip install --upgrade SomePackage

# Output and install packages in a requirement file
pip freeze > requirements.txt
pip install -r requirements.txt

#展示 包 细节 (位置,说明)
# Show details of a package
pip show SomePackage

# List outdated packages
pip list --outdated

# Upgrade all outdated packages, thanks to http://stackoverflow.com/a/3452888
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U

# Upgrade outdated packages on latest version of pip
pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U

# Install specific version of a package
pip install -I SomePackage1==1.1.0 'SomePackage2>=1.0.4'


# pip

> Python package manager.

- Install a package:

`pip install {{package_name}}`

- Install a specific version of a package:

`pip install {{package_name}}=={{package_version}}`

- Upgrade a package:

`pip install -U {{package_name}}`

- Uninstall a package:

`pip uninstall {{package_name}}`

- Save installed packages to file:

`pip freeze > {{requirements.txt}}`

- Install packages from file:

`pip install -r {{requirements.txt}}`
