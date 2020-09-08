#!/usr/bin/env python3
from pathlib import Path
import os
import argparse
import subprocess

import logging as log

log.basicConfig(level=log.DEBUG)

# file_path = Path(__file__).absolute()
# file_dir_path = file_path.parent
# original_working_path = Path("./").absolute()
# os.chdir(file_dir_path)


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

        imageroot = str(imagesDir) + "/image"

        log.debug(["pdfimages", "-j", filePath, imageroot])

        proc = subprocess.run(["pdfimages", "-j", filePath, imageroot])

    # split channel R
    for img in imagesDir.glob("image*"):
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
    separate_imgs = imagesDir.glob("separate*")

    if not out_file_dir.exists():
        out_file_dir.mkdir()

    proc = subprocess.run(
        ["img2pdf", *separate_imgs, "-o", out_file_dir / out_file_name,]
    )

    # convert image-003.jpg  -channel R -separate separate_red.jpg

