import cv2 #importing opencv
import os #importing os for file handling
import numpy as np #importing numpy for matrix operations
from Bounding_boxes import boxing, run #importing the functions from Bounding_boxes.py
from Euclidean_dist import euclidean_distance #importing the function from Euclidean_dist.py

video = input("Enter Input Video Path (in mp4 format): ") #input video path
output = input("Enter Output Video Storage Path: ") #output video path
output_path = os.path.abspath(output) #absolute path of the output video

if(video == '0'):
    cap = cv2.VideoCapture(0) #capturing from the webcam
else:
    path = os.path.abspath(video)                #saves path of the video file
    cap = cv2.VideoCapture(path)                 #takes path of the video file

ret = True                                       #creates a boolean 
ret, old_frame = cap.read()                      #ret is true and the first frame of video saved in old_frame

net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3.cfg') #reading the weights and config files
    
classes = [] #list of classes

with open('coco.txt', 'r') as f:
    classes = f.read().splitlines() #reads the classes from the file

frame_width = int(cap.get(3)) #width of the frame
frame_height = int(cap.get(4)) #height of the frame
   
size = (frame_width, frame_height) #size of the frame
rec_vid = cv2.VideoWriter(output_path, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size) #creates a video writer object
if not cap.isOpened():
    raise IOError("Error: unable to process input video or open webcam!") #if the video file is not found error is raised

while ret:
    ret, frame = cap.read()          #saves the first frame of video in frame
    sime = euclidean_distance(frame, old_frame) #calculates the euclidean distance between the two frames
    indexes = [] #stores the indexes of the bounding boxes
    boxes = [] #stores the coordinates and measurements of the bounding boxes
    class_ids = [] #stores the class ids
    confidences = [] #stores the confidence of the classes
    indexes, boxes, class_ids, confidences = run(frame, net, classes) #runs the function run()
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL #font style

    outfile = open("output.txt", "w") #writing the output to a file

    if len(indexes) <= 0:    #if no bounding box
        continue #continue to the next frame
    
    elif len(indexes) > 0:  #if bounding box is presrnt

        frame = boxing(frame, indexes, boxes, class_ids, confidences, classes, font) #boxes are the co-ordinates of the bounding box
        for i in range(len(boxes)): #for each bounding box
            x, y, w, h = boxes[i] #co-ordinates of the bounding box
            label = str(classes[class_ids[i]]) #the name of the object detected
            confidence = str(round(confidences[i], 2)) #the confidence of the object detected
            outfile.write("%s %s %s %s %s %s %s %s\n" % (x, y, w, h, label, confidence, sime, frame_width)) #writing the output to a file
        
    outfile.close() #closing the file

        
    if (sime > 92000): 
         rec_vid.write(frame) #writing the frame to the output video

    cv2.imshow('Processed Output Video:', frame)   #opens the webcam in a pop-up window
    old_frame = frame            #saves the vale of the new frame in old frame to be used later in the loop
    c = cv2.waitKey(1)           #new frame comes after () ms
    if cv2.waitKey(1) & 0xFF == ord('z'): #press z on keyboard to stop the webcam
        break

cap.release() #releases the webcam
cv2.destroyAllWindows() #Once out of the while loop, the pop-up window closes automatically

