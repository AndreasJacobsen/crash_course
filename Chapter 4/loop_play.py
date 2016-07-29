#print 1-20 in a loop
#First example we do it using value in range
x = 0
for value in range (0, 20):
    x = x+1
    print(x)
print ("We managed to count to 20!\n Let\'s do it again!")

x = 0
while x < 20:
    x = x+1
    print(x)
#Let's make a list up to 100000! :)
million = [];
for value in range (0, 100001):
    million.append(value)
print(million)
print(min(million))
print(max(million))

#Odd numbers
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)


even_numbers = list(range(2, 11, 2))
print(even_numbers)

#3 time to 30
x=0
numbers = list(range(0,30))
for tall in numbers:
    x=x+1

print(x)



