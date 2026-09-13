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
POPUP_BG_COLOR = (255, 255,255)
POPUP_BORDER_COLOR = (255, 182, 193)
POPUP_TEXT_COLOR = (90, 60, 90)
POPUP_BUTTON_COLOR = (255, 214, 224)
POPUP_BUTTON_HOVER_COLOR = (255, 160, 190)
POPUP_BUTTON_TEXT_COLOR = (90, 60, 90)

#Fonts -----------------------------------------------------------------------------------

title_font = pygame.font.SysFont("shootingstar", 80, bold=False)
button_font = pygame.font.SysFont("shootingstar", 48, bold=False)
placeholder_font = pygame.font.SysFont("shootingstar", 28, bold=False)
closet_font = pygame.font.SysFont("shootingstar", 30, bold=False)
popup_font = pygame.font.SysFont("shootingstar", 26, bold=False)
accessory_popup_font = pygame.font.SysFont("shootingstar", 22, bold=False)
popup_button_font = pygame.font.SysFont("shootingstar", 24, bold=False)

#Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Text shadow -----------------------------------------------------------------------------------------

def draw_text_with_shadow(text, font, text_color, position):
    shadow = font.render(text, True, (0, 0, 0))
    shadow.set_alpha(100)
    screen.blit(shadow, (position[0] + 2, position[1] + 2))

    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, position)

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

#Background images ----------------------------------------------------------------------------------------


title_background_image = pygame.image.load("assets/backgrounds/title_background.jpeg").convert()
title_background_image = pygame.transform.smoothscale(title_background_image, (WIDTH, HEIGHT))

game_background_image = pygame.image.load("assets/backgrounds/game_background.jpeg").convert()
game_background_image = pygame.transform.smoothscale(game_background_image, (WIDTH, HEIGHT))

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
#Accessory Closet -----------------------------------------------------------------------------------

accessory_closet_rect = closet_panel_rect.copy()
accessory_section_height = accessory_closet_rect.height / 2

