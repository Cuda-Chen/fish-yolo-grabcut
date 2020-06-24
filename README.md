# Fish YOLO GrabCut
YOLOv3 object detection then use GrabCut to do semantic segmentation to fish market images.

# Demo on Heroku
I have deployed this project on Heroku. You can try here: https://fish-yolo-grabcut.herokuapp.com/

# Set up and Run Demo Locally
First, create a virtual environment and install the dependencies (assume you are using `conda`):
```
$ conda create -n fish-yolo-grabcut python=3.6 pip 
$ conda activate fish-yolo-grabcut
$ pip install -r requirements.txt
```

Then, use `gdown` to download the pretrained weights from [here](https://drive.google.com/file/d/1L6JgzbFhC7Bb_5w_V-stAkPSgMplvsmq/view?usp=sharing) and put it to `yolo-fish` directory:
```
$ gdown --output ./yolo-fish/fish.weights --id 1L6JgzbFhC7Bb_5w_V-stAkPSgMplvsmq
```

Next, choose one of the following approaches you like.

## 1. Command Line Approach
```
$ python main.py --image ./images/DSC_0061.JPG --yolo yolo-fish
```

When finishing, you should find 8 jpg images in the project root directory.

## 2. Streamlit Approach
```
$ streamlit run app.py
```

You can upload fish market image to run the program.

The results are shown in the browser (make sure to scroll down).

## 3. Docker Approach
```
$ docker image build -t fish-yolo-grabcut:app .
$ docker container run -p 8501:8501 --rm -d grabcut:app
```

Then upload fish market image to run the program.

The results are shown in the browser (make sure to scroll down).

To shutdown the docker type this:
```
$ docker kill <weird id of fish-yolo-grabcut.app>
```
