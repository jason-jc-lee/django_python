cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
three_cities = cities[0:4]
cities[0] = "San Franscisco"
cities[2] = "New York City"
cities[7] = "Hollywood"
cities[5] = "Tampa"

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")

del cities[5] #memphis delete
cities.pop (7) #boston delete
cities.remove("Denver") #denver delete
print(three_cities)
print(cities)

#list
elements = ["Air", "Fire", "Water", "Dirt", "Electric", "Brick", "Computer", "Taco Bell", "Pyrite", "Chlorine"]
#element number
elements[0]
elements[2]
elements[4]
#append extend insert some stuff
elements.append("Water")
elements.extend(["Wood", "Fists"])
elements.insert(6, "Time")
#delete things
del elements[8] #taco bell delete
elements.pop(11) #water delete
elements.remove("Fire") #fire delete

#create lisrt from list
four_elements = elements[1:5]
#replace stuff
elements[2] = "Darkness"
elements[3] = "Electron"
elements[4] = "Plastic"
elements[7] = "Egg Drop Soup"
#replace other list
four_elements[2] = "Whoopie Cushion"



#lists lab 4

#-----

print(elements)
print(four_elements)

