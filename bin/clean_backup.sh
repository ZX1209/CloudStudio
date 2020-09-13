#!/usr/bin/bash

/usr/bin/find /home/gl/Archive/Category-backup/kde5/ -name "*--kde5_backup.zip" -type f -mtime +30 -exec rm -f {} \;