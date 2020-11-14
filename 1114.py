from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        print("Block ID " + str(block))
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.setBlock(x,y,z,57)
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.posToChat("Block ID " + str(block))
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'1','2','3','4')

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random 
import time

i = 0
while i < 30:
    pos = mc.player.getPos()
    i = i + 1
    x = pos.x + random.uniform(-20,20)
    y = pos.y + random.uniform(3,0)
    z = pos.z + random.uniform(-20,20)
    
    
    mc.spawnEntity(x,y,z,20)
    time.sleep(0.1)

