# A simple example of an ‘expression’ is 2 + 3.
# An expression can be broken down into operators and operands.
# ‘Operators’ are functionality that do something and can be represented by symbols such as + or by special keywords.
# Operators require some data to operate on and such data is called ‘operands’. In this case, 2 and 3 are the operands.

# Arithmetic Operators
# Summation
A = 3
B = 5
print(A + B)

A = 'a'
B = 'b'
print(A + B)

A = 2
print(+A)

# Subtraction
A = 5.2
print(-A)

A = 50
B = 24
print(A - B)

# Multiplication
A = 2
B = 3
print(A * B)

A = 'la'
B = 3
print(A * B)

A = 3
B = 4
print(A ** B)

# Division
A = 13
B = 3
print(A / B)

# Divide and Floor
A = 13
B = 3
print(A // B)

A = -13
B = 3
print(A // B)    # -4.3333

A = 9
B = 1.81
print(A // B)    # 4.972

# Modulo
A = 13
B = 3
print(A % B)    # 13-12

A = -25.5
B = 2.25
print(A % B)    # (2.25 * 12.0) - 25.5


# Relational Operators

x = 2
y = 2
print(x != y)

x = 2
y = 2
print("x == y", x == y)

x = 'str'
y = 'stR'
print(x != y)
print(x.lower() != y.lower())
print(x.upper() != y.upper())

x = 'str'
y = 'stR'
print("x == y", x == y)
print("x.lower() == y.lower()", x.lower() == y.lower())

x = 'str'
y = 'str'
print(x != y)

x = 'str'
y = 'str'
print("x == y", x == y)
