# Football Tracking and Analysis System

## 🎯 Introduction
This project aims to track football players, referees, and the ball throughout an entire video using YOLO.  
Key components of this project include:
- **Object Detection**: Improved YOLO-based detection model for players, referees, and the football.
- **Team Identification**: Assigning players to respective teams by detecting and clustering T-shirt colors using K-Means.
- **Ball Possession Analysis**: Measuring team ball possession percentages.
- **Camera Motion Compensation**: Using optical flow to adjust player movement metrics for camera motion.
- **Perspective Transformation**: Estimating real-world movement in meters, not just in pixels, using perspective correction.
- **Speed & Distance Estimation**: Estimating players' speed and total distance covered.

![Screenshot](output_videos/screenshot.png)

---

## 🚀 Improvements in YOLO
- Enhanced detection accuracy for the sports ball.
- Minimized false detection of people outside the football field boundaries.

---

## 📦 Bounding Box Specifications
- `cls`: Class ID  
- `conf`: Detection confidence  
- `xyxy`: Bounding box corner coordinates  
- `xywh`: Bounding box center coordinates and size  

---

## 📁 Dataset Used 
- [football-players-detection](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1) by Roboflow
  - **Train Set**: 92% (612 images)  
  - **Validation Set**: 6% (38 images)  
  - **Test Set**: 2% (13 images)  

  #### Data Augmentations
  - Outputs per training example: 3  
  - Flip: Horizontal  
  - Saturation: ±25%  
  - Brightness: ±20%  

---

## 🤖 YOLO Version Used
- **YOLOv5** was used due to its superior accuracy in ball detection compared to other versions.

---

## 🛡️ Tracking
- Used **ByteTrack** from the `supervision` library to track objects across frames.
- Assigned multiple bounding boxes to each player to maintain continuous tracking.

---

## ✏️ Player and Ball Annotation
- Used OpenCV (`cv2`) to annotate players with an elliptical base using bounding box dimensions.
- Marked the ball with a triangle symbol for differentiation.

---

## 🎨 Player Color Assignment
- Clustered T-shirt colors within each player's bounding box using K-Means clustering.
- Elliptical base annotations are colored according to the player's T-shirt color.

---

## ⚽ Ball Interpolation
- Applied interpolation (using Pandas) in frames where the ball was not detected to ensure continuous tracking.

---

## 🔎 Player-Ball Assignment
- Assigned ball possession to the player whose foot is nearest to the ball's location.
- If the distance between the ball and all players is beyond a threshold, no possession is assigned.

---

## 📊 Team Ball Control Calculation
- Calculated the ball possession percentage by measuring how long the ball was with each team’s players.

---

## 📷 Camera Movement Estimation
- Used optical flow to separate player movements from camera movements:
    - Corner features extracted with **Shi-Tomasi Corner Detection** (`cv2.goodFeaturesToTrack()`).
    - Tracked feature movement between frames using **Lucas-Kanade Optical Flow**.

---

## 🔄 Perspective Transformation
- Transformed the camera’s distorted viewpoint using `cv2.getPerspectiveTransform` and `cv2.PerspectiveTransform`.
- Helps convert pixel-based movements into real-world meters.

---

## 🏃‍♂️ Speed and Distance Estimation
- Calculated player speed and distance every 5 frames (at 24 FPS).
- Annotated speed and distance near the player’s foot bounding box on each frame.

---

## ✅ Conclusion
This project integrates advanced computer vision techniques to track players, referees, and the football, corrects for camera motion, calculates possession statistics, and estimates real-world metrics like player speed and distance covered.

---

## 📚 Technologies Used
- YOLOv5  
- OpenCV  
- PyTorch  
- Pandas  
- Supervision (for ByteTrack)  

---