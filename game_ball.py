def ball_guessing(list,ball,position):
    from random import shuffle
    shuffle(list)
    if position > len(list)-1:
        print("invalid guess")
    else:
        if list[ball]== list[position]:
            print("currect guess")
        else:
            print("incorrect guess")
list = [1,2,3,4,5,6,7]
ball_guessing(list,3,2)
