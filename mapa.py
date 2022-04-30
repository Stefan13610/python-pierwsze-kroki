import pygame
import random
from array import *
from constant import *

class kafelek:
    def __init__(self, r, g, b, x,y,id_tekstury):  # parametry koloru, pozycja, trochę dużo biorąc pod uwagę puźniejsze potrzebne parametry ;/
        self.r = r                      ##Promień
        self.g = g                      ##kolory RGB
        self.b = b
        self.x = x                      ##pozycja X,Y
        self.y = y
        self.level = 1                  ##Poziom pola
        self.id_tekstury = id_tekstury
        self.id_gracza = -1             ## id gracza do którego należy pole, nie wiem czy id to dobry pomysł, zobaczymy ;/


# tworzymy tablice kafelków
M = [kafelek(0, 0, 0, 0, 0,0)] * map_x_size * (map_x_size + 1)


def create_map():
    #print("test")

    p = 0 ##id/pozycja w tablicy
    r = 0 ##składowe rgb koloru kafelka
    g = 0
    b = 0
    # ustawiam wspulzedne pierwszego kafelka
    x1 = 1
    y1 = (R_kafelka - 1) / 2

    i = 0
    while i < map_x_size: ##generowanie parametrów mapy

        j = 0
        x = 0 #początkowa pozycja x (mapa jest rysowana od lewej do prawej i od fóry do dołu )
        if i % 2 == 1:  ##co drugi kafelek jest przesunięty o polowe długości kafelka
            x += R_kafelka * 1.72 / 2
        y = R_kafelka * 1.5 * i + R_kafelka / 2 #obliczamy pozycję y w danej iteracji
        while j < map_y_size:
            p = r + 256 * g + 65536 * b ## id jest wyznaczane zamieniając wpułżedną wektorową na skalar, mądrze brzmi ;)

            id_tekstury=random.randint(0,5)
            M[p] = kafelek(r, g, b, x, y, id_tekstury ) ##zapisujemy parametry kafelka, trzeba będzie tu puźniej sporo dorzucić ;/
            ##print("i=" + str(i) + " j=" + str(j) + " p=" + str(p));
            x += R_kafelka * 1.72; #obliczamy pozycię x kolejnego kafelka
            r += 1
            if r > 255:
                r = 0
                g += 1
                if g > 255:
                    g = 0
                    b += 1
            j += 1
        i += 1