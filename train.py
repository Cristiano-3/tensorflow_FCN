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
    
    # build model/construct graph
    net = vgg16()
    segmaps = net.create_architecture(inputs['images'], inputs['labels'], is_training=True)

    # define loss and optim
    loss = net._losses['total_loss']
    train_op = 

    # start a session and training
    tfconfig = tf.ConfigProto(allow_soft_placement=True)
    tfconfig.gpu_options.allow_growth = True
    max_iters = 50000
    with tf.Session(config=tfconfig) as sess:
        # run the initializer
        sess.run(tf.global_variables_initializer())

        for epoch in range(1, epochs + 1)
            sess.run(intpus['iterator_init_op'])
            while True:
            
    

if __name__ == "__main__":
    args = parser.parse_args()
    train()