#  File: TopoSort.py

#  Description: topological sort method for graph

#  Student Name: William Kwon 

#  Student UT EID: uk669

#  Partner Name: Brandon Ford

#  Partner UT EID: bef528

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 12/2/18

#  Date Last Modified: 12/3/18

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append ( item )

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek (self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))

class Queue (object):
    def __init__ (self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append (item)

    def dequeue (self):
        return (self.queue.pop(0))

    def isEmpty (self):
        return (len (self.queue) == 0)

    def size (self):
        return len (self.queue)

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def wasVisited (self):
        return self.visited

    # determine the label of the vertex
    def getLabel (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Edge(object):
    def __init__(self, fromVertex, toVertex, weight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight

class Graph (object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []
        self.topoList = []

    # check if a vertex already exists in the graph
    def hasVertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    # given a label get the index of a vertex
    def getIndex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if ((self.Vertices[i]).label == label):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def addVertex(self, label):
        if not self.hasVertex(label):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix for the new Vertex
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex in the adjacency matrix
            newRow = []
            for i in range(nVert):
                newRow.append(0)
            self.adjMat.append(newRow)

    # add weighted directed edge to graph
    def addDirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def addUndirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs(self, v):
        # create a Stack
        theStack = Stack()

        # mark vertex v as visited and push on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # vist other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)
        # the stack is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do breadth first search in a graph
    def bfs(self, v):
        # create a Queue
        theQueue = Queue()

        # mark vertex v as visited and insert into queue
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit other vertices acording to breadth
        while (not theQueue.isEmpty()):

            # front vertex
            v1 = theQueue.dequeue()
            # get an adjacent unvisted vertex
            v2 = self.getAdjUnvisitedVertex(v1)
            while(v2 != -1):
                (self.Vertices[v2]).visited = True
                print(self.Vertices[v2])
                theQueue.enqueue(v2)
                v2 = self.getAdjUnvisitedVertex(v1)


        # the queue is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visted = False

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight(self, fromVertexLabel, toVertexLabel):

        w = self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]
        if(w == 0):
            return -1
        return w

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors(self, vertexLabel):

        n = []

        idx = self.getIndex(vertexLabel)

        for i in range(len(self.adjMat[idx])):
            if(self.adjMat[idx][i] != 0):
                n.append(self.Vertices[i])

        return n

    # get a copy of the list of vertices
    def getVertices(self):
        verts = []
        for i in range(len(self.Vertices)):
            verts.append(self.Vertices[i])

        return verts

    # delete an edge from the adjacency matrix
    def deleteEdge (self, fromVertexLabel, toVertexLabel):

        coord = self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]

        if (coord != 0):
            self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] = 0

        return

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def deleteVertex (self, vertexLabel):

        vert = self.getIndex(vertexLabel)
        nVert = len(self.Vertices)

        # delete the column
        for i in range(nVert):
            for j in range(vert, nVert - 1):
                self.adjMat[i][j] = self.adjMat[i][j + 1]
            self.adjMat[i].pop()

        # delete the row
        self.adjMat.pop(vert)

        for i in self.Vertices:
            if(i.label == vertexLabel):
                self.Vertices.remove(i)

        return

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def hasCycle(self):

        # modified dfs function to check for cycle
        for i in range(len(self.Vertices)):
            # create a Stack
            theStack = Stack()

            # mark vertex as visited and push on the stack
            (self.Vertices[i]).visited = True
            # print(self.Vertices[v])
            theStack.push(i)

            # vist other vertices according to depth
            while (not theStack.isEmpty()):

                if(self.getEdgeWeight(theStack.peek(), i) != -1):
                    return True

                # get an adjacent unvisited vertex
                u = self.getAdjUnvisitedVertex(theStack.peek())
                if (u == -1):
                    u = theStack.pop()
                else:
                    (self.Vertices[u]).visited = True
                    # print(self.Vertices[u])
                    theStack.push(u)
            # the stack is empty let us reset the flags
            nVert = len(self.Vertices)
            for i in range(nVert):
                (self.Vertices[i]).visited = False

        return False


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):

        # checks if there is no cycle in the graph
        if(not self.hasCycle()):
            # create stack
            theStack = Stack()
            for vert in self.Vertices:
                if(vert.visited == False):
                    self.toposortHelper(self.getIndex(vert.label), theStack)

            # the stack is empty let us reset the flags
            nVert = len(self.Vertices)
            for i in range(nVert):
                (self.Vertices[i]).visited = False

            for i in range(theStack.size()):
                idx = theStack.pop()
                self.topoList.append(self.Vertices[idx].label)

        return

    # helper function for toposort
    def toposortHelper(self, vert, stack):

        # gets the unvisited vertex and marks it visited
        self.Vertices[vert].visited = True
        # get all the neighbors of the newly visited vertex
        neighbors = self.getNeighbors(self.Vertices[vert].label)
        # go through all the neighbors
        # if the neighbor is unvisited recursion finds the end point
        # then pushes all the vertices to the stack
        for i in neighbors:
            if(i.visited == False):
                self.toposortHelper(self.getIndex(i.label), stack)
        stack.push(vert)


        return



def main():
    # create a Graph object
    cities = Graph()

    # open file for reading
    inFile = open("./topo.txt", "r")

    # read the Vertices
    numVertices = int((inFile.readline()).strip())
    # print(numVertices)

    for i in range(numVertices):
        city = (inFile.readline()).strip()
        # print(city)
        cities.addVertex(city)

    # read the edges
    numEdges = int((inFile.readline()).strip())
    # print(numEdges)


    for i in range(numEdges):
        edge = (inFile.readline()).strip()
        # print(edge)
        edge = edge.split()
        start = cities.getIndex(edge[0])
        finish = cities.getIndex(edge[1])
        weight = int(edge[2])

        cities.addDirectedEdge(start, finish, weight)


    # close file
    inFile.close()

    # print(cities.hasCycle())

    cities.toposort()
    print(cities.topoList)




if __name__ == "__main__":
    main()