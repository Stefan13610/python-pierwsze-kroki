import pygame
print("test phytona")

#iniciowanie biblioteki do robienia gier
pygame.init();
#robimy sobie obszar do wyśiwetlania wysokość, szerokość
screen = pygame.display.set_mode((800,600))


##rysowanie prymitywów
##okreselnie koloru xD
#green = (0,255,0)
##wielokat
#pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
##kolo
#pygame.draw.circle(gameDisplay, white, (150,150), 75)
##prostokoąt pozycja, wysokosc, szerokosc
#pygame.draw.rect(gameDisplay, red, (400,400,50,25))
##linia
#pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
##piksele
#pixAr = pygame.PixelArray(gameDisplay) #gameDisplay to nasz screen
#pixAr[10][20] = green


#funkcja rysujaca szesciokat o okreslonym promieniu,kolorze i pozycji 
def draw_hex(kolor,x,y,r):
    pygame.draw.polygon(screen, kolor, ((x,y),(x+r*1.72/2,y-r/2),(x+r*172,y),(x+r*172,y+r),(x+r*1.72/2,y+1.5*r),(x,y+r)))



#tytuł i ikona aplikacji 
#ustawienie nazwy
pygame.display.set_caption("ShroomWorld")
#wczytywanie grafiki z pliku
icon=pygame.image.load('icon.png')
#ustawienie grafiki jako ikony aplikacji 
pygame.display.set_icon(icon)

#wczytywanie czcionki 
font1=pygame.font.Font('Aria.ttf',32)

#funkcja wypisująca coś na ekranie 
def print_text():
    #przygotowanie tekstu
    text=font1.render("Grzybnio, ojczyzno moja...",True,(255,255,255))
    #narysowanie tekstu na ekranie
    screen.blit(text,(20,20)) #przygotowany text, pozycjax, pozycjay
    
#wczytywanie testowej grafiki

testImg = pygame.image.load('test.png')

#zmienne do jej pozycji, testowanie wyśiwetlania ;)

testImg_x=100
testImg_y=100
#definiowanie funkci o ile tak się to tu nazywa xD
def obiekt():
#rysowanie obiektu, grafika, (pozycja x, pozycja y)
    screen.blit(testImg,(testImg_x,testImg_y))


running=True
#głowna pętla programu :)
while running:
#dodajemy obsługe eventów
    for event in pygame.event.get():
    #obsługa zamknięcia okna
        if event.type == pygame.QUIT:
            running=False
    #obsługa przycisków
        if event.type == pygame.KEYDOWN: #sprawdzamy czy jakikolwiek przycisk został wciśnięty
            if event.key == pygame.K_LEFT: #sprawdzamy stan konkretnego przycisku, lewej strzałki
                print("nacisnosłeś lewą strzałkę") #robimy coś z tym naciśnięciem
        if event.type == pygame.KEYUP: #sprawdzamy czy jakikolwiek przycisk został zwolniony
            if event.key == pygame.K_LEFT: #sprawdzamy stan konkretnego przycisku,znowu lewej strzałki
                print("zwolniłeś przycisk") #robimy coś z tym puszczeniem przycisku
   #ustawiamy kolor tła ;) RGB
    screen.fill((0, 0, 0))
    draw_hex((255,0,255),50,50,50)
    #wywołanie funkcji rysującej testowy obrazek, o ile takie coś w pythonie nazywa się funkcją 
    obiekt()
    #wywołanie funkcji rysujacej napis
    print_text()
    #narysowanie scrinna na ekranie ;)
    pygame.display.update()