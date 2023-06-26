"""
File: stanCodoshop.py
Name: Monica Peng
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
from typing import Any

import os
import sys
from simpleimage import SimpleImage
import statistics


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**(1/2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    list_r = []
    list_g = []
    list_b = []

    sum_r = 0
    sum_g = 0
    sum_b = 0

    bin_size = 10  # Define the bin size for the RGB value
    threshold = 5

    # The following section calculates both mode and average for all the pixels
    # If there are more than (threshold) pixels in the list, take mode, otherwise take average
    for pixel in pixels:
        list_r.append(pixel.red//bin_size)
        list_g.append(pixel.green//bin_size)
        list_b.append(pixel.blue//bin_size)

        sum_r += pixel.red
        sum_g += pixel.green
        sum_b += pixel.blue

    if len(pixels) >= threshold:
        mode_r = statistics.mode(list_r) * bin_size
        mode_g = statistics.mode(list_g) * bin_size
        mode_b = statistics.mode(list_b) * bin_size
        return [mode_r, mode_g, mode_r]
    else:
        return [sum_r//len(pixels), sum_g//len(pixels), sum_b//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    pixel_dic = {}
    avg_pixel = get_average(pixels)  # Return avg pixel in list [red, green, blue]
    for pixel in pixels:
        pixel_dic[pixel] = get_pixel_dist(pixel, avg_pixel[0], avg_pixel[1], avg_pixel[2])
    # Sort the dictionary using the color distance and ask the function to return the first pixel (min color distance)
    for sorted_pixel, color_d in sorted(pixel_dic.items(), key=lambda t: t[1]):
        return sorted_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for i in range(width):
        for j in range(height):
            new_pixel = result.get_pixel(i, j)

            # Loop over all the images to get the best pixels, reset pixel list before each iteration
            pixels = []
            for image in images:
                pixels.append(image.get_pixel(i, j))
            best_pixel = get_best_pixel(pixels)

            # Make the new pixel equal the best pixel
            new_pixel.red = best_pixel.red
            new_pixel.green = best_pixel.green
            new_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
