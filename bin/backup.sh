#!/bin/bash

predir=`pwd`

archivedir=~/Archive/Category-backup

cd $archivedir

filename=$(date +'%Y-%m-%d-%H:%M')
filename=$filename-kde.tar.gz


# kde first
# /etc/ /home/gl/CloudStudio/
sudo tar -cvzf $filename  /home/gl/.config/k* /home/gl/.config/plasma*

cd $predir