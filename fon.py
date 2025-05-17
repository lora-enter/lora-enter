import pygame

width = 1000
dlin = 700

class fon():
    def __init__(self):
        self.fon = pygame.transform.scale(pygame.image.load('fon.png').convert(), (2050, 700))
        self.rect = self.fon.get_rect()
        self.moving_speed: int = 9
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
               self.bgX1 = self.rect.width
        if self.bgX2 <= - self.rect.width:
                self.bgX2 = self.rect.width

    def render(self, screen):
      screen.blit(self.fon, (self.bgX1, self.bgY1))
      screen.blit(self.fon, (self.bgX2, self.bgY2))
