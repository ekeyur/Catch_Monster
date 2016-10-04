import pygame
from random import randint as r
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
K_RETURN = 13


class Character(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_y = 0
        self.speed_y = 0
        self.name = "character"

    def render(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def direction(self):
        d = r(1,4)
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
        if self.y > height - 5:
            self.y = 5
        if self.x < 5:
            self.x = width - 5
        if self.y < 5:
            self.y = height - 5


class Monster(Character):

    def __init__(self):
        self.x = r(20,480)
        self.y = r(20,430)
        self.speed_x = 1
        self.speed_y = 1
        self.image = pygame.image.load('monster.png').convert_alpha()
        self.name = 'monster'

    # def direction(self):
    #     super(Monster,self).direction()


class Goblin(Character):

    def __init__(self):
        self.x = r(20,480)
        self.y = r(20,430)
        self.speed_x = 1
        self.speed_y = 1
        self.image = pygame.image.load('goblin.png').convert_alpha()
        self.name = 'goblin'

    def direction(self):
        d = r(1,4)
        if d == 1:
            self.speed_x = 0
            self.speed_y = -1
        if d == 2:
            self.speed_x = 0
            self.speed_y = 1
        if d == 3:
            self.speed_x = -1
            self.speed_y = 0
        if d == 4:
            self.speed_x = 1
            self.speed_y = 0


class Hero(Character):
    def __init__(self):
        self.x = 250
        self.y = 235
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.image.load('hero.png').convert_alpha()
        self.name = 'hero'
        self.colided_with_monster = False
        self.colided_with_goblin = False
        self.level = 1

    def process_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_DOWN:
                self.speed_y = 5
            elif event.key == KEY_UP:
                self.speed_y = -5
            elif event.key == KEY_LEFT:
                self.speed_x = -5
            elif event.key == KEY_RIGHT:
                self.speed_x = 5
        if event.type == pygame.KEYUP:
            if event.key == KEY_DOWN:
                self.speed_y = 0
            elif event.key == KEY_UP:
                self.speed_y = 0
            elif event.key == KEY_LEFT:
                self.speed_x = 0
            elif event.key == KEY_RIGHT:
                self.speed_x = 0

    def wrap(self,width,height):
        self.x += self.speed_x
        self.y += self.speed_y

        padding = 32

        if self.x > width - 2 * padding:
            self.x =  width - 2 * padding
        if self.y > height - 2 * padding:
            self.y = height - 2 * padding
        if self.x < padding:
            self.x = padding
        if self.y < padding:
            self.y = padding

    def collision(self,enemy):
        dist = math.sqrt(((enemy.x - self.x) ** 2) + ((enemy.y - self.y) ** 2))
        if dist < 32:
            if enemy.name == 'monster':
                self.colided_with_monster = True
            elif enemy.name == 'goblin':
                self.colided_with_goblin = True

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    #blue_color = (97, 159, 182)
    pygame.mixer.init()
    win = pygame.mixer.Sound('win.wav')
    lose = pygame.mixer.Sound('lose.wav')
    music = pygame.mixer.Sound('music.wav')

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
    goblin_list = [Goblin()]
    # goblin = Goblin()
    # goblin1 = Goblin()
    # goblin2 = Goblin()
    game_over = False

    stop_game = False
    counter = 1
    #play_again = True

    while not stop_game:
        # when there is a collision

            # play_again = False
            # pygame.display.set_caption('Hit Enter to play again!')
        # look through user events fired
        for event in pygame.event.get():


            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            # Moving Hero around code with keypress event
            hero.process_event(event)

            if event.type == pygame.KEYDOWN:

                if event.key == K_RETURN:
                    if hero.colided_with_monster:
                        game_over = False
                        hero.level += 1
                        goblin_list.append(Goblin())
                        hero.colided_with_monster = False
                    if hero.colided_with_goblin:
                        hero.colided_with_goblin = False

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        screen.blit(background,(0,0))

        #math.sqrt(((monster.x - hero.x) ** 2) + ((monster.y - hero.y) ** 2))
        #dist_goblin = math.sqrt(((goblin.x - hero.x) ** 2) + ((goblin.y - hero.y) ** 2))
        for goblin in goblin_list:
            hero.collision(goblin)

        # hero.collision(goblin)
        # hero.collision(goblin1)
        # hero.collision(goblin2)

        hero.collision(monster)

        myfont = pygame.font.SysFont("monospace", 35)
        label = myfont.render("Hit Enter to play again!", 1, (255,255,0))

        myfont_level = pygame.font.SysFont("monospace", 15)
        level_banner = myfont.render("Level: %d" % hero.level, 1, (0,0,255))
        screen.blit(level_banner, (30,30))

        # rendering monster & hero
        hero.wrap(width,height)
        #hero.render(screen)
        for goblin in goblin_list:
            goblin.wrap(width,height)
            goblin.render(screen)

        # goblin1.wrap(width,height)
        # goblin1.render(screen)
        #
        # goblin2.wrap(width,height)
        # goblin2.render(screen)


        monster.wrap(width,height)

        if not hero.colided_with_monster and not game_over:
            monster.render(screen)

        if  hero.colided_with_monster:
            win.play(1)
            pygame.display.set_caption('Hit Enter to play again!')
            screen.blit(label, (140,150))
            game_over = True

        if not hero.colided_with_goblin:
            hero.render(screen)

        if  hero.colided_with_goblin:
            lose.play(1)
            pygame.display.set_caption('You Lose! Hit Enter to play again')
            screen.blit(label, (140,150))

        music.play(1)

            # if event.type == pygame.KEYDOWN:
            #     if event.key == K_RETURN:
            #         stop_game = False
            #         hero.colided = False
            #         print event.key
            #     pass




        # Counter to change direction every 80 moves
        counter +=1
        if counter >= 80:
            monster.direction()
            for goblin in goblin_list:
                goblin.direction()
            counter = 0

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
