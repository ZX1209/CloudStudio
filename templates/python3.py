#!/usr/bin/env python3


import logging as log

log.basicConfig(level=log.DEBUG)
log.debug("this is a demo massage")


def main():
    pass


###
##  UTIL
#


def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    main()
