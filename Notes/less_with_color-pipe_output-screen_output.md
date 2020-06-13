Use:

git diff --color=always | less -r
--color=always is there to tell git to output color codes even if the output is a pipe (not a tty). And -r is there to tell less to interpret those color codes and other escape sequences. Use -R for ANSI color codes only.

share  improve this answer  follow 
answered Aug 24 '11 at 12:18

Stéphane Gimenez
22.9k22 gold badges6464 silver badges8282 bronze badges
3
@ripper234. With recent gits, git config color.ui true should be enough to obtain colored output, and to automatically run a pager for long outputs. – Stéphane Gimenez Aug 24 '11 at 12:48 
5
In parallel to this Q/A, watch --color 'git diff --cached --color=always' and its friends can bring you some additional awesomeness. – Alois Mahdal Jul 26 '13 at 9:19
35
Isn't using less -R better (or export LESS=R in /etc/profile)? Why would you allow it to display anything but ANSI "color" escape sequences? Also, the man page says Warning: when the -r option is used, less cannot keep track of the actual appearance of the screen (since this depends on how the screen responds to each type of control character). Thus, various display problems may result, such as long lines being split in the wrong place. – x-yuri Jun 10 '14 at 12:57 
8
And if you forgot to specify -r option, you can just type "-r" at the less prompt. This of course works with most or all less options (i.e., -i to turn on ignorecase). – haridsv Jan 7 '16 at 9:32
5
grep --color=always works the same way. This is not part of this question or answer, but I got here from googling about that question so there it is. – Frank Bryce Dec 6 '16 at 14:37