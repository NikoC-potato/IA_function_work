import random
board =[["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
array = ["x","0","*", "+"]

for i in range (0,5):
    for j in range (0,5):
        randomchar = random.choice(array)
        board[i][j]= randomchar
for i in board:
    print(i)

pair_count = 0

for i in range(0,5):
    for j in range(0,4):
        if board[i][j] == board[i] [j+1]:
            pair_count = pair_count + 1
            print(board[i][j],board[i] [j+1], "pair found at ", i,j)
            print("pairs found so far row",pair_count)


print("========================")
for i in range(0,4):
    for j in range(0,5):
        if board[i][j] == board[i+1] [j]:
            pair_count = pair_count + 1
            print(board[i][j],board[i+1] [j], "pair found at ", i,j)
            print("pairs found so far row",pair_count)














#userinput = input("GIVE ME X and Y").split(",")









