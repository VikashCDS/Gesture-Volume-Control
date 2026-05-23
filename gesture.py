 # opencv for webcam access and image processing, drawing shapes/text and dsiplaying windows
import cv2        
import mediapipe as mp   # for hand detection and tracking finger points
import math   # used to calaculate the distance 
import numpy as np      # mathematical interpolation and operations,  
## pycaw for controlling system audio volume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# AUDIO SETUP

devices = AudioUtilities.GetSpeakers()  # get the laptop speaker device

interface = devices.EndpointVolume  #give permission to control systems

volume = interface.QueryInterface(IAudioEndpointVolume)   # creating the actual volume controller object

volRange = volume.GetVolumeRange()  #  get the min and max system volume range(db)

minVol = volRange[0]
maxVol = volRange[1]

# MEDIAPIPE HAND SETUP
# mediapipe model already knows palm,fingers,joint and landmarks
mpHands = mp.solutions.hands  # loading the media pipe hand detection module

hands = mpHands.Hands(
    static_image_mode=False,   # use for video tracking mode
    max_num_hands=1,         # used to detect only one hand
    min_detection_confidence=0.7,  # minimum confidence for hand detection
    min_tracking_confidence=0.7   # minimum confidence for hand tracking
)
# used to draw landmarks and hand connections
mpDraw = mp.solutions.drawing_utils

# WEBCAM SETUP

cap = cv2.VideoCapture(0)   # to start the webcam, 0 is the default webcam index

cap.set(3, 640)  # set width of the webcam feed to 640 pixels
cap.set(4, 480)  # set height of the webcam feed to 480 pixels

# MAIN LOOP

while True:   # runs continuoulsy until the user exits

    success, img = cap.read()   # read one frame from webcam

    # checking if webcam frame loaded correctly
    if not success:
        print("Failed to access webcam")
        break

    # Flip image
    img = cv2.flip(img, 1)  # without this, movement feels reversed

    # Convert BGR(opencv) to RGB(mediapipe)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Hand detection
    results = hands.process(imgRGB)  # mediapipe analyzes the image and detects hand landmarks

    lmList = []  # store finger positions 

    # HAND LANDMARK DETECTION

    if results.multi_hand_landmarks:  # check mediapipe find a hand or not 

        for handLms in results.multi_hand_landmarks:  # loop throgh detected hands
            # media pipe gives us 21 landmarks
            for id, lm in enumerate(handLms.landmark):  # loop through each landmark and get its id and position

                h, w, c = img.shape   # get dimensions for height, width and channels
                
                # Mediapipe give coodinates b/w 0 and 1, so we need to convert them to pixel coordinates by multiplying with image dimensions
                cx = int(lm.x * w) # convert normalized landmark x to pixel coordinate by multiplying with image width
                cy = int(lm.y * h) # convert normalized landmark y to pixel coordinate by multiplying with image height

                lmList.append([id, cx, cy])  # store the landmark id and x,y cpordiantes in a list

            # Draw hand landmarks(dots, lines and hand skeleton)
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

    # VOLUME CONTROL USING FINGERS

    if len(lmList) != 0:

        # Thumb Tip
        x1, y1 = lmList[4][1], lmList[4][2]  

        # Index Finger Tip
        x2, y2 = lmList[8][1], lmList[8][2]

        # Draw circles
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)  # draw circles at the thumb tip and index finger tip with pink color to visually indicate the positions of these two fingers on the webcam feed

        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED) # draw circles at the thumb tip and index finger tip with pink color to visually indicate the positions of these two fingers on the webcam feed

        # Draw line
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # draw a line between thumb tip and index finger tip with pink color to visually indicate the connection between the two fingers on the webcam feed

        # Midpoint
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # calculate the midpoint between thumb tip and index finger tip by averaging their x and y coordinates

        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)  # draw a circle at the midpoint with green color to visually indicate the center point between thumb and index finger on the webcam feed

        # DISTANCE CALCULATION

        # calculate the distance between thumb tip and index finger tip using the Euclidean distance formula
        length = math.hypot(x2 - x1, y2 - y1)  

        # CONVERT DISTANCE TO VOLUME

        vol = np.interp(length, [30, 200], [minVol, maxVol])   # interpolate the distance (length) between thumb and index finger to a corresponding volume level (vol) within the system's volume range (minVol to maxVol) using numpy's interp function

        volBar = np.interp(length, [30, 200], [400, 150])  # interpolate the distance (length) to a corresponding y-coordinate for the volume bar (volBar) within the range of 400 to 150 pixels, where 400 represents the minimum volume level and 150 represents the maximum volume level on the visual volume bar displayed on the screen

        volPer = np.interp(length, [30, 200], [0, 100])  # interpolate the distance (length) to a corresponding volume percentage (volPer) within the range of 0% to 100%, which can be displayed as text on the screen to indicate the current volume level in percentage form

        # Set system volume
        volume.SetMasterVolumeLevel(vol, None)  # set the system volume to the calculated volume level (vol) using the pycaw library's SetMasterVolumeLevel method

        # VOLUME BAR
        
        #  draw a rectangle to represent the volume bar background

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)   

        cv2.rectangle(   # draw a filled rectangle to represent the current volume level
            img,
            (50, int(volBar)),  # the top-left corner of the rectangle, where the y-coordinate is determined by the current volume level (volBar)
            (85, 400),  #   the bottom-right corner of the rectangle, fixed at y=400
            (0, 255, 0),  # the color of the rectangle (green)
            cv2.FILLED  #   fill the rectangle with color instead of just drawing the outline
        )

        # Volume Percentage
        cv2.putText(    # draw text on the image
            img,    # the image on which to draw the text
            f'{int(volPer)} %',  # the text to display, showing the current volume percentage
            (40, 450),   # position of the text on the image (x, y)
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),   # font color (green)
            3
        )

        # Distance Display
        cv2.putText(
            img,    # the image on which to draw the text
            f'Distance: {int(length)}',  # the text to display, showing the distance between thumb and index finger
            (250, 50),   # position of the text on the image (x, y)
            cv2.FONT_HERSHEY_COMPLEX,  # font style
            1, # font size
            (255, 255, 255), #  font color (white)
            2  #  thickness of the text
        )

    # PROJECT TITLE

    cv2.putText(
        img,   # the image on which to draw the text
        "Hand Gesture Volume Control",  # the text to display
        (120, 40),   # position of the text on the image (x, y)
        cv2.FONT_HERSHEY_COMPLEX,  # font style
        1,  # font size
        (255, 255, 255),  # font color (white)
        2      # thickness of the text
    )

    # SHOW OUTPUT

    cv2.imshow("Gesture Volume Control", img)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# RELEASE RESOURCES

cap.release()  # release the webcam resource

cv2.destroyAllWindows() # close all OpenCV windows