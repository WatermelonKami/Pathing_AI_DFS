import math

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
    start = 'A1'
    end = 'G1'
    path = ['B2']*len(locations)
    length = [0]*len(locations)
    findPath(Nodes[locations.index(start)], path, end, length, 0)
    #print(path)
    #print(sum(length))


def findPath(node,path, end, length, count):
    
    if node.loc == end:
        global BreakTheWorld
        BreakTheWorld = True
        return
    if visited[node.loc]:
        return
    else:
        visited[node.loc] = True
    print(node.loc)
    for tmp in node.next:
        dist = distance(node.x,node.y, tmp.x,tmp.y)
        #print(node.loc, tmp.loc)
        #length[count] = dist
        #path[count] = tmp.loc
        count += 1
        findPath(tmp, path, end, length, count)
        if BreakTheWorld:
            break


def distance(x1,y1,x2,y2):
    x = math.pow(int(x1)-int(x2), 2)
    y = math.pow(int(y1)-int(y2), 2)

    return math.sqrt(x+y)

main()
