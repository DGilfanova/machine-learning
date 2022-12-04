import cv2
from ObjectTracking.tracker import *

# Создаем объект трекера
tracker = Tracker()

cap = cv2.VideoCapture("content/roadway.mp4")

# читать readme.md
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

# Начинаем покадровое обнаружение
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Обнаружение объектов
    mask = object_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Вычисляем размер контуров и удаляем маленькие объекты
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # Получаем размер и id обнаруженных объектов (detections - обнаруженные контуры в виде прямоугольников)
    boxes_ids = tracker.update(detections)

    for box_id in boxes_ids:
        x, y, w, h, box_id = box_id
        # подписываем id объекта
        cv2.putText(frame, str(box_id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(15)

    # клавиша <Escape> прекращает цикл
    if key == 27:
        break

# Высвобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
