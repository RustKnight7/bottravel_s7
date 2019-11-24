
class Search_capital:
	"""docstring for Search_capital"""
	def __init__(self, search):
		self.search=search
	def poisk(self):
		file=open('base_date_city.txt',mode='r',encoding='UTF-8')
		for line in file:
			if self.search in line:
				capital=line[:line.index(':')]
				return(capital)
#print()