

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


print(mc.player.getTilePos())

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=57
y=200
z=339


mc.player.setTilePos(x,y,z)