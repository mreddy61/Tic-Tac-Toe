import pygame
import sys

pygame.init()
from pygame.locals import*
screen = pygame.display.set_mode((400,300))
pygame.image.load('d:/myfolder/python/Tic_Tac_Toe.png')
pygame.display.update()

board=[' ']*10
a=' '
player_win=False
def display_board(board):
    print ("-------------")
    print ("| "+board[1]+" | "+board[2]+" | "+board[3]+" |")
    print ("-------------")
    print ("| "+board[4]+" | "+board[5]+" | "+board[6]+" |")
    print ("-------------")
    print ("| "+board[7]+" | "+board[8]+" | "+board[9]+" |")
    print ("-------------")
display_board(board)
def win_check():
    win_check=True
    z=0
    global board
    global a
    global player_win
    for i in range(1,10):
        if board[i]==' ':
            z+=1
    if player_win==False:
        if board[1]==board[5]==board[9]:
            a=board[1]
        elif board[1]==board[2]==board[3]:
            a=board[1]
        elif board[1]==board[4]==board[7]:
            a=board[1]
        elif board[4]==board[5]==board[6]:
            a=board[4]
        elif board[2]==board[5]==board[8]:
            a=board[2]
        elif board[3]==board[6]==board[9]:
            a=board[3]
        elif board[9]==board[8]==board[7]:
            a=board[7]
        elif board[3]==board[5]==board[7]:
            a=board[3]
    if (z==0 and player_win==False):
        print("Board full: Play Another Game")
        player_win=True
    if a=='x':
        print ("Player 1 Won")
        player_win=True
    elif a=='o':
        print ("Player 2 Won")
        player_win=True
b=1
def player_input():
    global board
    global b
    win_check()
    while ((a!='x' and a!='o')==True):
        win_check()
        if player_win:
            break
        elif b%2==1:
            position=input('Enter the position of player1:')
            position=int(position)
            if position>9:
                print("Position value should be less than 10")
                display_board(board)
                player_input()
            elif board[position]!=' ':
                print("Position already filled, Enter new position")
                display_board(board)
                player_input()
            else:
                board[position]='x'
                b+=1
                display_board(board)
        else:
            position=input('Enter the position of player2:')
            position=int(position)
            if position>9:
                print("Position value should be less than 10")
                player_input()
            elif(board[position]!=' '):
                print("Position already filled, Enter new position")
                display_board(board)
                player_input()
            else:
                board[position]='o'
                b+=1
                display_board(board)
player_input()
