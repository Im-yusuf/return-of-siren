import pygame

class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coins_img.png')
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,coin_shift):
        self.rect.x+=coin_shift
