#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File    : test.py
# @Author  : Wang Weijian
# @Time    :  2023/11/10 13:44:57
# @function: the script is used to do something
# @version : V1
func = 'Color recognition'
device = 'myArm 300 for Pi'
mapping = {
                'QR code recognition': 'encode',
                '二维码识别': 'encode',
                'shape recognition': 'shape',
                '形状识别': 'shape',
                'Color recognition': 'color',
                '颜色识别': 'color',
                'Keypoints': 'feature',
                '特征点识别': 'feature',
                'yolov5': 'yolov5'
            }
if func in mapping:
    offset_file = f'/offset/{device}_{mapping[func]}.txt'
    print(offset_file)
    with open('./libraries' + offset_file, "r", encoding="utf-8") as f:
        offset = f.read().splitlines()
    # self.loger.info(offset)
    print(offset)
    camera_x, camera_y, camera_z = int(eval(offset[0])[0]), int(eval(offset[0])[1]), int(
        eval(offset[0])[2])
    print(camera_x, camera_y, camera_z)
