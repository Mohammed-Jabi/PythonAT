string = input("Enter a string: ")
vowels = 0
consonants = 0
if string .isalpha():
    for i in string:
        if i in ("aeiouAEIO:"):
            vowels += 1
        else:
            consonants += 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)