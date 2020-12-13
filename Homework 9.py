from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1, 5)
    e = random.randrange(0, 16)
    
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,35,e)
        x = x +4
       
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,35,e)
        x = x -4
    
    elif r == 3:
        mc.setBlocks(x,y,z,x,y+4,z,35,e)
        y = y +4
       
    elif r == 4:
        mc.setBlocks(x,y,z,x,y-4,z,35,e)
        y = y -4


