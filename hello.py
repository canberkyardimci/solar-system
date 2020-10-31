import turtle

turtle.register_shape("sun.gif")
turtle.register_shape("bg1.gif")
turtle.register_shape("venus.gif")
turtle.register_shape("mercury.gif")
turtle.register_shape("earth.gif")
turtle.register_shape("mars.gif")
turtle.register_shape("moon.gif")
turtle.register_shape("juputer (1).gif")
turtle.register_shape("sat (3).gif")
turtle.register_shape("uranus.gif")
turtle.register_shape("neptun.gif")

# Window Setup
wn = turtle.Screen()
wn.title("SpaceX")
wn.setup(600, 600)
wn.bgpic("bg1.gif")
wn.tracer(2)

# Pen 1
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.color("white")
pen1.setposition(-150, 440)
pen1.hideturtle()

# Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.setposition(-980, 360)

# Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.setposition(-950, -470)
pen3.hideturtle()

# Pen 4
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color("white")
pen4.penup()
pen4.setposition(550, -500)
pen4.write("FOR HELP PLEASE PRESS 'H'", align="left", font=("Calibri", 25, "normal"))
pen4.hideturtle()

# Pen 5
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.color("white")
pen5.penup()
pen5.setposition(450, 0)
pen5.write("HIT SPACEBAR TO START YOUR TEST", align="left", font=("Calibri", 20, "bold"))
pen5.hideturtle()

# Sun
sun = turtle.Turtle()
sun.setposition(0, 0)
sun.shapesize(4)
sun.shape("sun.gif")
sun.color("yellow", "orange")

# Mercury
mercury = turtle.Turtle()
mercury.speed(0)
mercury.penup()
mercury.setposition(59, 0)
mercury.setheading(90)
mercury.shape("mercury.gif")

# Venus
venus = turtle.Turtle()
venus.speed(0)
venus.penup()
venus.setposition(-117, 0)
venus.setheading(-90)
venus.shape("venus.gif")

# Earth
earth = turtle.Turtle()
earth.speed(0)
earth.penup()
earth.setposition(0, 180)
earth.setheading(-180)
earth.shape("earth.gif")

# Moon
moon = turtle.Turtle()
moon.speed(0)
moon.penup()
moon.shape("moon.gif")
moon.setposition(earth.xcor(), earth.ycor() - 20)

# Mars
mars = turtle.Turtle()
mars.speed(0)
mars.penup()
mars.setposition(-167, 170)
mars.setheading(-135)
mars.shape("mars.gif")

# Juputer
juputer = turtle.Turtle()
juputer.speed(0)
juputer.penup()
juputer.setposition(212, -212)
juputer.setheading(45)
juputer.shape("juputer (1).gif")

# Saturn
saturn = turtle.Turtle()
saturn.speed(0)
saturn.penup()
saturn.setposition(-265, -250)
saturn.setheading(-45)
saturn.shape("sat (3).gif")

# Uranus
uranus = turtle.Turtle()
uranus.speed(0)
uranus.penup()
uranus.setposition(297, 297)
uranus.setheading(135)
uranus.color("skyblue")
uranus.shapesize(.5)
uranus.shape("uranus.gif")

# Neptun
neptune = turtle.Turtle()
neptune.speed(0)
neptune.penup()
neptune.setposition(0, -480)
neptune.shape("neptun.gif")

planets = [mercury, venus, earth, mars, juputer, saturn, uranus, neptune]


# Mercury
def clickleft_m(x, y):
    mercury.hideturtle()


# Venus
def clickleft_v(x, y):
    venus.hideturtle()


# Earth
def clickleft_e(x, y):
    earth.hideturtle()


# Moon
def clickleft_mo(x, y):
    moon.hideturtle()


# Mars
def clickleft_ma(x, y):
    mars.hideturtle()


# Juputer
def clickleft_j(x, y):
    juputer.hideturtle()


# Saturn
def clickleft_s(x, y):
    saturn.hideturtle()


