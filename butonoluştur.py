import os
import pygame
def seçim():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Video Player")

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up fonts
    font = pygame.font.Font(None, 40)

    # Set up video folder
    video_folder = "videolar"

    # Get the list of videos in the folder
    video_files = os.listdir(video_folder)

    # Set up buttons
    button_width = 300
    button_height = 50
    button_margin = 20
    buttons_per_column = screen_height // (button_height + button_margin)
    total_columns = (len(video_files) + buttons_per_column - 1) // buttons_per_column

    buttons = []
    for i, video_file in enumerate(video_files):
        column_index = i // buttons_per_column
        row_index = i % buttons_per_column
        button_x = (button_width + button_margin) * column_index + (screen_width - (button_width + button_margin) * total_columns) // 2
        button_y = (button_height + button_margin) * row_index + 50
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        button_text = font.render(video_file, True, (0, 200, 0))
        buttons.append((button_rect, button_text))

    # Set up scrolling variables
    scroll_speed = 20
    scroll_direction = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    for button_rect, _ in buttons:
                        if button_rect.collidepoint(mouse_pos):
                            # Find the clicked video and open it
                            for i, (btn_rect, _) in enumerate(buttons):
                                if btn_rect.collidepoint(mouse_pos):
                                    video_file = video_files[i]
                                    video_path = os.path.join(video_folder, video_file)
                                    os.startfile(video_path)  # Open the video with default player
                elif event.button == 4:  # Mouse scroll up
                    scroll_direction = 1
                elif event.button == 5:  # Mouse scroll down
                    scroll_direction = -1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in (4, 5):  # Mouse scroll released
                    scroll_direction = 0

        # Scroll the buttons
        for i in range(len(buttons)):
            buttons[i] = (buttons[i][0].move(0, scroll_speed * scroll_direction), buttons[i][1])

        # Wrap the buttons to the next row when reaching the bottom of the screen
        if scroll_direction == -1 and buttons[0][0].top > screen_height:
            buttons = buttons[buttons_per_column:] + buttons[:buttons_per_column]
        elif scroll_direction == 1 and buttons[-1][0].bottom < 0:
            buttons = buttons[-buttons_per_column:] + buttons[:-buttons_per_column]

        # Clear the screen
        screen.fill(BLACK)

        # Draw buttons on the screen
        for button_rect, button_text in buttons:
            pygame.draw.rect(screen, WHITE, button_rect)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)

        pygame.display.flip()
