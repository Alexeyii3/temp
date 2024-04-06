import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Test")

# Цвета
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Переменные игры
start_button = pygame.Rect(220, 100, 200, 100)
reaction_button = pygame.Rect(220, 100, 200, 100)
button_color = red
font = pygame.font.Font(None, 36)
game_started = False
start_time = 0
reaction_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos) and game_started == False:
                game_started = True
                start_time = time.time() + random.uniform(2, 5)
                button_color = red
                reaction_time = 0
            elif reaction_button.collidepoint(mouse_pos) and game_started == True:
                reaction_time = round((time.time() - start_time) * 1000)
                game_started = False
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    if game_started:
        if time.time() > start_time:
            button_color = green

        pygame.draw.rect(screen, button_color, reaction_button)
        text = font.render("Нажми на меня!", True, white)
        screen.blit(text, (reaction_button.x + 10, reaction_button.y + 35))
    else:
        pygame.draw.rect(screen, red, start_button)
        text = font.render("Начать игру", True, white)
        screen.blit(text, (start_button.x + 30, start_button.y + 35))

        if reaction_time:
            result_text = font.render(f"Ваше время: {reaction_time} мс", True, white)
            screen.blit(result_text, (220, 300))
    pygame.display.flip()

pygame.quit()