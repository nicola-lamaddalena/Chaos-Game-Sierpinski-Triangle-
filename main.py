from numpy.random import choice, randint
import turtle
from models import TurtlePoint


if __name__ == "__main__":
    vertex_size = 5
    vertex_color = "red"

    verteces: list[TurtlePoint] = [
        TurtlePoint(-200, -100, vertex_size, vertex_color),
        TurtlePoint(0, 300, vertex_size, vertex_color),
        TurtlePoint(200, -100, vertex_size, vertex_color),
    ]

    for i in verteces:
        i.draw()

    first_point = TurtlePoint(randint(0, 500), randint(0, 500))
    first_point.draw()

    first_choice: TurtlePoint = choice(verteces)
    first_dot_pos: TurtlePoint = first_point.mid_point(first_choice)
    first_dot_pos.draw()

    point_list = []
    for _ in range(10_000):
        new_vertex = choice(verteces)
        new_dot_pos: TurtlePoint = first_dot_pos.mid_point(new_vertex)
        point_list.append(new_dot_pos)
        first_dot_pos = new_dot_pos

    for point in point_list:
        point.draw()
        turtle.update()
        turtle.delay(1)
