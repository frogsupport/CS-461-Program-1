class Node:
    def __init__(self, parent=str(), name=str(), children=list(), weight=float()):
        self.parent = parent
        self.name = name
        self.children = children
        self.weight = weight
    
    def printNode(self):
        print("-- ", self.name, "--")
        if len(self.children) > 0:
            for child in self.children:
                print("----------",child.name)

    def getChildren(self):
        childrenList = list()
        if len(self.children) > 0:
            for child in self.children:
                childrenList.append(child.name)

        return childrenList