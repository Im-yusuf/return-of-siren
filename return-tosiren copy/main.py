import pygame, sys
import pygame.time
from pygame.locals import QUIT
from settings import *
from level import *
from coins import *

pygame.display.set_caption('Return to siren!')
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#level = Level( screen, 1)  #gives access to the level

class Game():
  
    def __init__(self):
        self.level = Level(screen, 1)  #constructs the first level
        self.font = pygame.font.SysFont('bubble', 50)  #font for the writing
        self.time = 0  #start time
        self.get_time = 0  #time taken for the player to mouse click onto the screen

    def introduction(self):
        while True:
            screen.fill('white')  #fills the screen full white
            introduction_message = self.font.render('Click anywhere on the screen to start', False,'black')  # the intro message
            screen.blit(introduction_message,(400, 200))  #displays the message onto the screen
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: #if mouse click is pressed main game starts
                    self.get_time = int(pygame.time.get_ticks() / 1000) #the time taken for the player to press the mouse on the screen
                    game_state.main_game()  #runs the main game method
            pygame.display.update()  # updates the game display
    def draw_timer(self):
        self.time = 180 - int(pygame.time.get_ticks() / 1000) + self.get_time  #adding the time taken for the player to start the game onto the count down
        if self.time <= 0: 
            self.time = 0
            self.level.death = True # to end the game
        self.time_surface = self.font.render('Timer : ' + f'{self.time}',False, 'blue')
        screen.blit(self.time_surface, (1285, 0)) # displays the timer onto the screen

    def main_game(self): # the main game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill('black') #fills the screen to black
            self.level.run() #runs the level's run method
            self.draw_healthbar()
            self.draw_timer() 
            pygame.display.update()
            clock.tick(60)#sets the clock tick speed
    def draw_healthbar(self):
        player_current_health=self.level.player.sprite.current_health
        health_ratio=self.level.player.sprite.ratio_healthbar
        healthbar_length=self.level.player.sprite.health_barlength
        pygame.draw.rect(screen,(255,0,0),(5,30,player_current_health/health_ratio,25))# screen then colour then rectangle then stroke width
        pygame.draw.rect(screen,(255,255,255),(5,30,healthbar_length,25),4)# the last attribute is width 
game_state = Game()#creates an instance of the game
while True:
    game_state.introduction()#calls the game's introduction method to start the game
