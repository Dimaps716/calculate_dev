def calculate(operation, x, y):
	"""
	It takes in three arguments, an operation, and two numbers, and returns the result of the operation on the two numbers

	:param operation: This is the operation that the user wants to perform
	:param x: The first number
	:param y: The second number
	:return: The result of the calculation.
	"""
	if operation == 'Addition':
		return x + y

	elif operation == 'Subtraction':
		if x > y:
			return x - y
		else:
			return y - x

	elif operation == 'Multiplication':
		return x * y

	elif operation == 'Division':
		return x / y
