import numpy as np
import sys
import random 

 
def make_maze(n: int,  x: int ):
    maze = np.random.randint(1,n, size=(n, x))

    for i in range(n):
        for j in range(n):
            min1 = 1
            max1 = max(i, n-1-i, n-1-j, j)
            print(max1)
            maze[i][j]= random.randint(min1,max1)
    maze[n-1][x-1] = 0
    return maze

# check if we can actually add this value to the graph, cuz it may not be possible iwth length
def in_bounds(node, n):
    if node[0] < 0 or node[1] < 0:
        return False
    if node[0] >= n or node[1] >= n:
        return False
    return True

def solve_maze(rjm_array, n):
    '''finds the distance array of an rjm'''
    #init dist array
    dist = [None] * n
    for i in range(n):
        dist[i] = [None] * n
    dist[0][0] = 0
    depth = 0
    print("step 1")
    # print_arr(dist)
    while True: 
        farthest = []
        
        #do an iterative search to find nodes farthest traveled
        for r in range(n):
            for c in range(n):
                if dist[r][c] == depth:
                    farthest.append((r, c))
        
        if len(farthest) == 0:
            break
        #go thru list of farthest nodes and travel 1 more.
        for i in range(len(farthest)):
            curr_node = farthest.pop()
            jump_dist = rjm_array[curr_node[0]][curr_node[1]]
            up = (curr_node[0] - jump_dist, curr_node[1])
            down = (curr_node[0] + jump_dist, curr_node[1])
            left = (curr_node[0], curr_node[1] - jump_dist)
            right = (curr_node[0], curr_node[1] + jump_dist)
           
            # if the jump is valid and we haven't visited it yet, set the depth to be + 1
            if in_bounds(up, n):
                if dist[up[0]][up[1]] is None:
                    dist[up[0]][up[1]] = depth + 1
            if in_bounds(down, n):
                if dist[down[0]][down[1]] is None:
                    dist[down[0]][down[1]] = depth + 1
            if in_bounds(left, n):
                if dist[left[0]][left[1]] is None:
                    dist[left[0]][left[1]] = depth + 1
            if in_bounds(right, n):
                if dist[right[0]][right[1]] is None:
                    dist[right[0]][right[1]] = depth + 1
        print("depth "+str(depth))
        # print_arr(dist)
        depth+=1
    
    return dist




the_input = input("Rook Jumping Maze size (5-10)?: ")
# stupid casting lol, other it gives type errors
grant = make_maze(int(the_input),int(the_input))
print(grant)
print(solve_maze(grant, int(the_input)))


#knapsack problem?
# is this using a DP method?
# Sample Transcripts:
# 2 2 2 4 3
# 2 2 3 3 3
# 3 3 2 3 3
# 4 3 2 2 2
# 1 2 1 4 0
# Moves from start:
# 0 3 1 4 2
# 7 5 5 6 4
# 1 4 2 2 3
# 5 6 4 -- 3
# -- 4 3 4 5
# -5