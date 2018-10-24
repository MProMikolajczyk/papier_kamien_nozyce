#author: Marek Mikołajczyk
# Typowa gra papier/kamień/nożyce z kometarzami

#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
import time
#------------------------------zdefiniowanie zbioru----------------------------------------

zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}

#----------------------------zdefiniowanie wyborów player1----------------------------------

class class_player_one():
    wybor_player1 = []
    powtorzenia_palyer1 = 0
                                #komentarz pocztokowy dla player1
    def palyer1_wstep_do_gry(self):
        print('PLAYER 1'+'\n'+'Wybierz 1:PAPIER lub 2:KAMIEŃ albo 3:NOŻYCE')
                                #dodanie do zbioru wyboru player1
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

                                    #komunikaty dla różnych nieudanych prób wpisania przez palyer1 1,2,3
    def komunikaty_dla_else(self):
        if self.powtorzenia_palyer1==0:
            print('Nie ma takiej możliwości wybierz 1:PAPIER, 2:KAMIEŃ lub 3:NOŻYCE')
        elif self.powtorzenia_palyer1==1:
            print('Czytaj masz wybrać z kalawiatury numerycznej 1 lub 2 lub 3')
        elif self.powtorzenia_palyer1 >1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        self.powtorzenia_palyer1 += 1
        class_player_one().player1_wariant_wyboru()
                                    #ilość powtórzeń klasy
    def liczba_powtorzen(self): #wprowadzone dla stworzenia specjanego kometarza
        return self.powtorzenia_palyer1
                                    #kompresja funkcji player1 ponownego wyboru
    def powtorny_wybor_palyer1(self):
        p1.palyer1_wstep_do_gry()
        p1.player1_wariant_wyboru()

#--------------------------zdefiniowanie wyborów player2-----------------------------------

class class_player_two():
    wybor_player2 = []
    powtorzenia_palyer2 = 0

                                 # komentarz pocztokowy dla player2
    def palyer2_wstep_do_gry(self):
        print('\n'+'PLAYER 2''\n'+'Wybierz 1:PAPIER lub 2:KAMIEŃ albo 3:NOŻYCE')
                                 # dodanie do zbioru wyboru player2
    def player2_wariant_wyboru(self):
        player2 = input()
        if player2 == '1':
            z = zbior[1]
            print('Wybrałeś:', z)
            self.wybor_player2.clear()
            return self.wybor_player2.append(z)
        elif player2 == '2':
            z = zbior[2]
            print('Wybrałeś:', z)
            self.wybor_player2.clear()
            return self.wybor_player2.append(z)
        elif player2 == '3':
            z = zbior[3]
            print('Wybrałeś:', z)
            self.wybor_player2.clear()
            return self.wybor_player2.append(z)
        else:
            return p2.komunikaty_dla_else()

                                    # komunikaty dla różnych nieudanych prób wpisania przez palyer2 1,2,3
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
                                        #ilość powtórzeń klasy
    def liczba_powtorzen(self):         #wprowadzone dla stworzenia specjanego kometarza
        return self.powtorzenia_palyer2

#--------------------------zdefiniowanie wyborów palyer_komp-----------------------------------

class player_komputer():
    def __init__(self):
        self.los_koputera=[]
                            # komentarz dla player_komp
    def wywolanie_wyborow_kompa(self):
        print('\n'+'KOMPUTER')
        p_komp.wybory_komputera()
        print('Wybrał: ' + p_komp.koncowy_wybor()[0])
                             # dodanie do zbioru wyboru player_komp
    def wybory_komputera(self):
        wybory_komp = random.randint(1, len(zbior))
        self.los_koputera.clear()
        return self.los_koputera.append(zbior[wybory_komp])
                            # koncowy wybor player_komp == wyborowi
    def koncowy_wybor(self): #bez tego w komentarzu pojawia się kolejny losowy wybor player_komp
        return self.los_koputera

