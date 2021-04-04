#!/usr/bin/env python3
from pathlib import Path
import os
import argparse
import subprocess

import logging as log

log.basicConfig(level=log.DEBUG)

"""
convert_images.py {{/path/to/file}}

"""

if __name__ == "__main__":
    # input
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()

    # variables
    cwd = Path.cwd()
    filename = str(args.file)
    filePath = cwd / args.file
    imagesDir = cwd / (filename + "-images")
    out_file_dir = cwd / "nowatermarks"
    out_file_name = "nowatermark-" + str(filename)

    # extrac images
    if filePath.exists():
        if not imagesDir.exists():
            imagesDir.mkdir()

        imageroot = str(imagesDir) + "/image-"

        log.debug(["pdfimages", "-j", filePath, imageroot])

        proc = subprocess.run(["pdfimages", "-j", filePath, imageroot])

    # split channel R
    for img in imagesDir.glob("image-*"):
        log.debug(img)
        log.debug(
            [
                "convert",
                img,
                "-channel",
                "R",
                "-separate",
                imagesDir / ("separate-" + str(img.name)),
            ]
        )
        proc = subprocess.run(
            [
                "convert",
                img,
                "-channel",
                "R",
                "-separate",
                imagesDir / ("separate-" + str(img.name)),
            ]
        )

    # join (he cheng)
    # use subprocess.run shell=True
    # separate_imgs = imagesDir.glob("separate*")

    if not out_file_dir.exists():
        out_file_dir.mkdir()

    log.debug(" ".join(["img2pdf", str(imagesDir)+"/separate*", "-o", str(out_file_dir / out_file_name),]))
    proc = subprocess.run(
        " ".join(["img2pdf", str(imagesDir)+"/separate*", "-o", str(out_file_dir / out_file_name),]),shell=True,stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE
    )

