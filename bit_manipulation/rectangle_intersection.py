class Rectangle(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def intersect(self, other):
		if self.is_intersect(other):
			return Rectangle(max(self.x, other.x), max(self.y, other.y),
							 min(self.x + self.width, other.x + other.width) - max(self.x, other.x),
							 min(self.y + self.height, other.y + other.height) - max(self.y, other.y))
		return Rectangle(0, 0, -1, -1)

	def is_intersect(self, other):
		return (self.x <= other.x + other.width and other.x <= self.x + self.width 
				and self.y <= other.y + other.height and other.y <= self.y + self.height)

	def __str__(self):
		return ("x: " + str(self.x) + ", " + 
				"y: " + str(self.y) + ", " + 
				"width: " + str(self.width) + ", " + 
				"height: " + str(self.height))


print Rectangle(1, 1, 2, 2).intersect(Rectangle(2, 2, 2, 2))
print Rectangle(1, 1, 1, 1).intersect(Rectangle(3, 2, 2, 2))