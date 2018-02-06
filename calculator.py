def calculator(str):
	precedence = {"+":1, "-":1, "*":2, "/":2}
	operands = []
	operator = []
	length = len(str)
	i = 0

	def evaluate():
		second = operands.pop()
		first = operands.pop()
		op = operator.pop()
		res = apply_func(op, first, second)
		operands.append(res)

	while i < length:
		# get first number until symbol & add it stack
		j = i
		if str[i] == "(":
			operator.append("(")
			i += 1
			continue

		while j < length and str[j].isnumeric():
			j += 1
		number = int(str[i:j])
		operands.append(number)

		if j == length:
			break
		symbol = str[j]

		if symbol == ")":
			#eval until "("
			while operator[-1] != "(":
				# eval
				evaluate()
			operator.pop()
			j += 1
			if j < length:
				symbol = str[j]
			else:
				break

		# if next symbol is higher precedence eval it after
		# finding the second number unless its parentheses.
		if len(operator) > 0 and operator[-1] != "(" and precedence[symbol] <= precedence[operator[-1]]:
			# eval
			evaluate()
		operator.append(symbol)

		i = j+1

	while len(operands) > 1:
		# eval
		evaluate()

	return operands[0]

def apply_func(op, first, second):
	if op == "*":
		return first * second
	if op == "/":
		return first / second
	if op == "-":
		return first - second
	if op == "+":
		return first + second

if __name__ == '__main__':
	easy = "1+1"
	assert calculator(easy) == 2

	harder = "1+3*4"
	assert calculator(harder) == 13

	s = "12+34/(3-4)+21*4"
	assert calculator(s) == 62

	s2 = "3*4+1*(3-1*2)"
	assert calculator(s2) == 13

	s3 = "12+105/(2*9-4)/21*4"
	assert round(calculator(s3), 3) == 13.429

	s4 = "1095-2-3-15-5"
	assert calculator(s4) == 1070

	s5 = "1095-2+(4+(123*34-1+2)+5*3)*2"
	assert calculator(s5) == 9497

	s5 = "(1095*123)-9569+(4+(123*34-1+2)+5*3)*2"
	assert calculator(s5) == 133520

	print("All tests passed.")
