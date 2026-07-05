from turtle import Turtle, Screen

timmy = Turtle()
jimmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('blue')
timmy.shapesize()
timmy.forward(100)
timmy.left(30)
timmy.forward(200)
timmy.backward(100)

jimmy.shape("turtle")
jimmy.color('blue')
jimmy.shapesize()
jimmy.backward(100)
jimmy.right(30)
jimmy.backward(200)
jimmy.forward(100)


screen = Screen()
print(screen.canvheight)
screen.exitonclick()

print("lets go")

