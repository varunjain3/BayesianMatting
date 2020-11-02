# Assignment-3 EE321 Probability and Random Processes

This repository was made as an assignment for the FALL2020 course EE321. In this project we demonstrate the Bayesian Matting Algorithm which was first introduced in the paper ["A Bayesian Approach to Digital Matting"](https://grail.cs.washington.edu/projects/digital-matting/image-matting/)

## Table of contents

- [Problem Statement](#problem-statement)
- [Background](#background)
- [Dataset](#dataset)
- [Technologies](#technologies)
- [Setup](#setup)
  - [Face Detection](#1.-Viola-Jones-Face-Detection)
  - [Face Recognition](#2.-Eigen-Faces---Face-Recognition)
- [References](#references)

## Problem Statement

Image Matting is the process of accurately estimating the foreground object in images and videos. It is a very important technique in image and video editing applications, particularly in film production for creating visual effects. In order to fully separate the foreground from the background in an image, accurate estimation of the alpha values for partial or mixed pixels is necessary. Bayesian matting models both the foreground and background color distributions with spatially-varying mixtures of Gaussians, and assumes a fractional blending of the foreground and background colors to produce the final output. It then uses a maximum-likelihood criterion to estimate the optimal opacity, foreground and background simultaneously. The goal of this assignment is for you to understand the real life implications of theory that are covered in the class. The task is to implement bayesian matting in python.

## Background

This Bayesian framework for solving the matting problem, is based on extracting the foreground element from a backgound image by estimating an opacity for each pixel (Alpha) of the foreground element. In this approach they model both the foreground and background pixels as colour distributions spatially-varying mixtures of Gaussians and assume a fractional blending of the foreground and background colours to produce the final output. It uses a maximum likelihood estimation criteria to estimate the optimal opacity or alpha at a given pixel.

## Dataset

We were provided the ALpha Matting Dataset, which can be found on their [website](http://www.alphamatting.com/index.html)

The Input images are [here](http://www.alphamatting.com/datasets/zip/input_training_lowres.zip).

The Trimap images are [here](http://www.alphamatting.com/datasets/zip/trimap_training_lowres.zip).

The Ground truth alpha images are [here](http://www.alphamatting.com/datasets/zip/gt_training_lowres.zip).

The dataset contains 27 images, with their trimaps and ground truth alpha mattes.

## Technologies

The project uses Python >= 3.5

Other technologies used

- Jupyter Notebook
- OpenCV
- Pillow
- Matplotlib
- Numpy

##### \* The project is also compatible with [Google Colabaratory](https://colab.research.google.com/)

## Setup

This project tries to implement the algorithm introduced by the CV2001 paper.
The main algorithm is implemented in the [BayesianMatting.ipynb](https://github.com/varunjain3/BayesianMatting/blob/main/BayesianMatting.ipynb) and can be also opened in [Google Colaboratory](https://colab.research.google.com/github/varunjain3/BayesianMatting/blob/main/BayesianMatting.ipynb)

## References

[1] Christoph Rhemann, Carsten Rother, Jue Wang, Margrit Gelautz, Pushmeet Kohli, Pamela Rott. A Perceptually Motivated Online Benchmark for Image Matting.
Conference on Computer Vision and Pattern Recognition (CVPR), June 2009.
