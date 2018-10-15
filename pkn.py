#!/usr/bin/env python
#-*- coding: utf-8 -*-

#zdefiniowanie zbioru
zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}

#Polecenie gry
print('Wybierz 1 lub 2 albo 3')

#zdefiniowanie wyboru player1
class class_player_one():
    wybor_player1 = []
    def __init__(self):
        self.player1=input()

    def player1_wariant(self):
        if self.player1=='1':
            z=zbior[1]
            print('Wybrałeś:',z)
            return self.wybor_player1.append(z)
        elif self.player1=='2':
            z=zbior[2]
            print('Wybrałeś:', z)
            return self.wybor_player1.append(z)
        elif self.player1=='3':
            z=zbior[3]
            print('Wybrałeś:', z)
            return self.wybor_player1.append(z)
        else:
            print('Nie ma takiej możliwości wybierz 1, 2 lub 3')
            class_player_one().player1_wariant()


p1=class_player_one()
p1.player1_wariant()
print(p1.wybor_player1)


