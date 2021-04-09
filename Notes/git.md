git init
git add & git reset
git branch & git checkout
git merge

git show-branch

## 更新另一个分支的文件变化(最好commit 之后)
git checkout {branch} {file}

# 文件权限变更忽略
git config --global core.filemode false
.git/config;filemode=true

# 获取 上游 推送
git remote -v 
git remote add upstream git@github.com:xxx/xxx.git
git fetch upstream
git merge upstream/master
git push 

# git 永久删除文件
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch {path to you file}" --prune-empty --tag-name-filter cat -- --all

# 之后强制推送
git push origin --force --all

# log 更改的文件
git log --stat

# 更改上次的commit
git commit --amend
(git pull && git push)


# 不对0x80以上的字符进行quote，解决git status/commit时中文文件名乱码
git config --global core.quotepath false

# show ignored files (tracked file)
git status --ignored
>https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore

# todo
创建仓库不一定要登录github网站,我们实际上可以在本地通过命令行进行操作
git init
git commit -m "commit for add to github"
http -a {name[:pass]} https://api.github.com/user/repos name=githubApiTest
git remote add origin https://github.com/用户名/仓库名.git
//或者使用ssh,避免输入密码
//git remote add origin git@github.com:用户名/仓库名.git


# git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

# add remote node
git remote add origin {remote_url}
git push -u origin master
git push --set-upstream origin master # 设置默认 push 目标


# 取消上一次 commit (不会删除文件,只是版本树变化)
git reset HEAD^

# 创建并切换到分支
git checkout -b branchName

# 删除分支
git branch -d branchName
# 合并分支
$ git checkout master
$ git merge hotfix

# 本地git仓库关联GitHub仓库
git remote add origin git@github.com:han1202012/TabHost_Test.git





# To set your identity:
git config --global user.name "GL"
git config --global user.email 1404919041@qq.com
# or zxgaoling@gmail.com

# 设置git的编辑器(用于commit):
git config --global core.editor vim

# To enable color:
git config --global color.ui true

#保存密码到硬盘
git config credential.helper store

# 强制lf
git config --global core.autocrlf input

# 在工作区使用CRLF，使用git commit提交的时候git帮你把所有的CRLF转换为LF。
git config --global core.autocrlf true
# 在工作区使用LF
git config --global core.autocrlf input
# 避免文件中有混用换行符
git config --global core.safecrlf true
————————————————
版权声明：本文为CSDN博主「windanchaos」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/windanchaos/article/details/98958462

# To stage all changes for commit:
git add --all

# 快速commit
git commit -m "Your commit message"

# config file
/etc/gitconfig
`~/.gitconfig`
.git/config


#优化log显示
git log --pretty=oneline
git log --oneline


#比较相对于HEAD^(HEAD的上一个提交) HEAD 有什么改变
git diff HEAD^ HEAD

#相对于commit1,commit2有什么改变
git diff commit1 commit2

# 撤销工作树中的更改
git checkout -- <file>

# 撤销暂存区的更改
git reset HEAD [file]
# To stash changes locally, this will keep the changes in a separate changelist
# called stash and the working directory is cleaned. You can apply changes
# from the stash anytime
git stash

# To stash changes with a message
git stash save "message"

# To list all the stashed changes
git stash list

# To apply the most recent change and remove the stash from the stash list
git stash pop

# To apply any stash from the list of stashes. This does not remove the stash
# from the stash list
git stash apply stash@{6}


# Git commit in the past
git commit --date="`date --date='2 day ago'`"
git commit --date="Jun 13 18:30:25 IST 2015"
# more recent versions of Git also support --date="2 days ago" directly

# To change the date of an existing commit
git filter-branch --env-filter \
    'if [ $GIT_COMMIT = 119f9ecf58069b265ab22f1f97d2b648faf932e0 ]
     then
         export GIT_AUTHOR_DATE="Fri Jan 2 21:38:53 2009 -0800"
         export GIT_COMMITTER_DATE="Sat May 19 01:01:01 2007 -0700"
     fi'

# To removed staged and working directory changes
git reset --hard

# To go 2 commits back
git reset --hard HEAD~2

# To remove untracked files
git clean -f -d

# To remove untracked and ignored files
git clean -f -d -x

# To push to the tracked master branch:
git push origin master

# To push to a specified repository:
git push git@github.com:username/project.git

# To delete the branch "branch_name"
git branch -D branch_name

# To make an exisiting branch track a remote branch
git branch -u upstream/foo

# To see who commited which line in a file
git blame filename

# To sync a fork with the master repo:
git remote add upstream git@github.com:name/repo.git    # Set a new repo
git remote -v                                           # Confirm new remote repo
git fetch upstream                                      # Get branches
git branch -va                                          # List local - remote branches
git checkout master                                     # Checkout local master branch
git checkout -b new_branch                              # Create and checkout a new branch
git merge upstream/master                               # Merge remote into local repo
git show 83fb499                                        # Show what a commit did.
git show 83fb499:path/fo/file.ext                       # Shows the file as it appeared at 83fb499.
git diff branch_1 branch_2                              # Check difference between branches
git log                                                 # Show all the commits
git status                                              # Show the changes from last commit

# Commit history of a set of files
git log --pretty=email --patch-with-stat --reverse --full-index -- Admin\*.py > Sripts.patch

# Import commits from another repo
git --git-dir=../some_other_repo/.git format-patch -k -1 --stdout <commit SHA> | git am -3 -k

# View commits that will be pushed
git log @{u}..

# View changes that are new on a feature branch
git log -p feature --not master
git diff master...feature

# Interactive rebase for the last 7 commits
git rebase -i @~7

# Diff files WITHOUT considering them a part of git
# This can be used to diff files that are not in a git repo!
git diff --no-index path/to/file/A path/to/file/B

# To pull changes while overwriting any local commits
git fetch --all
git reset --hard origin/master

# Update all your submodules
git submodule update --init --recursive

# Perform a shallow clone to only get latest commits
# (helps save data when cloning large repos)
git clone --depth 1 <remote-url>

# To unshallow a clone
git pull --unshallow

# Create a bare branch (one that has no commits on it)
git checkout --orphan branch_name

# Checkout a new branch from a different starting point
git checkout -b master upstream/master

# Remove all stale branches (ones that have been deleted on remote)
# So if you have a lot of useless branches, delete them on Github and then run this
git remote prune origin

# The following can be used to prune all remotes at once
git remote prune $(git remote | tr '\n' ' ')

# Revisions can also be identified with :/text
# So, this will show the first commit that has "cool" in their message body
git show :/cool

# Undo parts of last commit in a specific file
git checkout -p HEAD^ -- /path/to/file

# Revert a commit and keep the history of the reverted change as a separate revert commit
git revert <commit SHA>

# Pich a commit from a branch to current branch. This is different than merge as
# this just applies a single commit from a branch to current branch
git cherry-pick <commit SHA1>
