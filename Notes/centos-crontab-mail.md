var/mail/gl


How to Install and Setup Mail Server on Ubuntu 18.04
We’re almost there, your Ubuntu email server is ready to come online. Here’s what you should do:

1. Install Postfix Email Server
Now it is time to install Postfix. Postfix is an email server written in C. Its main feature is the speed of execution and open source nature. Install it with the following command:

sudo apt install postfix
During installation, we will be asked to configure the package. On the first screen, choose the option Internet Site.

Then, we have to enter the name of the server. In this case test.com.

Postfix is very flexible and allows extensive configuration, but for this tutorial we’ll fix with the default configuration.

2. Add User
Then, we have to add our user to the group mail:

sudo usermod -aG mail $(whoami)
This must be done because in Ubuntu 18.04 only users who are in the mail group can make use of this utility.

After that, we have to create the users and add them to the mail group so they can send and receive mail. I’ll add Gabriel:

sudo useradd -m -G mail -s /bin/bash/ gabriel
Then, we need to set a password to the newly created user:

sudo passwd gabriel