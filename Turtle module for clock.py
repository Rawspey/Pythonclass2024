import turtle
import math

def draw_clock(radius):
    turtle.speed(0)
    turtle.shape("turtle")
    
    # Draw the outer circle
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)

    for hour in range(12):
        angle = (hour / 12.0) * 360  # Angle in degrees
        x = radius * 0.85 * math.sin(math.radians(angle))
        y = radius * 0.85 * math.cos(math.radians(angle))
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(-angle)  # Set heading so the turtle faces inward
        turtle.pendown()
        turtle.stamp()  # Draw the hour marker as a turtle

    # Draw the turtle in the middle
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)  # Ensure the central turtle is facing upward
    turtle.pendown()
    turtle.stamp()  # Draw the center marker as a turtle

    turtle.hideturtle()

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    turtle.color("blue")
    draw_clock(200)
    screen.mainloop()

if __name__ == "__main__":
    main()
