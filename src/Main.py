import math
from GetFrontierItems import getCities, getCityCoordinates

class Node:
    ## name of node, parent node, children[] nodes, and double weight
    def __init__(self, name, parent, children, weight):
        self.name = name
        self.parent = parent
        self.child = children
        self.weight = weight

    def addChild(self, newChild):
        self.children.append(newChild)

## The list of cities and their adjacencies. city: [list of adjacent cities]
cities = getCities()

## A dict of city: (coordinates)
cityCoordinates = getCityCoordinates()

## The cities already explored
closedList = list()

## The list of nodes
nodes = list()

lineBreak = "-------------------------------------"

for item in cities.items():
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
    nodes.append(Node(currentCity, currentCity, list(), 0.0));
    print("Selected node:", currentCity)
    print("Open list now:", openList)
    print("Closed list is now", closedList)
    printNodes(nodes)

    ## need to select the next city that is closest to our destination
    sortOpenList(openList)
    print("Sorted open list:", openList)

    while(len(openList) != 0 and not goalReached):
        print(lineBreak)

        node = openList[0]

        

        ## add adjacent cities from our selected node to the open list, and to it's children
        if node in cities.keys():
            adjacentCities = list()
            for city in cities[node]:
                adjacentCities.append(city)
                openList.append(city)
            nodes.append(Node(node, closedList[len(closedList) - 1], adjacentCities, compareCityCoordinates(node, closedList[len(closedList) - 1]))) 

        print("Selected node:", node)

        if node == goalCity:
            goalReached = True
            closedList.append(node)
            print("We made it!")
            print("Closed list is now", closedList)
            printNodes(nodes)

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
            printNodes(nodes)
            print("Not quite there yet")

## compares the given city to the goal city by coordinates
## and returns the value of the distance between them
def compareCityCoordinatesToGoalCity(e):
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

def compareCityCoordinates(city1, city2):
    ## given as latitude and longitude, which corresponds to
    ## y, x for euclidean formula
    x1 = float(cityCoordinates[city1][1])
    y1 = float(cityCoordinates[city1][0])

    x2 = float(cityCoordinates[city2][1])
    y2 = float(cityCoordinates[city2][0])

    p1 = [x1, y1]
    p2 = [x2, y2]

    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

    return distance

## sorts the open list based on how close the given city is to
## the goal city using each cities coordinates
def sortOpenList(openList):
    openList.sort(key=compareCityCoordinatesToGoalCity)
    return openList

def printNodes(nodes):
    print("Nodes:")
    for item in nodes:
        print(item.name)

## Calls main function
discoverRoute("Argonia", "Pratt")

# Kingman to wichita
# salina to wichita works


    
