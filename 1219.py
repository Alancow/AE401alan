from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


x,y,z = mc.player.getTilePos()



for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x + i
    
    
    for i in range(10):
        r = random.randrange(0,16) 
        z = z + 1
        mc.setBlock(x,y,z,35,r)