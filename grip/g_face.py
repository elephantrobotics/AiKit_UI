# coding=utf8
import time
from pymycobot.mycobot import MyCobot
import random
from time import sleep
import math

# port = '/dev/AMA0'
port = 'COM8'
baud = 115200
sp = 80
t = 0.05
mc = MyCobot(port,baud)
[189.7, -78.6, 334.0, -170.85, -0.86, -91.24]
# mc.set_gripper_mode(0)
# sleep(1)

angles = [[-27.64, 15.2, -53.34, -52.47, 88.76, 99.05]]
coords = [[242.4, -211.2, 122.4, -174.22, -8.42, -96.4]]

mc.send_angles(angles[0], 30)
sleep(4)
mc.set_gripper_state(0,50)
sleep(1)
mc.send_coords(coords[0],100,1)
sleep(10)
coords[0][1] +=120
mc.send_coords(coords[0],100,1)
sleep(7)
mc.set_gripper_state(1,50)
sleep(0.05)
mc.set_gripper_state(1,50)
sleep(2)
coords[0][2] += 70
mc.send_coords(coords[0],100,1)
sleep(2)
coords[0][1] += 220
mc.send_coords(coords[0],100,1)
sleep(7)
coords[0][0] += 80
mc.send_coords(coords[0],100,1)
sleep(5)
coords[0][2] -= 50
mc.send_coords(coords[0],100,1)
sleep(7)
mc.set_gripper_state(0,50)
sleep(0.05)
mc.set_gripper_state(0,50)
sleep(2)
coords[0][1] -= 50
mc.send_coords(coords[0],100,1)
sleep(4)
coords[0][0] -= 80
mc.send_coords(coords[0],100,1)
sleep(4)
mc.send_angles(angles[0], 30)
sleep(4)