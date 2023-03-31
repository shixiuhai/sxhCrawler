# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: /home/wenhua/python/pythonjh/wenhuaProjectPython/mixed_model/onnx_ort.py
# Compiled at: 2023-03-23 13:46:23
# Size of source mod 2**32: 6869 bytes
"""=================================================
@File   :onnx_ort.py
@IDE    :vscode
@Author :gpwang,yizhi
@Date   :2023/3/23
@Desc   :用onnxruntime部署yolov5
=================================================="""
import cv2, onnxruntime, argparse, numpy as np, sys
sys.path.append('..')
from onnx_utils import letterbox, scale_coords

class Detector:
    __doc__ = '\n    基于onnx的目标检测类\n    '

    def __init__(self, img_size, conf_thres, iou_thres, weight):
        super(Detector, self).__init__()
        self.img_size = img_size
        self.threshold = conf_thres
        self.iou_thres = iou_thres
        self.stride = 1
        self.weights = weight
        self.init_model()

    def init_model(self):
        """
        模型初始化这一步比较固定写法
        :return:
        """
        providers = [
         (
          'CUDAExecutionProvider', {'device_id': '1'})]
        sess = onnxruntime.InferenceSession((self.weights), providers=providers)
        self.input_name = sess.get_inputs()[0].name
        output_names = []
        for i in range(len(sess.get_outputs())):
            print('output node:', sess.get_outputs()[i].name)
            output_names.append(sess.get_outputs()[i].name)
        else:
            print(output_names)
            self.output_name = sess.get_outputs()[0].name
            print(f"input name {self.input_name}-----output_name{self.output_name}")
            input_shape = sess.get_inputs()[0].shape
            print('input_shape:', input_shape)
            self.m = sess

    def preprocess(self, img):
        """
        图片预处理过程
        :param img:
        :return:
        """
        img0 = img.copy()
        img = letterbox(img, new_shape=(self.img_size))[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img).astype(np.float32)
        img /= 255.0
        img = np.expand_dims(img, axis=0)
        assert len(img.shape) == 4
        return (img0, img)

    def detect(self, im):
        """
        :param img:
        :return:
        """
        img0, img = self.preprocess(im)
        pred = self.m.run(None, {self.input_name: img})[0]
        pred = pred.astype(np.float32)
        pred = np.squeeze(pred, axis=0)
        boxes = []
        classIds = []
        confidences = []
        for detection in pred:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID] * detection[4]
            if confidence > self.threshold:
                box = detection[0:4]
                centerX, centerY, width, height = box.astype('int')
                x = int(centerX - width / 2)
                y = int(centerY - height / 2)
                boxes.append([x, y, int(width), int(height)])
                classIds.append(classID)
                confidences.append(float(confidence))
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.threshold, self.iou_thres)
            pred_boxes = []
            pred_confes = []
            pred_classes = []
            if len(idxs) > 0:
                for i in idxs.flatten():
                    confidence = confidences[i]
                if confidence >= self.threshold:
                    pred_boxes.append(boxes[i])
                    pred_confes.append(confidence)
                    pred_classes.append(classIds[i])
            else:
                return (
                 im, pred_boxes, pred_confes, pred_classes)

    def detect_out(self, image: np.ndarray) -> dict:
        out_list = []
        shape = (self.img_size, self.img_size)
        img, pred_boxes, pred_confes, pred_classes = self.detect(image)
        if len(pred_boxes) > 0:
            for i, _ in enumerate(pred_boxes):
                box = pred_boxes[i]
                left, top, width, height = (box[0], box[1], box[2], box[3])
                box = (left, top, left + width, top + height)
                box = np.squeeze((scale_coords(shape, np.expand_dims(box, axis=0).astype('float'), img.shape[:2]).round()),
                  axis=0).astype('int')
                x0, y0, x1, y1 = (box[0], box[1], box[2], box[3])
                out_list.append({'xmin':x0,  'ymin':y0,  'xmax':x1,  'ymax':y1,  'confidence':pred_confes[i],  'name':pred_classes[i]})
        return out_list