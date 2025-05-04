import pygame_menu
import pygame as pg
import pygame_menu.events
import random

pg.init()

class Menu:
    def __init__(self):
        self.surface = pg.display.set_mode((900, 550))
        self.menu = pygame_menu.Menu(
            height=550,
            width=900,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title="Пример меню"
        )

        self.menu.add.text_input("Имя: ", default="Иван", onchange=self.set_name)
        self.menu.add.selector("Сложность: ", [('Лёгкая', 1), ('Сложная', 2)], onchange=self.set_difficulty)
        self.menu.add.label(title="Это ярлык")
        self.menu.add.button("Играть", self.start_game)

        self.menu.add.selector("Противник: ", [("Маг молний: ", 1), ("Маг земли: ", 2), ("Случайный: ", 3)], onchange=self.set_enemy)
        self.menu.add.button("Выйти", pygame_menu.events.EXIT)

        self.enemies = ["lightning wizard", "earth monk"]
        self.enemy = None

        self.run()

    def set_name(self, value):
        print("Ваше имя", value)

    def set_enemy(self, selected, value):
        if value in (1, 2):
            self.enemy = self.enemies[value - 1]
        else:
            self.enemy = random.choice(self.enemies)

    def set_difficulty(self, selected, value):
        print(selected)
        print(value)

    def start_game(self):
        ...

    def quit_game(self):
        ...

    def run(self):
        self.menu.mainloop(self.surface)

if __name__ == "__main__":
    menu_app = Menu()