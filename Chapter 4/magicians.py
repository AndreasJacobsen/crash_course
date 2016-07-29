magicians = ['alice','david', 'caroline']

for magicians_variable in magicians:
    print(magicians_variable)

dogs_cats = ['muts', 'cats', 'meow', 'woff']

x = 0

#egen løkke for å øve
for x in range (0, 3):
    if x ==1:
        print ('x er',x)
    else:
        print ('nå er x', x)

#la oss printe magicians med title, så de får store navn

magicians = ['alice','david', 'caroline']

for magicians_variable in magicians:
    print(magicians_variable.title() + " is a magician with capital letters in her name! " )
    print('I can\'t wait to see your next trick ' + magicians_variable.title() + ".\n")
#in order to print after a for then you stop having it indentet
#How many magicians are there?
i = 0
print ('Let\'s count magicians!')
for magicians_variable in magicians:
    i = i+1
    print ("Now we have counted", i, " magicians")
