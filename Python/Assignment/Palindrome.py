String = (input('Enter a string: '))#'Jabir'
reverse = ''#ribaj
for i in String:
    reverse = i + reverse
print('Reversed string is:', reverse)
if String == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')