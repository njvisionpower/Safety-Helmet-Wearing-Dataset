# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:22:50 2019

@author: czz
"""
from gluoncv import data, utils
from mxnet import gluon

import mxnet as mx
import cv2
classes = ['hat', 'person']
ctx = mx.gpu()


frame = '1.jpg'
img = cv2.imread(frame)
x, img = data.transforms.presets.yolo.load_test(frame, short=416)
x = x.as_in_context(ctx)
net=gluon.SymbolBlock.imports(symbol_file='./darknet53-symbol.json', input_names=['data'], param_file='./darknet53-0000.params', ctx=ctx)



box_ids, scores, bboxes = net(x)
ax = utils.viz.cv_plot_bbox(img, bboxes[0], scores[0], box_ids[0], class_names=classes,thresh=0.4)
cv2.imshow('image', img[...,::-1])
cv2.waitKey(0)
cv2.imwrite(frame.split('.')[0] + '_result.jpg', img[...,::-1])
cv2.destroyAllWindows()

