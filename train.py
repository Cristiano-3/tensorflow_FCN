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

tf.app.flags.DEFINE_integer('input_size', )

def build_model(image):
    """
    Args:
        params:
    
    Returns:
        description and example of return
    
    Raises:
        IOError: ...
    """



def train():
    """
    
    """
    # data pipline

    # build model
    image = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='image')
    label = tf.placeholder(tf.int32, shape=[None, None, None, 1], name='label')

    predict, logits = inference()


    # define loss and optim

    # start a session and training
    

if __name__ == "__main__":
    args = parser.parse_args()
    train()