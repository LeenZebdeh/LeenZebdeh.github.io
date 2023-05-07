---
layout: page
title: Semantic Image Segmentation on MNISTDD-RGB
description: A project where I customize U-Net for semantic segmentation on double digit MNIST RGB.
img: assets/img/4.jpg
importance: 1
category: CMPUT 404 - Web Applications and Architecture
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/YOLOv5-UNet-Double-MNIST/tree/main/Image%20Segmentation)

## Summary

I customize U-Net on a MNIST Double Digits RGB (MNISTDD-RGB) for a train-valid-test split dataset which was provided from CMPUT 328.

Dataset consists of:

<ul>
<li>input: numpy array of numpy arrays which each represent pixels in the image, shape: number of samples, 12288 (flattened 64x64x3 images)</li>
<li>output:</li>
<ul>
<li>segementations: numpy array of numpy arrays which each represents the labels in the corresponding image, shape: number of samples, 4096 (flattened 64x64)</li>
</ul></ul>

I customized a U-Net model for image segmentation. I achieve an accuracy of 87%.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/2.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    MNIST Double Digits RGB Dataset Sample.
</div>
<div class="row justify-content-md-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/4.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    I apply semantic segmentation where the background is black and each is colored.
</div>


