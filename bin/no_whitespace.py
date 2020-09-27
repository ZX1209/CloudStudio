#!/usr/bin/env python3
import os
from pathlib import Path
import argparse
import logging as log


log.basicConfig(level=log.DEBUG)
log.debug('this is a demo massage')


# setup
parser = argparse.ArgumentParser()
parser.add_argument('--rootdir')





if __name__ == "__main__":
    args = parser.parse_args()
    if args.rootdir :
        cwd = Path(args.rootdir)
    else:
        cwd = Path().cwd()


    path = cwd
    filenames = os.listdir(path)
    for filename in filenames:
        log.debug(filename)
        os.rename(filename, filename.replace(' ', '_').lower())