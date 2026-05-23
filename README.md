# ✋ Hand Gesture Volume Control System

A real-time AI-based Hand Gesture Volume Control System built using Python, OpenCV, MediaPipe, and Pycaw.

The system detects hand gestures through a webcam and controls the system volume dynamically based on finger distance and gestures.

---

# 🎥 Demo Video

https://github.com/user-attachments/assets/e3f6baf6-6a5d-4f12-8542-c9834213da5a

---

# 📌 Features

✅ Real-time Hand Detection  
✅ Dynamic Volume Control  
✅ Finger Distance Tracking  
✅ Volume Percentage Display  
✅ Hand Landmark Detection  
✅ Live Webcam Processing  
✅ Smooth Gesture Interaction  

---

# 🧠 Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- NumPy
- Pycaw
- Computer Vision
- Hand Tracking

---

# 🖼️ Project Preview

## Hand Detection

- Detects thumb and index finger
- Draws landmarks and connections
- Calculates finger distance

## Volume Control

- Fingers close → Low volume
- Fingers far → High volume

---

# 📂 Project Structure

```bash
Gesture-Volume-Control/
│
├── gesture.py
├── requirements.txt
├── README.md
└── demo-video.mp4
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/gesture-volume-control.git
```

---

## 2️⃣ Open Project Folder

```bash
cd gesture-volume-control
```

---

## 3️⃣ Create Virtual Environment

```bash
py -3.11 -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

OR

```bash
pip install opencv-python mediapipe==0.10.9 pycaw numpy comtypes
```

---

# ▶️ Run Project

```bash
python gesture.py
```

---

# ✋ How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Thumb tip and index finger tip are tracked
4. Distance between fingers is calculated
5. Distance is mapped to system volume
6. System volume changes dynamically

---

# 📐 Mathematical Formula

## Distance Formula

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

---

# 🖐️ Hand Landmarks

| Landmark ID | Finger |
|---|---|
| 4 | Thumb Tip |
| 8 | Index Finger Tip |
| 12 | Middle Finger Tip |
| 16 | Ring Finger Tip |
| 20 | Pinky Tip |

---

# 🧩 Libraries Used

## OpenCV

Used for:
- Webcam access
- Drawing shapes
- Image processing
- Displaying output

## MediaPipe

Used for:
- Hand detection
- Hand tracking
- Landmark extraction

## Pycaw

Used for:
- System audio control
- Volume adjustment

---

# 💻 Requirements

- Python 3.11
- Webcam
- Windows OS

---

# 🚀 Future Improvements

- ✋ Mute Gesture
- 👍 Thumbs Up/Down Control
- 👆 Finger Counting
- 🖱️ Virtual Mouse
- 💡 Brightness Control
- 🤖 AI Gesture Recognition
- 🎵 Spotify Integration

---

# 📸 Output Screen

The system displays:

- Hand landmarks
- Finger tracking
- Distance measurement
- Volume percentage
- Volume control bar

---

# 🎯 Applications

- Touchless systems
- Smart home control
- Accessibility tools
- AI gesture systems
- Human computer interaction

---

# 👨‍💻 Author

Vikash Kumar Singh

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.
