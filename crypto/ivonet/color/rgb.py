#!/usr/bin/env python
#  -*- coding: utf-8 -*-


def hsb2rgb(hsb):
    """
        Transforms a hsb array to the corresponding rgb tuple
        In: hsb = array of three ints (h between 0 and 360, s and v between 0 and 100)
        Out: rgb = array of three ints (between 0 and 255)
        """
    hsb_h = float(hsb[0] / 360.0)
    hsb_s = float(hsb[1] / 100.0)
    hsb_b = float(hsb[2] / 100.0)

    if hsb_s == 0:
        rgb_r = int(round(hsb_b * 255))
        rgb_g = int(round(hsb_b * 255))
        rgb_b = int(round(hsb_b * 255))
    else:
        var_h = hsb_h * 6
        if var_h == 6:
            var_h = 0  # H must be < 1
        var_i = int(var_h)
        var_1 = hsb_b * (1 - hsb_s)
        var_2 = hsb_b * (1 - hsb_s * (var_h - var_i))
        var_3 = hsb_b * (1 - hsb_s * (1 - (var_h - var_i)))

        if var_i == 0:
            var_r = hsb_b
            var_g = var_3
            var_b = var_1
        elif var_i == 1:
            var_r = var_2
            var_g = hsb_b
            var_b = var_1
        elif var_i == 2:
            var_r = var_1
            var_g = hsb_b
            var_b = var_3
        elif var_i == 3:
            var_r = var_1
            var_g = var_2
            var_b = hsb_b
        elif var_i == 4:
            var_r = var_3
            var_g = var_1
            var_b = hsb_b
        else:
            var_r = hsb_b
            var_g = var_1
            var_b = var_2

        rgb_r = int(round(var_r * 255))
        rgb_g = int(round(var_g * 255))
        rgb_b = int(round(var_b * 255))

    return [rgb_r, rgb_g, rgb_b]


def color2hex(h, s, b):
    """Transform a hsb color into a hex string representing that color."""
    (r, g, b) = hsb2rgb([h, s, b])
    color = '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)
    return color
