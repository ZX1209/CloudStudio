# basic
awk '{print $1, $4}' netstat.txt

# with regex
awk '/E/ {print $1 $2}' dot-paras-cut.txt

# sum integers from a file or stdin, one integer per line:
printf '1\n2\n3\n' | awk '{ sum += $1} END {print sum}'

# using specific character as separator to sum integers from a file or stdin
printf '1:2:3' | awk -F ":" '{print $1+$2+$3}'

# print a multiplication table
seq 9 | sed 'H;g' | awk -v RS='' '{for(i=1;i<=NF;i++)printf("%dx%d=%d%s", i, NR, i*NR, i==NR?"\n":"\t")}' 

# Specify output separator character
printf '1 2 3' | awk 'BEGIN {OFS=":"}; {print $1,$2,$3}'


# -F 指定文本中的分隔符
# pirnt $1 输出第一行的内容
awk -F ";" '{print $1}'

# printf("",) 格式化输出...跟C一样



