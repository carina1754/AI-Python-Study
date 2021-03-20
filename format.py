# The format method constructs strings from other information.
iAge = 20
sName = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(sName, iAge))
print('Why is {0} playing with that python?'.format(sName))

# The numbers between braces are optional.
iAge = 20
sName = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(sName, iAge))
print('Why is {} playing with that python?'.format(sName))

# There can be more detailed specifications such as:
# Alignment: fill with underscores (_) with the text centered (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
print('{0:_>11}'.format('hello'))
print('{0:_<11}'.format('hello'))

print('{0:_^11s}'.format('hello'))
print('{0:_>11s}'.format('hello'))
# ERROR: Unexpected type str in following.
# print('{0:_<11f}'.format('hello'))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3.0))
print('{0:_^10.3f}'.format(1.0/3.0))
# If the number of spaces is odd, place a smaller number of spaces in the front.

# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# cf.
print('{name} wrote {book}'.format(book='A Byte of Python', name='Swaroop'))
print('{book} wrote {name}'.format(name='Swaroop', book='A Byte of Python'))

print('{0:_^10.3f}'.format(1.0/3.0))
print('{0:_<10.3f}'.format(1.0/3.0))
print('{0:_>10.3f}'.format(1.0/3.0))

print('{0:_^14s}'.format('Centered'), '{0:_<14s}'.format('Left-aligned'), '{0:_>14s}'.format('Right-aligned'))
print('{0:_^14s}'.format('1'), '{0:_<14s}'.format('1'), '{0:_>14s}'.format('1'))
print('{0:_^14s}'.format('12'), '{0:_<14s}'.format('12'), '{0:_>14s}'.format('12'))
print('{0:_^14s}'.format('123'), '{0:_<14s}'.format('123'), '{0:_>14s}'.format('123'))
print('{0:_^14s}'.format('1234'), '{0:_<14s}'.format('1234'), '{0:_>14s}'.format('1234'))

print('{0:_^14s}'.format('Centered'), '{0:_<14s}'.format('Left-aligned'), '{0:_>14s}'.format('Right-aligned'))
print('{0:_^14s}'.format('1.1'), '{0:_<14s}'.format('1.1'), '{0:_>14s}'.format('1.1'))
print('{0:_^14s}'.format('2.12'), '{0:_<14s}'.format('2.12'), '{0:_>14s}'.format('2.12'))
print('{0:_^14s}'.format('3.123'), '{0:_<14s}'.format('3.123'), '{0:_>14s}'.format('3.123'))
print('{0:_^14s}'.format('4.1234'), '{0:_<14s}'.format('4.1234'), '{0:_>14s}'.format('4.1234'))

print('{0: ^14s}'.format('Centered'), '{0: <14s}'.format('Left-aligned'), '{0: >14s}'.format('Right-aligned'))
print('{0: ^14s}'.format('1.1'), '{0: <14s}'.format('1.1'), '{0: >14s}'.format('1.1'))
print('{0: ^14s}'.format('2.12'), '{0: <14s}'.format('2.12'), '{0: >14s}'.format('2.12'))
print('{0: ^14s}'.format('3.123'), '{0: <14s}'.format('3.123'), '{0: >14s}'.format('3.123'))
print('{0: ^14s}'.format('4.1234'), '{0: <14s}'.format('4.1234'), '{0: >14s}'.format('4.1234'))

# Print always ends with an invisible ‘new line’ character (\n)
# Repeated calls to print will all print on a separate line each.
# To prevent this newline character from being printed, specify that it should ‘end’ with a blank:
print('a', end='')
print('b')

# Or you can ‘end’ with a space:
print('a', end=' ')
print('b', end=' ')
print('c')
