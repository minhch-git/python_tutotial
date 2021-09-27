"""
Author: chiu cam minh
Date: 12/09/2021
Program: assignment_07_exercise_02.py
Problem:
    Darkening an image requires adjusting its pixels toward black as a limit, 
    whereas lightening an image requires adjusting them toward white as a limit.
    Because black is RGB (0, 0, 0) and white is RGB (255, 255, 255),
    adjusting the three RGB values of each pixel by the same amount in either direction will have the desired effect.
    Of course, the algorithms must avoid exceeding either limit during the adjustments.

    Lightening and darkening are actually special cases of a process known as color filtering.
    A color filter is any RGB triple applied to an entire image.
    The filtering algorithm adjusts each pixel by the amounts specified in the triple.
    For example, you can increase the amount of red in an image
    by applying a color filter with a positive red value and green and blue values of 0.
    The filter (20, 0, 0) would make an image’s overall color slightly redder.
    Alternatively, you can reduce the amount of red by applying a color filter with a negative red value.
    Once again, the algo- rithms must avoid exceeding the limits on the RGB values.

    Develop three algorithms for lightening, darkening,
    and color filtering as three related Python functions, lighten, darken, and colorFilter.
    The first two functions should expect an image and a positive integer as arguments.
    The third function should expect an image and a tuple of integers (the RGB values) as arguments.
    The following session shows how these functions can be used with
    the images image1, image2, and image3, which are initially transparent:

    >>> image1 = Image(100, 50) >>> image2 = Image(100, 50) >>> image3 = Image(100, 50) >>> darken(image1, 128)
    >>> darken(image2, 64)
    >>> colorFilter(image3, (255, 0, 0))
    # Converts to gray
    # Converts to dark gray
    # Converts to red
    Note that the function colorFilter should do most of the work.

Solution:
"""
from images import Image


def colorFilter(image, colorAmount):
    def baseValue(value, offset):
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    (r, g, b) = colorAmount
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            (red, green, blue) = (
                baseValue(red, r),
                baseValue(green, g),
                baseValue(blue, b),
            )
            image.setPixel(x, y, (red, green, blue))


def lighten(image, amount):
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    colorFilter(image, (-amount, -amount, -amount))


def convertToGray(image):
    colorFilter(image, (129, 129, 129))


# def grayscale(image):
#     """Converts the argument image to grayscale."""
#     for y in range(image.getHeight()):
#         for x in range(image.getWidth()):
#             (r, g, b) = image.getPixel(x, y)
#             # r = int(r * 0.299)
#             # g = int(g * 0.587)
#             # b = int(b * 0.114)
#             lum = (r + g + b) // 3
#             image.setPixel(x, y, (lum, lum, lum))


def convertToDarkGray(image):
    colorFilter(image, (78, 0, 78))


def convertToRed(image):
    colorFilter(image, (88, 0, 0))


def main(filename="smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()

    # lightening, darkening,
    darken(image, 120)
    # lighten(image, 128)

    # Converts to gray
    # convertToGray(image)
    colorFilter(image, (129, 100, 129))

    # Converts to dark gray
    # convertToDarkGray(image)
    # colorFilter(image, (78, 78, 78))

    # Converts to red
    # convertToRed(image)
    # colorFilter(image, (88, 0, 0))

    print("Close the image window to quit. ")
    image.draw()


if __name__ == "__main__":
    main()
