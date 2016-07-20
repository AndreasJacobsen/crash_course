bicycles = ['trek', "cannondale", 'reldine', 'specialized',] #her tolker den både " og ' likt

print(bicycles) #printer hele listen

print(bicycles[1]) #printer cannondale da der i posisjon 1

#husker du hvordan vi gjorde om en string til å ha store bokstaver?
print("the 0th element in the list",bicycles[0].title())

#om vi ønsker å akksesere det siste elementet i listen kan vi bruke -1 som alltid tar oss rett til det siste elementet i listen.
print("The last element in the list",bicycles[-1])

#vi kan også kalle på liste-verdier i en streng

message = "My first bicycle was a " +bicycles[0].title() +"."
message1 = "My first bicycle was a " +bicycles[-1].title() +"."

print(message, "\n", message1)