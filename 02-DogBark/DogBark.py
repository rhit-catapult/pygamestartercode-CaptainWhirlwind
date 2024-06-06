import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # DONE 1: Create an image with the 2dogs.JPG image
    image= pygame.image.load("2dogs.JPG")
    # DONE 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    image=pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # DONE 4: Create a font object with a size 28 font.
    font1= pygame.font.SysFont("comicsansms", 20,)

    # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1=font1.render("Two Dogs", True, (0,0,0))

    font2 = pygame.font.SysFont("comfortaa", 40)
    caption2 = font2.render("Move!", True, (255, 255, 255))

    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound= pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # DONE 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image, (0, 0))
        # Draw the text onto the screen
        # DONE 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        x= screen.get_width()/2 - caption1.get_width()/2
        y= image.get_height() - 4
        screen.blit(caption1, (x,y))

        # DONE 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.


        screen.blit(caption2, (50, 400))

        # Update the screen
        pygame.display.update()


main()
