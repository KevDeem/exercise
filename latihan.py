import numpy as np
import math

f = lambda x: (x ** 4) - (3 * x ** 3) + (6 * x ** 2) - (10 * x)  - 9

def fcentral1(f,x,h):
	df = (f(x + h) - f(x-h)) / (2 * h)
	print(df)

def fcentral2(f,x,h):
	df = (f(x + h) - (2 * f(x)) + f(x - h)) / (h ** 2)
	print(df)

wow = fcentral1(f,0,0.5)
amazing = fcentral2(f,0,0.5)


def function(x0,x1):
	return (2 * x0 * x1) + (2 * x0) + (x0 ** 2) - (2 * x1 ** 2)

def obj(x0,x1):
	gradient = np.array([(2 * x1) + 2 + 2* x0, (2 * x0) - (4 * x1)])
	return gradient

def steepest(obj, arr):
	s = np.array([])
	a = 0.1
	for i in range(11):
		print("Iteration", i, "x0=",arr[0],"x1=",arr[1],"f(x)=",function(arr[0],arr[1]))
		g = obj(arr[0],arr[1])
		s = g * -1
		arr = arr + (s * a)

arr = np.array([0.5,1.0])

wow = steepest(obj,arr)


f = lambda x: x**4 - 3*x**3 + 6*x**2 - 10*x - 9

def dfcentral1(f,x,h):
	df = (f(x+h) - f(x-h)) / (2 * h)
	print(df)

def dfcentral2(f,x,h):
	df = (f(x+h) - (2*f(x)) + (f(x-h))) / (h ** 2)
	print(df)


wow = dfcentral1(f,0,0.5)
amazing = dfcentral2(f,0,0.5)








