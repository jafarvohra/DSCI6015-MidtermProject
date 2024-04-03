import streamlit as st
import io
import numpy as np
import torch
import boto3
import json
from ember import PEFeatureExtractor

st.title("PE File Analyzer")

def extract_features(pe_file_path):
    """
    Extract features from a PE file using the EMBER feature extractor.
    """
    extractor = PEFeatureExtractor(2)  # The version parameter can be 1 or 2
    with open(pe_file_path, "rb") as f:
        bytez = f.read()
    features = extractor.feature_vector(bytez)
    return features

def format_features(features):
    """
    Formats the extracted features for the model. Adjust this function based
    on how your model expects the input data.
    """
    # This is a placeholder; adapt the formatting based on your model's needs
    features = np.array(features, dtype=np.float32)
    # Convert to a long tensor as expected by your model
    features_tensor = torch.tensor(features, dtype=torch.long)
    return features_tensor

def submit_to_endpoint(endpoint_name, features):
    """
    Submit the formatted features to the SageMaker endpoint for prediction.
    """
    # Create a BytesIO buffer and save the tensor to this buffer
    buffer = io.BytesIO()
    torch.save(features, buffer)
    buffer.seek(0)  # Move to the start of the buffer

    runtime = boto3.client('sagemaker-runtime',
                          region_name='us-east-1',
                          aws_access_key_id='ASIA6GBMC5NFLIFK2FNV',
                          aws_secret_access_key='fa88WkzZRRow2+IvU6f631ya35lOMQ99kCwcRC3U',
                          aws_session_token='IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIFLAs+VIfIEjUcmD34Q+ForNr5i5nk2NIOfxv6NRqMRrAiBcJG2b5SKVSOBznGNxl870lCQZGClGcFMeL54cnbm3FyqmAgh+EAAaDDk3NTA1MDA0MjE4NiIMFxRAaJcRultpe/CcKoMCQflD0HYGIucEjHCTOnWIjmtK563kvmTjjshyvR6aIFLaPukF2DBqB0IG0riH25beY1AzAYupnkMw85Quqk+DYXoWa17v9gHlmrEFn7oYrHV9gys9z/t6q9mHkAbelzm6Yw4Ij83dasY8l9pP2dElH9DqtTWY713wf0Ts+o67erijpCjTI2qteVVatdMn8OM+gVtvYqpIpVuRgRnooPQVLG5N0GW3lsOazrk7TcpPo5bBeHvu/i6cY0b6Mu6CH3Q01h42xKCoBlmFxSqW8GRaIp1spTaGqcraJ7MspuG+SPYKznYuXn67jkeSkZLqWrMqoAAnVGBSrI9qzi6U4KyLc+t3ETC1hbewBjqeAQoMB0MOFBs9vS9eioEPoziUd0yjzGxINXuP+TeJQVFAS4JXpP+UtUQjR4mV8Ds/ZQqYybN9O8lKiZ4/l5Jh8gNi2xyo6ttH3+gI21pECFRiXmoYXRaW6o2lRpNPlTiQMLhhc5nHWsiy7jafRs7PRGyK6FfcXx8NPjZeYZf+kA5IfFmMDWYnQSvJp1Oymz4g48BgkKvvmPh/xTp+hdAP'
                          )
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/octet-stream",
        Body=buffer.getvalue()  # Use the buffer's content
    )
    # Deserialize the response
    result = json.loads(response['Body'].read().decode())
    return result

uploaded_file = st.file_uploader("Upload a .exe file", type="exe")

if uploaded_file is not None:
    st.write("File uploaded successfully!")

    # Save the uploaded file
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getvalue())

    pe_file_path = uploaded_file.name
    endpoint_name = "pytorch-inference-2024-04-03-21-09-18-296"

    # Extract features from the PE file
    features = extract_features(pe_file_path)
    st.write("Features extracted!")

    # Format the features as required by the model
    formatted_features = format_features(features)
        st.write("Features formatted!")

    # Submit the formatted features to the SageMaker endpoint
    prediction = submit_to_endpoint(endpoint_name, formatted_features)
    st.write("Prediction result:", prediction)

    if prediction['benign'] < 0.5:
        st.write("Classification: Malware")
    else:
        st.write("Classification: Benign")