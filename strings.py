# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'JAOUAD'
age = 23

# concatenate
print('Hi, my name is '+ name + ' and I\'m ' + str(age))

# String Formatting

# Arguments by position
print('Hi, my name is {name} and I\'m {age}'.format(name = name, age = age))

# F-Strings
print(f'Hi, my name is {name} and I\'m {age}')

# String Methods
s = 'hello devs'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('devs', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('e'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
