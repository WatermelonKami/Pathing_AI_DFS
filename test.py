#Opening locations file
import array

flag = 0 
connections=[]
f = open("connections.txt", "r")
initial_location = input("Enter the initial location: ")
for line in f:
    if line.split(None, 1)[0] == initial_location:
        for x in range(int(line.split(None,1)[1],10)):
            connections[x] = line.split(None,1)[x+2]
        flag = 1
if flag == 0:
    print("invalid initial location. Default is Set to A1!")
    initial_location = "A1"

print(initial_location)
print(connections)   
