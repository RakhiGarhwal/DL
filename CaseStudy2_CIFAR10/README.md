# Image Classification using CNN (CIFAR-10)

## 📌 Objective
This project implements a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset into 10 categories.

## 🧠 Concepts Used
- Convolutional Neural Networks (CNN)
- Convolution & Pooling Layers
- Feature Extraction
- Softmax Classification

## 🏗️ Model Architecture
- Conv2D (32 filters) + ReLU
- MaxPooling (2×2)
- Conv2D (64 filters) + ReLU
- MaxPooling (2×2)
- Conv2D (64 filters) + ReLU
- Flatten
- Dense (128 neurons)
- Output Layer (10 neurons, Softmax)

## 📊 Dataset
- CIFAR-10 dataset
- 60,000 images (32×32×3)
- 10 classes (airplane, car, bird, cat, etc.)

## ⚙️ Implementation
- Implemented using TensorFlow/Keras
- Images normalized between 0 and 1

## 📈 Results
- Achieves good classification accuracy on test data

## 🚀 Learning Outcomes
- Understanding CNN architecture
- Feature extraction from images
- Training deep learning models

## 📌 Future Improvements
- Add Dropout and Batch Normalization
- Use Data Augmentation
- Try different optimizers (SGD, RMSprop)
- Apply Transfer Learning (VGG16, ResNet)