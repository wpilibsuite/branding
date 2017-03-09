![logo](https://rawgithub.com/wpilibsuite/branding/master/wpilib-horizontal.svg)

# WPILib Branding Standards

This repository contains WPILib's branding standards and guidelines.

## Color Palette

<table>
  <tr>
    <th>Red</th>
    <th>Dark Gray</th>
    <th>Light Gray</th>
  </tr>
  <tr>
    <td style="background-color: #ac2b37; color: white;">#AC2B37</td>
    <td style="background-color: #262626; color: white;">#262626</td>
    <td style="background-color: #a9b0b7; color: white;">#A9B0B7</td>
  </tr>
</table>

## Font

Our logo uses [DejaVu Sans](DejaVuSans.ttf), so we recommend using this font on other branding material for consistency.

## Logo Documentation

The following information is provided for maintenance of the logo.

### Gear

Inkscape provides a gear path renderer. The following settings were used.

* Number of teeth: 30
* Circular pitch (tooth size): 62.0
* Pressure angle (degrees): 22.5
* Diameter of center hole: 0.0
* Units: px

This path is centered within the image.

### Hexagon

The hexagon is sized to fit around the path the gear renderer generated. This path is centered within the image.

### Lettering

The lettering uses DejaVu Sans with the bold attribute. The character used in the logo was converted to a path and is sized to fit within the gear path. This path is positioned such that the centroid of the "W"'s bounding trapezoid is centered within the image.

The centroid measured from the longer base can be computed via `y = h / 3 * (2 * a + b) / (a + b)` where `a` is the length of the shorter base, `b` is the length of the longer base, and `h` is the height. For the current "W", `a = 278`, `b = 416`, and `h = 290`. The vertical offset needed to place the centroid of the "W" at the image center is given by `offset = y - h / 2`. That gives an offset of -9.6109, which is rounded down to -10.