# Uranus
def clickleft_u(x, y):
    uranus.hideturtle()


# Neptune
def clickleft_n(x, y):
    neptune.hideturtle()


# All back in
def clickright(x, y):
    for planet in planets:
        planet.showturtle()


def all_info():
    pen3.write("""
            Sun
            Mass: 1,989^30 kg
            Gravity: 274 m/s²
            Distance from Earth: 150 million km

            Mercury
            Mass: 3.285 × 10^23 kg
            Gravity: 3.7 m/s²
            Distance from Earth: 115.76 million km

            Venus
            Mass: 4.867 × 10^24 kg
            Gravity: 8.87 m/s²
            Distance from Earth: 43.472 million km

            Earth
            Mass: 5.972 × 10^24 kg
            Gravity: 9.81 m/s²
            Distance from Earth: 0 km

            Mars
            Mass: 6.39 × 10^23 kg
            Gravity: 3.711 m/s²
            Distance from Earth: 145.15 million km

            Juputer
            Mass: 1.898 × 10^27 kg
            Gravity: 24.79 m/s²
            Distance from Earth: 649.67 million km

            Saturn
            Mass: 5.683 × 10^26 kg
            Gravity: 10.44 m/s²
            Distance from Earth: 1.3826 billion km

            Uranus
            Mass: 8.681 × 10^25 kg
            Gravity: 8.87 m/s²
            Distance from Earth: 3.079 billion km

            Neptune
            Mass: 1,024 x 10^26 kg
            Gravity: 11.15 m/s²
            Distance from Earth: 4.3 billion km""", align="left", font=("Calibri", 12, "normal"))


def close_all_info():
    pen3.clear()


def take_test():
    pen5.clear()
    pen5.setposition(380, 250)
    pen5.write("""
    1) What is the mass of Sun?
    2)What is the 2nd planet on the system called?
    3)What is Earth's gravity rate?
    4)Which planet is the largest?
    Bonus*
    5)Did humanity succeed to travel to any of these planets?

    (For answers, hit "1")
    """, align="left", font=("Calibri", 17, "bold"))


def close_test():
    pen5.clear()
    pen5.setposition(450, 0)
    pen5.write("HIT THE SPACEBAR TO START YOUR TEST", align="left", font=("Calibri", 20, "bold"))


def help_screen():
    pen4.clear()
    pen4.setposition(400, -400)
    pen4.write("""
    HERE ARE THE KEYS AND THEIR FUNCTIONS:
    SPACEBAR = Opens the test
    q = Closes the test
    1 = Opens the information box
    2 = Closes the information box
    h = Opens the help section
    g = Closes the help section
    Left Click on Planets = Disappears the planet
    Right Click on screen = All planets appear back
    """, align="left", font=("Calibri", 20, "bold"))


def close_help_screen():
    pen4.clear()
    pen4.setposition(550, -500)
    pen4.write("FOR HELP PLEASE PRESS 'H'", align="left", font=("Calibri", 25, "normal"))


# Key Blindings
wn.listen()
wn.onkeypress(help_screen, "h")
wn.onkeypress(close_help_screen, "g")
wn.onkeypress(close_test, "q")
wn.onkeypress(take_test, "space")
wn.onkeypress(close_all_info, "2")
wn.onkeypress(all_info, "1")
mercury.onclick(clickleft_m, 1)
venus.onclick(clickleft_v, 1)
earth.onclick(clickleft_e, 1)
moon.onclick(clickleft_mo, 1)
mars.onclick(clickleft_ma, 1)
juputer.onclick(clickleft_j, 1)
saturn.onclick(clickleft_s, 1)
uranus.onclick(clickleft_u, 1)
neptune.onclick(clickleft_n, 1)
wn.onscreenclick(clickright, 3)

