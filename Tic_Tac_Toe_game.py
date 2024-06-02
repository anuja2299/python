def game_start():
    a = False
    b = False
    player = 'a'
    result = choose(player,position,mark)
    while result == 'y':
        if player == 'a':
            clear_output()
            print(position)
            player = 'b'
            result = choose(player,position,mark)
        else:
            clear_output()
            print(position)
            player = 'a'
            result = choose(player,position,mark)
    print("game finished !!!")
    
    
    #function used to choose the position and mark from the user
def choose(player,position,mark):
    result = cposition(player,position)
    return result
    
    
    #function to take the position in the board from the user
def cposition(player,position):
    row = ['0','1','2']
    col = ['2','1','0']
    user_row = 'nil'
    user_col = 'nil'
    print("chance of the player : {}".format(player))
    while user_row not in row:
        user_row = input("enter the row of the position 0 or 1: ")
        
    while user_col not in col:
        user_col = input("enter the col of the position 1 or 0: ")
    result = cmark(player,user_row,user_col)
    return result
    
    
    #function used to take the mark to make a change in the board
def cmark(player,row,col):
    mark=['*','o']
    user_mark = 'nil'
    while user_mark not in mark:
        user_mark = input("enter the mark * or o: ")
    row = int(row)
    col = int(col)
    position[row][col] = user_mark
    print("{} changed into {} at the position {}{}".format(player,user_mark,row,col))
    print(position)
    result = finish(player)
    return result
    
    # function used to decide whether or not to stop the game
def finish(player):
    r = ['y','n']
    result = 'nil'
    while result not in r:
        result = input("would you like to continue : y or n: ")
    return result
    
    
from IPython.display import clear_output
position = ['','',''],['','',''],['','','']
mark = ['*','o']
game_start()
