class Park:
	lastname="박"
	def __init__(self,name):
		self.fullname = self.lastname+name

pey=Park("응용")

print(pey.fullname)
