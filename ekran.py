import pygame
import sys
from butonoluştur import seçim
from main import oyun
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
title_font = pygame.font.Font(None, 80)
menu_font = pygame.font.Font(None, 40)

# Set up text
title_text = title_font.render("Efsanevi Tarih", True, WHITE)
play_text = menu_font.render("Oyna", True, WHITE)
öğren_text = menu_font.render("Öğren", True, WHITE)
quit_text = menu_font.render("Çık", True, WHITE)

# Set up text positions
title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
play_text_rect = play_text.get_rect(center=(screen_width // 2, screen_height // 2))
öğren_text_rect = play_text.get_rect(center=(screen_width // 2, screen_height // 2+ 70))
quit_text_rect = quit_text.get_rect(center=(screen_width // 2, screen_height * 3 // 4))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_text_rect.collidepoint(mouse_pos):
                oyun()
                # Add your play code here
            elif öğren_text_rect.collidepoint(mouse_pos):
                seçim()
            elif quit_text_rect.collidepoint(mouse_pos):
                print("Quit button clicked!")
                pygame.quit()
                sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw text on the screen
    screen.blit(title_text, title_text_rect)
    screen.blit(play_text, play_text_rect)
    screen.blit(öğren_text, öğren_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # Update the screen
    pygame.display.flip()
