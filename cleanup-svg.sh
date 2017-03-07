#!/bin/bash

# Removes cruft Inkscape adds to plain SVG files
sed -e '/<sodipodi:namedview/,/>/d' \
    -e '/sodipodi/d' \
    -e '/inkscape/d' \
    -e 's/id="svg8"$/id="svg8">/' \
    -i wpilib.svg
