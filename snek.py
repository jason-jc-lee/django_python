import random
import turtle
import time
delay = 0.2
score = 0
high_score = 0

screen = turtle.Screen()
#randomized background color
screen.bgcolor("#" + "%06x" % random.randint(0, 0xFFFFFF)
)


segment = turtle.Turtle()
segment.shape("turtle")
segment.color("#" + "%06x" % random.randint(2, 0xFFFFFF))
segment.speed(0)
segment.penup()

#?


snake = [segment]


#default pixels 22

def move():
    first = snake[0]
    last = snake[-1]
    x = first.xcor()
    y= first.ycor()

    if dir == "right":
        last.goto(x + 22, y)
    elif dir == "left":
        last.goto(x - 22, y)
    elif dir == "up":
        last.goto(x, y + 22)
    else:
        last.goto(x, y - 22)

    snake.insert(0, last)
    snake.pop()

def up():
    global dir
    if dir != "up":
            dir = "up"
def down():
    global dir
    if dir != "down":
        dir = "down"
def left():
    global dir
    if dir != "left":
        dir = "left"
def right():
    global dir
    if dir != "right":
        dir = "right"
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

def make_body(x, y):
    body = segment.clone()
    snake.append(body)
food = None
def make_food():
    global food
    food = segment.clone()
    x = random.randint(-10, 10)*22
    y = random.randint(-10, 10)*22
    food.goto (x,y)
    food.color("black")

def eat():
    head = snake[0]
    x = head.xcor()
    y= head.ycor()
    if x == food.xcor() and y == food.ycor():
        food.hideturtle()
        make_body(x, y)
        make_food()

running = True
def die():
    head = snake[0]
    x = head.xcor()
    y = head.ycor()
    for segment in snake[1:-1]:
        if x == segment.xcor() and y== segment.ycor():
            global running
            running = False

        
def update():
    if running:
        eat()
        move()
        die()
        screen.ontimer(update, 333)


make_food()

update()

#part 2 




















































#end
turtle.mainloop()