# coding: utf-8

'''
@Copyright: Copyright 2018 XX Inc 版权公告
@License: GPL 许可证版本
@Birth: 2019-08-16
@Content: 模型训练代码
@Version: 1.0.0
@Author: Cristiano-3 
@Contact: chunanluo@126.com
'''

import cv2
import numpy as np
import tensorflow as tf 
from lib.nets import vgg16
from dataset.dataset import create_dataset

tf.app.flags.DEFINE_integer('input_size', )
IMAGE_WIDTH = 600
IMAGE_HEIGHT = 400
NUM_CLASS = 11


def train():
    """
    
    """
    # data pipline
    inputs = create_dataset()
    
    # build model
    net = vgg16()
    predict, logits = net...


    # define loss and optim

    # start a session and training
    

if __name__ == "__main__":
    args = parser.parse_args()
    train()