#---------------------------------------Przebieg gry-----------------------------------------------
class rozgrywka():
    def __init__(self):
        self.zwyciestwa_player1=0
        self.zwyciestwa_player2=0
        self.zwyciestwa_komp=0
        self.remis_player1=0
        self.remis_player2=0
        self.remis_komp=0

                            #Mechanika gry. Zależności pomiędzy wyborami
    def mechanika_gry(self):
        # przypadek remisu
        if p1.wybor_player1 == p_komp.koncowy_wybor() or p1.wybor_player1 == p2.wybor_player2:
            print('\n' + 'REMIS')
            if p1.wybor_player1 == p_komp.koncowy_wybor():
                self.remis_player1+=1
                self.remis_komp+=1
            if p1.wybor_player1 == p2.wybor_player2:
                self.remis_player1+=1
                self.remis_player2+=1

        # przypadek PAPIER I KAMIEŃ
        elif p1.wybor_player1 == ['PAPIER'] and p2.wybor_player2 == ['KAMIEŃ'] or \
                                p1.wybor_player1 == ['PAPIER'] and p_komp.koncowy_wybor() == ['KAMIEŃ']:
            print('\n' + 'Wygrywa PLAYER 1')
            self.zwyciestwa_player1+=1 #dodanie do zwyciestwa

        elif p1.wybor_player1 == ['KAMIEŃ'] and p2.wybor_player2 == ['PAPIER'] or \
                                p1.wybor_player1 == ['KAMIEŃ'] and p_komp.koncowy_wybor() == ['PAPIER']:
            if p2.wybor_player2:
                print('\n' + 'Wygrywa PLAYER 2')
                self.zwyciestwa_player2 += 1 #dodanie do zwyciestwa
            if p_komp.koncowy_wybor():
                print('\n' + 'Wygrywa KOMPUTER')
                self.zwyciestwa_komp+=1 #dodanie do zwyciestwa

                # przypadek PAPIER I NOŻYCE
        elif p1.wybor_player1 == ['PAPIER'] and p2.wybor_player2 == ['NOŻYCE'] or \
                                p1.wybor_player1 == ['PAPIER'] and p_komp.koncowy_wybor() == ['NOŻYCE']:
            if p2.wybor_player2:
                print('\n' + 'Wygrywa PLAYER 2')
                self.zwyciestwa_player2 += 1 #dodanie do zwyciestwa
            if p_komp.koncowy_wybor():
                print('\n' + 'Wygrywa KOMPUTER')
                self.zwyciestwa_komp += 1 #dodanie do zwyciestwa

        elif p1.wybor_player1 == ['NOŻYCE'] and p2.wybor_player2 == ['PAPIER'] or \
                                p1.wybor_player1 == ['NOŻYCE'] and p_komp.koncowy_wybor() == ['PAPIER']:
            print('\n' + 'Wygrywa PLAYER 1')
            self.zwyciestwa_player1 += 1 #dodanie do zwyciestwa

        # przypadek KAMIEŃ I NOŻYCE
        elif p1.wybor_player1 == ['KAMIEŃ'] and p2.wybor_player2 == ['NOŻYCE'] or \
                                p1.wybor_player1 == ['KAMIEŃ'] and p_komp.koncowy_wybor() == ['NOŻYCE']:
            print('Wygrywa PLAYER 1')
            self.zwyciestwa_player1 += 1 #dodanie do zwyciestwa

        elif p1.wybor_player1 == ['NOŻYCE'] and p2.wybor_player2 == ['KAMIEŃ'] or \
                                p1.wybor_player1 == ['NOŻYCE'] and p_komp.koncowy_wybor() == ['KAMIEŃ']:
            if p2.wybor_player2:
                print('Wygrywa PLAYER 2')
                self.zwyciestwa_player2 += 1 #dodanie do zwyciestwa
            if p_komp.koncowy_wybor():
                print('Wygrywa KOMPUTER')
                self.zwyciestwa_komp += 1 #dodanie do zwyciestwa

        p1.wybor_player1.clear()
        p2.wybor_player2.clear()
        p_komp.koncowy_wybor().clear()
                                #Graj ponownie
    def graj_ponownie(self):
        print('\n' + 'Grasz jeszcze raz ? (T/N/Z)' + '\n\tHelp: '+'\n\tT=Zagraj ponownie, N=Koniec, Z=Zmiana trybu gry' )  # Trzeba dodadać jeszcze zmień gracza i żeby się komnatrze początkowe nie pojawiały
        graj_ponownie_input = input().upper()
        if graj_ponownie_input=='T':
            p1.powtorzenia_palyer1=0 #restart ilosci powtorzen klasy palyer1 - dotyczy kometarzy
            p2.powtorzenia_palyer2=0 #restart ilosci powtorzen klasy palyer2 - dotyczy kometarzy
            return True
        if graj_ponownie_input=='N':
            self.gratulacje()
            return False
        if graj_ponownie_input=='Z':
                self.wyswietlenie_pierwszych_kometarzy_i_mechaniki()
                self.wyswietlenie_kontarzy_dalszej_gry_i_mechanika()
        else:
            self.wyswietlenie_kontarzy_dalszej_gry_i_mechanika()
                                #Wstęp do gry
    def wyswietlenie_pierwszych_kometarzy_i_mechaniki(self):
        p1_vs_p2_vs_komp.pierwsze_kometarze()
        self.mechanika_gry()
        self.licznik_zwyciestw()
                                #Gra każda następna
    def wyswietlenie_kontarzy_dalszej_gry_i_mechanika(self):
        while self.graj_ponownie() == True:
            p1_vs_p2_vs_komp.wybory()
            self.mechanika_gry()
            self.licznik_zwyciestw()
                                #licznik ile razy kto wygral
    def licznik_zwyciestw(self):
        print('\n'+'Statystki gier :')
        print("Player1: "+str(self.zwyciestwa_player1) +'\t'+'Remisów: '+str(self.remis_player1))
        print("Player2: "+str(self.zwyciestwa_player2) + '\t'+'Remisów: '+str(self.remis_player2))
        print("Komputer: "+str(self.zwyciestwa_komp) + '\t' +'Remisów: '+str(self.remis_komp))
                                #Podziękowanie dla gracza
    def gratulacje(self):
        if self.zwyciestwa_player1 > self.zwyciestwa_komp:
            print("Gratuluje wygrałeś z komputerem")
        elif self.zwyciestwa_player1 > self.zwyciestwa_player2:
            print("Player1 był lepszy od Player2 ")
        elif self.zwyciestwa_player2 > self.zwyciestwa_player1:
            print("Player2 był lepszy od Player1 ")
        else:
            print("Następnym razem pójdzie ci lepiej")
        time.sleep(3)
