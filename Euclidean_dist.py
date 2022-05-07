#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2  # importing opencv 
import numpy as np  # importing os for file handling


# function to calculate the euclidean distance between two images
def euclidean_distance(image1, image2):
    img1_array = np.asarray(image1)  # converts old_frame to an array
    img2_array = np.asarray(image2)  # converts frame into an array

    # Convert image to grayscale for better results
    # converts old_frame to grayscale
    gray_img1_array = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    # converts frame to grayscale
    gray_img2_array = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Formula for Euclidean distance
    #euclidean_distance = (sigma[(x-y)^2])^0.5
    # calculates the euclidean distance between the two images
    eucdis = np.linalg.norm(gray_img1_array - gray_img2_array)
    return eucdis  # returns the euclidean distance
