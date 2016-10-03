import pygame
from random import randint as r

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

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
    hero = pygame.image.load('hero.png').convert_alpha()
    monster = pygame.image.load('monster.png').convert_alpha()
    monster_pos_x = r(20,480)
    monster_pos_y = r(20,430)
    # game loop
    stop_game = False
    counter = 1
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        screen.blit(background,(0,0))
        screen.blit(hero,((width/2-5),(height/2-5)))


        if monster_pos_x > width-5:
            monster_pos_x = 5
        if monster_pos_y > height-5:
            monster_pos_y = 5
        if monster_pos_x < 5:
            monster_pos_x = width - 5
        if monster_pos_y < 5:
            monster_pos_y = height - 5
        # fill background color
        #screen.fill(blue_color)
        # counter code
        if direction == 1:
            monster_pos_x += 2
        if direction == 2:
            monster_pos_y += 2
        if direction == 3:
            monster_pos_y -= 2
        if direction == 4:
            monster_pos_x -= 2

        counter +=1
        if counter >= 80:
            direction = r(1,4)
            # monster_pos_y = monster_pos_x
            # monster_pos_x = monster_pos_y
            # if direction == 1:
            #     monster_pos_y = monster_pos_y
            #     monster_pos_x = r(50,500)
            # if direction == 2:
            #     monster_pos_x = monster_pos_x
            #     monster_pos_y = r(50,500)
            # if direction == 3:
            #     monster_pos_y = -monster_pos_y
            #     monster_pos_x = r(50,500)
            # if direction == 4:
            #     monster_pos_x = -monster_pos_x
            #     monster_pos_y = r(50,500)
            counter = 0

        screen.blit(monster,(monster_pos_x,monster_pos_y))
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
