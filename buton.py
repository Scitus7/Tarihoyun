import pygame

class Button():
    def __init__(self, x, y, width, height, radius, inactive_color, active_color,altcolor ,text='',textcolor = (0,0,255), font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.rectalt = pygame.Rect(x, y+height/9, width, height)
        self.altcolor = altcolor
        self.radius = radius
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.textcolor = textcolor
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font("Khodijah_Free.ttf", self.font_size)
        self.image = self.font.render(self.text, True, self.textcolor)
        self.image_rect = self.image.get_rect(center=self.rect.center)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = False
        self.pushed = False

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True
        else:
            self.active = False

    def push(self, event):
        self.pushed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.pushed = True

    def draw(self, surface):
        if self.active:
            color = self.active_color
        else:
            color = self.inactive_color
        if self.pushed:
            self.rect = self.rectalt

        else:
            self.rect =  pygame.Rect(self.x, self.y, self.width, self.height)
        self.image_rect = self.image.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, self.altcolor, self.rectalt, border_radius=self.radius)
        surface.blit(self.image, self.image_rect)
        pygame.draw.rect(surface, color, self.rect, border_radius=self.radius)
        surface.blit(self.image, self.image_rect)


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((640, 480))

#oluşturma
button_width = 200
button_height = 200
button_x = screen_width // 2 - button_width // 2
button_y = screen_height // 2 - button_height // 2
button_inactive_color = (160,82,45)
button_active_color = (139,69,19)
altcolor = 	(205,133,63)
button_text = 'Oyna'
button_font_size = 30
button_radius = 30
#button = Button(button_x, button_y, button_width, button_height, button_radius, button_inactive_color, button_active_color,altcolor, button_text, button_font_size)
# döngünün içine bunları yaz


#button.handle_event(event)
#button.push(event)
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        button.handle_event(event)
#
#    screen.fill((0, 0, 0))
#    button.draw(screen)
#    pygame.display.update()

#pygame.quit()