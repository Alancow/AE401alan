from mcpi.minecraft import Minecraft
mc = Minecraft.create()



while True:
    x,y,z = mc.player.getTilePos()
    block =  mc.getBlock(x,y-1,z) 
    if block == 2:
        mc.setBlock(x,y,z,38)
    

