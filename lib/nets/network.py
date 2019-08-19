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


    def _category_loss(self):
        # labels: Tensor of shape [d_0, d_1, ..., d_{r-1}], dtype=int32 or int64
        # logits: Unscaled log probabilities of shape [d_0, d_1, ..., d_{r-1}, num_classes], dtype=float16, float32, float64
        loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=predictions)
        return loss
        
    def _add_losses():
        # compute and add all losses
        with tf.variable_scope('LOSS') as scope:
            loss = self._category_loss()
            regularization_loss = tf.add_n(tf.losses.get_regularization_losses(), 'regu')
            self._losses['total_loss'] = loss + regularization_loss

        return loss

    def cretate_architecture(self, images, labels, is_training):
        self._image = images
        self._label = labels

        seg_maps = self._build_network(is_training)
        return seg_maps
        

    def train_step(self, sess, blobs, train_op):
        

"""
Args:
    params:

Returns:
    description and example of return

Raises:
    IOError: ...
"""