#---------------------------------------Wybór graczy---------------------------------------------------
class player1_or_palayer2_or_komputer():

    wybor_palyerow=[]
                                    #kometarze przy wyborze graczy
    def pierwsze_kometarze(self):
        print('\n'+'WYBIERZ: ' + '\n')
        print('Gra przeciwko koputerowi naciśnij: 1')
        print('Gra multiplayer naciśnij: 2')
        return p1_vs_p2_vs_komp.dodawanie_do_listy_wybor_palyerow()
                                    #kometarz poajwiający się za każdym razem gdy nie wybierze sie 1 lub 2
    def kometarz_powtarzany_ciagle(self):
        print('Wybierz 1 lub 2')
        return p1_vs_p2_vs_komp.dodawanie_do_listy_wybor_palyerow()
                                    #dodawanie i czysczenie zbioru wybor_playerow
    def dodawanie_do_listy_wybor_palyerow(self):
        input_player=input()
        self.wybor_palyerow.clear()
        self.wybor_palyerow.append(input_player)
        return p1_vs_p2_vs_komp.wybory()
                                    #wybor palyerow
    def wybory(self):
        if self.wybor_palyerow==['2']:
                                    # wybor palyer1
            p1.powtorny_wybor_palyer1()

                                    # wybor palyer2
            p2.palyer2_wstep_do_gry()
            p2.player2_wariant_wyboru()
        elif self.wybor_palyerow==['1']:
                                    # wybor palyer1
            p1.powtorny_wybor_palyer1()
            p_komp.wywolanie_wyborow_kompa() # wybor palyer_komp
        else:
            p1_vs_p2_vs_komp.kometarz_powtarzany_ciagle()


#-----------------------------Wywolanie class--------------------------------------
p1 = class_player_one() #zdefiniowana klasa player1
p2 = class_player_two() #zdefiniowana klasa player2
p_komp = player_komputer() #zdefiniowana klasa palyer_komp
p1_vs_p2_vs_komp=player1_or_palayer2_or_komputer() #zdefiniowana klasa wyboru graczy
wywyowanie_gry=rozgrywka() #zdefiniowanie klasyy rozgrywki

#-------------------------------------Wywolanie gry----------------------------------------------
wywyowanie_gry.wyswietlenie_pierwszych_kometarzy_i_mechaniki()
wywyowanie_gry.wyswietlenie_kontarzy_dalszej_gry_i_mechanika()