accessory_slots = []
for i in range(2):
    accessory_slot_rect = pygame.Rect(
        accessory_closet_rect.left,
        accessory_closet_rect.top + i * accessory_section_height,
        accessory_closet_rect.width,
        accessory_section_height
    )

    accessory_slots.append({
        "rect": accessory_slot_rect,
        "accessory_index": i,
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

accessory_options = [
    {"name": "Gold Jewelry", "image": "Assets/Accessories/Accessory 1.png"},
    {"name": "Silver Jewelry", "image": "Assets/Accessories/Accessory 2.png"},
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
load_clothing_images(accessory_options)

#Clothing Dictionaries ----------------------------------------------------------------------------------------

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

equipped_accessory = None

DRAW_ORDER = ["shoe", "bottom", "top", "hair"]

#Intro Pop Up ----------------------------------------------------------------------------------------

popup_stage = None

popup_rect = pygame.Rect(0, 0, 520, 320)
popup_rect.center = (WIDTH // 2, HEIGHT // 2)

POPUP_GREETING_LINES = [
    "This diva is in dire need of",
    "a make-over! Can you help her",
    "choose an outfit?",
]

popup_button_width, popup_button_height = 200, 60

well_duh_rect = pygame.Rect(0, 0, popup_button_width, popup_button_height)
well_duh_rect.center = (popup_rect.centerx - 130, popup_rect.bottom - 70)

uhm_rect = pygame.Rect(0, 0, popup_button_width, popup_button_height)
uhm_rect.center = (popup_rect.centerx + 130, popup_rect.bottom - 70)

alright_fine_rect = pygame.Rect(0, 0, popup_button_width + 40, popup_button_height)
alright_fine_rect.center = (popup_rect.centerx, popup_rect.bottom - 70)

#Outfit Finilization ----------------------------------------------------------------------------------------

outfit_finalized = False
reveal_progress = 0.0
REVEAL_SPEED = 0.02

GROW_SCALE = 1.15
character_target_centerx = WIDTH // 2 - 10
character_start_centerx = character_rect.centerx

DOWNWARD_SHIFT = 80
character_start_bottom = character_rect.bottom
character_target_bottom = character_rect.bottom + DOWNWARD_SHIFT

DONE_BUTTON_SIZE = (160, 70)
done_button_rect = pygame.Rect(0, 0, DONE_BUTTON_SIZE[0], DONE_BUTTON_SIZE[1])
done_button_rect.center = ((character_rect.right + closet_panel_rect.left) // 2, HEIGHT // 2)

closet_fade_rect = closet_panel_rect.inflate(20, 20)
closet_fade_surface = pygame.Surface(closet_fade_rect.size)
ccloset_fade_rect = closet_panel_rect.inflate(20, 20)
closet_fade_surface = game_background_image.subsurface(closet_fade_rect).copy()

#Accessory Prompt ----------------------------------------------------------------------------------------

accessory_prompt_stage = None
accessory_popup_rect = pygame.Rect(0, 0, 350, 150)
how_could_i_forget_rect = pygame.Rect(0, 0, 260, 60)

accessory_closet_showing = False

#Done Button 2 ----------------------------------------------------------------------------------------

final_done_button_rect = pygame.Rect(0, 0, DONE_BUTTON_SIZE[0], DONE_BUTTON_SIZE[1])
final_done_button_rect.center = ((character_rect.right + closet_panel_rect.left) // 2, HEIGHT // 2)

#Screen Transition ----------------------------------------------------------------------------------------
game_state = "title"
transitioning = False
fade_alpha = 0
fade_direction = 1

fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill(FADE_COLOR)

#Final Transition ------------------------------------------------------------------------------------------

final_transitioning = False
final_fade_alpha = 0

final_transition_stage = 0
final_stage_timer = 0

PAN_DURATION_FRAMES = 150
PAN_DURATION_FRAMES = 150

PAN_HOLD_FRAMES = 45
FINAL_ZOOM_SCALE = 2.5

FINAL_REVEAL_SCALE = 1.0

final_character_image = None

zoomed_full_surface = None

PAN_STAGES = [
    (90.20, 0.22, "left"),
    (0.35, 0.68, "right" ),
    (0.50, 1.00, "left"),
]

pan_surface = None
pan_rect = None

#Main Loop ------------------------------------------------------------------------------------------

clock = pygame.time.Clock()
running = True

while running:

    outfit_complete = (
            equipped_items["hair"] is not None
            and equipped_items["top"] is not None
            and equipped_items["bottom"] is not None
            and equipped_items["shoe"] is not None
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "title" and not transitioning and button_rect.collidepoint(event.pos):
                transitioning = True
                fade_direction = 1


            elif game_state == "game" and popup_stage == "greeting":
                if well_duh_rect.collidepoint(event.pos):
                    popup_stage = "closed"
                elif uhm_rect.collidepoint(event.pos):
                    popup_stage = "hesitant"


            elif game_state == "game" and popup_stage == "hesitant":
                if alright_fine_rect.collidepoint(event.pos):
                    popup_stage = "closed"


            elif game_state == "game" and accessory_prompt_stage == "showing":
                if how_could_i_forget_rect.collidepoint(event.pos):
                    accessory_prompt_stage = "closed"
                    accessory_closet_showing = True

            elif game_state == "game" and accessory_closet_showing:
                if equipped_accessory is not None and final_done_button_rect.collidepoint(event.pos):
                    final_transitioning = True
                    final_transition_stage = 0
                    final_dade_alpha = 0
                    final_stage_timer = 0

                    final_character_image = character_image.copy()

                    for category in DRAW_ORDER:
                        if equipped_itmes[category] is not None:
                            final_character_image.blit(equipped_items[category],(0, 0))

                    if equipped_accessory is not None:
                        final_character_image.blit(equipped_accessory, (0, 0))

        #Shadows

                    final_character_shadow = final_character_image.copy()
                    final_character_shadow.fill(
                        (0, 0, 0, 100),
                        special_flags=pygame.BLEND_RGBA_MULT
                    )
                else:
                    for slot in accessory_slots:
                        if slot["rect"].collidepoint(event.pos):
                            current_accessory = accessory_options[slot["accessory_index"]]
                            accessory = current_accessory["surface"]

                            grown_width = int(accessory.get_width() * GROW_SCALE)
                            grown_height = int(accessory.get_height() * GROW_SCALE)

                            equipped_accessory = pygame.transform.smoothscale(
                                accessory,
                                (grown_width, grown_height)
                            )

            elif game_state == "game" and accessory_closet_showing:
                for slot in accessory_slots:
                    if slot["rect"].collidepoint(event.pos):
                        current_accessory = accessory_options[slot["accessory_index"]]
                        accessory = current_accessory["surface"]

                        grown_width = int(accessory.get_width() * GROW_SCALE)

                        grown_height = int(accessory.get_height() * GROW_SCALE)

                        equipped_accessory = pygame.transform.smoothscale(

                            accessory,
                        (grown_width, grown_height)

                        )

            elif game_state == "game" and popup_stage == "closed" and not accessory_closet_showing:
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


                if outfit_complete and not outfit_finalized and done_button_rect.collidepoint(event.pos):
                    outfit_finalized = True
                    reveal_progress = 0.0

                    new_width = int(character_image.get_width() * GROW_SCALE)
                    new_height = int(character_image.get_height() * GROW_SCALE)
                    character_image = pygame.transform.smoothscale(character_image, (new_width, new_height))
                    character_rect = character_image.get_rect(center=character_rect.center)

                    for category in equipped_items:
                        equipped_surface = equipped_items[category]
                        if equipped_surface is not None:
                            grown_width = int(equipped_surface.get_width() * GROW_SCALE)
                            grown_height = int(equipped_surface.get_height() * GROW_SCALE)
                            equipped_items[category] = pygame.transform.smoothscale(
                                equipped_surface, (grown_width, grown_height)
                             )

                    character_start_centerx = character_rect.centerx
                    character_start_bottom = character_rect.bottom

                    accessory_popup_rect.midright = (
                        character_target_centerx - character_rect.width // 2 + 300,
                        character_target_bottom - character_rect.height // 2 - 80
                    )
                    how_could_i_forget_rect.center = (accessory_popup_rect.centerx, accessory_popup_rect.bottom - 17)


    if game_state == "title":

        # Drawing the background
        screen.fill(title_background_image, (0, 0))

        # Drawing the title
        draw_text_with_shadow(
            "DRESS UP DIBA",
            title_font,
            TITLE_COLOR,
            title_rect.topleft
        )

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
        screen.fill(Ggame_background_image, (0, 0))

        if accessory_prompt_stage == "showing":
            pygame.draw.rect(screen, POPUP_BORDER_COLOR, accessory_popup_rect.inflate(10, 10), border_radius=25)
            pygame.draw.rect(screen, POPUP_BG_COLOR, accessory_popup_rect, border_radius=20)

            accessory_line = accessory_popup_font.render("Wait, what about accessories?", True, POPUP_TEXT_COLOR)
            accessory_line_rect = accessory_line.get_rect(
                center=(accessory_popup_rect.centerx, accessory_popup_rect.top + 60))
            screen.blit(accessory_line, accessory_line_rect)

            mouse_pos = pygame.mouse.get_pos()
            if how_could_i_forget_rect.collidepoint(mouse_pos):
                forget_color = POPUP_BUTTON_HOVER_COLOR
            else:
                forget_color = POPUP_BUTTON_COLOR
            pygame.draw.rect(screen, forget_color, how_could_i_forget_rect, border_radius=20)
            forget_text = popup_button_font.render("How could I forget!", True, POPUP_BUTTON_TEXT_COLOR)
            forget_text_rect = forget_text.get_rect(center=how_could_i_forget_rect.center)
            screen.blit(forget_text, forget_text_rect)

        #Draw character shadow

        character_shadow = character_image.copy()
        character_shadow.fill((0, 0, 0, 100), speical_flags=pygame.BLEND_RGBA_MULT)

        screen.blit(
            character_shadow,
            character_rect.x + 6, character_rect.y = 6)
        )

        #Draw character
        screen.blit(character_image, character_rect)

        for category in DRAW_ORDER:
            equipped_surface = equipped_items[category]
            if equipped_surface is not None:
                screen.blit(equipped_surface, character_rect)

        if equipped_accessory is not None:
            screen.blit(equipped_accessory, character_rect)

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

            if outfit_complete and not outfit_finalized:
                mouse_pos = pygame.mouse.get_pos()
                if done_button_rect.collidepoint(mouse_pos):
                    done_color= BUTTON_HOVER_COLOR
                else:
                    done_color = BUTTON_COLOR
                pygame.draw.rect(screen, done_color, done_button_rect, border_radius=25)

                done_text = button_font.render("DONE", True, BUTTON_TEXT_COLOR)
                done_text_rect = done_text.get_rect(center=done_button_rect.center)
                screen.blit(done_text, done_text_rect)

    #Accessory Closet

        if accessory_closet_showing:
            pygame.draw.rect(screen, CLOSET_PANEL_COLOR, accessory_closet_rect, border_radius=25)
            inner_panel_rect = accessory_closet_rect.inflate(-10, -10)
            pygame.draw.rect(screen, CLOSET_PANEL_COLOR, inner_panel_rect, border_radius=20)

            line_y = accessory_closet_rect.centery
            pygame.draw.line(
                screen, CLOSET_SEPERATOR_COLOR,
                (accessory_closet_rect.left + 15, line_y),
                (accessory_closet_rect.right - 15, line_y),
                3
            )

            for slot in accessory_slots:
                current_accessory = accessory_options[slot["accessory_index"]]
                thumbnail = current_accessory["thumbnail"]
                thumbnail_rect = thumbnail.get_rect(center=slot["rect"].center)
                screen.blit(thumbnail, thumbnail_rect)

        if equipped_accessory is not None:
            mouse_pos = pygame.mouse.get_pos()

            if final_done_button_rect.collidepoint(mouse_pos):
                final_done_color = BUTTON_HOVER_COLOR
            else:
                final_done_color = BUTTON_COLOR

            pygame.draw.rect(screen, final_done_color, final_done_button_rect, border_radius=25)

            final_done_text = button_font.render("DONE", True, BUTTON_TEXT_COLOR)

            final_done_text_rect = final_done_text.get_rect(center=final_done_button_rect.center)

            screen.blit(final_done_text, final_done_text_rect)
)
    #Intro Pop-Up
        if popup_stage in ("greeting", "hesitant"):
            pygame.draw.rect(screen, POPUP_BORDER_COLOR, popup_rect.inflate(10, 10), border_radius=25)

            if popup_stage == "greeting":
                lines_to_show = POPUP_GREETING_LINES
            else:
                lines_to_show = ["..."]

            line_y = popup_rect.top + 50
            for line in lines_to_show:
                line_surface = popup_font.render(line, True, POPUP_TEXT_COLOR)
                line_rect = line_surface.get_rect(center=(popup_rect.centerx, line_y))
                screen.blit(line_surface, line_rect)
                line_y += 40

            mouse_pos = pygame.mouse.get_pos()

            if popup_stage == "greeting":
                if well_duh_rect.collidepoint(mouse_pos):
                    well_duh_color = POPUP_BUTTON_HOVER_COLOR

                else:
                    well_duh_color = POPUP_BUTTON_COLOR
                pygame.draw.rect(screen, well_duh_color, well_duh_rect, border_radius=20)
                well_duh_text = popup_button_font.render("Well duh!", True, POPUP_BUTTON_TEXT_COLOR)
                well_duh_text_rect = well_duh_text.get_rect(center=well_duh_rect.center)
                screen.blit(well_duh_text, well_duh_text_rect)

                if uhm_rect.collidepoint(mouse_pos):
                    uhm_color = POPUP_BUTTON_HOVER_COLOR
                else:
                    uhm_color = POPUP_BUTTON_COLOR
                pygame.draw.rect(screen, uhm_color, uhm_rect, border_radius=20)
                uhm_text = popup_button_font.render("Uhm..", True, POPUP_BUTTON_TEXT_COLOR)
                uhm_text_rect = uhm_text.get_rect(center=uhm_rect.center)
                screen.blit(uhm_text, uhm_text_rect)

            else:
                if alright_fine_rect.collidepoint(mouse_pos):
                    alright_fine_color = POPUP_BUTTON_HOVER_COLOR
                else:
                    alright_fine_color = POPUP_BUTTON_COLOR
                pygame.draw.rect(screen, alright_fine_color, alright_fine_rect, border_radius=20)
                alright_fine_text = popup_button_font.render("Alright fine", True, POPUP_BUTTON_TEXT_COLOR)
                alright_fine_text_rect = alright_fine_text.get_rect(center=alright_fine_rect.center)
                screen.blit(alright_fine_text, alright_fine_text_rect)

    #Fade transition
    if transitioning:
        fade_alpha += FADE_SPEED * fade_direction

        if fade_alpha >= 255 and fade_direction == 1:

            fade_alpha = 255
            game_state = "game"
            fade_direction = -1

        elif fade_alpha <= 0 and fade_direction == -1:
            fade_alpha = 0
            transitioning = False
            if popup_stage is None:
                popup_stage = "greeting"

    if fade_alpha > 0:
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

    #Final Transition

    if final_transitioning or final_transition_stage > 0:

        if final_transition_stage == 0:
            finale_fade_alpha += 5
            if final_fade_alpha >= 255:
                final_fade_alpha = 255
                final_transition_stage = 1
                final_stage_timer = 0

                zoom_width = int(final_charcter_image.get_width() * FINAL_ZOOM_SCALE)
                zoom_height = int(final_character_image.get_height() * FINAL_ZOOM_SCALE)
                zoomed_full_surface = pygame.transform.smoothscale(final_character_image, (zoom_width, zoom_height))

                shadow_width = int(final_character_shadow.get_width() * FINAL_ZOOM_SCALE)
                shadow_height = int(final_character_shadow.get_height() * FINAL_ZOOM_SCALE)

                zoomed_shadow_surface = pygame.transform.smoothscale(
                    final_character_shadow, (shadow_width, shadow_height)
                )

            fade_surface.set_alpha(final_fade_alpha)
            screen.blit(fade_surface, (0, 0))

        elif final_transition_stage in (1, 2, 3):
            screen.blit(title_background_image, (0, 0))

            stage_index = final_transition_stage - 1
            top_fraction, bottom_fraction, slide_from = PAN_STAGES[stage_index]

            pan_progress = final_stage_timer / PAN_DURATION_FRAMES

            if pan_progress > 1:
                pan_progress = 1

            target_y_in_image = int(zoomed_full_surface.get_height() * (top_fraction + bottom_fraction) /2)
            zoomed_rect = zoomed_full_surface.get_rect()
            zoomed_rect.top = HEIGHT // 2 - target_y_in_image

            if slide_from == "left":
                start_x = -zoomed_rect.width // 2
            else:
                start_x = WIDTH + zoomed_rect.width // 2
            end_x = WIDTH //2
            zoomed_rct.centerx = int(start_x + (end_x - start_x) * pan_progress)


    #Outfit Reveal
    if outfit_finalized and reveal_progress < 1:
        reveal_progress += REVEAL_SPEED
        if reveal_progress > 1:
            reveal_progress = 1

        character_rect.centerx = int(
            character_start_centerx + (character_target_centerx - character_start_centerx) * reveal_progress
        )
        character_rect.bottom = int(
            character_start_bottom + (character_target_bottom - character_start_bottom) * reveal_progress
        )

        if reveal_progress >= 1 and accessory_prompt_stage is None:
            accessory_prompt_stage = "showing"

    if outfit_finalized and not accessory_closet_showing:
        closet_fade_alpha = int(255 * reveal_progress)
        if closet_fade_alpha > 0:
            closet_fade_surface.set_alpha(closet_fade_alpha)
            screen.blit(closet_fade_surface, closet_fade_rect.topleft)

#Update the game --------------------------------------------------------------------------------------

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
