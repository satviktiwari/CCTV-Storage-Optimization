import cv2  # importing opencv for image processing
import os  # importing os for file handling
from matplotlib.pyplot import box  # importing os for file handling
import numpy as np  # importing numpy for matrix operations
# importing the functions from Bounding_boxes.py for bounding boxes and YOLOv3
from Bounding_boxes import boxing, run
# importing the function from Euclidean_dist.py for euclidean distance
from Euclidean_dist import euclidean_distance
import datetime  # importing datetime for time stamping
import pandas as pd  # importing pandas for dataframe
import moviepy.editor as moviepy  # importing moviepy for video editing and saving

# input video path in mp4 format
video = input("Enter Input Video Path (in .mp4 format): ")
# output video path for storing the processed video
output = input("Enter Output Video Storage Path (in .avi format): ")
output_path = os.path.abspath(output)  # absolute path of the output video path

if(video == '0'):  # if the input video path is 0, then the program will exit
    cap = cv2.VideoCapture(0)  # capturing from the webcam
else:  # if the input video path is not 0, then the program will continue
    # saves path of the video file in a variable path
    path = os.path.abspath(video)
    # takes path of the video file and opens it in a variable cap
    cap = cv2.VideoCapture(path)

ret = True  # creates a boolean variable ret
# ret is true and the first frame of video saved in old_frame variable
ret, old_frame = cap.read()

# reading the weights and config files for YOLOv3
net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3.cfg')

classes = []  # list of classes for the YOLOv3 model

with open('coco.txt', 'r') as f:  # opening the file coco.txt for reading the classes of the YOLOv3 model
    # reads the classes from the file and stores them in the list classes
    classes = f.read().splitlines()

frame_width = int(cap.get(3))  # width of the frame in pixels
frame_height = int(cap.get(4))  # height of the frame in pixels

size = (frame_width, frame_height)  # size of the frame in pixels
# creates a video writer object for the output video with the codec MJPG, frame rate 10 and size of the frame in pixels
rec_vid = cv2.VideoWriter(
    output_path, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

if not cap.isOpened():  # if the video file is not opened, then the program will exit
    # if the video file is not found error is raised
    raise IOError("Error: unable to process input video or open webcam!")

while ret:  # while ret is true, the program will continue
    # saves the first frame of video in frame variable and ret is true
    ret, frame = cap.read()
    # calculates the euclidean distance between the two frames and stores it in sime variable
    sime = euclidean_distance(frame, old_frame)
    indexes = []  # stores the indexes of the bounding boxes of the objects in the frame
    boxes = []  # stores the coordinates and measurements of the bounding boxes of the objects in the frame
    class_ids = []  # stores the class ids of the objects in the frame
    confidences = []  # stores the confidence of the classes of the objects in the frame
    # runs the function run() from Bounding_boxes.py for bounding boxes and YOLOv3
    indexes, boxes, class_ids, confidences = run(frame, net, classes)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # font style for the text on the frame

    if len(indexes) <= 0:  # if no bounding box is detected, then the program will continue
        continue  # continue to the next frame

    elif len(indexes) > 0:  # if bounding box is present in the frame, then the program will continue

        # boxes are the co-ordinates of the bounding box and class_ids are the class ids of the objects in the frame
        frame = boxing(frame, indexes, boxes, class_ids,
                       confidences, classes, font)

    if (sime > 92000):  # if the euclidean distance is greater than 92000 then the program will continue
        rec_vid.write(frame)  # writing the frame to the output video file

    # # writing the output to a file called output.txt
    # outfile = open("output.txt", "w")
    # # writing the header to the file
    # outfile.write("x | y | w | h | class_id | confidence | class_name\n")
    # outfile.write("\n")  # new line
    # for i in range(len(boxes)):  # for each bounding box in the frame
    #     x, y, w, h = boxes[i]  # co-ordinates of the bounding box
    #     # the name of the object detected in the frame
    #     label = str(classes[class_ids[i]])
    #     # the confidence of the object detected in the frame
    #     confidence = str(round(confidences[i], 2))
    #     # writing the output to a file called output.txt
    #     outfile.writelines("%s %s %s %s %s %s %s\n" %
    #                        (x, y, w, h, label, confidence, sime))
    #     outfile.write("\n")  # new line
    #     continue  # continue to the next frame
    # outfile.close()  # closing the file

    # with open('stats.csv', 'a') as f:
    #     # writing the output to a file called stats.csv
    #     np.savetxt(f, np.row_stack(np.column_stack((label, confidence, sime, str(
    #         datetime.datetime.now())))), delimiter=",", fmt='%s')
    #     f.write("\n")  # new line

    # # opening the file logfiles.txt for appending the output of the program
    # with open('logfiles.txt', 'a') as the_file:
    #     stringto = "Object '"+label+"' was detected in camera with confidence level '"+confidence+"' having euclidean distance '" + \
    #         str(sime)+"' at time "+str(datetime.datetime.now()) + \
    #         "\n"  # string to be written to the file
    #     the_file.write(str(stringto))  # writing the string to the file

    # opens the webcam in a pop-up window
    cv2.imshow('Processed Output Video:', frame)
    # saves the vale of the new frame in old frame to be used later in the loop
    old_frame = frame
    c = cv2.waitKey(1)  # new frame comes after 1 millisecond
    if cv2.waitKey(1) & 0xFF == ord('z'):  # press z on keyboard to stop the webcam
        break  # break the loop

# df = pd.read_csv("stats.csv")  # reading the weather data from the csv file
# # writing the weather data to the excel file
# df.to_excel("stats.xlsx", sheet_name="Testing", index=False)

# reading the video file in avi format
clip = moviepy.VideoFileClip("test_video_output.avi")
# converting the video file into mp4 format
clip.write_videofile("test_video_output_temp.mp4")

open("logfiles.txt", "w").close()  # closing the file logfiles.txt

cap.release()  # releases the webcam
# Once out of the while loop, the pop-up window closes automatically
cv2.destroyAllWindows()

# input video path=> C:\Users\satvi\OneDrive\Desktop\CCTV-Data-Processing\test_video_1.mp4
# output video path=> C:\Users\satvi\OneDrive\Desktop\CCTV-Data-Processing\test_video_output.avi

# Output: Storage reduced from 12 MB to 2 MB !!!
# Frame data successfully written in csv file and text file frame-wise
# Overall frame data successfully stored in logfile
# Output video successfully written in avi format
# Output video successfully converted in mp4 format
