# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

# echo "\n\e[1m this is a test for bash_logout file \e[0m\n"


cd ~/CloudStudio

git add --all

commitdate=`date +"%Y%m%d_%H%M%S"`

git commit -m "${commitdate} : auto commit" && git push 




if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi




