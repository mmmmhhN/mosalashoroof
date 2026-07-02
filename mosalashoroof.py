import string

letters = string.ascii_uppercase

j = 0
for i in range(1, 10, 2):
    print(letters[j:i+j].center(9))
    j += i
print("hello")
