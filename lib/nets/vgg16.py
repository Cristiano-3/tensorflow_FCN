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

import tensorflow as tf 
import tensorflow.contrib.slim as slim
from lib.nets.network.py import Network
class vgg16(Network):
    """
    VGG16 Convolution NeuralNetwork
    """
    def __init__(self):
        self._predictions = {}
        self._losses = {}
        self._layers = {}
        
