import pygame

class Health_boost(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.image.load('hearts.png')
    self.image=pygame.transform.scale(self.image, (64, 64))
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y

  def update(self,shift):
    self.rect.x+=shift
class speed_boost(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.image.load('speed_icon.png')
    self.image=pygame.transform.scale(self.image, (64, 64))
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y  
  def update(self,shift):
    self.rect.x+=shift
