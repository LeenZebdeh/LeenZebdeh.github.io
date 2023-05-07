---
layout: page
title: Autonomous Driving in Duckietown 🦆🦆🦆🦆🦆🦆
importance: 1
description: I implement autonomous driving, obstacle avoidence and parking in Duckietown.
category: CMPUT 412 - Robotics 🦆
---

[Link to the GitHub repo](https://github.com/Leen-Alzebdeh/duckietown/tree/main/final_project)

<b> Contributors </b> <br>
Leen Alzebdeh, Tural Bakhtiyarli and Tianming Han


## Objective

<p> In this project, we have three separate tasks for the robot to complete in one go. To solve these tasks we would like to implement AprilTag detection, obstacle avoidance and object detection. The robot will follow the lane and handle intersections in stage 1, avoid a broken robot in the middle of the road in stage 2 and park inside one of the four parking slots specified in advance in stage 3. </p>

## Methods and Results

Here is a video of our best run recorded by Tural on my robot, completing all three stages of the project:

<div class = "row justify-content-md-center">
    <video width="320" height="240" controls>
    <source src="../../assets/vid/412_final_project/part1.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
<div class="caption">
    Video 1. Completing All Three Tasks
In this run, the duckiebot drives autonomously and completes the three tasks in the project. We can see it successfully follows its lane on stage 1, detects and waits for ducks in the crosswalks as well as avoids the broken robots in stage 2 and parks autonomously inside the target stall (specified as 4 before the program starts running) in the stage 3. 
</div>

#### Stage 1: AprilTag Detection and Lane Following

<p> For this stage, we need to go into a circular driveway and come out at the other side of the road. The AprilTag at the entry intersection will indicate whether we turn straight or turn right into the circular driveway, and the two cases are placed randomly for each run. <br>

We start with the reference solution for lane following on the previous exercises. We write a state machine to record the current progress of the robot in the task i.e. which intersection it is expecting to see. In the first stage, we only have red stop lines where the AprilTag at the right tells us which way we should turn. By detecting the id of the AprilTag before entering the intersection, we know if we should turn straight/right, and then the state machine will advance its state. After the first turn the rest of the path the robot should take is known, so we no longer look for AprilTag, but rely on the known map. (This avoids the possibility of AprilTag detection node missing one of the later AprilTags). <br>

A challenge we faced in this part is that the robot sometimes starts the lane following package before its AprilTag detection package. As this may lead to the robot not recognizing the first AprilTag, we rearrange the order of packages in the launch file and add a sleep statement after AprilTag detection node but before the lane following node. <br>

However, we overlook another issue at the end, which is that with the same parameters, the lane following package would work differently on each of our robots. This is because in development we only work on our own robot on the part assigned to each of us. As a result, the lane following in part one only works well on Tianming's robot, sometimes fails on Leen's robot. And on Tural's robot the lane following fails more catastrophically: the driving speed seems to be quite slow compared to when running on the other robots and the robot is not able to make a good turn at the first intersection. </p>

#### Stage 2: Obstacle Avoidance

<p>Now in the second stage, our robot will need to cross two crosswalks and go around a broken duckiebot. In one of the two crosswalks, there may be a few ducks in the middle of the road passing, and we want to avoid it hitting the ducks in the case they are on the crosswalk. <br>

The crosswalks are marked by blue stop lines, and an AprilTag at the right side. Initially we were considering using color contours to extract the blue stop lines, but we discover that the blue stop line is similar in color to the broken duckiebot that we need to recognize, and on top of that, the stop line appears to have some specular reflection on its surface making it not fit for color masking. Instead we let the robot stop when it sees the AprilTag at the side of the crosswalk, which seems to work well. <br>

For the ducks and the broken duckiebot, we decide to use object detection to recognize them (since ML is fun). This avoids the potential problem of mixing up color between yellow midline & yellow ducks or blue stop line & blue broken duckiebot. The model we use comes from Facebook research named detectron2. We fine-tune it using our own collected dataset, and the bounding box of the detected object is used to determine the distance between our robot and the ducks/broken robot. <br>

<b>Dataset collection:</b> We recorded two rosbags of the duckiebot approaching the ducks and broken duckiebot at different angles. Each bag lasts a few minutes, one is used for training and the other is used for testing. The training dataset is manually labelled by using cv2.selectROI on the frames of the input video that contains ducks/duckiebots. We go through the video twice, once to label ducks and another to label the duckiebot. Frames that contain none of those are discarded. This part is relatively easy to do but it requires some cv2 and Numpy programming. <br>

<b>Model training:</b> The training steps we take closely follows the example fine-tuning script provided by Facebook research on detectron2 examples. We add a few lines to mount the google drive and install the bagpy package so the google colab script is able to read our rosbags. The example training script uses a model that outputs a segmentation mask as well as a bounding box. With some research we believe it can be trained only on bounding boxes, and we try to simply take the entire bounding box as the segmentation mask and train the model, which seems to work. On the test bag, we use cv2_imshow to view the results on Google Colab. We see that the fine-tuned model is able to reliably detect the duckiebot and most of the ducks, though sometimes recognizing chairs at the side as a duckiebot. <br>

<b>Running the model:</b> Due to the difficulty of running PyTorch (which detectron2 depends on) on the robot, we run it on our Ubuntu laptop with -R option enabled. However, there are still a few obstacles that we did not expect. To run detectron2 on the GPU of our laptop, the docker needs to have GPU enabled. Since we use an unfamiliar platform and the command dts devel to run the program, we are not sure if we can follow the standard docker tutorials online to enable the GPU, so we decide to run the program on CPU instead. <br>

We also discovered that for some reason the GPU version of PyTorch can not be installed without a physical GPU, and the CPU version of PyTorch can not be installed in the docker without likely building from source because the Python version of the ROS docker is incompatible with the pre-built source on PyTorch website, so in the end we had to run our model on CPU in a laptop with a GPU. <br>

With the model set up inside the docker, we receive images from camera_node and publish the detected objects' bounding boxes to another topic in json format (with Python's json module). In the lane following package, we receive the bounding boxes on that topic, and compare the lower edge of the bounding box to obtain the distance between our robot and the detected object. <br>

