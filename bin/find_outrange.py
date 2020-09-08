from pathlib import Path
import os
import subprocess
import argparse
import logging as log

log.basicConfig(level=log.DEBUG)

if __name__ == "__main__":
    # setup
    parser = argparse.ArgumentParser()
    parser.add_argument("min")
    parser.add_argument("max")
    args = parser.parse_args()
    mina = args.min
    maxa = args.max

    log.debug(mina, maxa)

    cwd = Path.cwd()
    log.debug(cwd)

    # split channel R
    proc = subprocess.run(["find", "-size",])
