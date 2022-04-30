import pygame
from array import *
from local_event import *
pygame.init();
#wczytywanie czcionki 
font1=pygame.font.Font('arial.ttf',20)

##zmienna sprawdzajaca czy najechalismy na jakis przycisk
MOUSE_ON_BUTTON=False

class button:
    def __init__(self, x,y,w,h,tekst,color_1,color_2,aktywny,rodzaj_ewnetu):  # pozycja, wysokość,szerokość, kolor wypełnienia, kolor ramki i tekstu, czy jest aktywny
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tekst = tekst
        self.color_1 = color_1
        self.color_2 = color_2
        self.aktywny = aktywny
        self.event=rodzaj_ewnetu  ## wartości z pliku local_event
        size = width, height = (w,h)
        self.bufor_1=pygame.Surface(size)
        self.bufor_2=pygame.Surface(size)
        self.bufor_1.fill(self.color_1)
        pygame.draw.line(self.bufor_1, self.color_2, (0,0),(0,self.h),4)
        pygame.draw.line(self.bufor_1, self.color_2, (0,self.h-2),(self.w-2,self.h-2),4)
        pygame.draw.line(self.bufor_1, self.color_2, (self.w-2,self.h-2),(self.w-2,0),4)
        pygame.draw.line(self.bufor_1, self.color_2, (self.w,0),(0,0),4)
        text=font1.render(self.tekst,True,self.color_2)
        text_width=text.get_width()
        text_height = text.get_height()
        text_x=4;
        text_y=4;
        if self.w>text_width:
            text_x=(self.w-text_width)/2
        if self.h > text_height:
            text_y = (self.h - text_height) / 2
        self.bufor_1.blit(text,(text_x,text_y))
        self.bufor_2.fill(self.color_2)
        pygame.draw.line(self.bufor_2, self.color_1, (0,0),(0,self.h),4)
        pygame.draw.line(self.bufor_2, self.color_1, (0,self.h-2),(self.w,self.h-2),4)
        pygame.draw.line(self.bufor_2, self.color_1, (self.w-2,self.h-2),(self.w-2,0),4)
        pygame.draw.line(self.bufor_2, self.color_1, (self.w,0),(0,0),4)
        text=font1.render(self.tekst,True,self.color_1)
        self.bufor_2.blit(text,(text_x,text_y))
    def draw(self,space):#rysowanie przycisku
        if self.aktywny == 0:##sprawdza czy myszka jest na przycisku
            space.blit(self.bufor_1,(self.x,self.y))
        if self.aktywny == 1:
            space.blit(self.bufor_2,(self.x,self.y))
    def mouse_on(self,mx,my): ##funkcja sprawdza czy mysz znajduje się nad przyciskiem
        self.aktywny=0;
        if mx > self.x and mx < self.x+self.w:
            if my > self.y and my < self.y+self.h:
                self.aktywny=1

                if local_flag.MOUSE_CLICK_FLAG == True: ## jeżeli klikniemy myszką to ustawiamy event przycisku
                    local_flag.LOCAL_EVENT_FLAG = True
                    local_flag.Aplication_Event = self.event
                    local_flag.MOUSE_CLICK_FLAG = False
                    print("wcisnoles przycisk")
                local_flag.MOUSE_ON_BUTTON=True
                return True
        return False
        
#tworzymy testowy przycisk 
#bt1=button(60,60,100,50,"siemanko",(255,0,0),(0,0,255),1)
    ##rysujemy przycisk i sprawdzamy czy najechala na niego myszka 
    #bt1.draw(screen)
    #bt1.mouse_on(mx,my)
    
#dobra zrobimy też tutaj popupy