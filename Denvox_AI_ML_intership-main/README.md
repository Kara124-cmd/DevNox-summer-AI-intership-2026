# AI-ML Core — # Weapon Detection Using YOLO

## Project Overview

This project focuses on detecting weapons in images using the YOLO (You Only Look Once) object detection model.

Three publicly available weapon-related datasets were collected and combined into one unified dataset. The datasets were cleaned, their annotations were converted into a common YOLO format, duplicate images were removed, and the final dataset was divided into training, validation, and testing sets.

The final model is designed to detect two main classes:

- **Gun**
- **Knife**

The main goal of this project is to build a practical object detection pipeline that can identify weapons and their locations using bounding boxes.

---

## Project Objectives

The main objectives of this project are:

- Collect multiple weapon detection datasets.
- Convert different annotation formats into YOLO format.
- Standardize weapon classes.
- Remove duplicate images.
- Merge the datasets into one unified dataset.
- Split the dataset into training, validation, and testing sets.
- Train a YOLO object detection model.
- Evaluate the model using object detection metrics.
- Test the trained model on new images or videos.

---

## Dataset Sources

This project uses three datasets.

### 1. Roboflow Weapon Detection Dataset

The first dataset contains different types of weapons such as:

- Handgun
- Knife
- Pistol
- Rifle
- Shotgun

The original dataset contains five classes. These classes were standardized into the two final classes used in this project.

Original classes:

0 = handgun
1 = knife
2 = pistol
3 = rifle
4 = shotgun

## 👨‍💻 Author
Mian Abdul Basit

BS Computer Science

AI-ML Core Mini Project
  
