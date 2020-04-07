## if elif else

## Multi-Line Statements
Statements in Python typically end with a new line. Python, however, allows the use of the line continuation character (\) to denote that the line should continue. For example −

total = item_one + \
   item_two + \
   item_three

## '',"",""" """

## comment
 #

## input
input("\n\nPress the enter key to exit.")

## Multiple Statements on a Single Line
The semicolon ( ; ) allows multiple statements on a single line given that no statement starts a new code block. Here is a sample snip using the semicolon −

import sys; x = 'foo'; sys.stdout.write(x + '\n')

## variable assign
Python allows you to assign a single value to several variables simultaneously.

For example −

a = b = c = 1
Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

a, b, c = 1, 2, "john"

## del

## break,continue,pass

## iter,next