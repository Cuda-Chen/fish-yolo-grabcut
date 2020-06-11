FROM ubuntu:18.04
MAINTAINER Cuda Chen <clh960524@gmail.com>

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'
# install Python and Pip
RUN apt-get update && \
    apt-get install -y \
    python3.7 python3-pip

# expose port 8501 for streamlit
EXPOSE 8501

# make app directiry
WORKDIR /streamlit-docker

# copy requirements.txt
COPY requirements.txt ./requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy all files over
COPY . .

# download YOLO weights
RUN gdown --output ./yolo-fish/fish.weights --id 1L6JgzbFhC7Bb_5w_V-stAkPSgMplvsmq 

# launch streamlit app
CMD streamlit run app.py 
