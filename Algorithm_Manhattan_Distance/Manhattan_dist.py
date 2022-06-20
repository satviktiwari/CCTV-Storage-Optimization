import cv2  # importing opencv
import numpy as np  # importing os for file handling


# function to calculate the manhattan distance between two images
def manhattan_distance(image1, image2):
    p1 = np.asarray(image1)  # converts old_frame to an array
    p2 = np.asarray(image2)  # converts frame into an array

    # Convert image to grayscale for better results
    # converts old_frame to grayscale
    # gray_img1_array = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    # converts frame to grayscale
    # gray_img2_array = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Formula for Manhattan distance
    # calculates the manhattan distance between the two images
    manhatt = np.sum(np.abs(p1 - p2))
    return manhatt  # returns the manhattan distance
