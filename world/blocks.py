import camera
from vector import *

import pygame as pg
from GameMaker.Assets import Rectangle, Image

import random
import copy

class Assets:
	grass = pg.image.load("assets\\grass.png")
	stone = pg.image.load("assets\\stone.png")
	water = pg.image.load("assets\\water.png")

def Random(*args,**kwargs):
	rng = random.randint(0,10)

	# if rng == 0: return Water(*args,**kwargs)
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

class AssetBlock():
	def __init__(self,asset,position=(0,0,0)):
		self.position = Vector3(*position)

		self.asset = asset

		self.x,self.y,self.w,self.h = [0,0,0,0]

	def scale(self,zoom):
		return zoom * 10

	def render(self,camera):
		self.w = self.scale(camera.y)
		self.h = self.w

		self.x = (self.position.x * self.w) + camera.x 
		self.y = (self.position.z * self.h) + camera.z

		self.image = pg.transform.scale(copy.copy(self.asset), (self.w, self.h))

		self.rect = self.image.get_rect()

		self.rect.x = self.x
		self.rect.y = self.y

		return self

	def draw(self,window):
		window.blit(self.image,self.rect)

class Grass(AssetBlock):
	def __init__(self,*args,**kwargs):
		super().__init__(Assets.grass,*args,**kwargs)

class Stone(AssetBlock):
	def __init__(self,*args,**kwargs):
		super().__init__(Assets.stone,*args,**kwargs)

class Water(AssetBlock):
	def __init__(self,*args,**kwargs):
		super().__init__(Assets.water,*args,**kwargs)

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