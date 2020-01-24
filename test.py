import math

#Global variable to keep track of the final path
point_path = []

#node for the path
class Node:
    def __init__(self, loc=None, x=None,y=None):
        self.x = x
        self.y = y
        self.loc = loc
        self.next = []
visited = {}
BreakTheWorld = False


def main():
    f = open('locations.txt', 'r')
    file = f.readlines()
    locations = []
    Nodes = []
    ID = 0
    #format the two txt files(not changing the file itself but how its recieved) so that it is easier to use#################################################
    for lines in file:
        line = lines.rstrip('\n')
        line = line.split(' ')
        loc = line[0]
        if loc == 'END':
            break
        x = line[1]
        y = line[2]
        Nodes.append(Node(loc,x,y))
        locations.append(loc)
        visited[loc] = False
        ID += 1
    f.close()
    
    f = open('connections.txt', 'r')
    file = f.readlines()
    for lines in file:
        line = lines.rstrip('\n')
        line = line.split(' ')
        loc = line[0]
        if loc == 'END':
            break
        count = int(line[1])
        order = []
        for k in range(count+1):
            for x in range(count+1):
                if (x == 0):
                    continue

                elif (x == 1):
                    continue
                    #format connections from least to greatest
                elif (line[x] > line[x+1]):
                    temp = line[x]
                    line[x] = line[x+1]
                    line[x+1] = temp

        for i in range(count):
            x = locations.index(line[i + 2])
            Nodes[locations.index(loc)].next.append(Nodes[x])

    #input from user
    f.close()
    print("Please enter in the starting position:")
    start = input()
    while start not in locations:
        print("Invalid starting position. Please try again")
        start = input()
    print("Please enter in the ending position:")
    end = input()
    while end not in locations:
        print("Invalid ending position. Please try again")
        end = input()
    path = [start]*len(locations)
    length = [0]*len(locations)

    #start the path and print the path
    findPath(Nodes[locations.index(start)], path, end, length, 0, 0)
    for x in range(len(point_path)):
        print(point_path[len(point_path)-x-1])

    print("the total length of the path is " + str(bannana))
    


def findPath(node,path, end, length, count, final_distance):
    
    if node.loc == end:
        global BreakTheWorld
        BreakTheWorld = True
        global bannana
        bannana = final_distance
        return 
    if visited[node.loc]:
        return
    else:
        visited[node.loc] = True
    for tmp in node.next:
        #find the right path via DFS constraints given
        final_distance += distance(node.x,node.y, tmp.x,tmp.y)
        count += 1
        findPath(tmp, path, end, length, count,final_distance)
        #if the end has beend located
        if BreakTheWorld:
            point_path.append(node.loc + " to "  + tmp.loc + " is " + str(distance(node.x,node.y, tmp.x,tmp.y)))
            break
        else:
            final_distance -= distance(node.x,node.y, tmp.x,tmp.y)
        
    

#math function to calculate the distance between 2 individual nodes
def distance(x1,y1,x2,y2):
    x = math.pow(int(x1)-int(x2), 2)
    y = math.pow(int(y1)-int(y2), 2)

    return math.sqrt(x+y)

main()
