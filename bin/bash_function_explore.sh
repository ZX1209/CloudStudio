#!/bin/bash

foo(){
    echo "this is a function";
    tree -L 1;
    echo $1
}


ac(){

    git pull;
    git add --all;
    git commit -m "$1"
    git push;
}
