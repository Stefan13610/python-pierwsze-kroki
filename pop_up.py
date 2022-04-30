import pygame
from array import *
from button import *
from constant import *
from local_event import *
from gracz import *
##POP_UP_y i MENU
##przyciski komunikatów
BT_CLOSE = button(120, 230, 80, 40, CLOSE_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.CLOSE_BUTTON)
BT_CANCEL = button(120, 230, 80, 40, CANCEL_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.CANCEL_BUTTON)
BT_OK = button(220, 230, 80, 40, OK_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.OK_BUTTON)
BT_YES = button(300, 230, 80, 40, YES_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.YES_BUTTON)
BT_NO = button(120, 230, 80, 40, NO_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.NO_BUTTON)
BT_ANEX_FIELD = button(120, 180, 280, 40, ANEX_FIELD_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.ANEX_FIELD_BUTTON)
##zmienna sprawdzająca czy mamy jakikolwiek aktywny pop_up i zmienna przechowujaca jego id
# local_flag.POP_UP_IS_ACTIVE=True
# local_flag.ACTIVE_POP_UP_ID=0

##tworzę sobie bufor wiadomości, tablica przechowująca tekst podzielony na liniki
## i zamieniony na grafikę
wiadomosc = [font1.render("tekst_do_napisania", True, (0, 0, 0))] * 30


def create_text_image(tekst,max_lenght):  ## ta funkcja jest trochę połatana, pasowało by ją chyba przepisać jakoś sensowniej ;/

    podzielony_tekst = tekst.split()
    liczba_slow = len(podzielony_tekst)
    i = 0
    j = 0  ## to będzie liczba pasków z tekstem ;/ rysujemy je na koncu
    tekst_do_napisania = ""
    while i < liczba_slow:  ##dodaje elementy do zmiennej tekst_do_napisania i kiedy przekroczy max_length to zamieniam ją na tekst i zapisuje
        if len(tekst_do_napisania) < max_lenght:
            tekst_do_napisania = tekst_do_napisania + " " + podzielony_tekst[i]
            i = i + 1
        else:
            wiadomosc[j] = font1.render(tekst_do_napisania, True, (0, 0, 0))
            tekst_do_napisania = ""
            j = j + 1

        if i >= liczba_slow:  ## jeżeli wypisaliśmy wszytskie słowa ale nie przekroczyliśmy jeszcze długości to zamieniam to na tekst
            wiadomosc[j] = font1.render(tekst_do_napisania, True, (0, 0, 0))
            j = j + 1
    i = 0
    ##tworzę sobie obrazek o rozmiarze takim żeby mi się tekst zmiescil
    size = width, height = (max_lenght * 10 + 40, j * 30)
    ret_image = pygame.Surface(size)
    ret_image.fill((255, 255, 255))

    ##rysuje wygenerowane wczesniej paski tekstu jeden pod drugim
    while i <= j:
        wiadomosc_width = wiadomosc[i].get_width()
        wiadomosc_x = 4;
        wiadomosc_y = i * 30;
        if max_lenght * 10 + 40 > wiadomosc_width:
            wiadomosc_x = (max_lenght * 10 + 40 - wiadomosc_width) / 2
        ret_image.blit(wiadomosc[i], (wiadomosc_x, wiadomosc_y))
        i = i + 1
    # zwracam wygenerowaną tablice tekstu
    return ret_image


