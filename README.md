# Fish YOLO GrabCut
YOLOv3 object detection then use GrabCut to do semantic segmentation to fish market images.

# Set up and Run Demo
First, download the pretrained weights from [here](https://drive.google.com/file/d/1L6JgzbFhC7Bb_5w_V-stAkPSgMplvsmq/view?usp=sharing) and put it to `yolo-fish`
directory.

Then type the following commands (assuming you are using `conda`):
```
$ conda create -n fish-yolo-grabcut python=3.6 pip 
$ conda activate fish-yolo-grabcut
$ pip install -r requirements.txt
$ python main.py --image ./images/DSC_0061.JPG --yolo yolo-fish
