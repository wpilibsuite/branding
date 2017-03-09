#!/bin/bash

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable.svg
# Also add ">" after svg tag's width attribute

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i wpilib.svg

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable-horizontal.svg
# Also add ">" after svg tag's width attribute

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i wpilib-horizontal.svg

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable-vertical.svg
# Also add ">" after svg tag's width attribute

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i wpilib-vertical.svg
