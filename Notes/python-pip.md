# see pip.md

# version
pip --version

#展示 包 细节 (位置,说明)
# Show details of a package
pip show SomePackage

# List outdated packages
pip list --outdated

# install requirements
pip install -r requirements.txt

# Search for packages
pip search SomePackage
The query is just a string to search for and will match packages and their descriptions.

# Install some packages
pip install SomePackage

# Install some package in user space
pip install --user SomePackage

# Upgrade some package
pip install --upgrade SomePackage

pip install --upgrade -r requirements.txt

# upgrade pip
python -m pip install --upgrade pip

# Output and install packages in a requirement file
pip freeze > requirements.txt
pip install -r requirements.txt





# Upgrade all outdated packages, thanks to http://stackoverflow.com/a/3452888
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U

# Upgrade outdated packages on latest version of pip
pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U

# Install specific version of a package
pip install -I SomePackage1==1.1.0 'SomePackage2>=1.0.4'

# uninstall package..
pip uninstall certifi
pip uninstall urllib3 -y