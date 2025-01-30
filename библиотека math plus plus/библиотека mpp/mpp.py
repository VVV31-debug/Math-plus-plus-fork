from random import randint

def plus (a, b):
	return a + b

def minus (a, b):
	return a - b
	
def umnogh (a, b):
	return a * b
	
def razdelit (a, b):
	return a / b

def r_int(a, b):
	result = randint(a, b)
	return result
	
def dist_determinant(x_1, x_2, y_1, y_2):
	result = (((x_1 - x_2)**2) + ((y_1 - y_2)**2))**0.5
	return result