#hi
import math
point_path = []

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
        #print(loc)
        if loc == 'END':
            break
        count = int(line[1])
        #print(count)
        order = []
        for k in range(count+1):
            for x in range(count+1):
                #print(x)
                if (x == 0):
                    continue

                elif (x == 1):
                    continue

                elif (line[x] > line[x+1]):
                    temp = line[x]
                    line[x] = line[x+1]
                    line[x+1] = temp

        for i in range(count):
            x = locations.index(line[i + 2])
            Nodes[locations.index(loc)].next.append(Nodes[x])
        print(line)
    f.close()
    start = input()
    end = input()
    path = [start]*len(locations)
    length = [0]*len(locations)

    
    findPath(Nodes[locations.index(start)], path, end, length, 0, 0)
    #print(path)
    #print(sum(length))
    for x in range(len(point_path)):
        print(point_path[len(point_path)-x-1])

    print("the total length of the path is " + str(bannana))
    


def findPath(node,path, end, length, count, final_distance):
    
    if node.loc == end:
        global BreakTheWorld
        BreakTheWorld = True
        #print(final_distance)
        global bannana
        bannana = final_distance
        return 
    if visited[node.loc]:
        return
    else:
        visited[node.loc] = True
    #print(node.loc)
    for tmp in node.next:
        final_distance += distance(node.x,node.y, tmp.x,tmp.y)
        
        #print(node.loc, tmp.loc)
        #length[count] = dist
        #path[count] = tmp.loc
        count += 1
        findPath(tmp, path, end, length, count,final_distance)
        if BreakTheWorld:
            point_path.append(node.loc + " to "  + tmp.loc + " is " + str(distance(node.x,node.y, tmp.x,tmp.y)))
            break
        else:
            final_distance -= distance(node.x,node.y, tmp.x,tmp.y)
        
    


def distance(x1,y1,x2,y2):
    x = math.pow(int(x1)-int(x2), 2)
    y = math.pow(int(y1)-int(y2), 2)

    return math.sqrt(x+y)

main()
