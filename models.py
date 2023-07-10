import turtle

turtle.tracer(0, 0)
t = turtle.Turtle()
t.hideturtle()


class TurtlePoint:
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
        return TurtlePoint(x, y)
