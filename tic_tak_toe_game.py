# def sum(x,y,z):
#     return x+y+z
# def board(player1,player2):
#     zero='X' if player1[0] else ('0' if player2[0] else 0)
#     one='X' if player1[1] else ('0' if player2[1] else 1)
#     two='X' if player1[2] else ('0' if player2[2] else 2)
#     three='X' if player1[3] else ('0' if player2[3] else 3)
#     four='X' if player1[4] else ('0' if player2[4] else 4)
#     five='X' if player1[5] else ('0' if player2[5] else 5)
#     six='X' if player1[6] else ('0' if player2[6] else 6)
#     seven='X' if player1[7] else ('0' if player2[7] else 7)
#     eight='X' if player1[8] else ('0' if player2[8] else 8)

#     print(f"{zero} | {one} | {two} ")
#     print(f"--|---|---")
#     print(f"{three} | {four} | {five} ")
#     print(f"--|---|---")
#     print(f"{six} | {seven} | {eight}")
#     print(f"--|---|---")

# def check(player1,player2):
#     winner = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#     for x in winner:
#         if(sum(player1[winner[0]],player1[winner[1]],player1[winner[2]])==3):
#             print("X won the match")
#             return 1
#         if(sum(player2[winner[0]],player2[winner[1]],player2[winner[2]])==3):
#             print("0 won the match")
#             return 0
#     return -1
# if __name__=="__main()__":
#     player1=[0,0,0,0,0,0,0,0,0]
#     player2=[0,0,0,0,0,0,0,0,0]
#     turn=1
#     print("Welcome to Tic Tak Toe")
#     while True:
#         board(player1,player2)
#         if (turn==1):
#             print("Player1 chance")
#             i=int(input("Enter a value: "))
#             player1[i] = 1
#         else:
#             print("Player2 chance")
#             i=int(input("Enter a value: "))
#             player2[i] = 1
#         c=check(player1,player2)
#         if (c!=1):
#             print("Match over")
#             break
#         turn = 1-turn
def my_sum(x, y, z):
    return x + y + z

def board(player1, player2):
    zero = 'X' if player1[0] else ('0' if player2[0] else 0)
    one = 'X' if player1[1] else ('0' if player2[1] else 1)
    two = 'X' if player1[2] else ('0' if player2[2] else 2)
    three = 'X' if player1[3] else ('0' if player2[3] else 3)
    four = 'X' if player1[4] else ('0' if player2[4] else 4)
    five = 'X' if player1[5] else ('0' if player2[5] else 5)
    six = 'X' if player1[6] else ('0' if player2[6] else 6)
    seven = 'X' if player1[7] else ('0' if player2[7] else 7)
    eight = 'X' if player1[8] else ('0' if player2[8] else 8)

    print(f" {zero}  |  {one}  |  {two} ")
    print("----|-----|----")
    print(f" {three}  |  {four}  |  {five} ")
    print("----|-----|----")
    print(f" {six}  |  {seven}  |  {eight} ")
    print("----|-----|----")

def check(player1, player2):
    winner = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in winner:
        if my_sum(player1[x[0]], player1[x[1]], player1[x[2]]) == 3:
            print("X won the match")
            return 1
        if my_sum(player2[x[0]], player2[x[1]], player2[x[2]]) == 3:
            print("0 won the match")
            return 0
    return -1

if __name__ == "__main__":
    player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while True:
        board(player1, player2)
        if turn == 1:
            print("Player1 chance")
            i = int(input("Enter a value: "))
            player1[i] = 1
        else:
            print("Player2 chance")
            i = int(input("Enter a value: "))
            player2[i] = 1
        c = check(player1, player2)
        if c != -1:
            print("Match over")
            break
        turn = 1 - turn
