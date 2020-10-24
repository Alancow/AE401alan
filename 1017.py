from mcpi.minecraft import Minecraft
mc = Minecraft.create()




x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,57)
mc.setBlock(x-1,y,z,57)
mc.setBlock(x+1,y,z,57)
mc.setBlock(x-1,y,z-1,57)
mc.setBlock(x+1,y,z-1,57)
mc.setBlock(x,y,z+1,57)
mc.setBlock(x,y,z-1,57)






x,y,z = mc.player.getTilePos()
mc.setBlocks(x+40,y,z+40,x-40,y,z-40,57)





