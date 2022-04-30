from enum import Enum


##Akcje użytkownika będą ładowane do kolejki eventów i obsługiwane w głównej pętli, w sumie to nie do kolejki bo to jest
## jeden element xD ale ryckać, w danym cyklu wystarczy ;)

##lokalny event do obslugi w glownej petli, na razie wymyślone na pałe
class local_event(Enum):
    CLOSE_APP = 0
    YES_BUTTON = 1
    NO_BUTTON = 2
    OK_BUTTON = 3
    CANCEL_BUTTON = 4
    CLOSE_BUTTON = 5
    NEXT_RUND_BUTTON = 6
    ANEX_FIELD_BUTTON = 7
    CHOSE_FIELD_TO_ANEX = 8

##clasa przechowujaca globalne flagi aplikacji, bo zmienne globalne działają jakos dziwnie
class flag_class:
    def __init__(self):

        self.MOUSE_CLICK_FLAG = False                       ## czy myszka jest wcisnieta
        self.LOCAL_EVENT_FLAG = False                       ##sprawdza czy istnieje jakis lokalny event
        self.Aplication_Event = local_event.CLOSE_APP       ##rodzaj eventu z listy powyzej
        self.POP_UP_IS_ACTIVE = True                        ##czy jakis pop_up jest wyswietlany
        self.ACTIVE_POP_UP_ID = 0                           ## id wyswietlanego popapu
        self.MOUSE_ON_BUTTON = False                        ##sprawdzamy czy myszka jest na przycisku
        self.MOUSE_ON_POP_UP = False                        ## czy myszka jest na pop_upie
        self.OLD_MOUSE_POS_X = 0                            ##pozycja myszki w momęcie wciśnięcia przycisku
        self.OLD_MOUSE_POS_Y = 0                            ## przechowywana tak długo jak trzymany jest orzycisk myszy
        self.RUND_NUMBER = 1                                ##numer rundy
        self.CLICK_FIELD_ID = 0                             ## ID kliknietego pola
        self.PLAYER_SCORE = 0
        self.FIELD_IN_AREA = 0                              ## pola w zasięgu danego pola, patrz math_function.py

local_flag = flag_class()
