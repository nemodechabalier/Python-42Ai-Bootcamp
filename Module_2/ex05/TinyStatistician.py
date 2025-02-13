import math

class TinyStatistician:
	def __init__(self):
		pass
	
	def mean(self, x):
		try: 
			iter(x)
		except TypeError:
			return None
		for element in x :
			try :
				element = int(element)
			except ValueError:
				return None
		return sum(element for element in x) / len(x)
	def median(self, x):
		try: 
			iter(x)
		except TypeError:
			return None
		for element in x :
			try :
				element = int(element)
			except ValueError:
				return None
		sort = sorted(x)
		return sort[int(len(x)/2)]
	def quartile(self, x):
		try: 
			iter(x)
		except TypeError:
			return None
		for element in x :
			try :
				element = int(element)
			except ValueError:
				return None
		if len(x) < 4: 
			return None
		n = len(x)
		def percentile(tab, p):
			k = (p / 100) * (n + 1)
			f = int(k) - 1
			c = k - f - 1
			if f + 1 < n:
				return tab[f] + c * (tab[f + 1] - tab[f])
			else:
				return tab[f]
		Q = []
		sort = sorted(x)
		Q.append(percentile(sort, 25))
		Q.append(percentile(sort, 75))
		return Q

	def var(self, x):
		try: 
			iter(x)
		except TypeError:
			return None
		for element in x :
			try :
				element = int(element)
			except ValueError:
				return None
		if len(x) < 4: 
			return None
		return sum((element - self.mean(x))**2 for element in x )/ len(x)
	def std(self, x):
		try: 
			iter(x)
		except TypeError:
			return None
		for element in x :
			try :
				element = int(element)
			except ValueError:
				return None
		if len(x) < 4: 
			return None
		return math.sqrt(self.var(x))
tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print("mean = " ,tstat.mean(a))
print("median = " ,tstat.median(a))
print("quartile", tstat.quartile(a))
print("var", tstat.var(a))
print("std", tstat.std(a))