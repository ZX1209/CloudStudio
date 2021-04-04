#!/usr/bin/bash

/usr/bin/find /home/gl/Archive/Category-backup/kde5/ -name "*--kde5_backup.zip" -type f -mtime +120 -exec rm -f {} \;

/usr/bin/find /home/gl/gl_home/archive/category-backup/calendars/ -name "*--calendars-backup" -type f -mtime +120 -exec rm -f {} \;