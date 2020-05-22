# upgrade only one package
apt install {{ package_name }}
apt-get --only-upgrade install {{ package_name }}

# To search a package:
apt search package

# To show package informations:
apt show package

# To fetch package list:
apt update

# To download and install updates without installing new package:
apt upgrade

# To download and install the updates AND install new necessary packages:
apt dist-upgrade

# Full command:
apt update && apt dist-upgrade

# To install a new package(s):
apt install package(s)

# To uninstall package(s)
apt remove package(s)


# apt

> Package management utility for Debian based distributions.

- Update list of packages and versions available. This should be run before running further apt commands:

`sudo apt update`

- Search for packages:

`apt search {{package}}`

- Show information for a package:

`apt show {{package}}`

- Install a new package:

`sudo apt install {{package}}`

- Remove a package (using "purge" instead also removes its configuration files):

`sudo apt remove {{package}}`

- Upgrade installed packages to the newest available versions:

`sudo apt upgrade`
