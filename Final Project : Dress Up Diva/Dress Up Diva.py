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
GAME_BACKGROUND_COLOR = (200, 230, 255)
FADE_COLOR = (0, 0, 0)
FADE_SPEED = 3
CLOSET_PANEL_COLOR = (255, 214, 224)
CLOSET_PANEL_BORDER_COLOR = (232, 193, 140)
CLOSET_SEPERATOR_COLOR = (255, 255, 255)
CLOSET_ARROW_COLOR = (255, 160, 190)

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

#Character Artwork ----------------------------------------------------------------------------------------
character_image = pygame.image.load("assets/character_base.png")

CHARACTER_HEIGHT = 750
scale_factor = CHARACTER_HEIGHT / character_image.get_height()
character_width = int(character_image.get_width() * scale_factor)
character_image = pygame.transform.smoothscale(character_image, (character_width, CHARACTER_HEIGHT))

character_rect = character_image.get_rect()
character_rect.centerx = WIDTH // 4
character_rect.bottom = HEIGHT - 10

#Closet Layout ----------------------------------------------------------------------------------------
closet_panel_rect = pygame.Rect(0, 0, 280, 680)
closet_panel_rect.center = (WIDTH * 3 // 4, HEIGHT // 2)

closet_categories = ["hair", "top", "bottom", "shoe"]

ARROW_SIZE = 40

closet_slot_height = closet_panel_rect.height / len(closet_categories)

closet_slots = []
for i, category in enumerate(closet_categories):
    slot_rect = pygame.Rect(0, 0, closet_panel_rect.width - ARROW_SIZE * 2, closet_slot_height)
    slot_rect.centerx = closet_panel_rect.centerx
    slot_rect.top = closet_panel_rect.top + i * closet_slot_height

    left_arrow_rect = pygame.Rect(0, 0, ARROW_SIZE, ARROW_SIZE)
    left_arrow_rect.center = (closet_panel_rect.left + ARROW_SIZE // 2 + 10, slot_rect.centery)

    right_arrow_rect = pygame.Rect(0, 0, ARROW_SIZE, ARROW_SIZE)
    right_arrow_rect.center = (closet_panel_rect.right - ARROW_SIZE // 2 - 10, slot_rect.centery)

    closet_slots.append({
        "category": category,
        "rect": slot_rect,
        "left_arrow_rect": left_arrow_rect,
        "right_arrow_rect": right_arrow_rect,
        "selected_index": 0,
    })

#Clothing Options ----------------------------------------------------------------------------------------
hair_options = [
     {"name": "Black Long Hair", "image": "Assets/Hair/Hair 1.png"},
     {"name": "Blonde Half Up Half Down", "image": "Assets/Hair/Hair 2.png"},
     {"name": "Red Bob", "image": "Assets/Hair/Hair 3.png"},
     {"name": "Navy Bun", "image": "Assets/Hair/Hair 4.png"},
     {"name": "Brown Space Buns", "image": "Assets/Hair/Hair 5.png"},
 ]

top_options = [
    {"name": "Black 3/4 Sleeve", "image": "Assets/Tops/Top 1.png"},
    {"name": "Pink Tube Top", "image": "Assets/Tops/Top 2.png"},
    {"name": "Yellow Turtle Neck", "image": "Assets/Tops/Top 3.png"},
    {"name": "Green Tank Top", "image": "Assets/Tops/Top 4.png"},
    {"name": "Grey Hoodie", "image": "Assets/Tops/Top 5.png"},
]

bottom_options = [
    {"name": "Jeans", "image": "Assets/Bottoms/Bottom 1.png"},
    {"name": "Black Shorts", "image": "Assets/Bottoms/Bottom 2.png"},
    {"name": "Striped Skirt", "image": "Assets/Bottoms/Bottom 3.png"},
    {"name": "Dark Joggers", "image": "Assets/Bottoms/Bottom 4.png"},
    {"name": "Jean Capris", "image": "Assets/Bottoms/Bottom 5.png"},
]

shoe_options = [
    {"name": "Brown Boots", "image": "Assets/Shoes/Shoes 1.png"},
    {"name": "White Flats", "image": "Assets/Shoes/Shoes 2.png"},
    {"name": "Blue Sneakers", "image": "Assets/Shoes/Shoes 3.png"},
    {"name": "Red Boots", "image": "Assets/Shoes/Shoes 4.png"},
    {"name": "Black Heels", "image": "Assets/Shoes/Shoes 5.png"},
]


 #Clothing Loading ----------------------------------------------------------------------------------------
THUMBNAIL_MAX_SIZE = (150, 120)


def load_clothing_images(options_list):
    for item in options_list:
        image = pygame.image.load(item["image"]).convert_alpha()

        scaled_width = int(image.get_width() * scale_factor)
        scaled_height = int(image.get_height() * scale_factor)
        item["surface"] = pygame.transform.smoothscale(image, (scaled_width, scaled_height))

        content_rect = image.get_bounding_rect()
        cropped = image.subsurface(content_rect).copy()

        thumb_scale = min(
            THUMBNAIL_MAX_SIZE[0] / cropped.get_width(),
            THUMBNAIL_MAX_SIZE[1] / cropped.get_height()
        )
        thumb_size = (int(cropped.get_width() * thumb_scale), int(cropped.get_height() * thumb_scale))
        item["thumbnail"] = pygame.transform.smoothscale(cropped, thumb_size)

load_clothing_images(hair_options)
load_clothing_images(top_options)
load_clothing_images(bottom_options)
load_clothing_images(shoe_options)

 #Clothing Dictionaries
category_options = {
 "hair": hair_options,
 "top": top_options,
 "bottom": bottom_options,
 "shoe": shoe_options,
}

equipped_items = {
 "hair": None,
 "top": None,
 "bottom": None,
 "shoe": None,
}

DRAW_ORDER = ["shoe", "bottom", "top", "hair"]

#Screen Transition
game_state = "title"
transitioning = False
fade_alpha = 0
fade_direction = 1

fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill(FADE_COLOR)

#Main Loop ------------------------------------------------------------------------------------------

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "title" and not transitioning and button_rect.collidepoint(event.pos):
                transitioning = True
                fade_direction = 1

            elif game_state == "game":
                for slot in closet_slots:
                    options_list = category_options[slot["category"]]

                    if len(options_list) == 0:
                        continue

                    if slot["left_arrow_rect"].collidepoint(event.pos):
                        slot["selected_index"] = (slot["selected_index"] - 1) % len(options_list)

                    elif slot["right_arrow_rect"].collidepoint(event.pos):
                        slot["selected_index"] = (slot["selected_index"] + 1) % len(options_list)

                    elif slot["rect"].collidepoint(event.pos):
                        current_item = options_list[slot["selected_index"]]
                        equipped_items[slot["category"]] = current_item["surface"]

    if game_state == "title":

        # Drawing the background
        screen.fill(BACKGROUND_COLOR)

        # Drawing the title
        screen.blit(title_text, title_rect)

        # Drawing the button
        mouse_pos = pygame.mouse.get_pos()
        is_hovering = button_rect.collidepoint(mouse_pos)
        is_pressed = is_hovering and pygame.mouse.get_pressed()[0]

        if is_hovering or is_pressed:
            scale = BUTTON_HOVER_SCALE
            color = BUTTON_HOVER_COLOR
        else:
            scale = 1.0
            color = BUTTON_COLOR

        scaled_rect = pygame.Rect(
            0, 0,
            int(button_width * scale),
            int(button_height * scale)
        )

        scaled_rect.center = button_rect.center

        pygame.draw.rect(
            screen,
            color,
            scaled_rect,
            border_radius=35
        )

        scaled_button_text = pygame.transform.rotozoom(
            button_text, 0, scale
        )

        scaled_button_text_rect = scaled_button_text.get_rect(
            center=scaled_rect.center
        )

        screen.blit(
            scaled_button_text,
            scaled_button_text_rect
        )



    elif game_state == "game":

        #Drawing the background
        screen.fill(GAME_BACKGROUND_COLOR)

        #Drawing the character
        screen.blit(character_image, character_rect)

        for category in DRAW_ORDER:

            equipped_surface = equipped_items[category]

            if equipped_surface is not None:
                screen.blit(equipped_surface, character_rect)

        pygame.draw.rect(screen, CLOSET_PANEL_BORDER_COLOR, closet_panel_rect, border_radius=25)

        inner_panel_rect = closet_panel_rect.inflate(-10, -10)

        pygame.draw.rect(screen, CLOSET_PANEL_COLOR, inner_panel_rect, border_radius=20)

        for i, slot in enumerate(closet_slots):
            if i > 0:
                line_y = slot["rect"].top
                pygame.draw.line(
                    screen, CLOSET_SEPERATOR_COLOR,
                    (closet_panel_rect.left + 15, line_y),
                    (closet_panel_rect.right - 15, line_y),
                    3
                )

            la = slot["left_arrow_rect"]
            pygame.draw.polygon(screen, CLOSET_ARROW_COLOR, [
                (la.right, la.top),
                (la.right, la.bottom),
                (la.left, la.centery),
            ])

            ra = slot["right_arrow_rect"]
            pygame.draw.polygon(screen, CLOSET_ARROW_COLOR, [
                (ra.left, ra.top),
                (ra.left, ra.bottom),
                (ra.right, ra.centery),
            ])

            options_list = category_options[slot["category"]]
            if len(options_list) > 0:
                current_item = options_list[slot["selected_index"]]
                thumbnail = current_item["thumbnail"]
                thumbnail_rect = thumbnail.get_rect(center=slot["rect"].center)
                screen.blit(thumbnail, thumbnail_rect)
    #Fade transitiom
    if transitioning:
        fade_alpha += FADE_SPEED * fade_direction

        if fade_alpha >= 255 and fade_direction == 1:

            fade_alpha = 255
            game_state = "game"
            fade_direction = -1

        elif fade_alpha <= 0 and fade_direction == -1:
            fade_alpha = 0
            transitioning = False

    if fade_alpha > 0:
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

#Update the game --------------------------------------------------------------------------------------

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
