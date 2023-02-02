---
layout: page
title: Object Detection on MNISTDD-RGB
description: a project where I detect digit objects from a double-digit dataset.
img: assets/img/12.jpg
importance: 1
category: CMPUT 328 - Machine Vision
---
I customized a YOLOv5 model to do object detection on the MNIST Double Digits RGB (MNISTDD-RGB) dataset and achieved a 99% overall accuracy.

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
        {% include figure.html path="assets/img/12.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-3 mt-3 mt-md-0">
        {% include figure.html path="assets/img/13.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    I get the top two most likely digits as part of training.
</div>

