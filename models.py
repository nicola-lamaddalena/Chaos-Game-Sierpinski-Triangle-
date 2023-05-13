import random
import turtle

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
    point_size = 3
    point_color = "black"

    verteces: list[Point] = [
        Point(-250, -200, vertex_size, vertex_color),
        Point(250, -200, vertex_size, vertex_color),
        Point(0, 200, vertex_size, vertex_color),  # y should be 433
    ]

    for i in verteces:
        i.draw()

    first_point = Point(
        random.randint(0, 500), random.randint(500, 500), point_size, point_color
    )
    first_point.draw()

    first_choice: Point = random.choice(verteces)
    first_dot_pos: Point = first_point.mid_point(first_choice)
    first_dot_pos.draw()

    count = 0
    while count < 30_000:
        new_vertex = random.choice(verteces)
        new_dot_pos: Point = first_dot_pos.mid_point(new_vertex)
        new_dot_pos.draw()
        first_dot_pos = new_dot_pos
        count += 1

    turtle.mainloop()
