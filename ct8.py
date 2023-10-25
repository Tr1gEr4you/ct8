import math
from typing import NewType, Literal

class Logger:
    def log(self, message: str) -> None:
        pass

class LogToConsole(Logger):
    def log(self, message: str) -> None:
        print(message)

class Plotter:
    def __init__(self, logger):
        self.logger = logger
        self.position = (0, 0)
        self.angle = 0.0
        self.carriage_state = 'UP'
        self.line_color = 'Black'

    def calc_new_position(self, distance, angle):
        angle_in_rads = math.radians(angle)
        x = self.position[0] + (distance * math.cos(angle_in_rads))
        y = self.position[1] + (distance * math.sin(angle_in_rads))
        new_x = round(x, 2)
        new_y = round(y, 2)
        return (new_x, new_y)

    def draw_line(self, pos_from, pos_to):
        if self.carriage_state == 'DOWN':
            self.logger.log(f"...Чертим линию из {pos_from} в {pos_to} используя цвет {self.line_color}")

    def move(self, distance):
        self.logger.log(f"Передвигаем на {distance} от точки {self.position}")
        new_position = self.calc_new_position(distance, self.angle)
        self.draw_line(self.position, new_position)
        self.position = new_position

    def turn(self, angle):
        self.logger.log(f"Поворачиваем на {angle} градусов")
        self.angle = (self.angle + angle) % 360.0

    def carriage_up(self):
        self.logger.log("Поднимаем каретку")
        self.carriage_state = 'UP'

    def carriage_down(self):
        self.logger.log("Опускаем каретку")
        self.carriage_state = 'DOWN'

    def set_color(self, color):
        self.logger.log(f"Устанавливаем цвет линии в {color}")
        self.line_color = color

def draw_triangle(plotter, size):
    plotter.set_color('Green')
    for _ in range(2):
        plotter.carriage_down()
        plotter.move(size)
        plotter.carriage_up()
        plotter.turn(120.0)

if __name__ == "__main__":
    plotter = Plotter(LogToConsole())
    draw_triangle(plotter, 100.0)