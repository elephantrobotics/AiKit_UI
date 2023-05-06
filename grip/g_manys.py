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

# mc.set_gripper_mode(0)
# sleep(1)
mc.set_gripper_state(0,100)
sleep(0.05)

angles = [[-27.64, 15.2, -53.34, -52.47, 88.76, 99.05]]
coords = [189.7, -350.6, 334.0, -170.85, -0.86, -91.24]

for i in range(4):
    coords[1] += 150
    mc.send_coords(coords, 100, 1)
    sleep(2)
    mc.set_gripper_state(0,100)
    sleep(0.05)
    coords[2] -= 155
    mc.send_coords(coords,100,1)
    sleep(3)
    mc.set_gripper_state(1,100)
    sleep(1)
    coords[2] += 155
    mc.send_coords(coords,100,1)
    sleep(2)
    coords[2] -= 155
    mc.send_coords(coords,100,1)
    sleep(2)
    mc.set_gripper_state(0,100)
    sleep(1)
    coords[2] += 155
    mc.send_coords(coords,100,1)
    sleep(3)

