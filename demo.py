#!/usr/bin/python

import cv2 as cv
from utils import yolo, GrabCut
import numpy as np
import streamlit as st

yolopath = "./yolo-fish"
confidence = 0.25
threshold = 0.45

st.title("fish YOLO + GrabCut demo")

uploaded_img = st.file_uploader("Choose an image...", type=['png', 'jpg', 'bmp'])
if uploaded_img is not None:
    file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    image = cv.imdecode(file_bytes, 1)
    st.image(image, caption='Uploaded Image', channels="BGR", use_column_width=True)

boxes, idxs = yolo.runYOLOBoundingBoxes_streamlit(image, yolopath, confidence, threshold)
result_images = GrabCut.runGrabCut(image, boxes, idxs)

st.write("")
st.write("finish grabcut")
for i in range(len(result_images)):
    cv.imwrite(f'grabcut{i}.jpg', result_images[i])
