#!/sgoinfre/goinfre/Perso/fleste-l/anaconda3/bin/python
from pylab import *

def graph_poly(a1, b1, c1):
	a = float(a1)
	b = float(b1)
	c = float(c1)
	t = arange(-10.0, 10.0, 0.1)
	s1 = a * t**2 + b * t + c
	plot(t, s1)
	axhline(linewidth=2, color='r')
	title('Polynomial/Linear')
	grid(True)
	show()

def main():
	a = input("Quadratic coefficient: ")
	b = input("Linear coefficient: ")
	c = input("Constant: ")
	s = "Equation: "
	s+= str(a)
	s+= " * X^2 + "
	s+= str(b)
	s+= " * X + "
	s+= str(c)
	s+= " = 0"
	print(s)
	graph_poly(a, b, c)

if __name__ == "__main__":
	main()
