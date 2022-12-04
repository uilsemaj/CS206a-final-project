#!/usr/bin/env python
"""
This file will accept an image input and convert that to ROS coordinates/waypoints
for the Sawyer to follow for each time signature movement
"""

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd 

this_file = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = '/'.join(this_file.split('/')[:-2]) + '/img_processing/src'
print(IMG_DIR)

def read_image(img_name, grayscale=False):
    """ reads an image

    Parameters
    ----------
    img_name : str
        name of image
    grayscale : boolean
        true if image is in grayscale, false o/w
    
    Returns
    -------
    ndarray
        an array representing the image read (w/ extension)
    """

    if not grayscale:
        img = cv2.imread(img_name)
    else:
        img = cv2.imread(img_name, 0)

    print(img_name)

    return img

def write_image(img, img_name):
    """writes the image as a file
    
    Parameters
    ----------
    img : ndarray
        an array representing an image
    img_name : str
        name of file to write as (make sure to put extension)
    """

    cv2.imwrite(img_name, img)

def show_image(img_name, title='Fig', grayscale=False):
    """show the  as a matplotlib figure
    
    Parameters
    ----------
    img_name : str
        name of image
    tile : str
        title to give the figure shown
    grayscale : boolean
        true if image is in grayscale, false o/w
    """

    if not grayscale:
        plt.imshow(img_name)
        plt.title(title)
        plt.show()
    else:
        plt.imshow(img_name, cmap='gray')
        plt.title(title)
        plt.show()


def threshold_segment_naive(gray_img, lower_thresh, upper_thresh):
    """perform grayscale thresholding using a lower and upper threshold by
    blacking the background and whitening lying between the threholds (the
    foreground)

    Parameter
    ---------
    gray_img : ndarray
        grayscale image array
    lower_thresh : float or int
        lowerbound to threshold (an intensity value between 0-255)
    upper_thresh : float or int
        upperbound to threshold (an intensity value between 0-255)

    Returns
    -------
    ndarray
        thresholded version of gray_img
    """
    # TODO: Implement threshold segmentation by setting pixels of gray_img inside the 
    # lower_thresh and upper_thresh parameters to 1
    # Then set any value that is outside the range to be 0 
    # Hints: make a copy of gray_img so that we don't alter the original image
    # Boolean array indexing, or masking will come in handy. 
    # See https://docs.scipy.org/doc/numpy-1.13.0/user/basics.indexing.html

    new_img = np.copy(gray_img)
    print(np.shape(new_img))

    #thresholded image bw
    new_img_thresh = np.where((new_img <= upper_thresh) & (new_img >= lower_thresh),1,0)

    #finding out which pixel indices are of interest
    img_pixels = np.where((gray_img <= upper_thresh) & (gray_img >= lower_thresh))
    pixels_of_interest = np.copy(img_pixels)

    #scaling those into ROS 2D coords
    img_pixels = np.array([np.multiply(img_pixels[0], 0.0017), np.multiply(np.add(img_pixels[1], 8), 0.00014)])

    num_els = np.Inf #number of elements in each row of data

    #reducing number of pixels to make trajectory smoother
    while num_els >1000:
        
        num_els = np.shape(img_pixels)
        num_els = num_els[1]
        idel = np.arange(0, num_els, 2)
        print(num_els)

        point_array_z = img_pixels[0]
        point_array_z = np.delete(point_array_z, idel)

        pixel_array_z = pixels_of_interest[0]
        pixel_array_z = np.delete(pixel_array_z, idel)

        point_array_y = img_pixels[1]
        point_array_y = np.delete(point_array_y, idel)

        pixel_array_y = pixels_of_interest[1]
        pixel_array_y = np.delete(pixel_array_y, idel)

        img_pixels = np.array([point_array_z, point_array_y])

        pixels_of_interest = np.array([pixel_array_z, pixel_array_y])

    print(np.shape(pixels_of_interest))
    pixels_of_interest = np.transpose(pixels_of_interest)


    #save pixels of interest as csv file DONT FORGET TO UNCOMMENT FINALLY
    pd.DataFrame(img_pixels).to_csv(IMG_DIR + "/22wp1_coords.csv", header=None, index=None)

    reduced_img = np.where((new_img <= upper_thresh),0,0)

    for i in pixels_of_interest:
        print(i[0], i[1])
        reduced_img.itemset((i[0], i[1]), 1)

    show_image(reduced_img, title='reduced_22', grayscale=True) #debugging to see what the reduced image looks like

    return new_img_thresh

    # raise NotImplementedError()


def to_grayscale(rgb_img):
    return np.dot(rgb_img[... , :3] , [0.299 , 0.587, 0.114])

def segment_image(img): 
    # ONLY USE ONE SEGMENTATION METHOD

    # perform thresholding segmentation
    binary = threshold_segment_naive(to_grayscale(img), 0, 70).astype(np.uint8)

    # perform clustering segmentation.
    # binary = cluster_segment(img, 2).astype(np.uint8)

    # if np.mean(binary) > 0.5:
    #     binary = 1 - binary #invert the pixels if K-Means assigned 1's to background, and 0's to foreground

    return binary


"""
below are tests used for sanity checking you image, edit as you see appropriate

"""

def test_thresh_naive(img, lower_thresh, upper_thresh):
    thresh = threshold_segment_naive(img, lower_thresh, upper_thresh)
    show_image(thresh, title='thresh_naive_22', grayscale=True)
    cv2.imwrite(IMG_DIR + "/thresh_naive_22.jpg", thresh.astype('uint8') * 255)


if __name__ == '__main__':
    # adjust the file names here
    test_img = read_image(IMG_DIR + '/22_pt1.jpg', grayscale=True)

    # uncomment the test you want to run
    # it will plot the image and also save it

    test_thresh_naive(test_img, 0, 70)