## retrieves the frontier list to be used in the best first search algorithm
## assembles the list and makes sure we have all symmetric connections accounted for
def getCities():
    ## The dict that will hold all of the cites that are adjacent to each other
    adjacentCitiesDict = {}

    # first add all the cities into a file, make sure we get all the adjacencies proper
    with open("data/adjacencies.txt", "r") as adjacenciesFile:
        for line in adjacenciesFile:
            adjacentCities = []
            cities = line.split()
            cityName = cities[0]

            i = 1
            while i < len(cities):
                adjacentCityName = cities[i]
                adjacentCities.append(adjacentCityName)
                i += 1

            adjacentCitiesDict[cityName] = adjacentCities

    # for item in adjacentCitiesDict.items():
    #     print(item)

    ## add all cities to the keys that aren't there
    citiesToAdd = {}
    for item in adjacentCitiesDict.items():
        keyCity = item[0]
        for city in item[1]:
            if city not in adjacentCitiesDict.keys():
                citiesToAdd[city] = keyCity

    ## add those new cities to the main adjacent cities dict
    for item in citiesToAdd.items():
        adjacentCitiesDict[item[0]] = [item[1]]

    # for item in citiesToAdd.items():
    #     print(item)

    # for item in adjacentCitiesDict.items():
    #     print(item)

    # add all symmetric adjacencies if they don't exist
    for cityToCheck in adjacentCitiesDict.keys():
        # print(cityToCheck)
        for city in adjacentCitiesDict.items():
            # make sure we're not checking ourself
            if (city[0] != cityToCheck):
                # check if we're in the adjacent cities to this city
                for adjacentCity in city[1]:
                    # check if this city is in the adjacent cities, but not in our city to checks list of adjacent cities
                    if ((cityToCheck == adjacentCity) & (city[0] not in adjacentCitiesDict[cityToCheck])):
                        # add to our city to checks list of adjacencies
                        adjacentCitiesDict[cityToCheck].append(city[0])

    return adjacentCitiesDict

## retrieves the list of cities as the key, and their coordinates as the value
def getCityCoordinates():
    ## Dict that will hold the city name as the key, and its coordinates as the value
    coordinatesDict = {}

    with open("data/coordinates.txt", "r") as coordinatesFile:
        for line in coordinatesFile:
            items = line.split()

            # set the city that is the dict key
            city = items[0]

            # get the coordinates
            x = items[1]
            y = items[2]

            coordinatesDict[city] = (x, y)

    return coordinatesDict