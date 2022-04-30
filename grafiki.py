import pygame
from mapa import *
from constant import *
from pop_up import *
from math_function import *
from local_event import *
##rysowanie prymitywów - sciaga
##okreselnie koloru xD
# green = (0,255,0)
##wielokat
# pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
##kolo
# pygame.draw.circle(gameDisplay, white, (150,150), 75)
##prostokoąt pozycja, wysokosc, szerokosc
# pygame.draw.rect(gameDisplay, red, (400,400,50,25))
##linia
# pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
##piksele
# pixAr = pygame.PixelArray(gameDisplay) #gameDisplay to nasz screen
# pixAr[10][20] = green

# pozycja mapy względem okna aplikacji, przesówanie mapy
map_position_x_change = 0
map_position_y_change = 0
map_position_x=0
map_position_y=0
# główne okno aplikacji
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#tworzenie 3 grafik na których będą elementy związane z mapą
size = width, height = (BUFOR_MAP_WIDTH, BUFOR_MAP_HEIGHT)
bufor_mapy = pygame.Surface(size)   #na tym rysowany jest kolor(ID) kafelka
bufor_mapy2 = pygame.Surface(size).convert_alpha()  #na tym rysowana jest faktyczna mapa, tp co ma sie wyswietlac dla gracza
bufor_mapy3 = pygame.Surface(size)  #na tym rysowane sa elementy widoczne chwilowo
# wypełnianie bitmap lolorem ;)
bufor_mapy.fill((255, 255, 255))
bufor_mapy3.fill((0, 0, 0))
bufor_mapy2.fill((0, 0, 0, 0))  # ten będzie przezroczysty ;)


# funkcja rysujaca szesciokat o okreslonym promieniu,kolorze i pozycji
def draw_hex(space, kolor, x, y, r):
    pygame.draw.polygon(space, kolor, (
    (x, y), (x + r * 1.72 / 2, y - r / 2), (x + r * 1.72, y), (x + r * 1.72, y + r), (x + r * 1.72 / 2, y + 1.5 * r),
    (x, y + r)))


# funkcja rysujaca ramke dla tego szesciokata
def draw_hex_border(space, kolor, x, y, r, s):
    pygame.draw.line(space, kolor, (x, y), (x + r * 1.72 / 2, y - r / 2), s)
    pygame.draw.line(space, kolor, (x + r * 1.72 / 2, y - r / 2), (x + r * 1.72, y), s)
    pygame.draw.line(space, kolor, (x + r * 1.72, y), (x + r * 1.72, y + r), s)
    pygame.draw.line(space, kolor, (x + r * 1.72, y + r), (x + r * 1.72 / 2, y + 1.5 * r), s)
    pygame.draw.line(space, kolor, (x + r * 1.72 / 2, y + 1.5 * r), (x, y + r), s)
    pygame.draw.line(space, kolor, (x, y + r), (x, y), s)


def create_hex_texture_from_file(file):
    bitmap_size = 2*R_kafelka
    img_1 = pygame.Surface((bitmap_size, bitmap_size)).convert_alpha()  ##tworzymy obraz i konwertujemy go do obsługi kanału alfa
    img_2 = pygame.image.load(file).convert_alpha()  ## wczytujemy texture i konvertujemy ją do obsługi kanału alfa
    img_1.fill((0, 0, 0, 255))  ##ustawiamy kolor na czarny z zerową przezroczystością ;)
    draw_hex(img_1, (255, 255, 255, 0), 0, R_kafelka/2, R_kafelka)  ##rysujemy przezroczysty szesciokat na grafice
    img_2.blit(img_1,(0, 0))  ## rysuje grafikze z przezroczystym szesciokatem na grafice z teksturą
    img_2.set_colorkey((0, 0, 0))  ##ustawiam kolor czarny jako kolor tła, nie będzie rysowany
    img_1.blit(img_2, (0, 0))  ##rysuje grafike na grafice 1, zeby nie tworzyć 3 grafiki i zeby rozmiar sie zgadzal
    img_1.set_colorkey((0, 0, 0))  ##ustawiam kolor czarny jako kolor tła
    return img_1  ##zwracamy gotową grafikę którą wystarczy rysować na wspułżędnych x=0, y=0?

textury_mapy = [create_hex_texture_from_file('img/trawa.png')]*20


##ta funkcja jest do optymalizacji czy coś, pewnie wczytywanie z pliku będzie najlepsze
## ale to już załej stuktury kafelka i moze mapy
def load_textures():
    textury_mapy[0] = create_hex_texture_from_file('img/trawa.png')
    textury_mapy[1] = create_hex_texture_from_file('img/las.png')
    textury_mapy[2] = create_hex_texture_from_file('img/mrowisko.png')
    textury_mapy[3] = create_hex_texture_from_file('img/promieniowanie.png')
    textury_mapy[4] = create_hex_texture_from_file('img/ropa.png')
    textury_mapy[5] = create_hex_texture_from_file('img/woda.png')



