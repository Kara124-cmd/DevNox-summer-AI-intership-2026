dictionary = {}

for i in range(3):
    subject = input('enter your subject : ')
    marks = int(input('enter your marks : '))

    dictionary.update({subject : marks})
print(dictionary)
