# Early Plant-Disease Detection

Authors: Ayan Naskar and Sounak Mukherjee

## Description

This repository contains the code for our project: "Early plant disease detection using Convolutional Neural Network (CNN)."

The model is trained on various images of plant leaves, both healthy and diseased (with specific disease types). The project aims to assist farmers in predicting plant diseases early and taking necessary measures. The specifications of the computer where the model was trained are listed below.

## Table of Contents

- [System Specifications](#System_Specifications)
- [Getting Started](#Getting_Started)
- [Usage](#Usage)
- [Contact](#Contact)

## System Specifications

- Python Version: 3.10.11
- CPU: Ryzen 5 4600H
- GPU: GeForce GTX 1650 Ti (4GB VRAM)
- RAM: DDR4 16GB dual channel (8+8) @ 3200MHz
- Storage: 512GB M.2 NVME SSD

## Getting Started

1. Importing and setting up variables.
   - Imported libraries: os, tensorflow, matplotlib.pyplot, numpy.
   - Checking GPU availability.

2. Creating and preparing the dataset.
   - Utilized TensorFlow's `image_dataset_from_directory` to create the dataset.
   - Class names: ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
   - Splitting the dataset into training, validation, and test sets.

3. Preprocessing and Augmenting the Data.
   - Cached, shuffled, and prefetched datasets for optimization.
   - Used `Resizing` and `Rescaling` layers for preprocessing.
   - Applied data augmentation for model robustness.

4. Building the CNN Model.
   - Sequential model with Convolutional and Dense layers.
   - Utilized ReLU activation function.
   - Summarized model architecture.

5. Compiling and Training the Model.
   - Compiled the model with Adam optimizer and Sparse Categorical Crossentropy loss.
   - Trained the model using training and validation datasets.
   - Evaluated model accuracy on the test dataset.

6. Evaluating Model Performance.
   - Plotted graphs for training and validation accuracy.
   - Demonstrated predicted vs. actual classes on test images.
   - Displayed the confusion matrix for model evaluation.

7. Saving the Model.
   - Saved the trained model for future use.

8. Flask Application
   - Developed a Flask web application for plant disease classification.
   - Loaded the trained model and defined class names.
   - Utilized functions for classifying images and calculating greenishness.
   - Created routes for uploading images and returning classification results.

9. Web Interface
   - Included an HTML webpage for image classification.
   - Users can drag and drop an image to classify using the model.
   - JavaScript handles image drop and displays the classification result.

## Usage

1. Clone the repository.
2. Download the dataset from Kaggle using the following link: [Plant Village Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village).
3. Extract the downloaded dataset into a folder named `PlantVillage` within the project directory. The folder structure should look like this:


Early-Plant-Disease-Detection/
│
├── saved_models/
│
├── PlantVillage/
│ ├── Potato___Early_blight/
│ ├── Potato___Late_blight/
│ └── Potato___healthy/
│
├── README.md
│
├── app.py
│
├── index.html
│
├── style.css
│
└── script.js

4. Ensure required libraries are installed (`os`, `tensorflow`, `matplotlib.pyplot`, `numpy`, `sklearn`, `seaborn`, `flask`, `PIL`, `cv2`).
5. Run the provided code sections in your preferred Python environment.
6. Open the included HTML webpage (`index.html`) to classify images using the model.
7. Modify paths and configurations as needed for your dataset and setup.


## Contact

For any inquiries or feedback, please reach out to us at [ayannaskar5067@gmail.com](mailto:ayannaskar5067@gmail.com) and [mukherjee.sounak01@gmail.com](mailto:mukherjee.sounak01@gmail.com).
