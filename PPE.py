from ultralytics import YOLO
import cv2
import cvzone
import math

# WebCam
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280) # width
# cap.set(4, 720) # height

# Video
cap = cv2.VideoCapture(r"D:\open-cv\yolo-projects\PPE\videos\ppe1.mp4") # video

model = YOLO(r"D:\open-cv\yolo-projects\PPE\ppe-50.pt") # model file

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']


while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # bound box for cv
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # bound box for cvzone
            # x1, y1, w, h = box.xywh[0]
            w, h = x2-x1, y2-y1
            # bbox = int(x1), int(y1), int(w), int(h)

            # confidence
            confidence = math.ceil((box.conf[0] * 100))/100

            # class name
            className = int(box.cls[0])
            currentClass = classNames[className]

            cvzone.cornerRect(img, (x1, y1, w, h))
            cvzone.putTextRect(img, f"{confidence, currentClass}", (max(0, x1), max(35, y1)), scale=0.8, thickness=1,offset=3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
