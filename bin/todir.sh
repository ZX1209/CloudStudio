#!/bin/bash

cd ~/CloudStudio

dir="./tmp/"


for i in `ls`;do
  if [ -f $i ];then
    mv $i ${dir}${i}
  fi
done

