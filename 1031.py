from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
  


try:
    a = int(input('enter blockid:'))
    mc.setBlock(x,y,z,a)
except:
    print("error")

