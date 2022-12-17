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
    # new_img = cv2.flip(new_img, 0)

    #thresholded image bw
    new_img_thresh = np.where((new_img <= upper_thresh) & (new_img >= lower_thresh),1,0)

    #finding out which pixel indices are of interest
    pixels_of_interest = np.where((gray_img <= upper_thresh) & (gray_img >= lower_thresh))
    num_els = np.Inf #number of elements in each row of data

    #reducing number of pixels to make trajectory smoother
    #need to add functionality to discard pixels that are too close
    while num_els >300:

        #randomly remove every second element from array
        
        num_els = np.shape(pixels_of_interest)
        num_els = num_els[1]
        idel = np.arange(0, num_els, 2)

        pixel_array_z = pixels_of_interest[0]
        pixel_array_z = np.delete(pixel_array_z, idel)

        pixel_array_y = pixels_of_interest[1]
        pixel_array_y = np.delete(pixel_array_y, idel)

        pixels_of_interest = np.array([pixel_array_z, pixel_array_y])

    #take a transpose so coords are easier to visualize
    pixels_of_interest = np.transpose(pixels_of_interest)


    #we also want to make sure to remove pixels that are too close to each other. 
    #Keep a buffer of ~20 pixels

    dud_pixels = np.argwhere(np.diff(pixel_array_y) <= 3)
    pixel_array_y = np.delete(pixel_array_y, dud_pixels+1)
    pixel_array_z = np.delete(pixel_array_z, dud_pixels+1)

    pixels_of_interest = np.transpose(np.array([pixel_array_z, pixel_array_y]))

    #create a blank image
    reduced_img = np.where((new_img <= upper_thresh),0,0)

    #populate blank image with reduced pixels
    for i in pixels_of_interest:   
        reduced_img.itemset((i[0], i[1]), 50)
    reduced_img = cv2.flip(reduced_img, 0)

    
    ##finding and sorting pixels of interest and then scaling them
    #finding out which pixel indices are of interest
    img_pixels = np.where((reduced_img <= upper_thresh) & (reduced_img > lower_thresh))
    img_pixels = np.transpose(img_pixels)

    #sort the array by y axis to make sure we're moving as we want
    ind = np.lexsort((img_pixels[:,0], img_pixels[:,1]))
    img_pixels = img_pixels[ind]

    # #scaling those into ROS 2D coords
    # img_pixels = np.transpose(np.array([np.multiply(np.add(img_pixels[:,0],2), 0.0011), np.multiply(np.add(img_pixels[:,1], 2), 0.0005)]))
    # print((img_pixels))

    show_image(reduced_img, title='reduced_22', grayscale=True) #debugging to see what the reduced image looks like

    return img_pixels

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
    return thresh


if __name__ == '__main__':

    # """
    # implementing 22 reading
    # """

    # # adjust the file names here
    # test_img1 = read_image(IMG_DIR + '/22_pt1.jpg', grayscale=True)
    # test_img2 = read_image(IMG_DIR + '/22_pt2.jpg', grayscale=True)

    # # uncomment the test you want to run
    # # it will plot the image and also save it

    # img_pixels1 = test_thresh_naive(test_img1, 0, 70)

    # img_pixels2 = test_thresh_naive(test_img2, 0, 70)
    # img_pixels2 = np.flip(img_pixels2, 0)

    # # print(np.shape(img_pixels2))
    # # print(np.shape(img_pixels1))

    # img_pixels = np.vstack((img_pixels1, img_pixels2))
    # #scaling those into ROS 2D coords
    # img_pixels = np.transpose(np.array([np.multiply(np.add(img_pixels[:,0],2), 0.0011), np.multiply(np.add(img_pixels[:,1], 2), 0.0005)]))
    # # print((img_pixels))
    # # print((img_pixels))
    # # img_pixels = img_pixels1

    # #save pixels of interest as csv file DONT FORGET TO UNCOMMENT FINALLY
    # pd.DataFrame(img_pixels).to_csv(IMG_DIR + "/22wp1_coords.csv", header=None, index=None)

    """
    implementing 44 reading
    """

    # adjust the file names here
    test_img1 = read_image(IMG_DIR + '/44_pt1.jpg', grayscale=True)
    test_img2 = read_image(IMG_DIR + '/44_pt2.jpg', grayscale=True)
    test_img3 = read_image(IMG_DIR + '/44_pt3.jpg', grayscale=True)

    # uncomment the test you want to run
    # it will plot the image and also save it

    img_pixels1 = test_thresh_naive(test_img1, 0, 70)
    img_pixels2 = test_thresh_naive(test_img2, 0, 70)
    img_pixels2 = np.flip(img_pixels2, 0)
    img_pixels3 = test_thresh_naive(test_img3, 0, 70)

    # print(np.shape(img_pixels2))
    # print(np.shape(img_pixels1))

    img_pixels = np.vstack((img_pixels1, img_pixels2, img_pixels3))
    print(np.shape(img_pixels))
    # img_pixels = img_pixels1

    #scaling those into ROS 2D coords
    img_pixels = np.transpose(np.array([np.multiply(np.add(img_pixels[:,0],1), 0.0011), np.multiply(np.add(img_pixels[:,1], 8), 0.0005)]))
    # print((img_pixels))

    #save pixels of interest as csv file DONT FORGET TO UNCOMMENT FINALLY
    pd.DataFrame(img_pixels).to_csv(IMG_DIR + "/44wp1_coords.csv", header=None, index=None)

    print(img_pixels)