#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def rasterize(svg, raster_extension, raster_sizes):
    """Rasterizes plain SVGs in various sizes.

    Keyword arguments:
    svg -- name of SVG file to rasterize in the specified output format and sizes
    raster_extension -- file extension of raster image output format
    raster_sizes -- list of heights for raster images
    """
    os.makedirs(os.path.join("export", raster_extension), exist_ok=True)
    for size in raster_sizes:
        out_name = os.path.join(
            "export",
            raster_extension,
            f"{os.path.splitext(os.path.basename(svg))[0]}-{size}.{raster_extension}",
        )

        print(f"Rasterizing {svg} to {out_name}...", end="")
        sys.stdout.flush()

        if raster_extension == "png":
            try:
                subprocess.run(
                    [
                        "inkscape",
                        "--export-type=png",
                        f"--export-filename={out_name}",
                        f"--export-height={size}",
                        svg,
                    ]
                )
            except FileNotFoundError:
                print(
                    "Error: inkscape not found in PATH. Is it installed?",
                    file=sys.stderr,
                )
                sys.exit(1)
        elif raster_extension == "ico":
            try:
                subprocess.run(
                    [
                        "convert",
                        "-transparent",
                        "white",
                        "-density",
                        str(size),
                        svg,
                        "-define",
                        "icon:auto-resize",
                        out_name,
                    ]
                )
            except FileNotFoundError:
                print(
                    "Error: convert utility from ImageMagick not found in PATH. Is it installed?",
                    file=sys.stderr,
                )
                sys.exit(1)
        else:
            print(
                f"Error: unknown raster file extension '{raster_extension}'",
                file=sys.stderr,
            )
            sys.exit(1)

        print(" done.")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Produces plain SVG files from WPILib's Inkscape sources and rasterizes them."
    )
    parser.add_argument(
        "--svgs",
        dest="svgs",
        type=str,
        default="",
        nargs="+",
        help="list of names of SVG files to rasterize in the specified output format and sizes",
    )
    parser.add_argument(
        "--raster-extension",
        dest="raster_extension",
        type=str,
        default="png",
        help='file extension of raster image output format (valid values are "png" and "ico")',
    )
    parser.add_argument(
        "--raster-sizes",
        dest="raster_sizes",
        type=str,
        default="",
        nargs="+",
        help="list of heights for raster images",
    )
    args = parser.parse_args()

    # Exit early if there are no rasters to make
    if len(args.svgs) == 0 or len(args.raster_sizes) == 0:
        return 0

    # Rasterize SVGs
    for svg in args.svgs:
        rasterize(svg, args.raster_extension, args.raster_sizes)


if __name__ == "__main__":
    main()
