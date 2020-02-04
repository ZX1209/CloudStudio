Ensure your laptop is connected to power.
The upgrade should run uninterrupted.

If at all practical, ensure that you are connected to the Internet via a wired connection.
The upgrade may change your wireless networking applications and drivers.

Ensure your current installation is updated.
Install Updates.
Run Plasma Discover and install all available updates; or

in Konsole run

sudo apt-get update && sudo apt-get dist-upgrade

Allow upgrades to non LTS releases.
In Plasma Discover, Under 'Settings', click the top right ≡ menu and select 'Software Sources' menu item; or

in Konsole run

sudo software-properties-kde
Under the Updates tab, set 'Normal Releases' in the Release Upgrade section.

Upgrade.
Ensure that the package ubuntu-release-upgrader-qt is installed.

Run in Krunner or Konsole.


pkexec do-release-upgrade -m desktop -f DistUpgradeViewKDE &
Alternatively if you wish to do the entire upgrade in a terminal, in Konsole do;


sudo do-release-upgrade -m desktop
The Release Upgrade tool will be downloaded and started.
Follow instructions to complete the upgrade.

Restart
Restart your computer when prompted.

Welcome to Kubuntu 18.10.
Your computer should boot into Kubuntu 18.10, with the new Plasma 5.13 desktop.