# Handwritten Digit Recognition using MLP (From Scratch)

## 📌 Objective
This project implements a Multi-Layer Perceptron (MLP) from scratch using NumPy to classify handwritten digits (0–9) from the MNIST dataset.

## 🧠 Concepts Used
- Forward Propagation
- Backpropagation
- Gradient Descent
- Activation Functions (ReLU, Softmax)
- Cross-Entropy Loss

## 🏗️ Model Architecture
- Input Layer: 784 neurons (28×28 image flattened)
- Hidden Layer 1: 128 neurons (ReLU)
- Hidden Layer 2: 64 neurons (ReLU)
- Output Layer: 10 neurons (Softmax)

## 📊 Dataset
- MNIST dataset (handwritten digits)
- Images are normalized between 0 and 1

## ⚙️ Implementation
- Built completely using NumPy (no deep learning libraries)
- Manual implementation of forward and backward propagation

## 📈 Results
- Achieves good accuracy on test data (~85–90%)

## 🚀 Learning Outcomes
- Understanding neural networks from scratch
- Learning how backpropagation works
- Implementing gradient descent optimization

## 📌 Future Improvements
- Add mini-batch gradient descent
- Try different activation functions (Sigmoid, Tanh)
- Implement regularization techniques