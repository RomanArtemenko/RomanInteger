"""Module for converting Roman to integer and vice versa"""

DICTIONARY = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

ROMAN_SYMBOLS = {lt for ar, ro in DICTIONARY for lt in ro}    

def roman_to_integer(number):
	"""Covert roman to integer

	Keyword argument:
	number - roman number
	"""
	number = number.upper()
	result = 0

	for arabic, roman in DICTIONARY:
		while number.startswith(roman):
			result += arabic
			number = number[len(roman):]

	if number:
		print("Invalid roman number !")
		return 0
	if not is_valid_integer(result):
		print("Invalid roman number !")
		return 0

	return result

def integer_to_roman(number):
	"""Covert integer to roman 

	Keyword argument:	
	number - the integer
	"""
	result = ''

	for arabic, roman in DICTIONARY:
		while number >= arabic:
			result += roman
			number -= arabic

	
	return result
		
def is_valid_integer(number):
	"""Check correctly input integer

	Keyword argument:
	number - the integer
	"""
	return 0 < number <= 3999

def is_valid_roman_sumbols(number):
	"""Check correctly input Roman number

	Keyword argument:
	number - the roman number
	"""
	return set(number.upper()).issubset(ROMAN_SYMBOLS)

def _main(input_string):
	try:
		input_string = int(input_string)

		if is_valid_integer(input_string):
			print(integer_to_roman(input_string))
		else:
			print('The Number must be "0 < integer <= 3999"')
	except :
		if len(input_string) > 0 and is_valid_roman_sumbols(input_string):
			print(roman_to_integer(input_string))
		else:
			print("The input value must be an integer or roman number")
		 

if __name__ == "__main__":
	_main(input('Enter Roman or Integer number: '))
	

