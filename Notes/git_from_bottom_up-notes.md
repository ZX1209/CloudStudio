git hash-object [filename]


git cat-file -t [code]

git cat-file blob [code]

git ls-tree [code]


git rev-parse HEAD
decodes the alias into the commit it references



git write-tree

echo "Initial commit" | git commit-tree 0563f77

echo 5f1bc85745dcccce6121494fdd37658cb4ad441f > .git/refs/heads/master
or
git update-ref refs/heads/master 5f1bc857

git symbolic-ref HEAD refs/heads/master

git log


A branch is nothing more than a named reference to a commit


# show all objects
find .git/objects/ -type f | sort


# 清楚现在index的所有更改回到某一分治
git reset --hard [code]

--since="2 weeks ago"
--until="2 weeks ago"


git show-branch