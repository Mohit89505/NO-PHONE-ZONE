# NO PHONE ZONE - FINAL WORKING CODE
"""
import cv2
import time
from ultralytics import YOLO
from playsound import playsound

# ==============================
# Load YOLO Model
# ==============================
model = YOLO("yolov8n.pt")

# ==============================
# Initialize Camera
# ==============================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

# ==============================
# Variables
# ==============================
phone_detected_time = None
warning_issued = False
engine_off = False

WARNING_TIME = 3      # seconds
ENGINE_OFF_TIME = 6   # seconds

print("System Started...")

# ==============================
# Main Loop
# ==============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    results = model(frame, conf=0.5)

    phone_detected = False

    # ------------------------------
    # Detection
    # ------------------------------
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "cell phone":
                phone_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "PHONE DETECTED",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 2)

    # ------------------------------
    # Warning & Engine Logic
    # ------------------------------
    if phone_detected:
        if phone_detected_time is None:
            phone_detected_time = time.time()

        elapsed_time = time.time() - phone_detected_time

        # FIRST WARNING
        if elapsed_time >= WARNING_TIME and not warning_issued:
            print("WARNING: Do not use mobile while driving!")
            playsound("warning.mp3")
            warning_issued = True

        # ENGINE OFF (ONLY AFTER WARNING)
        if elapsed_time >= ENGINE_OFF_TIME and warning_issued and not engine_off:
            print("ENGINE OFF (SIMULATION)")
            engine_off = True

            cv2.putText(frame, "ENGINE POWER OFF",
                        (120, 240),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)

            cv2.imshow("Driver Monitoring System", frame)
            cv2.waitKey(3000)   # show message once
            break               # STOP PROGRAM

    else:
        phone_detected_time = None
        warning_issued = False

    # ------------------------------
    # Status Display
    # ------------------------------
    cv2.putText(frame,
                "ENGINE OFF" if engine_off else "DRIVING SAFE",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255) if engine_off else (0, 255, 0),
                2)

    cv2.imshow("Driver Monitoring System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ==============================
# Release Resources
# ==============================
cap.release()
cv2.destroyAllWindows()"""
# ADVANCED DRIVER MONITORING SYSTEM
# Features: Phone + Hand, Gaze, Drowsiness, Speed Control, Multi-Level Alerts
# Driver Monitoring System
# Techniques: 
# 1. Driver Gaze / Attention
# 2. Hand + Phone Interaction
# 3. Drowsiness Detection
# DRIVER MONITORING SYSTEM – NO PHONE ZONE
import cv2
import time
from ultralytics import YOLO
from playsound import playsound

# ==============================
# Load YOLOv8 Model
# ==============================
model = YOLO("yolov8n.pt")

# ==============================
# Initialize Camera
# ==============================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

# ==============================
# Variables
# ==============================
phone_detected_time = None
warning_issued = False
engine_off = False

WARNING_TIME = 3      # seconds
ENGINE_OFF_TIME = 6   # seconds

# ==============================
# Main Loop
# ==============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    results = model(frame, conf=0.5)
    phone_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "cell phone":
                phone_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 0, 255), 2)
                cv2.putText(frame, "PHONE DETECTED",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 2)

    # ==============================
    # Warning & Engine Off Logic
    # ==============================
    if phone_detected:
        if phone_detected_time is None:
            phone_detected_time = time.time()

        elapsed = time.time() - phone_detected_time

        if elapsed > WARNING_TIME and not warning_issued:
            print("WARNING: Do not use phone while driving!")
            playsound("warning.mp3")
            warning_issued = True

        if elapsed > ENGINE_OFF_TIME:
            engine_off = True

    else:
        phone_detected_time = None
        warning_issued = False

    # ==============================
    # Display Status
    # ==============================
    if engine_off:
        cv2.putText(frame, "ENGINE OFF (SIMULATION)",
                    (100, 240),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    else:
        cv2.putText(frame, "DRIVING SAFE",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    cv2.imshow("Driver Monitoring System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ==============================
# Release Resources
# ==============================
cap.release()
cv2.destroyAllWindows()
