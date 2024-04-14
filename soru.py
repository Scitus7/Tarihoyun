import pygame
import sys
import random
import os

def sor():
    GENİŞLİK = 1000
    UZUNLUK= 600
    pygame.init()
    screen = pygame.display.set_mode((GENİŞLİK, UZUNLUK))
    pygame.display.set_caption("SORU SORMA EKRANI")
    soruişareti = dot_imageo = pygame.image.load(f"soruişareti.PNG")
    pygame.display.set_icon(soruişareti)
    pygame.mixer.music.load('oyun_muzgi.mp3')

    doğru_mu = False
    class soru:
        def __init__(self,soru,a,b,c,d,cevap):
            self.soru = soru
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.doğru = cevap
            self.hak = 0
        def çıkışsoru(self):
            print(f"soru:{self.soru}")
            return f"soru:{self.soru} "
        def çıkışşık(self):
            return f" {self.a}\t{self.b}\t{self.c} \t{self.d}"
        def çöz(self, cevap):

            if cevap == self.doğru :
                return "doğru"
            else:
                return "yanlış"




    font = pygame.font.Font("slkscr.ttf", 20)
    font2 = pygame.font.Font(None, 18)
    şık = font2.render("Merhaba, Dünya!", True, (255, 255, 255))
    yazı = font.render("Merhaba, Dünya!", True, (255, 0, 0))
    ğ = []
    SIRA = 0

    q = False
    a = False
    uydur = 1
    qhak = 1
    ahak = 1
    sorun = False
    soruçalışsınn = 1
    with open("sıra.txt", "r") as dosya:
        content = dosya.read()
        a = content.split(",")
        print(a[0])
    sorun = True
    döngü = True
    while döngü:
        txtsoru = ""
        with open("sorular.txt", "r", encoding='utf-8') as dosya:
            content = dosya.readlines()
            for i in content:
                ğ.append(i.split("\n"))
            print(ğ)
            ü = random.choice(ğ)
            ğ.remove(ü)
            print(ü)
            for i in ü:
                txtsoru += i
            c = txtsoru.split(",")
            print(c)
            sorun = True
        while sorun:
            with open("sıra.txt", "r") as dosya:
                content = dosya.read()
                a = content.split(",")
                #print(a[0])





            soru1 = soru(f"{c[0]}", f"{c[1]}", f"{c[2]}", f"{c[3]}", f"{c[4]}", f"{c[5]}")

            sorum = font.render(str(soru1.çıkışsoru()), True, (255, 0, 0))
            şık = font.render(str(soru1.çıkışşık()), True, (255, 250, 250))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if uydur == 1:
                        if event.key == pygame.K_a:
                            a = soru1.çöz("a")
                        elif event.key == pygame.K_s:
                            a = soru1.çöz("b")
                        elif event.key == pygame.K_d:
                            a = soru1.çöz("c")
                        elif event.key == pygame.K_w:
                            a = soru1.çöz("d")
                        elif event.key == pygame.K_LEFT:
                            q = soru1.çöz("a")
                        elif event.key == pygame.K_DOWN:
                            q = soru1.çöz("b")
                        elif event.key == pygame.K_RIGHT:
                            q = soru1.çöz("c")
                        elif event.key == pygame.K_UP:
                            q = soru1.çöz("d")
            x = (GENİŞLİK - sorum.get_width()) / 2
            y = (UZUNLUK - sorum.get_height()) / 2
            screen.blit(sorum, (x, y-100))
            screen.blit(şık, (x-90, y+50))


            pygame.display.flip()
            if q == "doğru" and qhak == 1:
                SIRA = 1
                sorun = False
                döngü = False
            elif q == "yanlış":
                qhak = 0

            if a == "doğru" and ahak == 1:
                SIRA = 0
                sorun = False
                döngü = False
            elif a == "yanlış":
                ahak = 0



                #x = (screen.get_width() - yazı.get_width()) / 2
                #y = (screen.get_height() - yazı.get_height()) / 2
                #screen.blit(yazı, (x, y))
            pygame.mixer.music.play()
            pygame.display.update()


        #print(SIRA)

        with open('sıra.txt', mode='w', encoding='utf-8') as file:
            file.write(f'{SIRA},')
            print(SIRA)
    print(SIRA)
