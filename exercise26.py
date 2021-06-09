"""
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board.
 However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and
tell me which player won, if any. A Tic Tac Toe win is 3 in a row -
 either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	          [2, 1, 0],
	          [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	          [2, 1, 0],
	          [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                	[2, 1, 0],
	                [2, 1, 1]]

no_winner =        [[1, 2, 0],
	               [2, 1, 0],
	               [2, 1, 2]]

also_no_winner =  [[1, 2, 0],

             	  [ 2, 1, 0],
                 [2, 1, 0]]  """
def checker(data):
    for i in range(3):
        if data[i][0] ==data[i][1] ==data[i][2]:  # it will check for horizontal values
            return data[i][0]

        elif data[0][i] == data[1][i] == data[2][i]:# it will check for vertical values
            return data[0][i]
        else:
            pass  # it will not print anything if nobody get any rewards
def corner_check(data):

    if data[0][0] ==data[1][1]==data[2][2]:  # it will check diagonaly in this position\
        #print("\ won ")
        return data[0][0]
    elif data[2][2]==data[1][1]==[0][0]:  # it will check diagonaly in this position/
        #print("/ this won")
        return data[2][2]
    else:
        check=checker(data)
        return check
if __name__=="__main__":
    dat=[[2, 2, 0],
    	          [2, 1, 0],
    	          [2, 1, 1]]

    print("checking it")
    winner=corner_check(dat)
    if winner ==1:print("Player1 won ")
    elif winner ==2:print("PLayer2 won")
    else:print("nobody won the match ::)))))")
### done
#link>>https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
