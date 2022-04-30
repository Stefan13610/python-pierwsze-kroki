

# deklaruje kilka stalych
map_x_size = 20
map_y_size = 20
map_size=map_x_size*map_y_size-1
R_kafelka = 50
BUFOR_MAP_WIDTH = (map_x_size + 1) * R_kafelka * 1.72
BUFOR_MAP_HEIGHT = (map_y_size + 1) * R_kafelka * 1.5
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
map_position_x = 0
map_position_y = 0
POP_UP_WIDTH=500                                        ##ustawienie tego w ten sposób chyba nie ma sensu, chociaż nie wiem
POP_UP_HEIGHT=300
CLOSE_BUTTON_DESC="Zamknij"
OK_BUTTON_DESC="OK"
CANCEL_BUTTON_DESC="Anuluj"
YES_BUTTON_DESC="Tak"
NO_BUTTON_DESC="Nie"
MENU_WIDTH = 300
MENU_HEIGHT = 500
MENU_POS_X = SCREEN_WIDTH - MENU_WIDTH
MENU_POS_Y = 20
NEXT_RUND_BUTTON_DESC = "Zakoncz ture"
RUND_DESC = "Nr. Rundy"
ANEX_FIELD_DESC = "Zajmij pole"
MAX_PLAYER_SIZE = 200                                       ##maksymalna liczba pól jakie może zająć gracz
FIELD_LEVEL_POS_X = R_kafelka/2
SCORE_DESC = "Punkty grzybni"

if BUFOR_MAP_WIDTH < SCREEN_WIDTH:                       ## to musi być bo przy zamałej mapie gra się wykrzaczy
    BUFOR_MAP_WIDTH = SCREEN_WIDTH                     ## ze względu na prubę pobrania koloru z pozycji większej niż
if BUFOR_MAP_HEIGHT < SCREEN_HEIGHT:                     ## rozmiar grafiki
    BUFOR_MAP_HEIGHT = SCREEN_HEIGHT

BUFOR_MAP_WIDTH = BUFOR_MAP_WIDTH + MENU_WIDTH