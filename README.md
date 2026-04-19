# 🎨 AirCanvas AI

## 📌 Overview

AirCanvas AI is a real-time virtual drawing application built using computer vision. It allows users to draw in the air using a colored object without physically touching the screen.

---

## 🚀 Features

* Real-time object tracking using OpenCV
* Draw using a colored object (e.g., blue marker/pen)
* Multiple color selection (Blue, Green, Red)
* Eraser mode
* Clear screen functionality
* Interactive UI with on-screen buttons

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy

---

## ▶️ How to Run

### 1. Install dependencies

pip install opencv-python numpy

### 2. Run the project

python main.py

---

## 🎯 How It Works

* The system detects a specific color using HSV color masking
* Tracks object movement using contour detection
* Converts movement into drawing strokes in real time

---

## 💡 Use Cases

* Virtual whiteboards
* Touchless interaction systems
* Educational tools

---

## 📷 Demo

(Add screenshot or GIF here later)

---

## 🧠 Key Concept

This project uses color detection and contour tracking to simulate gesture-based drawing without requiring deep learning or external hardware.
