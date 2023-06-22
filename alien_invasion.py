import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion():
    """ Класс для управления ресурсами и поведением игры"""
    def __init__(self) :
        """ Инициализирует игру и создаёт игровые ресурсы """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height)) 
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """ Запуск основного цикла игры """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()       
            
    def _check_events(self):
        #? Отслеживание событий клавиатуры и мыши 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = False 
                        
                        
    
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
    
