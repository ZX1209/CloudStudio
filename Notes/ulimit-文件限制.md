> https://posidev.com/blog/2009/06/04/set-ulimit-parameters-on-ubuntu/

Set ulimit parameters on ubuntu
16 Replies
By default the number of open files  pro user in Ubuntu 8.04   is 1024. In my case this number was  too small so I have to increase it.This is done with the  ulimit command:

$ulimit -a   # see all the kernel parameters
$ulimit -n   #see the number of open files
$ulimit -n 9000  #  set the number open files to 9000

The problem with this way is that the ulimit parameter is only set currently  for this command terminal and user.If you open a new tab and type again ulimit -a you will see that the number of open files is 1024.This means that after a reboot you’ll need to set the parameter again.

First, in order to set this options automatically  you have to edit the etc/security/limits.conf file.

$sudo gedit /etc/security/limits.conf    #open the file in gedit

The # means that this part is commented.The wildcard * means  for all users.We need to set the nofile option meaning maximum number of open files.If you want to change the number of files of user, you should add this line in the limits.conf:

user  soft  nofile 9000

user  hard  nofile 65000

If  you want to set the nofile only for superuser you just write root instead of user.

root soft  nofile 9000

root hard  nofile 65000

Second you have to add a line in the /etc/pam.d/common-session file:

$ sudo gedit /etc/pam.d/common-session #open the file in gedit

Then add the line:

session required pam_limits.so

Now after rebooting you can see in the terminal with ulimit -a the change.

The option with wildcard *didn’t work for me , because I used root accout to run my programms and wildcard option doesn’t affect the superuser.

Remark: Using the same steps you should be able to set and change other parameters ( core file size, max user processes, stack size ….) from the ulimit options.

References:

Open File Limits Settings on Ubuntu
ulimits not set according to /etc/security/limits.conf for root – update documentation
Hacking Ubuntu to Improve Performance
This entry was posted in DBT2, Ubuntu and tagged DBT2, Ubunt

# ulimit

> Get and set user limits.

- Get the properties of all the user limits:

`ulimit -a`

- Get hard limit for the number of simultaneously opened files:

`ulimit -H -n`

- Get soft limit for the number of simultaneously opened files:

`ulimit -S -n`

- Set max per-user process limit:

`ulimit -u 30`
