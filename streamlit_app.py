def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('boto3')

import streamlit as st
import requests
import os
import io
import boto3
import botocore.auth
import json
import ast

# Function to upload and process PE file
def process_pe_file(file):
    # Prepare request body
    files = {'file': file.getvalue()}

    # Set up SageMaker client
    client = boto3.client('runtime.sagemaker',
                          region_name='us-east-1')

    # Invoke SageMaker endpoint
    response = client.invoke_endpoint(EndpointName='pytorch-inference-2024-03-27-04-29-46-877', Body=file.getvalue())
    response_body = response['Body']
    out = response_body.read()
    astr = out.decode("UTF-8")
    out = ast.literal_eval(astr)
    out = out['outputs']['score']['floatVal']

    if out[0] > 0.5:
        return "Malicious"
    else:
        return "Benign"

def main():
    st.title("Cloud-Based PE Malware Detection API")
    st.write("Upload a PE file to classify it as malware or benign!")

    # File upload
    file = st.file_uploader("Upload PE file", type=["exe"])

    # Check if file is uploaded
    if file:
        st.write("File Uploaded Successfully!")

        # Check if the file is an executable
        if file.type == "application/x-msdownload":
            # Process the file
            result = process_pe_file(file)
            st.write(f"Prediction: {result}")
        else:
            st.write("Please upload an executable file (PE file).")

if __name__ == "__main__":
    main()