load_textures()

def blit_on_screen(space, x, y): ##rysowanie obrazka na innym
    screen.blit(space, (x, y))  # rysowanie mapy na screenie

# funkcja zwraca id kafelka nad którym znajduje się kursor myszy, robi to na podstawie koloru z grafiki "bufor_mapy"
def get_map_part_id(x, y):
    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1
    x = int(x)
    y = int(y)
    # print("x="+str(x)+" y="+str(y)) # tu był jakiś błąd że zmienne nie są typu int, ciort wie czemu
    a = pygame.mouse.get_pos()
    bufor_mapy_x=a[0] + x
    bufor_mapy_y=a[1] + y

    color = bufor_mapy.get_at((bufor_mapy_x,bufor_mapy_y ))
    if color[2] > 254:
        return -1
    return color[0] + 256 * color[1] + 65536 * color[2]

def draw_bufor_mapy2(x):#rysuje podświetlenie nad najechanym kafelkiem
    draw_hex(bufor_mapy2, (216, 190, 40, 128), M[x].x, M[x].y, R_kafelka+1)
    draw_hex_border(bufor_mapy2, (10, 150, 31 , 80), M[x].x, M[x].y, R_kafelka, 4)


def draw_map(): ## funkcja rysuje mape kolorów, nie jest ona wyświetlona na ekranie w rzadnym momencie, służy jedynie do
                ## określenia id kafelka na podstawie kolory
    p = 0       ## pozycja w tablicy, mozna by w sumie zrobić to w 1 pętli od 0 do p gdzie p= i*j ale ryckać niewiele to zmienia
    i = 0
    while i < map_x_size:
        j = 0
        while j < map_y_size:
            draw_hex(bufor_mapy, (M[p].r, M[p].g, M[p].b), M[p].x, M[p].y, R_kafelka)
            # draw_hex_border(bufor_mapy,(0,0,0),M[p].x,M[p].y,R_kafelka,2) # to trzeba zakomentowac w przyszłosci
            p += 1
            j += 1
        i += 1


def draw_map2(): ## ta funkcja rysuje elementy wyświetlane na ekranie, to znaczy ta mapa jest rysowana
    p = 0
    i = 0
    while i < map_x_size: #
        j = 0
        while j < map_y_size:

            #draw_hex(bufor_mapy3, (160, 234, 94), M[p].x, M[p].y, R_kafelka)
            bufor_mapy3.blit(textury_mapy[M[p].id_tekstury],(M[p].x, M[p].y-R_kafelka/2))
            draw_hex_border(bufor_mapy3, (0, 0, 0), M[p].x, M[p].y, R_kafelka, 2)
            p += 1
            j += 1
        i += 1

###czcionka i pisanie po ekranie - można by było w nowym pliku
# wczytywanie czcionki, tą pobrałem przypadkiem, trzeba zadeklarować kilka nowych
font1 = pygame.font.Font('Aria.ttf', 32)


# funkcja wypisująca coś na ekranie, do poprawy
def print_text(tekst, x, y):
    # przygotowanie tekstu
    text = font1.render(tekst, True, (255, 255, 255))
    # narysowanie tekstu na ekranie
    screen.blit(text, (x, y))  # przygotowany text, pozycjax, pozycjay


def podswietl_pola_w_zasiegu():
    i = 0
    while i < local_flag.FIELD_IN_AREA.liczba_pol:
        draw_bufor_mapy2(local_flag.FIELD_IN_AREA.pola[i])

        i += 1


def rysuj_mape(map_position_x,map_position_y,mx,my): ##pozycja myszki x i y
    screen.fill((0, 0, 0))
    bufor_mapy2.fill((0, 0, 0, 0))

    kafelek_id = get_map_part_id(map_position_x, map_position_y)  # sprawdzenie nad jakim kafelkiem jest aktualnie mapa
    if kafelek_id >= 0:
        draw_bufor_mapy2(kafelek_id)

    podswietl_pola_w_zasiegu()
    # blit_on_screen(bufor_mapy2,map_position_x,map_position_y)
    # rysowanie głównych grafik mapy na ekranie
    blit_on_screen(bufor_mapy3, map_position_x, map_position_y)
    blit_on_screen(bufor_mapy2, map_position_x, map_position_y)


    print_text("Grzybowa kraina ;)", 20, 20)


