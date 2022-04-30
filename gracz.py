import pygame
from mapa import *
from constant import *
from grafiki import *

gracz_font_20=pygame.font.Font('arial.ttf',32)
class gracz:
    def __init__(self):
        self.pola = [1]*MAX_PLAYER_SIZE             #Tablica przechowujaca id zajetych pul
        self.size = 0                               #liczba zajetych pól
        self.punkty = 0                             #zgromadzone punkty, wydawane na kupowanie nowych pól i rozwuj technologi
        self.id_gracza=1                            ##to jest do poprawienia, może nie będzie potrzebne, może będzie tablica graczy, ciort wie

    def draw(self):                                 ##Rysujemy zaanektowane przez gracza pola ;)
        i = 0
        while i < self.size:
            draw_hex(bufor_mapy3, (191, 57, M[self.pola[i]].level*25), M[self.pola[i]].x, M[self.pola[i]].y, R_kafelka)
            draw_hex_border(bufor_mapy3, (255, 0, 0), M[self.pola[i]].x, M[self.pola[i]].y, R_kafelka, 2)
            text1 = gracz_font_20.render(str(int(M[self.pola[i]].level)), True, (0, 0, 0))
            bufor_mapy3.blit(text1, (M[self.pola[i]].x+FIELD_LEVEL_POS_X, M[self.pola[i]].y+5))
            i+=1

    def increment_field_level(self):        ##podnosze poziom co runde najpierw oblicza liczbe punktow
        i=0
        while i < self.size:
            self.punkty+=int(M[self.pola[i]].level)
            i+=1
        local_flag.PLAYER_SCORE = self.punkty
        i=0
        while i< self.size:
            if M[self.pola[i]].level < 10:
                M[self.pola[i]].level += 1/M[self.pola[i]].level #taki dziwny sposób na spowolnienie rozwoju ;)
            i+=1

    def anex_field(self,id_pola,id_gracza):                ##anektujemy/zajmujemy pole dla gracza
        self.pola[self.size]=id_pola
        self.size+=1
        M[id_pola].id_gracza = id_gracza

    def is_field_anex(self,id):             ##Sprawdzamy czy pole jest anektowane przez gracza :)
        i = 0
        while i < self.size:
            if self.pola[i] == id:
                return True
            i+=1
        return False


player = gracz()

player.anex_field(50,player.id_gracza) ##gracz rozpocznie sobie na tym polu, tylko do testowania ;)


#bufor_mapy2