# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

a = 1            # int
b = 2.3          # float
name = 'jad'     # string
is_true = True   # bool

# multiple assignement
x, y, last_name, is_false = (2, 3.4, 'ajad', False)

# basic math
z = b + y
c = x * a / 100

#casting
x = str(x)
d = int(y)
# name_err = int(name)
e = float(a)

print(type(e), name, d)