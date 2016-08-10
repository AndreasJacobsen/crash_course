my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] #Når vi bruker slice ender vi opp med en ny seperat liste vi kan jobbe uavhengig på

print("My favorit foods are:")
print(my_foods)

print("\nMy friends favorit foods are:")
print(friends_foods)

my_foods.append('Cannoli')
friends_foods.append('ice cream')

print (my_foods)
print(friends_foods)