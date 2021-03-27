# Have to specify that this single quote does not indicate the end of the string.
# You specify the single quote as \'. (Notice the backslash.)
print('What\'s your name?')
# print('What's your name?')

# Another way of specifying this specific string would be using double quotes:
print("What\'s your name?")
print("What's your name?")

# Backslash itself - \\
# Newline character - \n
# Tab - \t
# Single quote - \'
# Double quote - \"

print('a\\b')
print('a\nb')
print('a\tb')
print('a\'b')
print('a\"b')
print('He asked \"What\'s your name?\"')

# Multiple-line string specification:
# Triple-quoted string
print('''This is the first line
This is the second line''')
# Newline character \n
print('This is the first line\nThis is the second line')

print('''He asked 
\"What\'s your name?''')
print('He asked\n \"What\'s your name?')

# A ‘single backslash at the end of the line’ indicates that the string is continued in the next line
# But no newline is added.
