import turtle
import random


# coordinates of the verteces of the triangle
VERTECES = [(0,0),(500,0),(250,250)]
WIDTH, HEIGHT = 800, 800

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
t = turtle.Turtle()
t.hideturtle()

def draw_dot(new_position, size, color):
    """Function to draw a dot in turtle

    Args:
        new_position (tuple): Coordinates of the point
        size (int): Size of the point
        color (str): Color of the point
    """
    t.pu()
    t.goto(new_position)
    t.dot(size, color)


# creating the verteces of the triangle
def draw(verteces):
    for i in verteces:
        draw_dot(i, 10, 'green')
    sierpinski(draw_first_point())
    

# drawing the first random point
def draw_first_point():
    pos = [random.randint(0,500),random.randint(0,500)]  # choosing a random position for the first point
    draw_dot(pos, 4, 'black')
    return pos


# drawing the Sierpinski triangle
def sierpinski(pos):
    first_point = random.choice(VERTECES)
    new_position = [(first_point[0] + pos[0]) //2,
                    (first_point[1] + pos[1]) //2]
    draw_dot(new_position, 4, 'black')

    for _ in range(30000):
        vertex = random.choice(VERTECES)
        new_position = [(vertex[0] + new_position[0]) //2,
                        (vertex[1] + new_position[1]) //2]
        if vertex == VERTECES[0]:
            draw_dot(new_position, 4, "red")
        elif vertex == VERTECES[1]:
            draw_dot(new_position, 4, "blue")
        else:
            draw_dot(new_position, 4, "orange")


if __name__ == "__main__":
    draw(VERTECES)
    turtle.mainloop()
