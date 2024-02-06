import pygame
from support import import_folder

class Enemy(pygame.sprite.Sprite):
  def __init__(self,x,y):
        super().__init__()
        self.import_stuf()
        self.frame_index=0
        self.animation_speed=0.20
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (32, 64))
        self.rect  = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.move_direction=1
        self.move_counter=0
        self.status = 'idle'
    
  def import_stuf(self):
        char_path = 'slime_images/'
        self.animations = {'idle': [],'slime_death': []}
        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)
          
  def animate(self):
      animation= self.animations[self.status]
      #loop over frame index
      
      self.frame_index+=self.animation_speed

      if self.frame_index>=len(animation):
        self.frame_index=0
        
      image=animation[int(self.frame_index)]
      self.image=image
      self.image = pygame.transform.scale(self.image, (32, 64))   
     
      if self.frame_index > 3 and self.status=='slime_death':
        self.kill()
        #level.sprite.coin_counter+=1
  def update(self,shift):
    self.animate()
    self.rect.x+=shift
    self.rect.x+=self.move_direction
    self.move_counter+=1
    if abs(self.move_counter)>50:
      self.move_counter*=-1
      self.move_direction*=-1
  

