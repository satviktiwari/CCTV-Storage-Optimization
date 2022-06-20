import cv2  # importing opencv
import numpy as np  # importing os for file handling


# function to calculate the normal distance between two images
def normal_distance(image1, image2):
    p1 = np.squeeze(np.asarray(image1))  # converts old_frame to an array
    p2 = np.squeeze(np.asarray(image2))  # converts frame into an array

    # # Convert image to grayscale for better results
    # # converts old_frame to grayscale
    # gray_img1_array = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    # # converts frame to grayscale
    # gray_img2_array = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Formula for normal distance
    # calculates the normal distance between the two images
    normal = np.dot(p1, p2, out=None)
    return normal  # returns the normal distance