class pop_up:
    def __init__(self, text, type, position_x, position_y):
        self.text = text
        self.type = type
        self.position_x = position_x
        self.position_y = position_y
        size = width, height = (POP_UP_WIDTH, POP_UP_HEIGHT)
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.aktywny = 0  ##sprawdzamy czy wcisnelismy myszke na pop_up_ie
        img = create_text_image(self.text, 40)
        img_width = img.get_width()
        img_height = img.get_height()
        img_x = 4;
        img_y = 4;
        if POP_UP_WIDTH > img_width:
            img_x = (POP_UP_WIDTH - img_width) / 2
        if POP_UP_HEIGHT > img_height:
            img_y = (POP_UP_HEIGHT - 120 - img_height) / 2

        self.image.blit(img, (img_x, img_y))

    def draw(self, space, mx, my):  ##rysowanie popupu na wskazanej powierzchni
        if self.type == 1:  ## w zależności od typu będą się wyświetlać różne przyciski ;)
            BT_YES.draw(self.image)
            BT_YES.mouse_on(mx - self.position_x, my - self.position_y)
            BT_NO.draw(self.image)
            BT_NO.mouse_on(mx - self.position_x, my - self.position_y)
        if self.type == 2:
            BT_OK.draw(self.image)
            BT_OK.mouse_on(mx - self.position_x, my - self.position_y)
            BT_ANEX_FIELD.draw(self.image)
            BT_ANEX_FIELD.mouse_on(mx - self.position_x, my - self.position_y)
        if self.type == 3:
            BT_OK.draw(self.image)
            BT_OK.mouse_on(mx - self.position_x, my - self.position_y)
            #BT_ANEX_FIELD.draw(self.image)
            #BT_ANEX_FIELD.mouse_on(mx - self.position_x, my - self.position_y)
        space.blit(self.image, (self.position_x, self.position_y))

    def mouse_on(self, mx, my):
        self.aktywny = 0;
        local_flag.MOUSE_ON_POP_UP = False
        if mx > self.position_x and mx < self.position_x + POP_UP_WIDTH:
            if my > self.position_y and my < self.position_y + POP_UP_HEIGHT:
                self.aktywny = 1
                local_flag.MOUSE_ON_POP_UP = True
        if local_flag.MOUSE_CLICK_FLAG == True and local_flag.MOUSE_ON_POP_UP == True:
            self.position_x = self.position_x + (mx - local_flag.OLD_MOUSE_POS_X)
            self.position_y = self.position_y + (my - local_flag.OLD_MOUSE_POS_Y)
            local_flag.OLD_MOUSE_POS_X = mx
            local_flag.OLD_MOUSE_POS_Y = my


# testowe_okienko=pop_up("testowa dlugosc wiadomosci bo musze ogarnac jak to zrobc zeby to sie ladnie ogarnialo",2,100,100)            ## tworze testowy pop_up
Komunikaty = [pop_up("testowa dlugosc wiadomosci bo musze ogarnac jak to zrobc zeby to sie ladnie ogarnialo", 1, 100,
                     100)] * 20  ## w tej liście będą wszystkie pop_upy, tak myślę ;)
Komunikaty[1] = pop_up("Zwykle pole", 3, 200, 200)
Komunikaty[2] = pop_up("Pole nalezy do ciebie", 2, 200, 200)
Komunikaty[3] = pop_up("Pole jest za daleko zeby je zajac", 3, 200, 200)
Komunikaty[4] = pop_up("To pole już należy do ciebie", 3, 200, 200)
def rysuj_komunikaty(screen, mx, my):
    if local_flag.POP_UP_IS_ACTIVE == True:
        Komunikaty[local_flag.ACTIVE_POP_UP_ID].draw(screen, mx, my)
        Komunikaty[local_flag.ACTIVE_POP_UP_ID].mouse_on(mx, my)
    else:
        local_flag.MOUSE_ON_POP_UP = False


##czcionki do menu

menu_font_32=pygame.font.Font('arial.ttf',32)
menu_font_20=pygame.font.Font('arial.ttf',20)

##przyciski menu
BT_MENU_NEXT_RUND = button(50, 400, 180, 40, NEXT_RUND_BUTTON_DESC, (145, 189, 60), (255, 255, 135), 1, local_event.NEXT_RUND_BUTTON)

class game_menu:
    def __init__(self):
        self.position_x = MENU_POS_X
        self.position_y = MENU_POS_Y
        size = width, height = (MENU_WIDTH, MENU_HEIGHT)
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))

    def draw_menu(self,space,mx,my):
        space.blit(self.image,(self.position_x, self.position_y))
        BT_MENU_NEXT_RUND.draw(self.image)
        BT_MENU_NEXT_RUND.mouse_on(mx - self.position_x, my - self.position_y)
    def re_draw_menu(self):
        self.image.fill((255, 255, 255))
        text1=menu_font_20.render(str(RUND_DESC), True, (0, 0, 0))
        self.image.blit(text1, (50, 50))
        text1=menu_font_20.render(str(local_flag.RUND_NUMBER), True, (0, 0, 0))
        self.image.blit(text1, (190, 50))
        text1=menu_font_20.render(str(SCORE_DESC), True, (0, 0, 0))
        self.image.blit(text1, (50, 100))
        text1=menu_font_20.render(str(local_flag.PLAYER_SCORE), True, (0, 0, 0))
        self.image.blit(text1, (190, 100))


menu_gry = game_menu()
menu_gry.re_draw_menu()

