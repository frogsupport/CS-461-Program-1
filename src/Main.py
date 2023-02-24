import math
from GetData import getCities, getCityCoordinates
from Node import Node

cities = getCities() ## The list of cities and their adjacencies { city, [list of adjacent cities] }
cityCoordinates = getCityCoordinates() ## A dict of cities and their coordinates { city, (coordinates) }
# closedList = list() ## The cities already explored
nodesDict = dict()## The dict of nodes { cityName, Node }
lineBreak = "-------------------------------------"

## Takes a starting and ending city and calculates the route using
## a best first search algorithm. The heuristic is sorting the frontier
## cities based on how close they are to the goal
def discoverRoute(startingCity, targetCity):
    goalReached = False ## The goal reached state
    openList = list() ## The queue
    closedList = list() ## The cities already explored
    global goalCity ## The target city
    goalCity = targetCity ## set the goal city

    openList = cities[startingCity] ## initialize the open list
    currentCity = startingCity ## select the starting / current city
    parentNode = currentCity ## set the parent node for the first node in the algorithm
    closedList.append(currentCity) ## add the city to the list of cities searched
    nodesDict[currentCity] = Node(currentCity, currentCity, createChildren(currentCity, list()), 0.0) ## add the city to the nodes dict
    sortOpenList(openList)

    print(lineBreak)
    print("Starting city:", startingCity, " - Goal City:", goalCity)
    print(lineBreak)
    print("Selected node:", currentCity)
    print(currentCity, "adjacencies: ", cities[currentCity])
    print("Open list:", openList)
    print("Closed list", closedList)

    ## main loop
    while(len(openList) != 0 and not goalReached):
        print(lineBreak)

        node = openList[0] ## Pick the city with the lowest weight
        openList.remove(node)
        # closedList = addToClosedList(openList, closedList, node)
        # if node not in closedList:
        #     closedList.append(node) ## Add this city to the searched list

        nodesDict[node] = Node(getParentNode(node, closedList, nodesDict), node, createChildren(node, closedList), distanceBetweenCities(node, parentNode))

        print("Selected node:", node)
        if node == goalCity:
            goalReached = True
            closedList.append(node) ## Add this city to the searched list
            print("We made it!")
            print("Closed list", closedList)
            printIdealPathToRoute(nodesDict, startingCity, goalCity)
            # printNodes(nodes)

        else:
            print(node, "adjacencies: ", cities[node])
            # add adjacent cities from our selected node to the open list
            for city in cities[node]:
                openList.append(city)
                # openList = addToOpenList(openList, closedList, city)

            closedList.append(node)

            # remove duplicates
            for city in openList:
                if city in closedList:
                    openList.remove(city)

            sortOpenList(openList)
            print("Open list:", openList)
            print("Closed list", closedList)

def printNodes(nodesDict):
    print("Nodes dict:")
    for value in nodesDict.values():
        print(value.printNode())

def createChildren(parentCity, closedList):
    ## need to create a list of nodes to return
    nodesList = list()

    for selectedCity in cities[parentCity]:
        if selectedCity not in closedList: ## make sure that we're not adding a city that's already been explored
            newNode = Node(parentCity, selectedCity, list(), distanceBetweenCities(parentCity, selectedCity))
            nodesList.append(newNode)

    return nodesList

## start at the ending city node, and print parent nodes until we're at the root
def printIdealPathToRoute(nodesDict, startingCity, goalCity):
    finishToStart = list()
    node = nodesDict[goalCity] ## grab the goal city node
    finishToStart.append(node.name)

    ## add nodes until we get to the starting city
    while node.name != startingCity:
        node = nodesDict[node.parent]
        finishToStart.append(node.name)

    print(lineBreak)
    print("Path from", startingCity, "to", goalCity)
    print()

    count = 0
    lastNode = Node()
    for node in reversed(finishToStart):
        if count < len(finishToStart) - 1:
            print(node, "->", end=" ")
        else:
            lastNode = node
        count += 1
    print(lastNode)
    print()

## gets the parent node for the specified city
## starts at the end of the closed list and goes up until it finds a node with this
## city as its child. Get the node itself by its name from the nodes dict
def getParentNode(city, closedList, nodesDict):
    for closedListCity in closedList:
        if city in nodesDict[closedListCity].getChildren():
            return closedListCity

## compares the given city to the goal city by coordinates
## and returns the value of the distance between them
def distanceFromCityToGoalCity(e):
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

## returns the distance between two cities
def distanceBetweenCities(city1, city2):
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
    openList.sort(key=distanceFromCityToGoalCity)
    return openList

## Execute the program
print()
print()
executing = True
while(executing):

    print("Which city are you starting from?  ", end="")
    startCity = input()
    if startCity not in cityCoordinates.keys():
        print("Invalid city, please try again\n")
        continue

    print()
    print("Which city are you going to?  ", end="")
    targetCity = input()
    if targetCity not in cityCoordinates.keys():
        print("Invalid city, please try again\n")

    else:
        discoverRoute(startCity, targetCity)
        print("Enter q to quite, anything else to continue")
        quitOrNot = input()
        if quitOrNot.lower() == "q":
            executing = False
        