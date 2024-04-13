import math

# function that solves the quadratic formula, returning the two X-intercepts

i = +1		# single "1" to denote the imaginary i value, and adding the two number together
			# "-1" to denote the imaginary i value, and subtracting the two numbers from each other
def 	quad_roots(a, b, c):
	discriminant = (b * b - (4 * a * c))
	numerator_minus = (-b - (math.sqrt(abs(discriminant))))
	numerator_plus = (-b + (math.sqrt(abs(discriminant))))
	if discriminant > 0: 
		print("real and different roots")
		print((numerator_minus) / (2 * a))
		print((numerator_plus) / (2 * a))
	elif discriminant == 0:
		print("real and same roots")
		print((numerator_minus) / (2 * a))
		print((numerator_plus) / (2 * a))
	else: 
		print("complex roots")
		print(-b / (2 * a), i, (math.sqrt(abs(discriminant)) / (2 * a)))
		print(-b / (2 * a), -i, (math.sqrt(abs(discriminant)) / (2 * a)))

quad_roots(2, 3, 5)

quad_roots(3, 7, 8)

quad_roots(1, -5, 2)

quad_roots(1, 5, 1)

quad_roots(1, 2, 1)

quad_roots(-2, -4, -2)

quad_roots(1, -7, 10)

quad_roots(-1, 2, 3)