"""
Generative Pixelated Pusheen Cat - REFACTORED VERSION

Refactoring improvements:
- Added main() function
- Defined constants at top
- Created modular functions with arguments/returns
- Better naming conventions
- Added comprehensive comments
- Improved code structure and readability
"""

from turtle import *
import random

# ============== CONSTANTS (Global Variables) ==============
# Canvas settings
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
BACKGROUND_COLOR = 'white'

# Drawing settings
PIXEL_SIZE = 15
GRID_WIDTH = 20
GRID_HEIGHT = 20

# Color palettes
GRAY_SHADES = ['#9b9b9b', '#a8a8a8', '#b5b5b5', '#c2c2c2', '#cfcfcf']
DARK_GRAY = ['#6b6b6b', '#787878', '#858585']
PINK_SHADES = ['#ff69b4', '#ff85c1', '#ffa1ce']
BLACK = '#000000'

# Pattern values (what each number means in the cat_pattern grid)
EMPTY = 0
BODY = 1
DARK = 2
PINK = 3
FEATURE = 4


# ============== HELPER FUNCTIONS ==============

def setup_canvas(width, height, bg_color):
    """

    Args:
        width (int): Canvas width in pixels
        height (int): Canvas height in pixels
        bg_color (str): Background color name or hex code

    Returns:
        None
    """
    setup(width, height)
    bgcolor(bg_color)
    tracer(0, 0)
    speed(0)
    hideturtle()


def get_pixel_color(pattern_value):
    """

    Args:
        pattern_value (int): Value from cat_pattern (0-4)

    Returns:
        str: Hex color code, or None if empty space
    """
    if pattern_value == EMPTY:
        return None
    elif pattern_value == BODY:
        return random.choice(GRAY_SHADES)
    elif pattern_value == DARK:
        return random.choice(DARK_GRAY)
    elif pattern_value == PINK:
        return random.choice(PINK_SHADES)
    elif pattern_value == FEATURE:
        return BLACK
    else:
        # Fallback for unexpected values
        return GRAY_SHADES[0]


def draw_pixel(x, y, size, fill_color):
    """

    Args:
        x (int): X-coordinate of top-left corner
        y (int): Y-coordinate of top-left corner
        size (int): Width/height of the square in pixels
        fill_color (str): Hex color code for the fill

    Returns:
        None
    """
    penup()
    goto(x, y)
    pendown()

    color(BLACK)
    fillcolor(fill_color)
    pensize(1)

    # Draw square
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()


def calculate_grid_position(grid_width, grid_height, pixel_size):
    """

    Args:
        grid_width (int): Number of columns in the grid
        grid_height (int): Number of rows in the grid
        pixel_size (int): Size of each pixel

    Returns:
        tuple: (start_x, start_y) coordinates for top-left corner
    """
    start_x = -((grid_width * pixel_size) / 2)
    start_y = ((grid_height * pixel_size) / 2)
    return start_x, start_y


def get_cat_pattern():
    """

    Pattern values:
    0 = empty space
    1 = body (gray)
    2 = dark areas (ears, stripes)
    3 = pink (cheeks)
    4 = black features (eyes, nose, feet)

    Returns:
        list: 2D list representing the cat pattern (20x20 grid)
    """
    return [
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],  # Ears
        [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # Head
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 0],  # Eyes
        [0, 1, 1, 4, 4, 1, 1, 1, 4, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 0],  # Eyes + nose
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1],  # Cheeks
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Body
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],  # Stripes
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 4, 4, 1, 1, 1, 0, 0, 1, 1, 1, 4, 4, 1, 1, 0, 0],  # Feet
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    ]


def draw_cat_body(pattern, start_x, start_y, pixel_size):
    """

    Args:
        pattern (list): 2D list representing the cat pattern
        start_x (float): X-coordinate of grid's top-left corner
        start_y (float): Y-coordinate of grid's top-left corner
        pixel_size (int): Size of each pixel square

    Returns:
        None
    """
    grid_height = len(pattern)
    grid_width = len(pattern[0])

    # Nested loops to iterate through the pattern
    for row in range(grid_height):
        for col in range(grid_width):
            # Get pattern value at this position
            pattern_value = pattern[row][col]

            # Calculate pixel position
            x = start_x + (col * pixel_size)
            y = start_y - (row * pixel_size)

            # Determine color based on pattern value
            pixel_color = get_pixel_color(pattern_value)

            # Draw pixel if it's not empty
            if pixel_color is not None:
                draw_pixel(x, y, pixel_size, pixel_color)


def draw_whiskers(left_x, right_x, center_y, whisker_length):
    """

    Args:
        left_x (int): X-coordinate for left whisker starting point
        right_x (int): X-coordinate for right whisker starting point
        center_y (int): Y-coordinate for middle whisker
        whisker_length (int): How far whiskers extend

    Returns:
        None
    """
    color(BLACK)
    pensize(2)

    # Left whiskers (3 whiskers)
    whisker_positions = [
        (center_y + 20, 30),  # Top whisker
        (center_y + 10, 10),  # Middle whisker
        (center_y, -10)  # Bottom whisker
    ]

    for start_y, end_offset in whisker_positions:
        penup()
        goto(left_x, start_y)
        pendown()
        goto(left_x - whisker_length, start_y + end_offset)

    # Right whiskers (3 whiskers)
    for start_y, end_offset in whisker_positions:
        penup()
        goto(right_x, start_y)
        pendown()
        goto(right_x + whisker_length, start_y + end_offset)


def finalize_drawing():
    """

    Returns:
        None
    """
    hideturtle()
    update()
    print("Pusheen complete!")
    done()


# ============== MAIN FUNCTION ==============

def main():
    """

    Returns:
        None
    """
    # Step 1: Setup the canvas
    setup_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, BACKGROUND_COLOR)

    # Step 2: Get the cat pattern
    cat_pattern = get_cat_pattern()

    # Step 3: Calculate grid position
    start_x, start_y = calculate_grid_position(GRID_WIDTH, GRID_HEIGHT, PIXEL_SIZE)

    # Step 4: Draw the cat body
    draw_cat_body(cat_pattern, start_x, start_y, PIXEL_SIZE)

    # Step 5: Draw whiskers
    whisker_left_x = -120
    whisker_right_x = 120
    whisker_center_y = 20
    whisker_length = 60
    draw_whiskers(whisker_left_x, whisker_right_x, whisker_center_y, whisker_length)

    # Step 6: Finalize and display
    finalize_drawing()


# ============== PROGRAM ENTRY POINT ==============
if __name__ == "__main__":
    main()