> https://help.ubuntu.com/community/RenameUSBDrive


### Using the Command line
There are at least 6 separate command line tools used to label a partition - the program used depends on the partition's filesystem type:

For FAT16 and FAT32 partitions, use mlabel from the mtools package.

For NTFS partitions, use ntfslabel from the ntfs-3g package.

For ext2, ext3, or ext4 partitions, use e2label.

For JFS partitions, use jfs_tune.

For ReiserFS (v3) partitions, use reiserfstune.

For XFS partitions, use xfs_admin


### Install the Labeling Program
Based on the package names listed above for each filesystem type, install the correct package for your partition:

sudo apt-get install <package>
Here are all the different ones:

 sudo apt-get install mtools
 sudo apt-get install ntfsprogs
 sudo apt-get install e2fsprogs
 sudo apt-get install jfsutils
 sudo apt-get install reiserfsprogs
 sudo apt-get install xfsprogs
or install the appropriate package from Synaptic.