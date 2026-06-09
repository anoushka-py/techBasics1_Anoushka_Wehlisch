
import pygame
import random
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = (15, 15, 30)
FPS = 60
IMAGE_FILE = "nyan_cat.png"



class NyanCat:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height


        scale = random.uniform(0.4, 1.0)
        base_width = 200
        base_height = 100
        self.width = int(base_width * scale)
        self.height = int(base_height * scale)


        self.x = random.randint(-300, -self.width)
        self.y = random.randint(50, screen_height - self.height - 50)


        self.speed_x = random.uniform(2.0, 5.0)


        self.bob_offset = random.uniform(0, math.pi * 2)
        self.bob_speed = random.uniform(0.05, 0.1)
        self.bob_amount = random.randint(5, 15)
        self.base_y = self.y


        self.color_offset = random.randint(0, 360)


    def update(self, frame):


        self.x += self.speed_x


        self.y = self.base_y + math.sin(frame * self.bob_speed + self.bob_offset) * self.bob_amount


        if self.x > self.screen_width + 50:
            self.x = random.randint(-300, -self.width)
            self.base_y = random.randint(50, self.screen_height - self.height - 50)
            self.speed_x = random.uniform(2.0, 5.0)   # New random speed on reset


    def draw(self, screen, image):

        screen.blit(image, (int(self.x), int(self.y)))



def load_image(file_name, width, height):

    try:
        image = pygame.image.load(file_name)
        image = pygame.transform.scale(image, (width, height))
        return image

    except FileNotFoundError:
        print(f"ERROR: Could not find '{file_name}'.")
        print("Make sure your image is in the same folder as this script!")
        pygame.quit()
        exit()



def draw_background(screen, stars):


    screen.fill(BACKGROUND_COLOR)


    for (x, y, size) in stars:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), size)


def generate_stars(screen_width, screen_height, count=80):

    stars = []
    for _ in range(count):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        size = random.randint(1, 2)
        stars.append((x, y, size))
    return stars



def main():


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("🌈 Nyan Cat Animation 🌈")
    clock = pygame.time.Clock()


    stars = generate_stars(SCREEN_WIDTH, SCREEN_HEIGHT)


    cats = []
    for _ in range(3):
        cat = NyanCat(SCREEN_WIDTH, SCREEN_HEIGHT)
        cats.append(cat)

    images = []
    for cat in cats:
        image = load_image(IMAGE_FILE, cat.width, cat.height)
        images.append(image)


    frame = 0


    running = True
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        draw_background(screen, stars)

        for i, cat in enumerate(cats):
            cat.update(frame)
            cat.draw(screen, images[i])


        pygame.display.flip()


        clock.tick(FPS)


        frame += 1


    pygame.quit()



if __name__ == "__main__":
    main()