# 20demo.py by mackenziesanchez

import math

print('hello, again') # greeting
print(1.5e-2)
print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))
print(pow(2, 3))
print(math.pow(2, 3))
print(2 ** 0.5)
print(math.sqrt(2))
print(math.log(2))
# print(1 / 0)				# division by zero
# print(math.log(0))		# math domain error
# print(math.sqrt(-1))		# math domain error
print ((-1)**0.5) 			# complex number, not a math domain error
print(0.1 * 1)
print(0.1 * 3)

a = 3 					# side of triangle
b = 4						# side of triangle
c = math.sqrt(a**2 + b**2) 		# hypotenuse
print(c)

print(type(a), type(b), type (c))

print(type(a), type(b), type (c), sep=', ')

def	greeting():
	print("hello yourself")
greeting()
    
def	pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
x = pythagoras(3, 4)
print(x)
    
def	pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))

# function that turns negative numbers positive. 
def	ntopos(x):
	c = abs(x)
	return c
c = ntopos(-3)
print(ntopos(c))

# function that turns positive numbers negative
def	ptone(x):
	c = -abs(x)
	return c
c = ptone(6)
print(ptone(c))

# function that computes area of a square
def	asqu(a):
	return print(a ** 2)
print(asqu(4))

# function that computes area of a rectangle
def	arec(a, b):
	return print(a * b)
print(arec(3, 4))

# function that computes the area of a circle
def	acir(r):
	return print(math.pi * (r ** 2))
print(acir(3))

# function that computes the perimeter of a square
def	psqu(l):
	return (4 * l)
print(psqu(5))

# function that computes the perimeter of a rectangle
def	prec(l, w):
	return print((2 * l) + (2 * w))
print(prec(3, 2))

# function that computes the circumference of a circle
def	ccir(r):
	return print(2 * math.pi * r)
print(ccir(5))

# function that computes the volume of a cube
def	vcub(a):
	return print(a ** 3)
print(vcub(3))

# function that computes the volume of a box
def	vbox(l, w, h):
	return print(l * w * h)
print(vbox(3, 4, 5))

# function that computes the volume of a sphere
def	vshp(r):
	return print((4 / 3) * math.pi * (r ** 3))
print(vshp(5))

# function that converts temperature from C to K
def	c_k(d):
	return print(d + 273.15)
print(c_k(25))

# function that converts F to C
def 	f_c(d):
	return print((d - 32) * (5 / 9))
print(f_c(70))

# function that converts mph to kph
def	mph_kph(s):
	return print(s / 0.6214)
print(mph_kph(65))

# function that converts fps to mps
def	fps_mps(l):
	return print(l * 0.3048)
print(fps_mps(3))

# function that computes DNA concentration from OD260
# for 50 = 50 mg/mL x 10^-3 mg/mL, 50 = dilution factor
# output is in mg/mL
def conc_od(o):
	return print(o * 50 * 50)
print(conc_od(0.65))

# function that computes the distance between two points on a graph
def	distpts(x1, y1, x2, y2):
	return print(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
print(distpts(3, 2, 5, 6))

# function that computes the midpoint between two points
def	midpoint(x1, y1, x2, y2):
	mx = print((x1 + x2) / 2)
	my = print((y1 + y2) / 2)
	return mx, my
x, y = midpoint (2, 6, 4, 8)

s = 'hello world' 
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
print(a, b)

c = a == b
print(c)
print(type(c))

if 	a <  b: 	print('a < b')
elif 	a > b : 	print('a > b')
else:			print('a == b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if 	a < b: 	print('a < b')
elif	a > b: 	print('a > b')
else: 		print('a == b')

print(abs(a - b)) 
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A' 
s2 = 'B' 
s3 = 'a' 
if s1 < s2: print('A < B') 
if s2 < s3: print('B < a')

# function that determines if a number is an integer
def	is_integer(a):
	if type(a) is int: return print('is integer')
is_integer(6.5)
is_integer(4)

# function that determines if a number is odd
def	is_odd(x):
	if  not (x % 2 == 0): 	return print('is odd')
	else: 		return print('is not odd')
is_odd(15)
is_odd(6)

# function that determines if a number is a valid probability
def	valid_prob(x):
	a = 0
	b = 1
	if x > a and x < b: 	return print('valid probability')
	else: 			return print('invalid probability')
valid_prob(0.3)
valid_prob(4)

# function that returns the molecular weight of a DNA letter 
a = 135.13
t = 126.113
g = 151.13
c = 111.1
def	mw_dna(x):
	if x == "A": 		return print(a)
	if x == "T": 		return print(t)
	if x == "G": 		return print(g)
	if x == "C": 		return print(c)
	else: 			return print('not a DNA base')
mw_dna("A")
mw_dna("T")
mw_dna("B")

# function that returns the complement of a DNA letter
def	complement_dna(x):
	if x == "A": 		return print('T')
	if x == "T":			return print('A')
	if x == "G":		return print('C')
	if x == "C": 		return print('G')
	else: 			return print('not a DNA base')
complement_dna("G")
complement_dna("T")

















