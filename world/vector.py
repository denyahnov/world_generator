from math import *

class Vector2():
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def vector_check(self,b):
		if type(b) != Vector2: return Vector2(b,b)
		return b

	def __sub__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x-b.x, self.y-b.y)

	def __add__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x+b.x, self.y+b.y)

	def __mul__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x*b.x, self.y*b.y)

	def __div__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x/b.x, self.y/b.y)

	def __pow__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x**b.x, self.y**b.y)

	def __eq__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x==b.x, self.y==b.y)

	def __lt__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x<b.x, self.y<b.y)

	def __gt__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x>b.x, self.y>b.y)

	def __le__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x<=b.x, self.y<=b.y)

	def __ge__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x>=b.x, self.y>=b.y)

	def __ne__(self,b):
		b = self.vector_check(b)
		return Vector2(self.x!=b.x, self.y!=b.y)

	def __neg__(self):
		return Vector2(-self.x, -self.y)

	def __pos__(self):
		return self

	def clamp(self):
		self.y = -89 if self.y < -89 else self.y
		self.y = 89 if self.y > 89 else self.y

	def to_int(self):
		self.x = int(self.x)
		self.y = int(self.y)

	def to_float(self):
		self.x = float(self.x)
		self.y = float(self.y)

	def format(self):
		return (self.x,self.y)

	def multiply(self,val : int):
		self.x *= val
		self.y *= val

	def from_int(value):
		return Vector2(value,value)

class Vector3():
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def vector_check(self,b):
		if type(b) == Vector2: return Vector3(b.x,0,b.y)
		if type(b) != Vector3: return Vector3(b,b,b)
		return b

	def __sub__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x-b.x, self.y-b.y, self.z-b.z)

	def __add__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x+b.x, self.y+b.y, self.z+b.z)

	def __mul__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x*b.x, self.y*b.y, self.z*b.z)

	def __div__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x/b.x, self.y/b.y, self.z/b.z)

	def __pow__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x**b.x, self.y**b.y, self.z**b.z)

	def __eq__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x==b.x, self.y==b.y, self.z==b.z)

	def __lt__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x<b.x, self.y<b.y, self.z<b.z)

	def __gt__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x>b.x, self.y>b.y, self.z>b.z)

	def __le__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x<=b.x, self.y<=b.y, self.z<=b.z)

	def __ge__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x>=b.x, self.y>=b.y, self.z>=b.z)

	def __ne__(self,b):
		b = self.vector_check(b)
		return Vector3(self.x!=b.x, self.y!=b.y, self.z!=b.z)

	def __neg__(self):
		return Vector3(-self.x, -self.y, -self.z)

	def __pos__(self):
		return self

	def clamp(self):
		if self.x > 89: self.x = 89
		elif self.x < -89: self.x = -89

		while self.y > 180: self.y -= 360
		while self.y < -180: self.y += 360

		self.z = 0

	def to_int(self):
		self.x = int(self.x)
		self.y = int(self.y)
		self.z = int(self.z)

	def to_float(self):
		self.x = float(self.x)
		self.y = float(self.y)
		self.z = float(self.z)

	def format(self, rounding=0):
		if rounding == 0:
			return (self.x,self.y,self.z)
		else:
			return (round(self.x,2),round(self.y,2),round(self.z,2))

	def to_angle(self):
		return Vector3(
			atan2(-1 * self.z, hypot(self.x,self.y)) * (180.0 / pi),
			atan2(self.y,self.x) * (180.0 / pi),
			0.0,
		)

	def is_zero(self):
		return self == 0

	def from_int(value):
		return Vector3(value,value,value)