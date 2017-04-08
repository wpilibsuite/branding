#!/bin/bash

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable.svg
echo "wpilib-edittable.svg: also add '>' after svg tag's width attribute"

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i svg/wpilib.svg

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable-horiz-indiv.svg \
       wpilib-edittable-horiz-team.svg
echo "wpilib-edittable-horiz.svg: also add '>' after svg tag's width attribute"

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i svg/wpilib-horiz-indiv.svg \
       svg/wpilib-horiz-team.svg

sed -e '/sodipodi:docname/d' \
    -e '/inkscape:export/d' \
    -e '/inkscape:version/d' \
    -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -e '/<sodipodi:namedview/,/>/d' \
    -i wpilib-edittable-vert-indiv.svg \
       wpilib-edittable-vert-team.svg
echo "wpilib-edittable-vert.svg: also add '>' after svg tag's width attribute"

sed -e '/<metadata/,/<\/metadata>/d' \
    -e '/<defs/,/>/d' \
    -i svg/wpilib-vert-indiv.svg \
       svg/wpilib-vert-team.svg
