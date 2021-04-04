also with chrome-no-wallet.md

KDE 5/Plasma 5.8:

Add the following lines to the end of ~/.config/kwalletrc

[Wallet]
Enabled=false
Restart Plasma.

KDE4:
KDE Wallet is a core part of KDE, it's in the package kdebase-runtime.

To disable it run kcmshell4 kwalletconfig and continue at step 3 or start from the beginning:

Start System setings
Open Account Details
Go to the "KDE Wallet" tab
Uncheck Enable the KDE Wallet subsystem
Click Apply to apply the changes and close the settings window.
To get a list of the programs that depends on the kdebase-runtime package, run:

 apt-cache --no-enhances --no-suggests --no-recommends --installed rdepends kdebase-runtime
On Ubuntu, the output shows just "kdebase-runtime [newline] Reverse Depends:". On Kubuntu, a whole list follows.