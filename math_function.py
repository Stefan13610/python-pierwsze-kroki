from mapa import *
from constant import *
from local_event import local_flag

class field_container:
    def __init__(self):
        self.pola = [0]*100          ##tablica zwracanych pól
        self.liczba_pol = 0        ##liczba zwracanych pól -1 dla pustego kontenera

local_flag.FIELD_IN_AREA = field_container()

def is_field_in_conteiner(id):
    i=0
    while i < local_flag.FIELD_IN_AREA.liczba_pol:
        if local_flag.FIELD_IN_AREA.pola[i]==id:
            return True
        i+=1
    return False

def clear_field_conteiner():
    local_flag.FIELD_IN_AREA.liczba_pol=0



def sasiednie_pola(id_pola,odleglosc):
    if is_field_in_conteiner(id_pola) == False and id_pola > -1 and id_pola < map_size :
        local_flag.FIELD_IN_AREA.pola[local_flag.FIELD_IN_AREA.liczba_pol]=id_pola
        local_flag.FIELD_IN_AREA.liczba_pol+=1
    ##tak, tak wiem to można zapisać krucej xD ale długość kodu chyba nie ma znaczenia xD
    id_mod=int(id_pola/map_y_size)%2
    if odleglosc>0:
        if id_mod == 0:
            if int(id_pola/map_x_size) == int((id_pola-1)/map_x_size):
                sasiednie_pola(id_pola-1, odleglosc-1)
            if int(id_pola / map_x_size) == int((id_pola + 1) / map_x_size):
                sasiednie_pola(id_pola + 1, odleglosc - 1)
            if int((id_pola + map_x_size) / map_x_size) == int((id_pola + map_x_size - 1) / map_x_size):
                sasiednie_pola(id_pola + map_x_size -1, odleglosc - 1)
            sasiednie_pola(id_pola + map_x_size, odleglosc - 1)
            if int((id_pola - map_x_size) / map_x_size) == int((id_pola - map_x_size - 1) / map_x_size):
                sasiednie_pola(id_pola - map_x_size - 1, odleglosc - 1)
            sasiednie_pola(id_pola - map_x_size, odleglosc - 1)
        else:
            if int(id_pola/map_x_size) == int((id_pola-1)/map_x_size):
                sasiednie_pola(id_pola-1, odleglosc-1)
            if int(id_pola / map_x_size) == int((id_pola + 1) / map_x_size):
                sasiednie_pola(id_pola + 1, odleglosc - 1)
            if int((id_pola + map_x_size) / map_x_size) == int((id_pola + map_x_size + 1) / map_x_size):
                sasiednie_pola(id_pola + map_x_size +1, odleglosc - 1)
            sasiednie_pola(id_pola + map_x_size, odleglosc - 1)
            if int((id_pola - map_x_size) / map_x_size) == int((id_pola - map_x_size + 1) / map_x_size):
                sasiednie_pola(id_pola - map_x_size + 1, odleglosc - 1)
            sasiednie_pola(id_pola - map_x_size, odleglosc - 1)