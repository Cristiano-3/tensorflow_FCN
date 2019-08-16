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

class Network(object):
    """
    Convolution Neural Network
    This is a abstract class, define the common part of model.
    and some implementations are flexible.
    """
    def __init__(self):
        self._predictions = {}
        self._losses = {}
        self._layers = {}

    def _build_network(self, is_training=True):
        # 

    def _category_loss():
        # sparse_softmax_cross_entropy_with_logits

    def _add_losses():
        # compute and add all losses

    def create_architecture(self, mode, num_class):
        self._image = tf.placeholder()
        self._label = tf.placeholder()

        


        