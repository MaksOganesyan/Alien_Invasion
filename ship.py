import pygame

class Ship():
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom =  self.screen_rect.midbottom
        #? Флаг перемещения
        self.moving_right = False
        
    def update(self):
         """ Обновляет позицию корабля с учётом флага """
         if self.moving_right:
             self.rect.x += 1
        
        
    def blitme(self):
        """ Рисует корабль в текущей  позиции  """
        self.screen.blit(self.image, self.rect)
