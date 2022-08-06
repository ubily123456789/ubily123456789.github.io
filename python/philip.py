# Kenneth
import turtle
phil = turtle.Pen()
phil.shape("turtle")

def fname(sides, size):
    for i in range():
        pass

# fname(7, 70)fd AD F

# phil.circle(size/2, 180)
# half a circle ^
#               |

#-----------------------------------------------------------------------------------------------------------

def shape(sides, size):
    if sides == 2:
        phil.forward(size)
        phil.left(90)
        phil.circle(size/2, 180)
        phil.left(90)
    elif sides == 1:
        phil.circle(size/2)
    else:
        for i in range(sides):
            phil.forward(size)
            phil.left(360/sides)



shape(1, 100)

# Philip

# 1st B
# 2nd A+
# 3rd ?
# current grade: A

turtle.mainloop()
