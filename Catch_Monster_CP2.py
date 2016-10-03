import pygame
from random import randint as r
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


class Character(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_y = 0
        self.speed_y = 0
        self.name = "character"

    def render(self,screen):
        screen.blit(self.image,(self.x,self.y))


class Monster(Character):
    def __init__(self):
        self.x = r(20,480)
        self.y = r(20,430)
        self.speed_x = 1
        self.speed_y = 1
        self.image = pygame.image.load('monster.png').convert_alpha()
        self.name = 'monster'



    def direction(self,d):
        if d == 1:
            self.speed_x = 0
            self.speed_y = -2
        if d == 2:
            self.speed_x = 0
            self.speed_y = 2
        if d == 3:
            self.speed_x = -2
            self.speed_y = 0
        if d == 4:
            self.speed_x = 2
            self.speed_y = 0

    def wrap(self,width,height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > width - 5:
            self.x = 5
        if self.y > height-5:
            self.y = 5
        if self.x < 5:
            self.x = width - 5
        if self.y < 5:
            self.y = height - 5



class Hero(Character):
    def __init__(self):
        self.x = 250
        self.y = 235
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.image.load('hero.png').convert_alpha()
        self.name = 'hero'
        self.collision = False

    def direction(self,d):
        if d == 1:
            self.speed_x = 0
            self.speed_y = -2
        if d == 2:
            self.speed_x = 0
            self.speed_y = 2
        if d == 3:
            self.speed_x = -2
            self.speed_y = 0
        if d == 4:
            self.speed_x = 2
            self.speed_y = 0

    def wrap(self,width,height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > width - 35:
            self.x =  width - 35
        if self.y > height - 35:
            self.y = height - 35
        if self.x < 4:
            self.x = 4
        if self.y < 4:
            self.y = 4

    def collision(self,dist):
        if dist < 32:
            self.collision = True
        return self.collision

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    #blue_color = (97, 159, 182)
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/win.wav')

    # initialize the pygame framework
    pygame.init()

    direction = 1



    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()


    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background = pygame.image.load('background.png').convert_alpha()

    # game loop
    monster = Monster()
    hero = Hero()



    stop_game = False
    counter = 1

    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################

            # Moving Hero around code with keypress event
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 5
                elif event.key == KEY_UP:
                    hero.speed_y = -5
                elif event.key == KEY_LEFT:
                    hero.speed_x = -5
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 5

            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        screen.blit(background,(0,0))

        hero.wrap(width,height)

        # hero.x += hero.speed_x
        # hero.y += hero.speed_y
        # Rendering hero
        hero.render(screen)

        dist = math.sqrt(((monster.x - hero.x) ** 2) + ((monster.y - hero.y) ** 2))


        if dist <= 32:
            monster.display = False

        monster.wrap(width,height)

        # monster.x += monster.speed_x
        # monster.y += monster.speed_y

        # Counter to change direction every 80 moves
        counter +=1
        if counter >= 80:
            monster.direction(r(1,4))
            counter = 0

        # rendering monster

        monster.render(screen)
        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(200)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
