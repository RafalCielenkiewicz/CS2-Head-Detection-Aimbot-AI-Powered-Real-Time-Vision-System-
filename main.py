import cv2
import numpy as np
from ultralytics import YOLO
import mss
import ctypes
import keyboard
import time

# Mouse
def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(0x0001, int(dx), int(dy), 0, 0)


AIM_SPEED = 0.9
COOLDOWN = 0.03
locked_target = None


model = YOLO('best.pt')
class_names = model.names

monitor = {
    "top": 300,
    "left": 640,
    "width": 640,
    "height": 480
}
screen_center_x = monitor['width'] // 2
screen_center_y = monitor['height'] // 2

sct = mss.mss()
last_inference_time = 0

while True:

    screenshot = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    results = model(frame, stream=True, imgsz=416, conf=0.25)
    targets = []

    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = class_names[class_id]

            if class_name == 'head':
                head_x = int((x1 + x2) / 2)
                head_y = int((y1 + y2) / 2)
                targets.append((head_x, head_y, confidence))


    if locked_target and locked_target in [(x, y, c) for x, y, c in targets]:
        head_x, head_y, _ = locked_target
    else:
        if targets:
            targets.sort(key=lambda t: (t[0] - screen_center_x) ** 2 + (t[1] - screen_center_y) ** 2)
            locked_target = targets[0]
            head_x, head_y, _ = locked_target
        else:
            locked_target = None
            head_x = head_y = None


    if locked_target and keyboard.is_pressed('q'):
        dx = head_x - screen_center_x
        dy = head_y - screen_center_y

        if abs(dx) > 2 or abs(dy) > 2:
            move_mouse(dx * AIM_SPEED, dy * AIM_SPEED)


    if keyboard.is_pressed('k'):
        break