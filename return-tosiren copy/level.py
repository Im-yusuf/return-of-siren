import pygame
from tiles import Tile # importing the tile class from the tile file
from settings import * #imports everything inside of the settings class
from player import * # imports everything inside of the player class
from coins import Coin #imports the coin class from the coin file.
from enemies import * #imports everything inside of the enemies class
from gateway import Gateway #imports the gaetway class from the gateway file 
from powerups import Health_boost, speed_boost #imports the variables from the powerups class

class Level: 
    def __init__(self, surface, current_level):
        self.display_surface = surface #gives the attribute the passed in surface
        self.current_level = current_level # gives the attribute the passed in current level
        self.level_data = levels[self.current_level] # selects the indexed level layout
        self.setup_level(self.level_data)# calls in the setup_level method inside the attribute
        self.world_shift = 0 # world shift value set to 0
        self.current_x=0
        #fonts
        self.font_coin = pygame.font.SysFont('bubble', 50) 
        self.colour = ('orange') #stores self.colour for easier accesss in the future
        self.coin_counter = 0 # starting coin count is initiated here
        self.death = False #death attribute is initially set to false
        #speed boost
        self.speed_boost=False
        self.speed_timer=15000
        self.speed_boost_collision_time=0
        #self.time_surface=self.font_coin
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group() #makes tiles a group with useful attributes
        self.player = pygame.sprite.GroupSingle() #makes player a single group as we would only have one player.
        self.coins = pygame.sprite.Group() #makes coins a group 
        self.slimes = pygame.sprite.Group() #makes slimes a group 
        self.gates=pygame.sprite.Group() #makes gates a group 
        self.healths=pygame.sprite.Group() #makes a group for the health boosts
        self.speed_boosts=pygame.sprite.Group() # makes a group for the speed boosts
        for row_index, row in enumerate(layout): # loops through each row 
            for col_index, cell in enumerate(row):#loops through each column
                x = col_index * tile_size # multiplies the x coordinate by the tile size 
                y = row_index * tile_size # multiplies the x coordinate by the tile size 
                if cell == 'X': #checks if the cell has an X
                    tile = Tile((x, y), tile_size) #creates an instance of the tile
                    self.tiles.add(tile) #adds the tile to the sprite group
                if cell == 'P': #checks if the cell has the letter P
                    player_sprite = Player((x, y)) # creates an instance of the player
                    self.player.add(player_sprite) #adds the player to the group
                if cell == 'C': # checks if the cell has a C
                    coin = Coin(x, y) # creates an instance of the coin
                    self.coins.add(coin) # adds the coin to the group
                if cell == 'S': # checks if the cell has an S
                    slime = Enemy(x, y) # creates an instance of the enemy
                    self.slimes.add(slime) # adds the slime to the enemy group
                if cell =='G': # checks if there is a G in the cell
                    gate=Gateway(x,y) # creates an instance of the gate
                    self.gates.add(gate) #adds gate to its sprite group
                if cell=='H': # checks if there is a H in the cell
                    health=Health_boost(x,y) # creates an instance of the health boost
                    self.healths.add(health) # adds the healt boost into the group
                if cell=='B': # checks for an B's in the cell
                    boost=speed_boost(x,y) # makes an instance of the speed boost
                    self.speed_boosts.add(boost) # adds the speed boost to the group
    def x_scrolling(self):
        player = self.player.sprite  # the player sprite
        player_x_pos = player.rect.centerx  # x position of the player
        x_direction = player.direction.x # the x direction of the player
        player_y_pos=player.rect.centery # the y direction of the player
        if player_x_pos < screen_width / 4 and x_direction < 0: # checks if the player is in the lower quartile of the map and is 'left'
            self.world_shift = player.speed2 # value of world shift gets set to the speed of the player 
            player.speed = 0 #sets the player's speed to 0
        elif player_x_pos > screen_width - screen_width / 4 and x_direction > 0:# checks if the player is trying to go into the upper quartile of the map and is moving right
            self.world_shift = -player.speed2 # sets the world shift to the negative value of the player's speed
            player.speed = 0 # sets the player's speed to 0
        else: # else it sets the attributes values to their default values
            self.world_shift = 0 # no world shift
            player.speed=player.speed2 # speed gets set to the modified speed
        if player_y_pos>=screen_height:
          self.setup_level(self.level_data)
          self.coin_counter=0
    def horizontal_collisions(self):
        player = self.player.sprite  #to save space and time when trying to access attributes of the player
        player.rect.x += player.direction.x * player.speed 

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):  #checks if there is a sprite collision
                if player.direction.x < 0: #if the player is facing left
                    player.rect.left = sprite.rect.right #player's left side of the rectangle is set the right side of the tile
                    player.on_left=True
                    self.current_x=player.rect.left
                elif player.direction.x > 0: #if the player is facing right
                    player.rect.right = sprite.rect.left # the player's right rectangle is set to the left side of the tile
                    player.on_right=True
                    self.current_x=player.rect.right
        if player.on_left and (player.rect.left<self.current_x or player.direction.x>=0):
            player.on_left=False
        if player.on_right and (player.rect.right>self.current_x or player.direction.x<=0):
            player.on_right=False
    def vertical_collision(self):
        player = self.player.sprite #sets the player variable to the player sprite
        player.apply_gravity() #calls in the apply gravity method
        for sprite in self.tiles.sprites(): # loops through each sprite in the tile sprite group
            if sprite.rect.colliderect(player.rect): #if the player collides with the tile
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0  #to cancel out the gravity when the player is standing on a tile
                    player.on_ground=True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.apply_gravity()  # to re-apply the gravity when the player hits its head on soemthing
                    player.on_ceiling=True
        if player.on_ground and player.direction.y<0 or player.direction.y>1:
            player.on_ground=False
        if player.on_ceiling and player.direction.y>0:
            player.on_ceiling=False



    def coin_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.coins, True):  # if the collision occurs between the player and the coin,the coin will be 'killed'
            self.coin_counter += 1 # coin counter increased by 1
        self.draw_coin_counter('Coin Count : ' + str(self.coin_counter),self.font_coin, self.colour, 0, 0)# draws the coin counter with its passed in variables
    def draw_coin_counter(self, text, font, text_col, x, y):
        coin_tracker = font.render(text, True, self.colour) 
        self.display_surface.blit(coin_tracker, (x, y)) #draws the coin tracker onto the screen with the inputted x and y coordinates
    def slime_collisions(self):
        slime_collision = pygame.sprite.spritecollide(self.player.sprite, self.slimes, False) # checks for collisions between the player and the slimes
        if slime_collision: # if there is a collision
            for enemy in slime_collision: # loops through the collisions 
                slime_center = enemy.rect.centery #sets the slime center to the y center rectangle of the slime
                slime_top = enemy.rect.top # sets the top of the slime to slime_top to save code for the future
                player_bottom = self.player.sprite.rect.bottom # sets player_bottom to the bottom of the player to save code
                if slime_top < player_bottom < slime_center and self.player.sprite.direction.y >= 0: #if the player's bottom is in the player's top half and the player is falling onto the slime
                    self.player.sprite.jump() # calls the player's jump method
                    self.coin_counter += 1 #increases the player's coin count by 1
                    enemy.status = 'slime_death' #changed the enemy status to dead so the animation can play and the slime can be killed
                else:  #collision from either left or right
                    self.player.sprite.take_damage(25) # calls the player's take damage method so the player takes damage
        if self.player.sprite.current_health<=0:
            self.death=True
    def portal_collision(self):
      if pygame.sprite.spritecollide(self.player.sprite,self.gates,False) and self.coin_counter>=1:
        self.current_level+=1
        self.level_data = levels[self.current_level] 
        self.setup_level(self.level_data)
    def health_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.healths,True):
          if self.player.sprite.current_health>=50:
            self.player.sprite.current_health=100
          elif self.player.sprite.current_health<50 and self.player.sprite.current_health>0:
            self.player.sprite.current_health+=50
    def speed_boost_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.speed_boosts,True):
          self.speed_boost=True
          self.speed_boost_collision_time=pygame.time.get_ticks()
    def speed_boost_timer(self):
        if speed_boost:
          self.player.sprite.speed2=6
          self.player.sprite.speed=6
          current_time = pygame.time.get_ticks()
          if current_time - self.speed_boost_collision_time >= self.speed_timer:
              self.player.sprite.speed2 = 4
              self.speed_boost=False
    def run(self):
        if self.death == False:
          #tile tiles
          self.tiles.update(self.world_shift)
          self.tiles.draw(self.display_surface)
          self.x_scrolling()
          #player
          self.player.update()
          self.horizontal_collisions()
          self.vertical_collision()
          self.player.draw(self.display_surface)
          #Coin
          self.coins.draw(self.display_surface)
          self.coins.update(self.world_shift)
          self.coin_collision()
          #slime
          self.slimes.draw(self.display_surface)
          self.slimes.update(self.world_shift)
          self.slime_collisions()
          #Gateway
          self.gates.draw(self.display_surface)
          self.gates.update(self.world_shift)
          self.portal_collision()
          #power-ups:
          self.healths.draw(self.display_surface)
          self.healths.update(self.world_shift)
          self.health_collision()
          #speed boost
          self.speed_boosts.draw(self.display_surface)
          self.speed_boosts.update(self.world_shift)
          self.speed_boost_timer()
          self.speed_boost_collision()
        else:
          self.display_surface.fill('black')
          self.display_surface.blit(self.font_coin.render('DEATH SCREEN', False, 'RED'),(600,320))
