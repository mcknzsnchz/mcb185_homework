# fizz if divisible by 3
# buzz if divisible by 5
# fizzbuzz if divisible by both

for i in range(1, 100): 
	a = (i % 3) == 0
	b = (i % 5) == 0
	c = (i % 15) == 0
	if c: 		print('FizzBuzz')
	elif a: 	print('Fizz')
	elif b: 	print('Buzz')
	else: 		print(i)
