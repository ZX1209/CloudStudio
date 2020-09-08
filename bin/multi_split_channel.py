from pathlib import Path
import os
import subprocess
import argparse
import logging as log

log.basicConfig(level=log.DEBUG)

if __name__ == "__main__":
    # setup
    parser = argparse.ArgumentParser()
    parser.add_argument("filepattern")
    args = parser.parse_args()
    filepattern = args.filepattern

    log.debug(filepattern)

    cwd = Path.cwd()
    log.debug(cwd)

    # split channel R
    for img in cwd.glob(filepattern):
        log.debug(img)

        proc = subprocess.run(
            [
                "convert",
                img,
                "-channel",
                "R",
                "-separate",
                cwd / ("separate-" + str(img.name)),
            ]
        )
