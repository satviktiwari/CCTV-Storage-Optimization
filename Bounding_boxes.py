import cv2 ##importing opencv
import numpy as np #importing os for file handling

def run(frame, net, classes): #function to run the YOLOv3 algorithm
        
    height, width, _ = frame.shape   #height and width of the frame captured
        
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), (0, 0, 0), swapRB = True, crop = False) #creates a blob from the frame
    net.setInput(blob) #sets the input blob for the network
    
    output_layers_names = net.getUnconnectedOutLayersNames() #gets the names of the output layers
    layerOutputs = net.forward(output_layers_names) #runs the forward pass to get the output of the output layers
    
    boxes = []       #stores the coordinates and measurements for the bounding box
    confidences = [] #Stores the confidence, i.e how much the object atches with a given class
    class_ids = []   #stores all the labels

    for output in layerOutputs:   #get ouput layers information
        for detection in output:  #extract information from each output (detection contains 85 parameters)
            
            scores = detection[5:] #prediction from all the classes, 6th element onwards
            
            class_id = np.argmax(scores) #extract location of the class with maximum confidence(index)
            confidence = scores[class_id] #extract the vaue of the confidence
            if confidence > 0.5:
                #these are normalised co-ordinates that is why we multiply them with heigth and width to
                #scale them back
                center_x = int(detection[0]*width) #the center x co-ordinate of the bounding box
                center_y = int(detection[1]*height) #the center y co-ordinate of the bounding box
                w = int(detection[2]*width)         #width of the bounding box
                h = int(detection[3]*height)        #height of the bounding box

                x = int(center_x - w/2)             #corner x co-ordinate
                y = int(center_y - h/2)             #corner y co-ordinate

                boxes.append([x, y, w, h])          #saves the co-ordinates and measurement in boxes[]
                confidences.append((float(confidence))) #saves the confidences of the classes
                class_ids.append(class_id)              #index of the classes detected
    
    #performs non-Max Supression on the classes with confidence greater then the threshold
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.2) 


    return indexes, boxes, class_ids, confidences #returns the indexes, boxes, class_ids, confidences

def boxing(frame, indexes, boxes, class_ids, confidences, classes, font): #function to draw the bounding boxes
    for i in indexes.flatten(): #for each detected object
            x, y, w, h =  boxes[i] #co-ordinates if bounding boxes of final object after NMS
            label = str(classes[class_ids[i]]) #the name of the object detected
            confidence = str(round(confidences[i], 2)) #saves the confidence rounding it to 2 decimals
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) #bounda a rectangle around the object
            #shows the confidence and object name at top left
            cv2.putText(frame, label + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 4)

    return frame #returns the frame with bounding boxes drawn

