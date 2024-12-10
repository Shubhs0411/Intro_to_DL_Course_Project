# Intro_to_DL_Course_Project

# Detection of Surgical Instruments Using Faster RCNN & YOLO: An Enhanced Approach

This repository contains the training code for surgical instrument detection using two state-of-the-art object detection architectures: **Faster R-CNN** and **YOLOv8**. The models are evaluated on the **SOCAL (Simulated Outcomes Following Carotid Artery Laceration)** dataset for detecting 8 classes of surgical instruments.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Dataset](#dataset)


## Introduction

Accurate detection of surgical instruments is critical for improving precision in medical procedures. This repository implements:
- **Faster R-CNN**: Known for high precision but slower inference.
- **YOLOv8**: Designed for real-time detection with competitive accuracy.

## Features

- **Custom Training**: Supports transfer learning with pre-trained weights (e.g., COCO dataset).
- **Flexible Configurations**: Hyperparameter tuning for both Faster R-CNN and YOLOv8.
- **Evaluation Metrics**: Mean Average Precision (mAP), precision, recall, and F1-score.
- **Visualization**: Generates confusion matrix, loss curves, and mAP progression plots.

## Requirements

Install the necessary dependencies before running the code:
- Python 3.8+
- PyTorch 1.9+
- torchvision 0.10+
- albumentations
- OpenCV
- numpy
- matplotlib
- ultralytics (for YOLOv8)

## Dataset
The One Drive Link for the dataset is: https://drive.google.com/drive/folders/10wAWTjpNhfA5CTC7nmA0YjRtE0J638n1?usp=sharing



