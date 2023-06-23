class Settings():
    """ Класс для хранения  всех настроек игры Alien Invasion  """
    
    def __init__(self) -> None:
        """ Инициализирует настройки игры """
        #? Параметры экрана 
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)
        
        #* Настройки корабля
        self.ship_speed = 1.5
         
        
