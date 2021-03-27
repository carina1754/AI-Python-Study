i = 5
print(i)
print(i + 1)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

a1 = 1.1
a2 = 2.12
a3 = 3.123
a4 = 4.1234

print(f'{"Centered": ^14s}', f'{"Left-aligned": <14s}', f'{"Right-aligned": >14s}')
print('{0: ^14}'.format(a1), '{0: <14}'.format(a1), '{0: >14}'.format(a1))
print('{0: ^14}'.format(a2), '{0: <14}'.format(a2), '{0: >14}'.format(a2))
print('{0: ^14}'.format(a3), '{0: <14}'.format(a3), '{0: >14}'.format(a3))
print('{0: ^14}'.format(a4), '{0: <14}'.format(a4), '{0: >14}'.format(a4))