for value in range(1,5):
    print(value)

print ("\n")
for value in range (1,6): #STOPPER på sluttverdien, så sluttverdien blir ikke telt
    print(value)

#we can use the list function to store a set of numbers in a variabler
numbers = list(range(1,10))
print(numbers)

'''for tall in numbers:
    print(tall) '''

even_numbers = list(range(2, 11, 2))
print(even_numbers)
#Here the range function starts with the number 2
#Then we tell it to increase by two until it reaches 11

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)