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
def impossibleYes(curr_node, length):
    if curr_node[0] < 0 or curr_node[1] < 0:
        return False
    if curr_node[0] >= length or curr_node[1] >= length:
        return False
    return True


def solve_maze(board,length: int):

    frontier = []
    explored = []
    # dist =  np.empty((length, length))
    dist = [None] * length
    for i in range(length):
        dist[i] = [None] * length
    dist[0][0] = 0
    depth = 0

    # frontier.append(board[0][0])
    while True:
        connected_nodes = []
        # if frontier is None:
        #     break;

        # current_node = frontier.pop(0)
        # if current_node not in explored:
            # explored.append(current_node)
        #get the front node
        #do an iterative search to find nodes farthest traveled
        for r in range(length):
            for c in range(length):
                if dist[r][c] == depth:
                    connected_nodes.append((r, c))
        if len(connected_nodes) == 0:
            break 
        #handling the stupid tuple and checking the children
        # check if the child? nodes are in this. Return the child node if it is, or at least add it 
        print("HASMMOND!", connected_nodes)
        for node in (connected_nodes):
            curr_node = connected_nodes.pop()
            jump_dist = board[curr_node[0]][curr_node[1]] # get the array cube's value we are on now to do the jump
            # check the jumps
            up = (curr_node[0] - jump_dist, curr_node[1])
            down = (curr_node[0] + jump_dist, curr_node[1])
            left = (curr_node[0], curr_node[1] - jump_dist)
            right = (curr_node[0], curr_node[1] + jump_dist)


            # if the jump is valid and we haven't visited it yet, set the depth to be + 1
            if impossibleYes(up,length):
                if dist[up[0]][up[1]] is None:
                    dist[up[0]][up[1]] = depth + 1
            if impossibleYes(down, length):
                if dist[down[0]][down[1]] is None:
                    dist[down[0]][down[1]] = depth + 1
            if impossibleYes(left, length):
                if dist[left[0]][left[1]] is None:
                    dist[left[0]][left[1]] = depth + 1
            if impossibleYes(right, length):
                if dist[right[0]][right[1]] is None:
                    dist[right[0]][right[1]] = depth + 1
            # print(dist)
            depth+=1
            # if node not in frontier or node.ID not in explored:
            #     frontier.append(node)

            # again based off the psuedocode
            # print(frontier, "        explore:", explored)
            # children = [i for i, item in enumerate(current_node.connected_nodes) if item[0] == node]
            # if children == True:
            #     explored.append(children)
            # else:
            #     explored[children[0].ID] = (node, current_node)
            #     break
                # explored.append(node.ID)
            # as per psuedo code
            # # if node not in frontier or node.ID not in explored:
            #     # add to frontier before checking if children are the end result. Otherwise the node will not be added to explore.
            #     frontier.append(node)
            #     if node.ID == goal_node:
            #         # explored.append(node.ID)
            #         break

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