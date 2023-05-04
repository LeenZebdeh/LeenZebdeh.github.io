---
layout: page
title: Object Detection on MNISTDD-RGB
description: a project where I detect digit objects from a double-digit dataset.

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/YOLOv5-UNet-Double-MNIST/tree/main/Object%20Detection)
img: assets/img/2.jpg
importance: 1
category: CMPUT 328 - Machine Vision
---

## Summary

I customize YOLOv5 on MNIST Double Digits RGB (MNISTDD-RGB) for a train-valid-test split dataset which was provided from CMPUT 328.

Dataset consists of:

<ul>
<li>input: numpy array of numpy arrays which each represent pixels in the image, shape: number of samples, 12288 (flattened 64x64x3 images)<li>
<li>output:</li>
<ul>
<li>classes: numpy array of numpy arrays which each represents the classes in the corresponding image, shape: number of samples, 2</li>
<li>prediction boxes: numpy array of numpy arrays which each represents the bounding boxes in the corresponding image, format: [y_min, x_min, y_max, x_max], shape: number of samples, 2, 4</li>
</ul>
</ul>

I use YOLOv5 for object detection. I achieve a classification score of 98.786% and a IOU score of 63.371%, resulting in an overall score of 81.078%.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/2.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    MNIST Double Digits RGB Dataset Sample.
</div>
<div class="row justify-content-md-center">
    <div class="col-3 mt-3 mt-md-0">
        {% include figure.html path="assets/img/13.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    I get the top two most likely digits as part of training.
</div>

## References

Pytorch. PyTorch. (n.d.). Retrieved May 2, 2023, from https://pytorch.org/hub/ultralytics_yolov5/<br>

Kathuria, A. (2023, April 10). How to train Yolo V5 on a custom dataset. Paperspace Blog. Retrieved May 2, 2023, from https://blog.paperspace.com/train-yolov5-custom-data/<br>

Solawetz, J. (2020, September 29). How to train a custom object detection model with Yolo V5. Medium. Retrieved May 2, 2023, from https://towardsdatascience.com/how-to-train-a-custom-object-detection-model-with-yolo-v5-917e9ce13208<br>

I used CMPUT 328's code templates from: <br>
Assignment 7: Object Detection/predict.py from A7_submission and Object detection/predict.py from A7_main
