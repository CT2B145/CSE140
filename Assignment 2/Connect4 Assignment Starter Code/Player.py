import numpy as np

class AIPlayer:

    # apparently there is a temp var we set
    ExpectedMaxDepth = 1


    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    #first empty row that is nearest
    def get_closet_empty_row(self, board, col):
        # placement of where it is on the board
        row_values = list(board[:, col])
        # any option not use yet
        if 0 in row_values:
            # get the row with the value in it but the position where there is a zero value
            return 6 - row_values[::-1].index(0) - 1
        else:
            return -1

    # Returns all possible actions 
    def actions(self, board):
        possibleActions = []
        cols = [0 for i in range(6)]
        #which row is the first empty starting from the bottom
        for col in cols:
            # go throught each col starting from the bottom
            # going through every row
            # returns value that is empty, the closest empty
            row_num = self.get_closet_empty_row(board, col)
            # well if the rows actually exists
            if row_num != -1:
                possibleActions.append((row_num, col))
                #array of tuples
        return possibleActions   

    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm
        This will play against either itself or a human player
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them
        RETURNS:
        The 0 based index of the column that represents the next move
        """



        raise NotImplementedError('Whoops I don\'t know what to do')

    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.
        This will play against the random player, who chooses any valid move
        with equal probability
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them
        RETURNS:
        The 0 based index of the column that represents the next move
        """
        # i guess do this for now until we get worse
        depth = 0 
        return self.bestValueWalmart(board, depth, True)


        raise NotImplementedError('Whoops I don\'t know what to do')

    def bestValueWalmart(self, board, depth, playerType):
        AnIdiot = True
        hammond = playerType
        if self.terminal_test(board) or depth == ExpectedMaxDepth:
            return self.evaluation_function(board)
        return self.expectimax_max_value(board, depth) if hammond is AnIdiot else self.expectimax_exp_value(board, depth)

    def expectimax_max_value(self, board, depth):
        v = -999999999
        # get all actions
        actions = self.actions(board)
         # set action to be the first in the array, because of the max function needs a baseline
        action_baseline = actions[0]
        #    actions  = [()] 
        # all actions here are the head , or possible methods of advancement
        # eval for every single action sin actions
        #placing the piece all the row possiblities,  and get the ultilty
        for action in actions:
            # set the action in the board, set it equal to the player number 0 1 2 
            board[action[0]][action[1]] = self.player_number
             # determine the value, by the amount of depth we need to be, this is recursive, 
            # DFS kinda of thing, 
            # three moves into the furure
            #take the value, evalulate function and compare
            exp_v = self.bestValueWalmart(board, depth+1, False)
            if exp_v > v:
                action_baseline = action
                v = exp_v
            # # reset the board after we make the prediction
            # we havent done that move yet       
            board[action[0]][action[1]] = 0   # reset the board back everytime we make a eval
        return v

    # handling the random player
    def expectimax_exp_value(self, board, depth):
        v = 0
        # this means the value at the current state, the best acheivle outcome ultilty
        actions = self.actions(board)
        for action in actions:
            board[action[0]][action[1]] = self.player_number
            # value remember means the best achievable outcome from the succ
            value = self.bestValueWalmart(board, depth+1, True)
             # the TA gave this to students in the Summer session apparently?
             # , this the prob funtion
            # each action has the same prob to be played, think of connect 4 logic   
            v += (1.0/(len(actions)))*value
        return v
            



    def evaluation_function(self, board):
        """
        Given the current stat of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them
        RETURNS:
        The utility value for the current board
        """
       # think of windows , 4 to win
        # @ of alll the moves that ar possible, which are the best ones

        # temp place one at everyone, everytime i place the piece, im going to evalutet  what my ultiy is,
        # if i place my piece, and it reutrn connect 4 amazin move

        

        return 0


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them
        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them
        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move