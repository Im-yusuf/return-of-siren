import pygame
from support import import_folder
class Gateway(pygame.sprite.Sprite):
  def __init__(self,x,y):
    super().__init__()
    self.import_images()
    self.frame_index=0
    self.animation_speed=0.2
    self.image=self.animations['idle'][self.frame_index]
    self.image=pygame.transform.scale(self.image, (96, 128))
    self.status='idle'
    self.rect=self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
  def import_images(self):
    char_path = 'portal_images/'
    self.animations = {'idle': [],}
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
      self.image = pygame.transform.scale(self.image, (64, 128))      
  def update(self,gate_shift):
    self.animate()
    self.rect.x+=gate_shift
  
    