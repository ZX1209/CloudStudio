#rename rules
rename 's/{search parten}/{replace parten}' files
#like
rename 's/\.md//' *.md



# Lowercase all files and folders in current directory
rename 'y/A-Z/a-z/' *

# -n 显示改变结果 但不实际改变

# $ 代表结尾
rename -n 's/$/.md/' *
