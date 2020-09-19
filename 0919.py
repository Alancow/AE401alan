# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:28:30 2020

@author: 李佳珍
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()


mc.postToChat("i'm watching you")

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("x:"+ str(x) +"Y:" + str(y) +"Z:" + str(z))