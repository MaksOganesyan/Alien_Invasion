import pygame

class Ship():
    """ Класс для управления кораблём"""
    def __init__(self, ai_game):
        """ Иницциализирует корабль и задаёт его начальную позицию """
        self.screen = ai_game.screen.get_rect()
        
        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        # Каждый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """ Рисует корабль в теукщей позиции"""
        self.screen.blit(self.image, self.rect)
