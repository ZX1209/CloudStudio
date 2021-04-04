#!/usr/bin/env python3
import fileinput

# exit with code 1 for nothing to update
# 0 for something to update
for line in fileinput.input():
    #print(line)
    if line=='Already up-to-date.\n':
        raise SystemExit(1)
