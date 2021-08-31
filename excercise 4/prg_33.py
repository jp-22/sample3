def dec1(p1,p2):
	def inner(func):

		return func(p1*p2)

	return inner

@dec1(4,3)
def func(f1,f2=6):
	print(f1+f2)


