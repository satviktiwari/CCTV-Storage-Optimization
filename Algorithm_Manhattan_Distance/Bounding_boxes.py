import cv2  # importing opencv
import numpy as np  # importing os for file handling


def run(frame, net, classes):  # function to run the YOLOv3 algorithm

    height, width, _ = frame.shape  # height and width of the frame captured

    # creates a blob from the frame
    blob = cv2.dnn.blobFromImage(
        frame, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)  # sets the input blob for the network

    # gets the names of the output layers
    output_layers_names = net.getUnconnectedOutLayersNames()
    # runs the forward pass to get the output of the output layers
    layerOutputs = net.forward(output_layers_names)

    boxes = []  # stores the coordinates and measurements for the bounding box
    confidences = []  # Stores the confidence, i.e how much the object atches with a given class
    class_ids = []  # stores all the labels

    for output in layerOutputs:  # get ouput layers information
        # extract information from each output (detection contains 85 parameters)
        for detection in output:

            # prediction from all the classes, 6th element onwards
            scores = detection[5:]

            # extract location of the class with maximum confidence(index)
            class_id = np.argmax(scores)
            confidence = scores[class_id]  # extract the vaue of the confidence
            if confidence > 0.5:
                # these are normalised co-ordinates that is why we multiply them with heigth and width to
                # scale them back
                # the center x co-ordinate of the bounding box
                center_x = int(detection[0]*width)
                # the center y co-ordinate of the bounding box
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)  # width of the bounding box
                h = int(detection[3]*height)  # height of the bounding box

                x = int(center_x - w/2)  # corner x co-ordinate
                y = int(center_y - h/2)  # corner y co-ordinate 

                # saves the co-ordinates and measurement in boxes[] and confidences[]
                boxes.append([x, y, w, h])
                # saves the confidences of the classes in confidences[]
                confidences.append((float(confidence)))
                class_ids.append(class_id)  # index of the classes detected in the frame

    # performs non-Max Supression on the classes with confidence greater then the threshold value
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.2)

    # returns the indexes, boxes, class_ids, confidences and classes
    return indexes, boxes, class_ids, confidences


# function to draw the bounding boxes on the frame
def boxing(frame, indexes, boxes, class_ids, confidences, classes, font):
    for i in indexes.flatten():  # for each detected object in the frame
        # co-ordinates if bounding boxes of final object after NMS is applied
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])  # the name of the object detected in the frame
        # saves the confidence rounding it to 2 decimals and appends it to the label
        confidence = str(round(confidences[i], 2))
        # bounda a rectangle around the object detected
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # shows the confidence and object name at top left corner of the bounding box
        cv2.putText(frame, label + " " + confidence,
                    (x, y+20), font, 2, (255, 255, 255), 4)

    return frame  # returns the frame with bounding boxes drawn on it