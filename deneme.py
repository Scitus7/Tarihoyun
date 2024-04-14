import pygame
import sys
import time
pygame.init()

# ekran genişliği ve yüksekliği
screen_width = 800
screen_height = 600

class button():
    def __init__(self,renk,konumbüyüklük, kıvrılma,yazı,renkyazı = (0,0,255)):
        self.renk = renk
        self.konumbüyüklük = konumbüyüklük
        self.kıvrılma = kıvrılma
        self.yazı = yazı
        self.aşağırenk =  [self.renk[0]-25, self.renk[1] - 55, self.renk[2]-55]
        self.rect = pygame.Rect(0,0,0,0)
        self.a = 0
        self.renkyazı = renkyazı
        self.x, self.y = pygame.mouse.get_pos()
        self.yazımm = font.render(str("Play"), True, (self.renkyazı))
        for i in self.konumbüyüklük:
            self.rect[self.a] = i
            self.a +=1
        self.rect2 = self.rect
        self.rect2.y = self.rect.y+5
    def çiz(self):
        pygame.draw.rect(screen, self.renk, self.rect, border_radius=self.kıvrılma)
        pygame.draw.rect(screen, self.aşağırenk, self.rect2, border_radius=self.kıvrılma)
        screen.blit(self.yazımm, (self.rect.x + 3, self.rect.y + 3))
    def durma(self):
        if self.x > self.rect.x and self.x < self.rect.x + self.rect.size[0] and \
                self.y > self.rect.y and self.rect.y + self.rect.size[1] < self.y:
            self.renk = self.aşağırenk
    def bas(self):
        if self.x > self.rect.x and self.x < self.rect.x + self.rect.size[0] and \
                self.y > self.rect.y and self.rect.y + self.rect.size[1] < self.y:
            self.rect[1]+= 5
    def çek(self):
        self.rect[1] -=5

# ekran yüzeyini oluştur
screen = pygame.display.set_mode((screen_width, screen_height))

# pencere başlığı
pygame.display.set_caption("Yuvarlak Köşeli Dikdörtgen Çizimi")


# beyaz renk
white = (255, 255, 255)

# dikdörtgenin konumu ve boyutu
rect = pygame.Rect(100, 100, 70, 30)
rect2 = pygame.Rect(100,105, 70, 30)
whitee = (200, 200, 200)
font = pygame.font.Font("slkscr.ttf", 23)
# köşelerin yarıçapı
radius = 30


buton1 = button(white,(230, 420, 70, 30),radius,"Play")
değer = 0
while True:
    a = 105
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            buton1.durma()
            if event.button == 1:
                buton1.bas()




    # dikdörtgeni çiz
    pygame.draw.rect(screen, whitee, rect2, border_radius=radius)
    pygame.draw.rect(screen, white, rect, border_radius=radius)
    buton1.çiz()
    # ekranda göster

    x, y = pygame.mouse.get_pos()
    print(pygame.mouse.get_pos())
    sorum = font.render(str("Play"), True, (0, 0, 255))
    screen.blit(sorum, (rect.x+3, rect.y+3))
    if x > rect.x and x < rect.x + rect.size[0] and y > rect.y and rect.y + rect.size[1] < 450:
        pass
    else:
        white = (255, 255, 255)
    if buton1.rect[1] >= 105:
        buton1.çek()


    pygame.display.flip()