laps = -.5
mer_turn = 0
while True:
    pen1.write("Solar System", align="left", font=("Arial", 35, "bold"))
    wn.update()
    print("""
    """)
    # Mercury Check
    if mercury.isvisible():
        print("Mercury is on the track ")
    else:
        print("Mercury has disappeared")

        # Venus Check
    if venus.isvisible():
        print("Venus is on the track ")
    else:
        print("Venus has disappeared")

    # Earth Check
    if earth.isvisible():
        print("Earth is on the track")
    else:
        print("Earth has disappeared")

    # Mars Check
    if mars.isvisible():
        print("Mars is on the track ")
    else:
        print("Mars has disappeared")

    # Juputer Check
    if juputer.isvisible():
        print("Juputer is on the track ")
    else:
        print("Juputer has disappeared")

    # Saturn Check
    if saturn.isvisible():
        print("Saturn is on the track")
    else:
        print("Saturn has disappeared")

    # Uranus Check
    if uranus.isvisible():
        print("Uranus is on the track")
    else:
        print("Uranus has disappeared")

    # Neptune Check
    if neptune.isvisible():
        print("Neptune is on the track")
    else:
        print("Neptune has disappeared")
    laps += .5
    # Mercury Info
    pen2.write("""
            Mercury
            Mass: 3.285 × 10^23 kg
            Gravity: 3.7 m/s²
            Distance from Earth: 115.76 million km""", align="left", font=("Calibri", 20, "bold"))
    if laps == .5:
        pen2.clear()
        pen2.write("""
            Venus
            Mass: 4.867 × 10^24 kg
            Gravity: 8.87 m/s²
            Distance from Earth: 43.472 million km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 1:
        pen2.clear()
        pen2.write("""
            Earth
            Mass: 5.972 × 10^24 kg
            Gravity: 9.81 m/s²
            Distance from Earth: 0 km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 1.5:
        pen2.clear()
        pen2.write("""
            Mars
            Mass: 6.39 × 10^23 kg
            Gravity: 3.711 m/s²
            Distance from Earth: 145.15 million km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 2:
        pen2.clear()
        pen2.write("""
            Juputer
            Mass: 1.898 × 10^27 kg
            Gravity: 24.79 m/s²
            Distance from Earth: 649.67 million km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 2.5:
        pen2.clear()
        pen2.write("""
            Saturn
            Mass: 5.683 × 10^26 kg
            Gravity: 10.44 m/s²
            Distance from Earth: 1.3826 billion km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 3:
        pen2.clear()
        pen2.write("""
            Uranus
            Mass: 8.681 × 10^25 kg
            Gravity: 8.87 m/s²
            Distance from Earth: 3.079 billion km""", align="left", font=("Calibri", 20, "bold"))
    if laps == 3.5:
        pen2.clear()
        pen2.write("""
            Neptune
            Mass: 1,024 x 10^26 kg
            Gravity: 11.15 m/s²
            Distance from Earth: 4.3 billion km""", align="left", font=("Calibri", 20, "bold"))
        laps = -1

    for x in range(360):
        # Mercury Rotation
        mercury.penup()
        mercury.forward(.21)
        mercury.left(.2)
        # Venus Rotation
        venus.penup()
        venus.forward(.4)
        venus.left(.2)
        # Earth Rotation
        earth.penup()
        earth.forward(.6)
        earth.left(.2)
        # Moon Rotation
        moon.penup()
        moon.setposition(earth.xcor(), earth.ycor() - 20)
        moon.forward(.05)
        moon.left(.02)
        # Mars Rotation
        mars.penup()
        mars.forward(.8)
        mars.left(.2)
        # Juputer Rotation
        juputer.penup()
        juputer.forward(1.1)
        juputer.left(.2)
        # Saturn Rotation
        saturn.penup()
        saturn.forward(1.28)
        saturn.left(.2)
        # Uranus Rotation
        uranus.penup()
        uranus.forward(1.48)
        uranus.left(.2)
        # Neptune Rotation
        neptune.penup()
        neptune.forward(1.67)
        neptune.left(.2)

wn.mainloop()