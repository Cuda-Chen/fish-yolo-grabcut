#!/usr/bin/python

import cv2 as cv
from utils import yolo, GrabCut
import numpy as np
import streamlit as st
from PIL import Image

st.title("fish YOLO + GrabCut demo")

uploaded_img = st.file_uploader("Choose an image...", type=['png', 'jpg', 'bmp'])
if uploaded_img is not None:
    file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    opencv_image = cv.imdecode(file_bytes, 1)
    st.image(opencv_image, caption='Uploaded Image', channels="BGR", use_column_width=True)
