name = 'global name'

class test:
	name = 'class name'
	age = 'sss'
	def __init__(self):
		name = 'init name'
		self.age = '123'
		self.height = '22'
	
	def printName(self):
		print('name = %s' % self.name)

	def printAge(self):
		print('age = %s' % self.age)
		
	def changeHeight(self):
		height = '33'
		#self.height = '34'

	def printHeight(self):
		print('height = %s' % self.height)

	
if __name__ == '__main__':
	t = test()
	t.printName()
	t.printAge()
	t.changeHeight()
	t.printHeight()
