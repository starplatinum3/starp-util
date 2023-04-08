import cv2
 
# url = "rtsp://**********************"
url = "rtsp://localhost/demo"
cap = cv2.VideoCapture(url)
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# python3  opencv_rtsp_read.py