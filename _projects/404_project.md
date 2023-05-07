---
layout: page
title: Distributed Social Networking Web App
description: I worked as a Django developer to build a social media app that links to other teams' APIs and aggregates activity from their webserver/ app.
importance: 1
category: CMPUT 404 - Web Applications and Architecture
---

[Link to the GitHub repo](https://github.com/hbheesetti/CMPUT404-project-socialdistribution)

## Summary

The web is fundamentally interconnected and peer to peer. In this course, each team creates their own app with their own API. We created ours and we linked with two other teams' APIs in order to connect our apps with theirs.

In a team of 5, we built the frontend in React, and the backend in Django. I was responsible for creating the backend for the app and for linking with other teams' API.

## Description

We build a similar, simpler version of [diaspora](https://diasporafoundation.org/).

This blogging/social network platform will allow the importing of other sources of posts (github) as well allow the distributing sharing of posts and content.

An author sitting on one server can aggregate the posts of their friends on other teams' servers.

We are going to go with an inbox model where by you share posts to your friends by sending them your posts, similar to [activity pub](https://www.w3.org/TR/activitypub/).

<div class = "row justify-content-md-center">
    <video width="320" height="240" controls>
    <source src="../../assets/vid/404/demo.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
<div class="caption">
    Demo of our app linking with other teams' apps. 
</div>
