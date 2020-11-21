from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(100):
    mc.setBlocks(x+i,y-1,z+i,x+i,y,z+i+2,57)
