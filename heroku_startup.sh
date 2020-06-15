#!/bin/bash

echo PORT $PORT
streamlit run --server.port $PORT app.py
