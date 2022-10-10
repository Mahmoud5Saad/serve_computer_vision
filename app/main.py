from fastapi import FastAPI
from facenet_pytorch import MTCNN
from PIL import Image
import requests
import json
import torchvision
import cv2 as cv
import numpy as np

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is working"}

@app.post("/face_detect")
def face_detect(url):

    img = Image.open(requests.get(url, stream=True).raw)

    mtcnn = MTCNN(keep_all=True)

    boxes, probs, points = mtcnn.detect(img, landmarks=True)

    boxes_list = boxes.tolist()
    box_dims = [[x[2] - x[0], x[3] - x[1]] for x in boxes_list]

    source_height = img.height
    source_width = img.width
    img_size = source_height*source_width

    boxes_list = boxes.tolist()
    return {
                "no_of_boxes": len(boxes_list),
                "boxes": boxes_list,
                "box_dims": box_dims,
                "points": points.tolist(),
                "img_height": source_height,
                "img_width": source_width,
                "img_size": img_size
            }