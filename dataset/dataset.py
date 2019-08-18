# coding: utf-8

import numpy as np 
import tensorflow as tf 


def _parse_func(image_name, label_name, params):
    """
    Obtain the image from the filename.
    """
    image_string = tf.read_file(image_name)
    label_string = tf.read_file(label_name)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    label_decoded = tf.image.decode_jpeg(label_string, channels=1)

    image = tf.image.convert_image_dtype(image_decoded, tf.float32) # Convert to float and to range [0, 1]
    resized_image = tf.image.resize_images(image, [params.IMAGE_HEIGHT, params.IMAGE_WIDTH])
    return resized_image, label_decoded


def _train_prep(image, label):
    """
    Image preprocessing for training.
    """
    image = tf.image.random_brightness(image, max_delta=32.0 / 255.0)
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    # Make sure the image is still in [0, 1]
    image = tf.clip_by_value(image, 0.0, 1.0)

    return image, label


def create_dataset(is_training, image_names, label_names, params):
    """
    Create a dataset serving batches of images and labels.
    """
    num_samples = len(image_names)
    assert len(image_names) == len(label_names), "Image filenames and Label filenames should have same length."
    
    parse_fn = lambda f, l: _parse_func(f, l, params)
    train_fn = lambda f, l: _train_prep(f, l, params)

    if is_training:
        dataset = (tf.data.Dataset.from_tensor_slices((tf.constant(image_names), tf.constant(label_names)))
            .shuffle(num_samples)  # whole dataset into the buffer ensures good shuffling
            .map(parse_fn, num_parallel_calls=params.num_parallel_calls)
            .map(train_fn, num_parallel_calls=params.num_parallel_calls)
            .batch(params.batch_size)
            .prefetch(1)  # make sure you always have one batch to serve
            )

    else:
        dataset = (tf.data.Dataset.from_tensor_slices((tf.constant(image_names), tf.constant(label_names)))
            .map(parse_fn)
            .batch(params.batch_size)
            .prefetch(1)
            )

    # Create reinitializable iterator from dataset
    iterator = dataset.make_initializable_iterator()
    images, labels = iterator.get_next()
    iterator_init_op = iterator.initializer

    inputs = {'images': images, 'labels': labels, 'iterator_init_op': iterator_init_op}
    return inputs
