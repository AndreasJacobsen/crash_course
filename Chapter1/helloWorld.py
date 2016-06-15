message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course World!"

print(message)
#Nesting of " and '
hyphons = 'I told my friend, "Pything is my favorit language!"'

print(hyphons)
#.title setter store bokstaver på alle ord
name = "ada lovelace"
print(name.title())

myname1 = "Andreas Jacobsen"
myname2 = "andreas jacobsen"
myname3 = "ANDREAS JACOBSEN"
#sette alle bokstaver store eller små
print(myname1.upper())
print(myname2.upper())
print(myname2.lower())

#\t er tabulator
first_name = "andreas"
last_name = " \tjacobsen"
print("")
print(first_name.title() + " " + last_name.title())

#\n er newline
fullname = "andreas\njacobsen"
print(fullname.title())

#disse argumentene kan nøstes
print("Languages\n\tPython\n\tC\n\tJavaScript")

#vi kan fjerne mellomrom med rstrilp
favorit_language = 'python '
print(favorit_language)
print(favorit_language.rstrip())
print(favorit_language) #her ser vi at rstrip bare kjører når vi pgerinter, den endrer ikke variabelen. da fjernen den right strip

#for å fjerne left strip bruker vi .lstrip, for å fjerne alle mellomrom bruker vi .strip