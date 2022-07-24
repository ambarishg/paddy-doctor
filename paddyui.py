import streamlit as st
from PIL import Image, ImageDraw, ExifTags, ImageColor

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = "YOUR ENDPOINT"
training_key = "YOUR training_key"
prediction_key = "YOUR prediction_key"
prediction_resource_id = "YOUR prediction_resource_id"
project_id = "YOUR project_id"
publish_iteration_name = "YOUR publish_iteration_name"

st.title('Welcome To Paddy Doctor')
instructions = """
        Upload your image. 
        The image you upload will be fed through the Paddy Doctor [ Paddy Disease Detection ] in real-time 
        and the output will be displayed to the screen.
        """
st.write(instructions)

uploaded_file = st.file_uploader('Upload An Image')

if uploaded_file is not None:
    image_binary =  Image.open((uploaded_file)) 
    resized_image = image_binary.resize((336, 336))
    imgWidth, imgHeight = image_binary.size 
    draw = ImageDraw.Draw(image_binary) 
    st.image(resized_image)

     # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
     

    # Now there is a trained endpoint that can be used to make a prediction
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

    results = predictor.classify_image(
            project_id, publish_iteration_name, bytes_data)

        # Display the results.
    for prediction in results.predictions:
            st.write("\t" + prediction.tag_name +
                ": {0:.2f}%".format(prediction.probability * 100))