import pygame
import sys
import random
import math


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, color, x, y, radius, direction, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
        self.color = color
        self.xspeed = math.cos(self.direction) * speed
        self.yspeed = math.sin(self.direction) * speed

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def vector(self):
        if self.y <= self.radius:
            self.yspeed = 0-self.yspeed
        elif self.y >= 600-self.radius:
            self.yspeed = 0-self.yspeed
        elif self.x < self.radius:
            self.xspeed = 0-self.xspeed
        elif self.x > 600-self.radius:
            self.xspeed = 0-self.xspeed
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('white'))
    clock = pygame.time.Clock()


    balls = []
    for k in range(10):
        x = random.randint(150, 450)
        y = random.randint(150, 450)
        radius = random.randint(10, 50)
        direction = random.randint(0, 360)
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        speed = random.randint(3,15)

        color = (color1, color2, color3)

        ball = Ball(screen, color, x, y, radius, direction, speed)
        balls.append(ball)

    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)
        screen.fill(pygame.Color('white'))

        for ball in balls:
            ball.vector()
            ball.move()
            ball.draw()

        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
