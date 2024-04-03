# DSCI6015-MidtermProject

## Cloud-based-PE-Malware-Detection-API
## Midterm Project for the AI &amp; Cybersecurity Course - University of New Haven - Spring 2024

**Introduction:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The purpose of this project is to deploy machine learning models for malware classification. This project is comprised of three tasks. The initial task is to train a deep neural network to classify PE files as malware or benign using the Ember opensource dataset, EMBER-2017 v2. EMBER stands for Endgame Malware Benchmark for Research which is a large dataset composed of labeled and unlabeled samples of parsed features of PE header files from binaries. More details about the dataset are available at https://github.com/endgameinc/ember.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The second and third tasks deal with deploying the model to the cloud and creating an endpoint (~API) to the model. As a final task, create a client nothing but a Python script that loads a PE file and classifies it as malicious or benign. The created client uses 'calc.exe' as the sample. One can use any PE file, with no restrictions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The detailed instructions to work on this project are in the Project Instructions file.

[**Task 1: Model Building:**]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this task the data is initially extracted and vectorized. Then a deep neural network architecture is designed in PyTorch. The model is trained, validated, and tested on the extracted data. Hyperparameters are tweaked to obtain better model performance. The model and its weights are saved. Lastly, a method is created that takes a PE (.exe) file and gives the nature of it i.e., Benign or Malicious.

[**Task 2: Model Deployment to Cloud:**]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The cloud service used in this task is AWS Sagemaker. The saved model is uploaded and the model is loaded to deploy it to Sagemaker. This created an endpoint.

[**Task 3: Client Creation:**]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This task comprises of creating local client that takes PE file, converts it into a feature vector compatible with the model, runs the vector on the cloud API, and then prints the results (i.e., Malware or Benign – or probabilities of each). A streamlit app was attempted for this part, but the resources were limited.

[**Project Report:**] 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The project report has a detailed description of the working and execution of the project along with the explanation of the code. 

**Project Presentation:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The presentation video of this project is available @ TBD
