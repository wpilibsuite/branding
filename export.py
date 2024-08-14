#!/usr/bin/env python3

import os
import re
import subprocess
import sys


def main():
    svg = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".svg")]

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
        subprocess.run(
            [
                "inkscape",
                "--export-type=svg",
                "--export-filename=" + plain_svg[i],
                "--export-text-to-path",
                svg[i],
            ]
        )
        print(" done.")

    # Compile regexes
    rgxes = [
        re.compile(r'^\s+sodipodi:docname="((.|\n)*?")\n', re.M),
        re.compile(r"^\s+<metadata\s+((.|\n)*?</metadata>)\n", re.M),
        re.compile(r"^\s+<defs\s+((.|\n)*?/>)\n", re.M),
        re.compile(r"^\s+<sodipodi:namedview\s+((.|\n)*?/>)\n", re.M),
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

    # Rasterize SVGs
    args = ["./rasterize.py", "--svgs", "svg/wpilib.svg", "--raster-extension"]
    subprocess.run(args + ["png", "--raster-sizes", "16", "128"])
    subprocess.run(args + ["ico", "--raster-sizes", "256"])


if __name__ == "__main__":
    main()
