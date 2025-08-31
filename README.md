![Neural network](https://github.com/user-attachments/assets/14a41c90-9938-489e-9e3d-e37f3557f682)Handwritten Digit Recognizer


This project is a machine learning application that recognizes handwritten digits from 0 to 9. It uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to achieve high accuracy in classifying handwritten numbers.





Project Directory
The project is structured to support both Flask and Streamlit deployments. The core files are:
```
my_project/
├── .gitignore               # Recommended for version control
├── README.md                # This file
├── mnist_model.h5           # The trained model file
├── model_training.py        # Script for data analysis and model training
├── Train (1).csv            # Training dataset
├── test.csv                 # Test dataset
│
├── # FLASK DEPLOYMENT
├── app.py                   # Flask application logic
├── templates/
│   └── index.html           # HTML file for the web UI
└── static/
    └── style.css            # CSS file for styling

├── # STREAMLIT DEPLOYMENT
└── app_streamlit.py         # Streamlit application logic
```


The project demonstrates two distinct deployment methods for machine learning models:

Flask Deployment: A web application with a custom user interface built using HTML and CSS, providing an interactive canvas for drawing digits.

Streamlit Deployment: A simplified, all-in-one Python web application that uses Streamlit's built-in components to create a user-friendly interface with an integrated drawing canvas.

This repository serves as a showcase for building, training, and deploying a deep learning model for real-world use cases.

Outputs

Flask Web Interface
Here is the initial interface of the Flask web app where users can draw a digit.

<img width="1920" height="1080" alt="interface of Flask" src="https://github.com/user-attachments/assets/3840a345-92ea-4765-b2be-052b5e9bb00b" />


This screenshot shows the predicted output after a user draws a digit.

<img width="1920" height="1080" alt="predicted output" src="https://github.com/user-attachments/assets/91f7d000-c096-4423-87a3-93195d8397c4" />

Model Evaluation

This plot shows the training and validation accuracy of the model over several epochs.

<img width="1189" height="490" alt="output" src="https://github.com/user-attachments/assets/a5733be9-9bea-4494-9a4a-b4af920f9030" />

This is the confusion matrix, which visualizes the performance of the classification model.

<img width="838" height="701" alt="confussion matrix" src="https://github.com/user-attachments/assets/306ee69b-e78e-453e-837e-cdc95b879e09" />
