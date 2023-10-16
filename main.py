from turtle import Turtle,Screen
import random
import tkinter as tk

is_race_on = False
screen = Screen()
screen.title("Race")
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet", prompt="Which tutle will win the race? Pick a colour: ")
colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
y_axis = 75
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_axis)
    y_axis = y_axis - 25
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                is_race_on = False
                root = tk.Tk()
                root.eval('tk::PlaceWindow . center')
                root.title("info")
                root.geometry("140x80")
                tk.Label(root, text="You won!!!").pack()
                root.after(5000, lambda: root.destroy())  # time in ms
                root.mainloop()
                print("You won!!!")
                exit()
            else:
                root = tk.Tk()
                root.eval('tk::PlaceWindow . center')
                root.title("info")
                root.geometry("140x80")
                tk.Label(root, text=f"{turtle.pencolor()} won.").pack()
                root.after(5000, lambda: root.destroy())  # time in ms
                root.mainloop()
                print(f"You lost. the {turtle.pencolor()} is the winner.")
                exit()
        random_speed = random.randint(0, 10)
        turtle.fd(random_speed)
screen.exitonclick()