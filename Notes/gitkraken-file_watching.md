https://techsparx.com/blog/2018/02/gitkraken-inotify.html

What is Inotify?
From Wikipedia:

Inotify (inode notify) is a Linux kernel subsystem that acts to extend filesystems to notice changes to the filesystem, and report those changes to applications.

One major use is in desktop search utilities like Beagle, where its functionality permits reindexing of changed files without scanning the filesystem for changes every few minutes, which would be very inefficient.

Since GitKraken automagically notices changes in files in a workspace, it obviously must be using this subsystem on Linux. Since I'm using Ubuntu, this applies to me.

Inotify limits
Type this command:

$ cat /proc/sys/fs/inotify/max_user_watches
8192
This is the limit on your computer.

Each inotify watch consumes a modest amount of memory. On a 64-bit computer like this one, each consumes 1 KB, so 8,192 watches consumes about 8 MB of memory. On a 16GB main memory computer that's a drop in the bucket.

Temporarily increasing the limit is this simple:

# echo 99999 > /proc/sys/fs/inotify/max_user_watches
After which you'll get this:

$ cat /proc/sys/fs/inotify/max_user_watches
99999
To make a permanent change, set fs.inotify.max_user_watches= in sysctl settings. On some systems (Debian/Ubuntu/etc) those settings are in /etc/sysctl.conf and on some others there will be a file in /etc/sysctl.d.

After editing the sysctl settings, run this:

# sysctl -p
fs.inotify.max_user_watches = 99999
Putting it on one line:

# echo fs.inotify.max_user_watches=99999 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
Or on certain other systems:

# echo fs.inotify.max_user_watches=99999 | sudo tee /etc/sysctl.d/40-max-user-watches.conf && sudo sysctl --system
References:

(github.com) github.com guard listen Increasing-the-amount-of-inotify-watchers
(unix.stackexchange.com) unix.stackexchange.com questions kernel-inotify-watch-limit-reached