# Brain Tumor Detection using CNN

## 📌 Objective
This project implements a Convolutional Neural Network (CNN) to classify brain MRI images into:
- Tumor
- No Tumor

## 🧠 Concepts Used
- Medical Image Classification
- CNN Architecture
- Image Preprocessing
- Model Training and Evaluation

## 🏗️ Model Architecture
- Conv2D (32 filters) + ReLU
- MaxPooling (2×2)
- Conv2D (64 filters) + ReLU
- MaxPooling (2×2)
- Conv2D (128 filters) + ReLU
- MaxPooling (2×2)
- Flatten
- Dense (128 neurons)
- Output Layer (2 neurons, Softmax)

## 📊 Dataset
- Brain MRI images
- Two classes: Tumor / No Tumor
- Image size: 224×224×3

## ⚙️ Implementation
- Implemented using TensorFlow/Keras
- Data preprocessing using ImageDataGenerator
- Includes training and validation split

## 📈 Results
- Model achieves good validation accuracy

## 🚀 Learning Outcomes
- Applying CNNs to medical imaging
- Understanding preprocessing techniques
- Improving model performance

## 📌 Future Improvements
- Add Data Augmentation (rotation, flip, zoom)
- Use Dropout and Batch Normalization
- Apply Transfer Learning (ResNet, MobileNet)