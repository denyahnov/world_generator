import camera
from vector import *

from GameMaker.Assets import Rectangle

import random

def Random(*args,**kwargs):
	rng = random.randint(0,10)

	if rng == 0: return Water(*args,**kwargs)
	if rng < 4: return Stone(*args,**kwargs)

	return Grass(*args,**kwargs)

class Block(Rectangle):
	def __init__(self, r,g,b, position=(0,0,0)):
		self.position = Vector3(*position)

		super().__init__([0,0,0,0],outline=int(camera.SHOW_GRID),foreground_color=(r,g,b))

	def scale(self,zoom):
		return zoom * 10

	def render(self,camera):
		self.w = self.scale(camera.y)
		self.h = self.w

		self.x = (self.position.x * self.w) + camera.x 
		self.y = (self.position.z * self.h) + camera.z

		return self

class Grass(Block):
	def __init__(self,*args,**kwargs):
		super().__init__(0,150,0,*args,**kwargs)

class Stone(Block):
	def __init__(self,*args,**kwargs):
		super().__init__(150,150,150,*args,**kwargs)

class Water(Block):
	def __init__(self,*args,**kwargs):
		super().__init__(0,0,150,*args,**kwargs)

class Chunk():
	def __init__(self, default = Block, position = Vector2.from_int(0) ):
		self.position = position

		self.data = [[[default(position=(x,y,z)) for x in range(camera.CHUNK_SIZE.x)] for z in range(camera.CHUNK_SIZE.z)] for y in range(camera.CHUNK_SIZE.y)]

	def layer(self,layer):
		l = []
		for line in self.data[layer]:
			l += line
		return l

	def block(self,x,y,z):
		return self.data[y][z][x]