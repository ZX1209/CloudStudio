# combine output
ss -l | { head -n 1 ;  grep :6379; }

# expansion

# ref
https://www.assertnotmagic.com/2018/06/20/bash-brackets-quick-reference/


The first use for single curly braces is expansion.

echo h{a,e,i,o,u}p
# => hap hep hip hop hup
echo "I am "{cool,great,awesome}
# => I am cool I am great I am awesome

mv friends.txt{,.bak}
# => braces are expanded first, so the command is `mv friends.txt friends.txt.bak`
BashCopy
The cool thing is that you can make ranges as well! With leading zeros!

echo {01..10}
01 02 03 04 05 06 07 08 09 10
echo {01..10..3}
01 04 07 10
BashCopy
They can also be used for grouping commands:

[[ "$1" == secret ]] && {echo "The fox flies at midnight"; echo "Ssssshhhh..."}
BashCopy
These commands are all run together in a block, but no new subshell is started.

Thanks for reminding me of this usage, Robert!