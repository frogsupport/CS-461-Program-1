import math
from GetFrontierItems import getCities, getCityCoordinates

## The list of cities and their adjacencies. city: [list of adjacent cities]
cities = getCities()

## A dict of city: (coordinates)
cityCoordinates = getCityCoordinates()

## The cities already explored
closedList = list()

lineBreak = "-------------------------------------"

for item in cities.items():
    print(item)

for item in cityCoordinates.items():
    print(item)

def discoverRoute(startingCity, targetCity):
    ## Whether or not we've reached our goal
    goalReached = False
    openList = list()
    global goalCity
    goalCity = targetCity

    print(lineBreak)
    print("Starting city:", startingCity)
    print("Goal city:", goalCity)
    print(lineBreak)

    ## initialize the open list
    openList = cities[startingCity]
    currentCity = startingCity
    closedList.append(currentCity)
    print("Selected node:", currentCity)
    print("Open list now:", openList)
    print("Closed list is now", closedList)

    ## need to select the next city that is closest to our destination
    sortOpenList(openList)
    print("Sorted open list:", openList)

    while(len(openList) != 0 and not goalReached):
        print(lineBreak)

        node = openList[0]

        if node in cities.keys():
            for city in cities[node]:
                openList.append(city)

        print("Selected node:", node)

        if node == goalCity:
            goalReached = True
            closedList.append(node)
            print("We made it!")
            print("Closed list is now", closedList)

        else:
            openList.remove(node)
            closedList.append(node)

            for city in openList:
                if city in closedList:
                    openList.remove(city)

            print("Open list now:", openList)
            print("Closed list is now", closedList)

            sortOpenList(openList)
            print("Sorted open list:", openList)
            print("Not quite there yet")

## compares the given city to the goal city by coordinates
## and returns the value of the distance between them
def compareCityCoordinates(e):
    ## given as latitude and longitude, which corresponds to
    ## y, x for euclidean formula
    x1 = float(cityCoordinates[e][1])
    y1 = float(cityCoordinates[e][0])

    x2 = float(cityCoordinates[goalCity][1])
    y2 = float(cityCoordinates[goalCity][0])

    p1 = [x1, y1]
    p2 = [x2, y2]

    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

    return distance

## sorts the open list based on how close the given city is to
## the goal city using each cities coordinates
def sortOpenList(openList):
    openList.sort(key=compareCityCoordinates)
    return openList

## Calls main function
discoverRoute("Kingman", "Wichita")

# Kingman to wichita
# salina to wichita works