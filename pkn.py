#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
                                        #zdefiniowanie zbioru
zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}
                                        #zdefiniowanie wyborów player1
class class_player_one():
    wybor_player1 = []
    powtorzenia_palyer1 = 0

    def palyer1_wstep_do_gry(self):
        print('PLAYER 1'+'\n'+'Wybierz 1:PAPIER lub 2:KAMIEŃ albo 3:NOŻYCE')

    def player1_wariant_wyboru(self):
        player1 = input()
        if player1=='1':
            z=zbior[1]
            print('Wybrałeś:',z)
            self.wybor_player1.clear()
            return self.wybor_player1.append(z)
        elif player1=='2':
            z=zbior[2]
            print('Wybrałeś:', z)
            self.wybor_player1.clear()
            return self.wybor_player1.append(z)
        elif player1=='3':
            z=zbior[3]
            print('Wybrałeś:', z)
            self.wybor_player1.clear()
            return self.wybor_player1.append(z)
        else:
            return p1.komunikaty_dla_else()
                                    #komunikaty dla różnych wyników else
    def komunikaty_dla_else(self):
        if self.powtorzenia_palyer1==0:
            print('Nie ma takiej możliwości wybierz 1:PAPIER, 2:KAMIEŃ lub 3:NOŻYCE')
        elif self.powtorzenia_palyer1==1:
            print('Czytaj masz wybrać z kalawiatury numerycznej 1 lub 2 lub 3')
        elif self.powtorzenia_palyer1 >1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        self.powtorzenia_palyer1 += 1
        class_player_one().player1_wariant_wyboru()

    def liczba_powtorzen(self):
        return self.powtorzenia_palyer1

    def powtorny_wybor_palyer1(self):
        p1.palyer1_wstep_do_gry()
        p1.player1_wariant_wyboru()
                                        #zdefiniowanie wyborów player2
class class_player_two():
    wybor_player2 = []
    powtorzenia_palyer2 = 0

    def palyer2_wstep_do_gry(self):
        print('\n'+'PLAYER 2''\n'+'Wybierz 1 lub 2 albo 3')

    def player2_wariant_wyboru(self):
        player2 = input()
        if player2 == '1':
            z = zbior[1]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        elif player2 == '2':
            z = zbior[2]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        elif player2 == '3':
            z = zbior[3]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        else:
            return p2.komunikaty_dla_else()
                                                # komunikaty dla różnych wyników else
    def komunikaty_dla_else(self):
        if self.powtorzenia_palyer2 == 0:
            print('Twoja kolej wybierz 1:PAPIER, 2:KAMIEŃ lub 3:NOŻYCE')
        elif self.powtorzenia_palyer2 == 1:
            print('Nie ma takiej możliwości wybierz 1:PAPIER, 2:KAMIEŃ lub 3:NOŻYCE')
        elif self.powtorzenia_palyer2 > 1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        if p1.liczba_powtorzen() >= 3 and p2.liczba_powtorzen() == 3:
            print('\n'+'Mam przyjemność z prawdziwymi głąbami')
        self.powtorzenia_palyer2 += 1
        class_player_two().player2_wariant_wyboru()

    def liczba_powtorzen(self):
        return self.powtorzenia_palyer2


class player_komputer():
    def __init__(self):
        self.los_koputera=[]

    def wywolanie_wyborow_kompa(self):
        print('\n'+'KOMPUTER')
        p_komp.wybory_komputera()
        print('Wybrał: ' + p_komp.koncowy_wybor()[0])


    def wybory_komputera(self):
        wybory_komp = random.randint(1, len(zbior))
        self.los_koputera.clear()
        return self.los_koputera.append(zbior[wybory_komp])

    def koncowy_wybor(self):
        return self.los_koputera


#Mechanika gry. Zależności pomiędzy przedmiotami
def mechanika_gry():
    pass

#Gratulacje
def gratulacje():
    pass

#Graj ponownie
def graj_ponownie():
    print('\n'+'Grasz jeszcze raz') #Wymaga wprowadzenia poprawek w zależności czy gramy jeszcze raz to samo czy nie
    return p1_vs_p2_vs_komp.pierwsze_kometarze()

#Wybór graczy
class player1_or_palayer2_or_komputer():

    wybor_palyerow=[]

    def pierwsze_kometarze(self):
        print('WYBIERZ: ')
        print('Gra przeciwko koputerowi naciśnij: 1')
        print('Gra multiplayer naciśnij: 2')
        return p1_vs_p2_vs_komp.dodawanie_do_listy_wybor_palyerow()

    def kometarz_powtarzany_ciagle(self):
        print('Wybierz 1 lub 2')
        return p1_vs_p2_vs_komp.dodawanie_do_listy_wybor_palyerow()

    def dodawanie_do_listy_wybor_palyerow(self):
        input_player=input()
        self.wybor_palyerow.clear()
        self.wybor_palyerow.append(input_player)
        return p1_vs_p2_vs_komp.wybory()

    def wybory(self):
        if self.wybor_palyerow==['2']:
                                    # wybor palyer1
            p1.powtorny_wybor_palyer1()
            print(p1.wybor_player1)         #zbiory do mechaniki gry

                                    # wybor palyer2
            p2.palyer2_wstep_do_gry()
            p2.player2_wariant_wyboru()
            print(p2.wybor_player2)     #zbiory do mechaniki gry
        elif self.wybor_palyerow==['1']:
                                    # wybor palyer1
            p1.powtorny_wybor_palyer1()
            print(p1.wybor_player1)  # zbiory do mechaniki gry
            p_komp.wywolanie_wyborow_kompa()
            print(p_komp.koncowy_wybor())  # zbiory do mechaniki gry
        else:
            p1_vs_p2_vs_komp.kometarz_powtarzany_ciagle()


# Wywolanie class + pozostalych komend
p1 = class_player_one()
p2 = class_player_two()
p_komp = player_komputer()
p1_vs_p2_vs_komp=player1_or_palayer2_or_komputer()
p1_vs_p2_vs_komp.pierwsze_kometarze()
while True:
    graj_ponownie()