We program our robot to temporarily switch to English driver mode to go around the broken robot. The result is tested on Leen's robot, which seems to work fine after a bit of parameter tuning E.g. slowing down the robot to allow for more detection time. We also discovered that the detection rate seems to go up significantly when the laptop is plugged into the wall, as the CPU runs faster as it gets a sufficient power supply. The image detection processing rate ends up at around one to two images per second.</p>

#### Stage 3: The Parking Lot

In this stage, we are tasked to park the robot in the desired parking slot. There were 4 parking slots: 1 and 2 on the left side of the entrance to the parking slot, and 3 and 4 on the right. We separated this problem into 2 main parts:

<ol>
<li>Taking Position: the initial idea for taking position was to go certain distance after entering the parking lot, then turn to towards the target slot and calculate the distance towards the AprilTag of it, then turn towards the parking slot in the opposite side of the target(further mentioned as helper slot) and then go backwards to the target.<ul>
<li>Travelling certain distance: we knew that the parking slots 2 and 4 were closer to the entrance than the parking slots 1 and 3. We used this information to travel a certain distance after determining which parking slot was the target. For parking in slot 2 or 4, we would travel 0.25 meters from the entrance. For parking in slot 1 or 3, we would travel 0.5 meters. However, we saw that these constants weren’t very reliable as the robot would not stop at an exact location before entering the parking lot. Therefore, we started calculating the distance from the robot to the AprilTag that was facing the entrance of the parking lot, but the idea for travelling a certain distance for each slot would remain the same.</li>

<li>Calculating the distance to target: after travelling a certain distance, we would need to turn 90 degrees towards the target slot. For turning, we were using opposite values of velocity for each wheel so that the robot would turn on its axis. Also, to determine the angle it has turned, we would use the kinematics of differential drive that we have learned from the class. After this, we would calculate the distance to the AprilTag. However, this value would be similar for all of the parking slots. Therefore, to save time, we stopped calculating the distance to the target for each run, and just did it once and used it as a constant for every run. This way, we wouldn’t have to turn towards the target slot at all.</li>

<li>Turning towards the helper slot:<ul>
<li><b>First idea</b>: we would apply the same kinematics to turn towards the helper slot as we used in calculating the distance to the target. When we were calculating the distance, we would have to turn 180 degrees. After we stopped calculating the distance, we would only have to turn 90 degrees after travelling a certain distance from the parking lot entrance. However, in our tests, we would see that a small offset in the turn towards the helper slot, would cause the robot to go towards the wrong parking slot when backing.</li>

<li><b>Making it more precise</b>: to make facing the helper slot more precise, we decided to use the translation vector to align the robot with the AprilTag of the helper slot and then go backward. We were trying to achieve this by making very small angle turns using the sign of the x value of the translation matrix. Nevertheless, the issue of small offset of angle would occur again and cause the robot to park in the wrong parking slot. Another obstacle that we were facing was that the robot didn’t have the capability of making small turns: If we gave the velocity too low, the robot would sometimes stop moving as it didn’t have enough power to turn in its place; If we gave the velocity too high, the robot would turn too much and cause the robot to enter the loop of turning too much to the left of the AprilTag, then turning too much to the right. We tried to fix this problem by using the x value of the translation matrix for the amount of angle it has to turn towards the AprilTag. To be more precise, we started using x/3 when turning so that the value of x will decrease to 0 eventually after making small x/3 turns. However, the issue of overturning, or not being able to turn was still there.</li>

<li><b>Final idea</b>: in the end, we decide to not be very precise when facing the helper slot, and make up for this by taking into the consideration the x_value of the translation matrix that we would receive from the AprilTag of the helper slot when we were backing to the target slot. So, we would approximately do 90 degrees turn towards the helper slot and start to go backwards.</li>

</ul>
</li>
</ul>
</li>

<li>Backing to the desired parking slot: as we weren’t precise when turning towards the helper slot, we had to make up for it when backing. We made the wheels turn in the same direction, however, one faster than the other. First, we would find the sign of the x_value of the translation matrix to determine whether the robot is facing towards the right side of the AprilTag of the helper slot, or the left. Then, we would decide which wheel should have higher velocity than the other using this information. For example: if the robot is facing towards the right side of the AprilTag, then we would give the left wheel velocity the value of -(v_constant + abs(x)) and the right wheel the value of -(v_constant) when going backwards. The negative sign causes the robot to go backwards, and adding the absolute value of x to a certain wheel, would cause the robot to align itself towards the AprilTag of the helper slot when going backwards, which would cause the robot to park in the target area. We also used the distance to the target slot when backing so that the robot would not hit the AprilTag in the target area.</li>

</ol>

In most of the tests, our program would park perfectly between the yellow lanes of each parking slot. However, sometimes it would touch the yellow lane, but park in the desired location, which was the main goal of this task.

## References

Reference lane following and AprilTag detection nodes solutions on Eclass<br>
detectron2 Github: [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)<br>
detectron2 Colab notebook: [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)<br>
detectron2 output format: [https://detectron2.readthedocs.io/tutorials/models.html#model-output-format](https://detectron2.readthedocs.io/tutorials/models.html#model-output-format)<br>
Notes about differential drive kinematics from eclass.<br>
