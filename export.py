#!/usr/bin/env python3

import os
import re
import subprocess
import sys


def main():
    # Tuple is (SVG file name, list of raster image heights)
    png_rasters = [("svg/wpilib.svg", [16, 128])]

    svg = [
        f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".svg")
    ]

    # Generate plain SVG
    print("Generating plain SVGs from Inkscape SVGs...")
    try:
        os.mkdir("svg/")
    except Exception:
        pass
    plain_svg = ["svg/" + re.sub("-edittable", "", f) for f in svg]
    for i in range(len(svg)):
        print(plain_svg[i] + "...", end="")
        sys.stdout.flush()
        subprocess.run([
            "inkscape", "-z", "--file=" + svg[i],
            "--export-plain-svg=" + plain_svg[i], "--export-text-to-path"
        ])
        print(" done.")

    # Compile regexes
    rgxes = [
        re.compile("^\s+sodipodi:docname=\"((.|\n)*?\")\n", re.M),
        re.compile("^\s+inkscape:export=\"((.|\n)*?\")\n", re.M),
        re.compile("^\s+inkscape:version=\"((.|\n)*?\")\n", re.M),
        re.compile("^\s+<metadata\s+((.|\n)*?</metadata>)\n", re.M),
        re.compile("^\s+<defs\s+((.|\n)*?/>)\n", re.M),
        re.compile("^\s+<sodipodi:namedview\s+((.|\n)*?/>)\n", re.M)
    ]

    # Remove excess metadata from Inkscape and plain SVGs
    print("Removing excess metadata...")
    lines = ""
    for name in svg + plain_svg:
        print(name + "...", end="")
        with open(name, "r") as file:
            lines = file.read()
        output = lines
        for rgx in rgxes:
            output = rgx.sub("", output)
        if lines != output:
            with open(name, "wb") as file:
                file.write(output.encode())
        print(" done.")

    # Rasterize plain SVGs in various sizes
    try:
        os.mkdir("png/")
    except Exception:
        pass
    for raster in png_rasters:
        for size in raster[1]:
            out_name = "png/" + os.path.splitext(os.path.basename(
                raster[0]))[0] + "-" + str(size) + ".png"
            print("Rasterizing " + raster[0] + " to " + out_name + "...")
            sys.stdout.flush()
            subprocess.run([
                "inkscape", "-z", "--file=" + raster[0],
                "--export-png=" + out_name, "--export-height=" + str(size)
            ])


if __name__ == "__main__":
    main()
