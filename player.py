import pygame
from settings import *
from support import import_folder
from math import sin


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()  # super method to get the attritubes of the sprite class
        self.import_char_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (32, 64))
        self.rect = self.image.get_rect(topleft=pos)
        #player movements
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
        self.speed2 = 4
        self.gravity = 0.85
        self.jump_speed = -16
        #status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground=False
        self.on_ceiling=False
        self.on_left=False
        self.on_right=False
        #health
        self.current_health = 100  #health
        self.max_health = 100
        self.health_barlength = 300  #distance
        self.ratio_healthbar = self.max_health / self.health_barlength  # ratio betweeen health and healthbar
        #invincibility
        self.invincible = False
        self.invincibility_time = 1200  # time the player would be incvincible for
        self.damage_time = 0  #time the player has taken damage

    def import_char_assets(self):
        char_path = 'alien/PNG/'
        self.animations = {'idle': [], 'run': [], 'jump': []}
        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        #loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
            self.image = pygame.transform.scale(self.image, (32, 64))
        else:
            image_flip = pygame.transform.flip(image, True, False)  #the first boolean is flip in x axis and second is y axis
            self.image = image_flip
            self.image = pygame.transform.scale(self.image, (32, 64))
        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
        #set rect
        if self.on_ground and self.on_right:
            self.rect=self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect=self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect=self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect=self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect=self.image.get_rect(topleft=self.rect.topleft)          
        elif self.on_ceiling:
            self.rect=self.image.get_rect(midtop=self.rect.midtop)
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and self.direction.y == 0 or keys[pygame.K_UP] and self.direction.y == 0:  #checks if there is a collision with floor by check if the direction.y = 0
            self.jump()
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'idle'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def take_damage(self, amount):
        if not self.invincible:
            if self.current_health > 0:
                self.current_health -= amount
            if self.current_health <= 0:
                self.current_health -= amount
            self.invincible = True
            self.damage_time = pygame.time.get_ticks()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time >= self.invincibility_time:
                self.invincible = False

    def get_health(self, amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0

    def update(self):
        self.get_input()  #calls the get_input method
        self.rect.x += self.direction.x * self.speed  #multiplies x direction by speed
        self.get_status()  # calls the get_status method
        self.animate()  # calls the animate method
        self.invincibility_timer()  # calls the invincibility timer method
