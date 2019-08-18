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

    def _image_to_head(self, is_training, reuse=None):
        raise NotImplementedError

    def _head_to_tail(self, is_training, reuse=None):
        raise NotImplementedError
        
    def _build_network(self, is_training=True):
        # 完整的模型架构
        # part1 backbone/forward
        net_conv = self._image_to_head(is_training)

        # part2 use feature map
        seg_maps = self._head_to_tail(net_conv)

        return seg_maps


    def _category_loss():
        # sparse_softmax_cross_entropy_with_logits

    def _add_losses():
        # compute and add all losses

    def cretate_architecture(self, training):
        self._image = tf.placeholder(tf.float32, shape=[None, IMAGE_HEIGHT, IMAGE_WIDTH, 3], name='image')
        self._label = tf.placeholder(tf.int32, shape=[None, IMAGE_HEIGHT, IMAGE_WIDTH, 1], name='label')

        seg_maps = self._build_network(training)

    def train_step(self, sess, blobs, train_op):    
        

"""
Args:
    params:

Returns:
    description and example of return

Raises:
    IOError: ...
"""