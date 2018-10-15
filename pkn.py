#!/usr/bin/env python
#-*- coding: utf-8 -*-

#zdefiniowanie zbioru
zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}

#Polecenie gry
print('Wybierz 1 lub 2 albo 3')

#zdefiniowanie wyboru player1
wybor_player1=[]
def player1_input():
    player1=input()
    if player1=='1':
        z=zbior[1]
        print('Wybrałeś:',z)
        return wybor_player1.append(z)
    elif player1=='2':
        z=zbior[2]
        print('Wybrałeś:', z)
        return wybor_player1.append(z)
    elif player1=='3':
        z=zbior[3]
        print('Wybrałeś:', z)
        return wybor_player1.append(z)
    else:
        print('Nie ma takiej możliwości wybierz 1, 2 lub 3')
        player1_input()
player1_input()










