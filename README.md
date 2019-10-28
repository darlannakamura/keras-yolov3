# keras-yolo3

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)


This is a copy from https://github.com/allanzelener/YAD2K.

## Introduction

A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).


---

## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to a Keras model.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```

3. Install dependencies

`pip install -r requirements.txt`

4. Put the directory with images in `datasets`.

5. Run YOLO to generate JSONs, and specify the directory path as bellow

`python generate_json.py --dir_path datasets/test2017`


