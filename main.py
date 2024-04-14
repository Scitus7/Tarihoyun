import sys
import time
import os
import subprocess
import pygame
import random
from soru import sor
import buton

def oyun():
    #text dosyasını tazele
    with open("gezegen_konum.txt", "w") as file:
        # Append some text to the file
        file.write("")
    # Set up the game window
    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("efsanevi tarih")
    DOT_SIZE = 50
    new_width = DOT_SIZE
    new_height = DOT_SIZE
    Ghost_number = 3
    background = random.choice(["çöl"])
    background_image = pygame.image.load(f"{background}.png").convert()
    # Load game assets

    karakterler = ["Muhammed","Ömer","halid"]
    s = 0

    kişi = random.choice(karakterler)
    karakterler.remove(kişi)
    rakipkişi = random.choice(karakterler)

    gamestart_imageo = pygame.image.load("Efsanevi Tarih.png")
    gamestart_image = pygame.transform.scale(gamestart_imageo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    gamestart_image_rect = gamestart_image.get_rect()

    gameover_imageo = pygame.image.load("game_over.png")
    gameover_image = pygame.transform.scale(gameover_imageo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    intro_imageo = pygame.image.load("intro.png")
    intro_image = pygame.transform.scale(intro_imageo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    karakteriniseç_imageo = pygame.image.load("karakterseç.png")
    karakteriniseç_image = pygame.transform.scale(karakteriniseç_imageo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    planets = ["hilal"]
    planet = random.choice(planets)

    font = pygame.font.Font(None, 70)


    #ghost_imageo = pygame.image.load(f"{hoca}.PNG")
    #ghost_image = pygame.transform.scale(ghost_imageo, (new_width, new_height))
    dot_imageo = pygame.image.load(f"{planet}.PNG")
    #dot_image = pygame.transform.scale(dot_imageo, (,60))

    # Define game constants

    PACMAN_SIZE = 40
    GHOST_SIZE = 40
    PACMAN_SPEED = 1
    with open("sıra.txt","r",encoding="utf-8") as dosya:

        content = dosya.read()
        a = content.split(",")
        SIRA = a[0]





    SPEEDY = 1


    dot_image = pygame.transform.scale(dot_imageo, (DOT_SIZE,DOT_SIZE))
    pygame.display.set_icon(dot_image)
    # Define game classes
    class Pacman:
        def __init__(self):

            self.puan = 0
            self.image = pacman_image
            self.rect = self.image.get_rect()
            self.rect.center = (62.5,62.5)
            self.direction = "right"

            self.doğru_konumx = 0
            self.doğru_konumy = 0
            self.dosya = []
            self.bool = False


        def update(self):

            if self.rect.left < 0:
                # self.rect.x += 30
                self.rect.x += DOT_SIZE * 2
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.x -= DOT_SIZE * 2
            elif self.rect.top < 0:
                self.rect.y += DOT_SIZE * 2
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.y -= DOT_SIZE * 2

            else:

                if self.direction == "right" :
                    self.rect.x += DOT_SIZE*2
                elif self.direction == "left" :
                    self.rect.x -= DOT_SIZE*2
                elif self.direction == "up" :
                    self.rect.y -= DOT_SIZE*2
                elif self.direction == "down":
                    self.rect.y += DOT_SIZE*2

                if self.direction == "gezegenustu":
                    pass
                    #self.sıra = 0









        def change_direction(self, direction):
            self.direction = direction

    class Rakip(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.puan = 0
            self.image = rakip_image
            self.rect = self.image.get_rect()
            self.rect.center = (550,375)
            self.direction = "right"

            self.doğru_konumx = 0
            self.doğru_konumy = 0
            self.dosya = []
            self.bool = False


        def update(self):

            if self.rect.left < 0 :
                #self.rect.x += 30
                self.rect.x += DOT_SIZE*2
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.x -= DOT_SIZE*2
            elif self.rect.top < 0 :
                self.rect.y += DOT_SIZE*2
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.y -= DOT_SIZE*2

            else:


                if self.direction == "right" :
                    self.rect.x += DOT_SIZE*2
                elif self.direction == "left" :
                    self.rect.x -= DOT_SIZE*2
                elif self.direction == "up" :
                    self.rect.y -= DOT_SIZE*2
                elif self.direction == "down":
                    self.rect.y += DOT_SIZE*2

                if self.direction == "gezegenustu":
                    pass
                    #self.sıra = 1




                            #print(doğru_konummu)
                            #print(self.rect.midright[0])




        def change_direction(self, direction):
            self.direction = direction

    class Ghost(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = ghost_image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.direction = random.choice(["left", "right", "up", "down"])
            self.SPEEDY = SPEEDY

        def update(self):
            # Change direction if the ghost hits a wall
            if self.rect.left < 0:
                self.rect.y = random.randint(0, SCREEN_HEIGHT)
                self.rect.x = random.randint(0,SCREEN_WIDTH)
                self.SPEEDY *=-1
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.y = random.randint(0, SCREEN_HEIGHT)
                self.rect.x = random.randint(0,SCREEN_WIDTH)
                self.SPEEDY *= -1
            elif self.rect.top < 0:
                self.rect.y = random.randint(0,SCREEN_HEIGHT)
                self.rect.x = random.randint(0, SCREEN_WIDTH)
                self.SPEEDY *= -1
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.y = random.randint(0,SCREEN_HEIGHT)
                self.rect.x = random.randint(0, SCREEN_WIDTH)
                self.SPEEDY *= -1
            else:
                if self.direction == "right":
                    self.rect.x += GHOST_SPEED*self.SPEEDY
                    self.rect.y -= GHOST_SPEED * self.SPEEDY
                elif self.direction == "left":
                    self.rect.x -= GHOST_SPEED*self.SPEEDY
                    self.rect.y += GHOST_SPEED * self.SPEEDY
                elif self.direction == "up":
                    self.rect.x += GHOST_SPEED * self.SPEEDY
                    self.rect.y -= GHOST_SPEED * self.SPEEDY
                elif self.direction == "down":
                    self.rect.x -= GHOST_SPEED * self.SPEEDY
                    self.rect.y += GHOST_SPEED * self.SPEEDY




    class Gezgen(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = dot_image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def çıkar(self):
            return self.rect

    # Set up game objects

    #ghosts = pygame.sprite.Group()
    gezgenler = pygame.sprite.Group()
    rakipler = pygame.sprite.Group()
    for i in range(Ghost_number):
        x = random.randint(SCREEN_HEIGHT,SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT,SCREEN_WIDTH)
        #ghost = Ghost(x,y)
        #ghosts.add(ghost)
    # Create the dots
    for x in range(DOT_SIZE, SCREEN_WIDTH, DOT_SIZE*2):
        for y in range(DOT_SIZE, SCREEN_HEIGHT, DOT_SIZE*2):
            a = random.randint(0,DOT_SIZE)
            dot = Gezgen(x, y)
            gezgenler.add(dot)
            with open("gezegen_konum.txt", "a") as file:
                # Append some text to the file

                file.write(f"{dot.rect.bottomleft[0]},")
                file.write(f"{dot.rect.bottomright[0]},")
                file.write(f"{dot.rect.midtop[1]},")
                file.write(f"{dot.rect.midbottom[1]},")
                file.write(f"{dot.rect.center[0]},")
                file.write(f"{dot.rect.center[1]},\n")


    alpha_value = 255  # a value between 0 and 255, with 0 being completely transparent and 255 being completely opaque
    giriş = True



    sıra1 = 0
    seçili = False
    oynak = 0
    while seçili:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_RIGHT:
                oynak +=1
            if event.type == pygame.K_LEFT:
                oynak -=1



            ass = os.listdir("C:/Users/mhmz/Desktop/TeamGunner_By_SecretHideout_060519/karakterlerrr")
            print(ass)
            gösteri = pygame.image.load(os.path.join("karakterlerrr", f"{ass[oynak]}"))
            screen.blit(gösteri,( 180,310))
            #screen.blit(f"{ass[oynak][:-4]}", (180, 310))
            if event.type == pygame.K_KP_ENTER:
                kişi = ass[oynak][:-4]

            screen.blit(karakteriniseç_image, [0, 0])
            pygame.display.flip()

    pygame.mixer.music.load('oyun_muzgi.mp3')

    pacman_imageo = pygame.image.load(os.path.join("karakterlerrr",f"{kişi}.png"))

    pacman_image = pygame.transform.scale(pacman_imageo, (new_width, new_height))
    pacman = Pacman()

    rakip_imageo = pygame.image.load(os.path.join("karakterlerrr",f"{rakipkişi}.png"))

    rakip_image = pygame.transform.scale(rakip_imageo, (new_width, new_height))
    rakip = Rakip()
    rakipler.add(rakip)

    # Start the game loop


    bitti = False
    sa = 1
    uydur = 1
    soru = True
    para = 0
    running = True
    q = False
    a = False
    durdur = 0
    ilk = 1
    başlama = time.time()
    while running:
        pygame.mixer.music.play()


        with open("sıra.txt", "r") as dosya:
            content = dosya.read()
            a = content.split(",")
            SIRA = a[0]

            #soruçalışsın = a[1]


        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN :
                print("Çalıştı")
                if event.key == pygame.K_q:

                    sor()
                    durdur = 0
                if SIRA == "1" and durdur == 0:
                    if event.key == pygame.K_LEFT:
                        pacman.change_direction("left")
                        durdur = 1
                    elif event.key == pygame.K_RIGHT:
                        pacman.change_direction("right")
                        durdur = 1
                    elif event.key == pygame.K_UP:
                        pacman.change_direction("up")
                        durdur = 1
                    elif event.key == pygame.K_DOWN:
                        pacman.change_direction("down")
                        durdur = 1
                elif SIRA == "0" and durdur == 0:
                    print("bende")
                    if event.key == pygame.K_a:
                        rakip.change_direction("left")
                        durdur = 1
                    elif event.key == pygame.K_d:
                        rakip.change_direction("right")
                        durdur = 1
                    elif event.key == pygame.K_w:
                        rakip.change_direction("up")
                        durdur = 1
                    elif event.key == pygame.K_s:
                        rakip.change_direction("down")
                        durdur = 1


        # Update game objects
        pacman.update()
        rakip.update()
        # Update the ghosts
        #for ghost in ghosts:
        #    ghost.update()
        #check collusions for ghost
        yakalanma = pygame.sprite.spritecollide(pacman, rakipler, True)
        if yakalanma:
            print("yakalandın")
            if SIRA == "1":
                print("1.oyuncu kazandı")
                running = False
                bitti = True

            if SIRA == "0":
                print("2.oyuncu kazandı")
                running = False
                bitti = True
        #    time.sleep(1.5)
        #    print(kişi,para,"lira topladı!")
        #    sys.exit()


        # Check for collisions with planets
        eaten_dots = pygame.sprite.spritecollide(pacman, gezgenler, True)
        eaten_dots_rakip = pygame.sprite.spritecollide(rakip, gezgenler, True)
        if eaten_dots or eaten_dots_rakip:
            #print("Gelsin Paralar!")
            #print(f"x={dot.rect.x}\n y = {dot.rect.y}" )
            #    para +=1
            pacman.change_direction("gezegenustu")
            rakip.change_direction("gezegenustu")
            soru = True
        #    if SIRA == 1:
        #        SIRA = 0
        #    elif SIRA == 0:
        #        SIRA = 1
        if SIRA == "1":
            print("sıra =1")

        # Draw game objects
        screen.blit(background_image, (0, 0))
        gezgenler.draw(screen)
        screen.blit(pacman.image, pacman.rect)
        screen.blit(rakip.image, rakip.rect)
        #for ghost in ghosts:
        #    screen.blit(ghost.image, ghost.rect)

        # Update the display
        pygame.display.update()
        if sa == 1:
            time.sleep(3)
            sa += 10

        bitme = time.time()
    while bitti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    x, y = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    if x > 230 and x < 300 and y > 420 and y < 450:

                        subprocess.call(['python', 'main.py'])
                    elif x > 500 and x < 570 and y > 420 and y < 450:
                        sys.exit()

            screen.blit(gameover_image, [0, 0])
            pygame.display.flip()
