#/bin/sh

currentdir=`pwd`


echo "parament is $#\n"

for gitrepo in ~/CloudStudio ;
  do
    (cd $gitrepo && git add --all && git commit -m "auto commit     by git-auto-save.sh" && git pull && git push)
  done

cd $currentdir
