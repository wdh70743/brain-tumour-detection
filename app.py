import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
import cv2

pre_trained_model_weights = 'models/last.pt'
pre_trained_model = YOLO(pre_trained_model_weights)

st.header("Brain-Tumour Detection Using YOLOv11 Large model")
st.subheader("Implemented by Dohun Won")

st.write("")
st.write("")

MIN_CONF_VALUE=0.0
MAX_CONF_VALUE=1.0
STEP_CONF_VALUE=0.1

ACCEPTED_FILE_FORMAT = ['jpg', 'png', 'jpeg']

IMG_SIZE = 640

with st.sidebar:
    img_buffer = st.file_uploader("Choose a MRI Scans (only images)", type=ACCEPTED_FILE_FORMAT)
    conf_level = st.slider("Confidence Level", MIN_CONF_VALUE, MAX_CONF_VALUE, STEP_CONF_VALUE)
    detect_button = st.button("Detect")


if detect_button and img_buffer is not None:
    image = Image.open(img_buffer)

    col1, col2 = st.columns(2)

    if image is not None:
        results = pre_trained_model.predict(source=image, imgsz=IMG_SIZE, conf=conf_level)

        save_path = 'output/result.jpg'
        results[0].save(filename=save_path)

        result_image = Image.open(save_path)

        with col1:
            st.image(image, caption="Original Image", use_column_width=True)
        with col2:
            st.image(result_image, caption='Detected Image', use_column_width=True)



