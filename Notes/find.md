## basic use

find /folder --name "something"



## maxdepth

## older than 30 days
find ./ -name "*.log" -type f -mtime +30 -exec rm -f {} \;

-mmin n
              File's data was last modified n minutes ago.

Numeric arguments can be specified as

       +n     for greater than n,

       -n     for less than n,

       n      for exactly n.


# To find files by case-insensitive extension (ex: .jpg, .JPG, .jpG):

find . -iname "*.jpg"

# To find directories:
find . -type d

# To find files:
find . -type f

# To find files by octal permission:
find . -type f -perm 777

# To find files with setuid bit set:
find . -xdev \( -perm -4000 \) -type f -print0 | xargs -0 ls -l

# To find files with extension '.txt' and remove them:
find ./path/ -name '*.txt' -exec rm '{}' \;

# To find files with extension '.txt' and look for a string into them:
find ./path/ -name '*.txt' | xargs grep 'string'

# To find files with size bigger than 5 Mebibyte and sort them by size:
find . -size +5M -type f -print0 | xargs -0 ls -Ssh | sort -z

# To find files bigger than 2 Megabyte and list them:
find . -type f -size +200000000c -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'

# To find files modified more than 7 days ago and list file information
find . -type f -mtime +7d -ls

# To find symlinks owned by a user and list file information
find . -type l --user=username -ls

# To search for and delete empty directories
find . -type d -empty -exec rmdir {} \;

# To search for directories named build at a max depth of 2 directories
find . -maxdepth 2 -name build -type d

# To search all files who are not in .git directory
find . ! -iwholename '*.git*' -type f

# To find all files that have the same node (hard link) as MY_FILE_HERE
find . -type f -samefile MY_FILE_HERE 2>/dev/null

# To find all files in the current directory and modify their permissions
find . -type f -exec chmod 644 {} \;


# find

> Find files under the given directory tree, recursively.

- Find files by extension:

`find {{root_path}} -name '{{*.ext}}'`

- Find files matching path pattern:

`find {{root_path}} -path '{{**/lib/**/*.ext}}'`

- Run a command for each file, use {} within the command to access the filename:

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Find files modified since a certain time:

`find {{root_path}} -name '{{}}' -mtime {{-1}}`

- Find files using case insensitive name matching, of a certain size:

`find {{root_path}} -size +500k -size -10MB -iname '{{*.TaR.gZ}}'`

- Delete files by name, older than a certain number of days:

`find {{root_path}} -name '{{*.ext}}' -mtime {{-180}} -delete`

- Find files matching more than one search criteria:

`find {{root_path}} -name '{{*.py}}' -or -name '{{*.r}}'`

- Find files matching a given pattern, while excluding specific paths:

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`
