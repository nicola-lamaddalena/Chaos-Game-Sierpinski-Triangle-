from numpy.random import choice, randint
import turtle

turtle.tracer(0, 0)
t = turtle.Turtle()
t.hideturtle()


class Point:
    def __init__(
        self,
        x: float,
        y: float,
        size: int = 3,
        color: str = "black",
        t: turtle.Turtle = t,
    ) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.t = t

    def draw(self):
        self.t.up()
        self.t.setpos(self.x, self.y)
        self.t.dot(self.size, self.color)

    def mid_point(self, other):
        x: float = (self.x + other.x) / 2
        y: float = (self.y + other.y) / 2
        mid: Point = Point(x, y)
        return mid


if __name__ == "__main__":
    vertex_size = 5
    vertex_color = "red"

    verteces: list[Point] = [
        Point(-200, -100, vertex_size, vertex_color),
        Point(0, 300, vertex_size, vertex_color),
        Point(200, -100, vertex_size, vertex_color),
    ]

    for i in verteces:
        i.draw()

    first_point = Point(randint(0, 500), randint(0, 500))
    first_point.draw()

    first_choice: Point = choice(verteces)
    first_dot_pos: Point = first_point.mid_point(first_choice)
    first_dot_pos.draw()

    point_list = []
    for _ in range(10_000):
        new_vertex = choice(verteces)
        new_dot_pos: Point = first_dot_pos.mid_point(new_vertex)
        point_list.append(new_dot_pos)
        first_dot_pos = new_dot_pos

    for point in point_list:
        point.draw()
        turtle.update()
        turtle.delay(1)
