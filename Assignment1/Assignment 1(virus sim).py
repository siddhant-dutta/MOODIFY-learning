import matplotlib.pyplot as plt 
import numpy as np 
import random 

def travel (arr):
    for i in range (8):
        x1 = random.randint(0, 99)
        y1 = random.randint(0, 149)
        x2 = random.randint(0, 99)
        y2 = random.randint(0, 149)
        temp = arr[x1,y1]
        arr[x1,y1] = arr[x2,y2]
        arr[x2,y2] = temp

def effecton_neigh1(arr, x, y):
    # used tuple for the indexes of the first neighbour because we don't wan't to 
    # change their value 
    neigh1idx = [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y-1), 
                 (x+1,y-1), (x-1,y+1)] 
    
    for coord in neigh1idx:
        # getting rid of the neighbors which fall out of the matrix 
        if coord[0] < 0 or coord[1] <0 or coord[1] > 149 or coord[0] > 99:
            continue 
        # infecting the neighbors using the given probability of infection i.e 0.25 
        # for each neighbour 
    
        elif arr[coord[0], coord[1]] == 0:
            arr[coord[0], coord[1]] = random.choices([0, 1], [0.75, 0.25])[0]

def effecton_neigh2(arr, x, y):
    neigh2idx = [(x+2, y), (x-2, y), (x, y+2), (x, y-2), (x+2, y+2), (x-2, y-2), 
                 (x+2, y-2), (x-2, y+2), (x+1, y+2), (x+1, y-2), (x-1, y+2), 
                 (x-1, y-2), (x+2, y+1), (x-2, y+1), (x+2, y-1), (x-2, y-1), ]
        
    for coord in neigh2idx:
        # getting rid of the neighbors which fall out of the matrix 
        if coord[0] < 0 or  coord[1] < 0 or coord[0] > 99 or coord[1] > 149:
            continue

        # infecting the neighbors using the given probability of infection i.e 0.08 
        # for each neighbour 
    
        elif arr[coord[0], coord[1]] == 0: 
            arr[coord[0], coord[1]] = random.choices([0, 1], [0.92, 0.08])[0]

arr = np.zeros((100,150), dtype= int )
arr[50, 75] = 1
iterations = 0
ones = [1]
onesadded = [0]
posnof1s = {(50, 75)}  #`making a set to avoid repeating elements
boolval = True

while boolval :
    # first make the people travel randomly
    travel (arr) 
    boolval = False

    for posn in posnof1s: 
        effecton_neigh1(arr, posn[0], posn[1])
        effecton_neigh2(arr, posn[0], posn[1])
    
    for i in range (0,100):
        for j in range(0,150):
            if arr[i, j] == 1 :
                # storing the posns of the new infected people also
                posnof1s.add((i,j))
            else:
                boolval = True  # even if atleast one 0 remains in the matrix then it will help to proceed to the next iteration till no 0 remains

    ones.append(len(posnof1s)) 
    onesadded.append(ones[len(ones)-1] - ones[len(ones)-2])
    iterations+= 1

plt.subplot(2,1,1)
x = range(iterations+1)
plt.plot(x, ones)
plt.xlabel("Number of Iterations")
plt.ylabel("Number of 1's in the Matrix")
plt.show()

plt.subplot(2,1,2)
plt.plot(x, onesadded)
plt.xlabel("Number of Iterations")
plt.ylabel("Number of 1's added")
plt.show()

print(f'Number of Maximum 1\'s added is {max(onesadded)}' )




        