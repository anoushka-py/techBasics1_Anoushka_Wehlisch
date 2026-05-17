

from turtle import *
import random

# Setup
width = 600
height = 600
setup(width, height)

# Turn off animation for instant result
tracer(0, 0)

# Background
bgcolor('white')

# Drawing settings
speed(0)
hideturtle()

# Color Palette
# Gray shades for cat body
gray_shades = ['#9b9b9b', '#a8a8a8', '#b5b5b5', '#c2c2c2', '#cfcfcf']
dark_gray = ['#6b6b6b', '#787878', '#858585']  # For stripes/ears
pink_shades = ['#ff69b4', '#ff85c1', '#ffa1ce']  # For cheeks
black = '#000000'  # Outline and features


def draw_pixel(x, y, size, fill_color):
    penup()
    goto(x, y)
    pendown()

    color(black)
    fillcolor(fill_color)
    pensize(1)

    # Draw square
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()


# Main Drawing Function
def draw_pusheen():

    pixel_size = 15

    # Defining the cat pattern as a grid (1 = body, 2 = dark, 3 = pink, 0 = empty)
    # 20 rows × 20 columns
    cat_pattern = [
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],  # Row 0 (ears)
        [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0],  # Row 1
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0],  # Row 2
        [0, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 0],  # Row 3
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # Row 4 (head starts)
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # Row 5
        [0, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 0],  # Row 6 (eyes)
        [0, 1, 1, 4, 4, 1, 1, 1, 4, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 0],  # Row 7 (eyes + nose)
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # Row 8
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # Row 9
        [1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1],  # Row 10 (pink cheeks)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Row 11 (body)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Row 12
        [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],  # Row 13 (stripe)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Row 14
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Row 15
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # Row 16
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # Row 17
        [0, 0, 1, 1, 4, 4, 1, 1, 1, 0, 0, 1, 1, 1, 4, 4, 1, 1, 0, 0],  # Row 18 (feet)
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # Row 19 (feet)
    ]

    grid_width = len(cat_pattern[0])
    grid_height = len(cat_pattern)
    start_x = -((grid_width * pixel_size) / 2)
    start_y = ((grid_height * pixel_size) / 2)

    # Nested Loops
    for row in range(grid_height):  # OUTER LOOP: rows
        for col in range(grid_width):  # INNER LOOP: columns

            pixel_value = cat_pattern[row][col]

            x = start_x + (col * pixel_size)
            y = start_y - (row * pixel_size)

            # Conditionals

            if pixel_value == 0:
                continue

            elif pixel_value == 1:
                pixel_color = random.choice(gray_shades)

            elif pixel_value == 2:
                pixel_color = random.choice(dark_gray)

            elif pixel_value == 3:
                pixel_color = random.choice(pink_shades)

            elif pixel_value == 4:
                pixel_color = black

            else:
                pixel_color = gray_shades[0]

            draw_pixel(x, y, pixel_size, pixel_color)

    # Add whiskers
    penup()
    goto(-120, 20)
    pendown()
    color(black)
    pensize(2)

    # Left whiskers
    goto(-180, 30)
    penup()
    goto(-120, 10)
    pendown()
    goto(-180, 10)
    penup()
    goto(-120, 0)
    pendown()
    goto(-180, -10)

    # Right whiskers
    penup()
    goto(120, 20)
    pendown()
    goto(180, 30)
    penup()
    goto(120, 10)
    pendown()
    goto(180, 10)
    penup()
    goto(120, 0)
    pendown()
    goto(180, -10)

    # Finish
    hideturtle()
    update()
    print("Pusheen complete! 🐱")
    done()


# ============== RUN THE PROGRAM ==============
draw_pusheen()