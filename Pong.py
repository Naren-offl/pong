import turtle
player1 = input("Enter name of player 1:-")
player2 = input("Enter name of player 2:-")
score_a = 0
score_b = 0

#display screen
win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong Game")
win.tracer(0)



#left_paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=4,stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-380,0)

#right_paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=4,stretch_len=1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(375,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.dx = 0.1
ball.dy = 0.1

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(player1 + " :" + str(score_a) + " " + player2 + " :" + str(score_b), align="center",font=("Arial", 24, "normal"))


#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')


while 1:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #walls
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        pen.clear()
        score_a+=1
        pen.write(player1+" :"+str(score_a)+" "+player2+" :"+str(score_b), align="center", font=("Arial", 24, "normal"))
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        pen.clear()
        score_b+=1
        pen.write(player1+" :"+str(score_a)+" "+player2+" :"+str(score_b), align="center", font=("Arial", 24, "normal"))
    #collission
    if ball.xcor() > 360 and ball.ycor()<right_paddle.ycor()+40 and ball.ycor()>right_paddle.ycor()-40:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -360 and ball.ycor()<left_paddle.ycor()+40 and ball.ycor()>left_paddle.ycor()-40:
        ball.setx(-360)
        ball.dx *= -1
