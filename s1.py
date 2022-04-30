import pygame
from array import *
from button import *
from constant import *
from mapa import *
from local_event import *
from gracz import *
from grafiki import *
print("test phytona")

# iniciowanie biblioteki do robienia gier
pygame.init();

# deklarujemy zegar zeby nam wszystko tak nie zapierdzielalo
clock = pygame.time.Clock()

# wczytywanie czcionki
# font1=pygame.font.Font('Aria.ttf',32)

# tytuł i ikona aplikacji
# ustawienie nazwy
pygame.display.set_caption("ShroomWorld")
# wczytywanie grafiki z pliku
icon = pygame.image.load('icon.png')
# ustawienie grafiki jako ikony aplikacji
pygame.display.set_icon(icon)

# wywołanie czesci funkcii, tworzenie mapy i pierwsze rysowanie niektórych rzeczy ;)
create_map()
menu_gry.re_draw_menu()
draw_map()
draw_map2()
player.draw()

running = True ##zmienna do głównej petli aplikacji
# głowna pętla programu :)
while running:
    #wczytanie pozycji myszki
    mouse_position = pygame.mouse.get_pos()
    mx = mouse_position[0]
    my = mouse_position[1]
    # petla do obsługi eventów
    for event in pygame.event.get():
        # obsługa zamknięcia okna
        if event.type == pygame.QUIT:
            running = False
        # obsługa przycisków
        if event.type == pygame.KEYDOWN:  # sprawdzamy czy jakikolwiek przycisk został wciśnięty
            if event.key == pygame.K_LEFT:  # sprawdzamy stan konkretnego przycisku, lewej strzałki
                map_position_x_change = 5
            if event.key == pygame.K_RIGHT:  # sprawdzamy stan konkretnego przycisku, lewej strzałki
                map_position_x_change = -5
            if event.key == pygame.K_UP:  # sprawdzamy stan konkretnego przycisku, lewej strzałki
                map_position_y_change = 5
            if event.key == pygame.K_DOWN:  # sprawdzamy stan konkretnego przycisku, lewej strzałki
                map_position_y_change = -5
        if event.type == pygame.KEYUP:  # sprawdzamy czy jakikolwiek przycisk został zwolniony
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # sprawdzamy stan konkretnego przycisku,znowu lewej strzałki
                map_position_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # sprawdzamy stan konkretnego przycisku,znowu lewej strzałki
                map_position_y_change = 0
        if event.type == pygame.MOUSEWHEEL:
            print(event)
            #print(event.x, event.y)
            #print(event.flipped)
            #print(event.which)
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                local_flag.MOUSE_CLICK_FLAG=True
                local_flag.OLD_MOUSE_POS_X = mx
                local_flag.OLD_MOUSE_POS_Y = my
                #print(local_flag.MOUSE_ON_BUTTON)
                if local_flag.MOUSE_ON_BUTTON == False and local_flag.MOUSE_ON_POP_UP == False and local_flag.Aplication_Event != local_event.CHOSE_FIELD_TO_ANEX:
                    #print("Wciśnięto " + str(get_map_part_id(map_position_x, map_position_y)) + " kafelek")
                    local_flag.CLICK_FIELD_ID= get_map_part_id(map_position_x, map_position_y)
                    if local_flag.CLICK_FIELD_ID >=0:
                        if player.is_field_anex(local_flag.CLICK_FIELD_ID):
                            local_flag.ACTIVE_POP_UP_ID = 2
                        else:
                            local_flag.ACTIVE_POP_UP_ID = 1
                        local_flag.POP_UP_IS_ACTIVE = True

            if middle:
                print("Left Mouse Key is being pressed")
            if right:
                print("Left Mouse Key is being pressed")
                local_flag.Aplication_Event = local_event.CLOSE_APP
                clear_field_conteiner()
                ##rysujemy sobie zaznaczone pola, to znaczy rysowanie jest w grafiki.py tutaj zaznaczamy co ma być rysowane, to tylko test
                #local_flag.CLICK_FIELD_ID = get_map_part_id(map_position_x, map_position_y)
                #clear_field_conteiner()
                #sasiednie_pola(local_flag.CLICK_FIELD_ID, 2)
                #local_flag.POP_UP_IS_ACTIVE = True

        if event.type == pygame.MOUSEBUTTONUP: ## obslugujemy puszczenie przycisków myszy
            local_flag.MOUSE_CLICK_FLAG = False
    #koniec obsłui wbudowanych ewentów eventów

    if local_flag.LOCAL_EVENT_FLAG == True:

        if local_flag.Aplication_Event == local_event.OK_BUTTON:
            print("Właśnie obsluzyłeś swuj pierwszy event wcisiecia przycisku ;)")
            local_flag.POP_UP_IS_ACTIVE=False
            clear_field_conteiner()
        if local_flag.Aplication_Event == local_event.NO_BUTTON:
            print("Właśnie obsluzyłeś swuj pierwszy event wcisiecia przycisku ;)")
            local_flag.POP_UP_IS_ACTIVE=False
            clear_field_conteiner()
        if local_flag.Aplication_Event == local_event.YES_BUTTON:
            print("Właśnie obsluzyłeś swuj pierwszy event wcisiecia przycisku ;)")
            local_flag.POP_UP_IS_ACTIVE=False
            clear_field_conteiner()
        #obsluzylismy wiec ustawiamy flage na falsz
        local_flag.LOCAL_EVENT_FLAG=False
        if local_flag.Aplication_Event == local_event.NEXT_RUND_BUTTON:
            local_flag.Aplication_Event = local_event.CLOSE_APP
            clear_field_conteiner()
            local_flag.RUND_NUMBER+=1
            player.increment_field_level()
            player.draw()
            menu_gry.re_draw_menu()
        if local_flag.Aplication_Event == local_event.ANEX_FIELD_BUTTON:
            clear_field_conteiner()                         ##czyszcze sasiednie pola
            sasiednie_pola(local_flag.CLICK_FIELD_ID, 1)    ##obliczam sasiednie pola
            local_flag.POP_UP_IS_ACTIVE = False             ##wylanczam pop_up
            local_flag.Aplication_Event = local_event.CHOSE_FIELD_TO_ANEX
            local_flag.MOUSE_CLICK_FLAG = False
        if local_flag.Aplication_Event == local_event.CHOSE_FIELD_TO_ANEX:
            print(1)
            if local_flag.MOUSE_CLICK_FLAG==True:
                if is_field_in_conteiner(local_flag.CLICK_FIELD_ID) and player.is_field_anex(local_flag.CLICK_FIELD_ID)==False:
                    player.draw()
                    player.anex_field(local_flag.CLICK_FIELD_ID, player.id_gracza)
                    local_flag.Aplication_Event = local_event.CLOSE_APP
                    clear_field_conteiner()

        local_flag.LOCAL_EVENT_FLAG = False

    ## to jest poza if LOCAL_EVENT_FLAG bo to jest ciągły event, może trzeba nową flagę dołożyć jeżeli ciongłych enventów będzie więcej
    if local_flag.Aplication_Event == local_event.CHOSE_FIELD_TO_ANEX:
        if local_flag.MOUSE_CLICK_FLAG == True:
            local_flag.CLICK_FIELD_ID = get_map_part_id(map_position_x, map_position_y)
            if is_field_in_conteiner(local_flag.CLICK_FIELD_ID) == True:
                if player.is_field_anex(local_flag.CLICK_FIELD_ID) == False:
                    player.anex_field(local_flag.CLICK_FIELD_ID, player.id_gracza)
                    local_flag.Aplication_Event = local_event.CLOSE_APP
                    clear_field_conteiner()
                    player.draw()
                    menu_gry.re_draw_menu()
                else:
                    local_flag.POP_UP_IS_ACTIVE = True
                    local_flag.ACTIVE_POP_UP_ID = 4
            else:
                local_flag.POP_UP_IS_ACTIVE = True
                local_flag.ACTIVE_POP_UP_ID = 3

    # ustawiamy liczbę fps chyba
    clock.tick(100)
    # ustawiamy kolor tła ;) RGB, albo inaczej czyszczenie tła


    rysuj_mape(map_position_x,map_position_y,mx,my)
    # zmiana pozycji mapy,  jeśli wciśnięty jest przycisk, map_position_x_change ustawiane jest w obsłudze eventów
    map_position_x += map_position_x_change
    map_position_y += map_position_y_change
    # kontrola czy nie wyjdziemy z mapą poza obszar rysowania
    if map_position_x > 0:
        map_position_x = 0
        map_position_x_change = 0

    if -1 * map_position_x > BUFOR_MAP_WIDTH - SCREEN_WIDTH:
        map_position_x = -1 * (BUFOR_MAP_WIDTH - SCREEN_WIDTH)

    if map_position_y > 0:
        map_position_y = 0
        map_position_y_change = 0

    if -1 * map_position_y > BUFOR_MAP_HEIGHT - SCREEN_HEIGHT:
        map_position_y = -1 * (BUFOR_MAP_HEIGHT - SCREEN_HEIGHT)


    #resetujemy flagę obecności myszki na przycisku
    local_flag.MOUSE_ON_BUTTON = False
    menu_gry.draw_menu(screen,mx,my)
    rysuj_komunikaty(screen, mx, my)

    #głowna metoda rysująca na ekranie
    pygame.display.update()


