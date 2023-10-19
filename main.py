import random
board =[["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
array = ["x","0","*", "+"]

for i in range (0,5):
    for j in range (0,5):
        randomchar = random.choice(array)
        board[i][j]= randomchar
for i in board:
    print(i)


temp = ["_","_","_","_","_"]
pair_count = 1

for i in range(0,5):
    for j in range(0,5):
        if board[i][j] == "x":
            temp[j]= "x"
        else:
            temp[j] = "_"
    for k in range(0, 4):

        if temp[k] == temp[k + 1] and temp[k] != "_":

            pair_count = pair_count + 1
    print(temp)



print(pair_count)







