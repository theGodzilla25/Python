'''
author: thegodzilla25
dated: 10.09.2019
program: tictactoe

'''
from random import randint

def initialiseBoard():
    print('Following is the board and the respective positions.\nEnter the row and column separated by a space to play.')
    board=[['' for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            print('[{0},{1}] '.format(i+1,j+1),end='')
        print()
    return board  

def inputBoard(board,turn,play):
    print()
    if play=='player':
        if turn%2==0:
            print('X player turn, enter your position ',end='')
        else:
            print('O player turn, enter your position ',end='')
        x,y = map(int, input().split(' '))
        if x>3 or y>3 or x<1 or y<1:
            print("Enter valid position")
            return True
    if play=='ai':
        print('Computer entered its position ')
        while True:
            x=randint(1,3)
            y=randint(1,3)
            if board[x-1][y-1]=='':
                break
    i=x-1
    j=y-1
    if board[i][j]!='':
        print("Enter row and column that hasnt already been chosen.")
        return True
    if turn%2==0:
        board[i][j]='X'
    else:
        board[i][j]='O'
    return    

def checkWin(board,ch,play):
    for i in range(3):
        if board[i][0]==ch and board[i][1]==ch and board[i][2]==ch:
            if play=='player':
                print('Player ',ch,' Wins!')
            if play=='ai':
                print('Computer wins!')
            return True
    for i in range(3):
        if board[0][i]==ch and board[1][i]==ch and board[2][i]==ch:
            if play=='player':
                print('Player ',ch,' Wins!')
            if play=='ai':
                print('Computer wins!')
            return True 
    if (board[0][0]==ch and board[1][1]==ch and board[2][2]==ch) or (board[0][2]==ch and board[1][1]==ch and board[2][0]==ch):
            if play=='player':
                print('Player ',ch,' Wins!')
            if play=='ai':
                print('Computer wins!')
            return True 
    else:
        return False

print('Welcome to Tic Tac Toe.\nLets begin!')
while 1:
    choice=input("Select option\n1)Play against another player\n2)Play against computer\n3)Exit\n")
    if choice not in ['1','2','3']:
        print("Please enter valid option")
        continue
    else:
        break
while(choice!='3'):
    while True:
        board=initialiseBoard() 
        print("X plays first")
        turn=0
        while turn<9:
            if choice=='1':
                if(inputBoard(board,turn,'player')):
                    continue
            elif choice=='2' and turn%2==0:
                if(inputBoard(board,turn,'player')):
                    continue
            elif choice=='2' and turn%2==1:
                if(inputBoard(board,turn,'ai')):
                    continue
            for i in range(3):
                for j in range(3):
                    if board[i][j]=='':
                        print('[   ]',' ',end='')
                    else:    
                        print('[',board[i][j],']',' ',end='')
                print()    
            if turn%2==0:
                if(checkWin(board,'X','player')):
                    break
            if turn%2==1 and choice=='1':
                if(checkWin(board,'O','player')):
                    break
            if turn%2==1 and choice=='2':
                if(checkWin(board,'O','ai')):
                    break         
            turn=turn+1
            if turn==9:
                print("Its a draw! Everybody sucks!")
        x=input("Want to play again? Press 1 for yes, anything else to exit out.")
        if x=='1':
            break
        else:
            print("Thank you for playing!")
            exit()
    choice=input("Select option\n1)Play against another player\n2)Play against computer\n3)Exit\n")

