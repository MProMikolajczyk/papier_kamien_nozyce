#!/usr/bin/env python
#-*- coding: utf-8 -*-

                                        #zdefiniowanie zbioru
zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}

                                        #Polecenie gry
print('Wybierz 1 lub 2 albo 3')

                                        #zdefiniowanie wyborów player1
class class_player_one():
    wybor_player1 = []
    powtorzenia = 0
    def __init__(self):
        self.player1=input()


    def player1_wariant_wyboru(self):
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
            return p1.komunikaty_dla_else()

                                        #komunikaty dla różnych wyników else
    def komunikaty_dla_else(self):
        if self.powtorzenia==0:
            print('Nie ma takiej możliwości wybierz 1, 2 lub 3')
        elif self.powtorzenia==1:
            print('Czytaj masz wybrać z kalawiatury numerycznej 1 lub 2 lub 3')
        elif self.powtorzenia >1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        self.powtorzenia += 1
        class_player_one().player1_wariant_wyboru()


p1=class_player_one()
p1.player1_wariant_wyboru()
print(p1.wybor_player1)


