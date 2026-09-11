#--------------------------------------------------------------------------------------------------
####################################################################################################
#Dress Up Diva! Fashion Game <3   by : Anoushka Wehlisch 4008031
####################################################################################################
#---------------------------------------------------------------------------------------------------

import pygame
import sys


#Set Up --------------------------------------------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 1100, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dress Up Diva")

#Design Settings -----------------------------------------------------------------------------------
BACKGROUND_COLOR = (255, 214, 235)
TITLE_COLOR = (255, 105, 180)
BUTTON_COLOR = (255, 105, 180)
BUTTON_HOVER_COLOR = (255, 105, 180)
BUTTON_TEXT_COLOR = (255, 255, 255)

#Fonts

title_font = pygame.font.SysFont("comicsansms", 80, bold=True)
button_font = pygame.font.SysFont("comicsansms", 48, bold=True)

#Title Text -----------------------------------------------------------------------------------------
title_text = title_font.render("Dress Up Diva", True, TITLE_COLOR)
title_rect = title_text.get_rect(center=(WIDTH // 2, 170))

#Play Button ----------------------------------------------------------------------------------------
button_width, button_height = 260, 90
button_rect = pygame.Rect(0, 0, button_width, button_height)
button_rect.center = (WIDTH // 2, 400)

button_text = button_font.render("PLAY", True, BUTTON_TEXT_COLOR)
BUTTON_HOVER_SCALE = 1.15

#Main Loop ------------------------------------------------------------------------------------------

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Play button clicked!")

    #Drawing the background -------------------------------------------------------------------------
    screen.fill(BACKGROUND_COLOR)

    #Drawing the title ------------------------------------------------------------------------------
    screen.blit(title_text, title_rect)

    #Drawing the button ------------------------------------------------------------------------------
    mouse_pos = pygame.mouse.get_pos()
    is_hovering = button_rect.collidepoint(mouse_pos)
    is_pressed = is_hovering and pygame.mouse.get_pressed()[0]

    if is_hovering or is_pressed:
        scale = BUTTON_HOVER_SCALE
        color = BUTTON_HOVER_COLOR
    else:
        scale = 1.0
        color = BUTTON_COLOR


    scaled_rect = pygame.Rect(0, 0, int(button_width * scale), int(button_height * scale))
    scaled_rect.center = button_rect.center
    pygame.draw.rect(screen, color, scaled_rect, border_radius=35)

    scaled_button_text = pygame.transform.rotozoom(button_text, 0, scale)
    scaled_button_text_rect = scaled_button_text.get_rect(center=scaled_rect.center)

#Update the game --------------------------------------------------------------------------------------

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
