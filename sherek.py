import pygame

class Sherek():
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load("images/sherek.bmp")
        self.image_rect = self.image.get_rect()
        
        self.image_rect.midbottom = self.rect.midbottom
        
    def sherek_blitme(self):
        self.screen.blit(self.image, self.image_rect)


    