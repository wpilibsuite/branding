#!/usr/bin/env python3

import os
import subprocess
import sys


def main():
    svgs = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".svg")]

    # Export plain SVGs
    os.makedirs(os.path.join("export", "svg"), exist_ok=True)
    for svg in svgs:
        print(f"Exporting {svg} to plain SVG export/svg/{svg}...", end="")
        sys.stdout.flush()

        subprocess.run(
            [
                "inkscape",
                "--export-type=svg",
                f"--export-filename=export/svg/{svg}",
                "--export-text-to-path",
                svg,
            ]
        )

        print(" done.")

    # PNG rasterizations
    subprocess.run(
        [
            "./rasterize.py",
            "--svgs",
            "export/svg/wpilib-icon.svg",
            "--raster-extension",
            "png",
            "--raster-sizes",
            "16",
            "32",
            "64",
            "128",
            "256",
            "512",
            "1024",
        ]
    )

    # ICO rasterizations
    subprocess.run(
        [
            "./rasterize.py",
            "--svgs",
            "export/svg/wpilib-icon.svg",
            "--raster-extension",
            "ico",
            "--raster-sizes",
            "256",
        ]
    )


if __name__ == "__main__":
    main()
