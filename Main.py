from GetFrontierItems import getCities, getCityCoordinates

cities = getCities()
coordinates = getCityCoordinates()
closedList = list()
success = True
goalReached = False



for item in cities.items():
    print(item)



def discoverRoute(startingCity, goalCity):
    openList = list()

    print("Starting city:", startingCity)
    print("Goal city:", goalCity)

    openList = cities[startingCity]
    currentCity = startingCity

    print("Current city:", currentCity)
    print("Open list of cities: ", openList)

    print("Not quite there yet")




discoverRoute("Rago", "El_Dorado")

# for item in coordinates.items():
#     print(item)