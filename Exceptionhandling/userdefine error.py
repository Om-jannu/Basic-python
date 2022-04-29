
class MyError(Exception):

	def __init__(self, value):
		self.value = value

	# def __str__(self):
	# 	return(repr(self.value))

try:
	raise(MyError(5*5))

except MyError as error:
	print('A New Exception occured: ',error.value)
