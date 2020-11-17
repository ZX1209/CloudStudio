#!/usr/bin/env bash
/usr/bin/pactl -- set-sink-volume 0 +30% 
/usr/bin/mpv /home/gl/gl_home/archive/category-multiMedia/sounds/bell.oga 
notify-send "cron info" "整点报时"
/usr/bin/pactl -- set-sink-volume 0 -30%