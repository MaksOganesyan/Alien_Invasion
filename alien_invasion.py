import pygame
import sys

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры"""
    def __init__(self) -> None:
        """ Инициализирует игру и создаёт игровые ресурсы """
        pygame.init()
        
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """ Запуск основного цикла игры """
        while True:
            #* Отслеживание событий клавиатуры и мыши 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #! Отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
