motorcycles = ['honda', 'yamaha', 'suzuki']
print("First list of items")
print(motorcycles)


#kan vi endre verdie 0 i listen? La oss prøve, vi gjør om honda til ducati
motorcycles[0] = 'ducati'
#print ='Change the value of the first item in the list (0)'
print(motorcycles)
#la oss prøve å legge en til på slutten, vi har en egen funksjon for det

motorcycles.append('toyota')
print("Adds a toyoate to the end of the list")
print(motorcycles)

motorcycles2 = []
motorcycles2.append('merke1')
motorcycles2.append('merke2')
motorcycles2.append('merke3')
#Print an emtpy list with appended values
print(motorcycles2)
#vi kan også slette fra lister
print(motorcycles[1])
del motorcycles[1] #sletter yamah
print("Deletes (Yamaha) from the list (value 1)")
print(motorcycles)
print(motorcycles[1])