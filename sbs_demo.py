#!/bin/python
from PIL import Image, ImageDraw, ImageFont

# Generates 3D side by side(SBS) picture for VR/AR glasses.

img_size = (1920 * 2, 1080)
font_size = 25
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

def draw_background(draw):
        step = 50
        x = 0
        while x < img_size[0] / 2:
                y = 0
                while y < img_size[1]:
                        draw.point((x, y))
                        draw.point((x + img_size[0] / 2, y))
                        y += step
                x += step

def draw_text(draw, x_scale, right_off):
        draw_background(draw)

        rows = img_size[1] / font_size + 2
        i = 0
        while i < rows:
                x = img_size[0] / 2 * i / rows * x_scale
                y = img_size[1] * i / rows
                str = "%d/%d" % (x, y)
                draw.text((x, y), str, font = font) # left, move right
                draw.text((img_size[0] / 2 + right_off, y), str, font = font) # right, vertical
                i = i + 1

        str = "x axis scale: %f, right x axis offset: %d" % (x_scale, right_off)
        draw.text((0, 0), str, font = title_font)
        draw.text((img_size[0] / 2, 0), str, font = title_font)

def draw_scales(right_off):
        i = 0
        while i <= 0.25:
                img = Image.new("RGBA", img_size, "#000000") # black
                draw = ImageDraw.Draw(img)
                draw_text(draw, i, right_off)
                file_name = "outputs/sbs-demo-%f-right-%d.png" % (i, right_off)
                print(file_name)
                img.save(file_name)
                i += 0.05

def draw_right_offsets():
        off = 0
        while off <= 150: # from 0 to half screen
                draw_scales(off)
                off += 50

draw_right_offsets()
