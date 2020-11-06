from mcpi.minecraft import Minecraft
mc = Minecraft.create()
key = input ('enter key word:' )
if key == 'house':
    x,y,z = mc.player.getTilePos()
    
    mc.setBlocks(x,y,z,x+10,y+6,z+5, 57)
    mc.setBlocks(x+1,y+1,z+1,x+10-1,y+6-1,z+5-1, 0)