# NO-PHONE-ZONE
# 🚗 Driver Monitoring System – No Phone While Driving

A real-time **Driver Monitoring System** that detects mobile phone usage while driving using **YOLOv8 Object Detection**.  
If the driver uses a phone continuously, the system issues a warning sound and then simulates engine shutdown for safety.

---

## 🎯 Project Objective
To prevent road accidents caused by driver distraction due to mobile phone usage by:
- Detecting phone usage in real time
- Issuing an audio warning
- Simulating engine power-off if the driver ignores the warning

---

## 🧠 Techniques Used
1. **YOLOv8 Object Detection** – Detects mobile phone in live video feed  
2. **Time-Based Threshold Logic** – Warning & engine-off decision  
3. **Custom Audio Alert System** – Plays warning sound  

---

## 🛠️ Technologies Used
- Python 3.10+
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- playsound

---

## 📂 Project Files
| File | Description |
|-----|------------|
| `main.py` | Main Python source code |
| `yolov8n.pt` | YOLOv8 pretrained model |
| `warning.mp3` | Custom warning sound |
| `requirements.txt` | Required Python libraries |

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python -m venv dms_env
