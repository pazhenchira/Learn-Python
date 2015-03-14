import turtle
import math

s = turtle.Screen()
a = turtle.Turtle()

def fracLine(lines):
    newLines = [];
    for l in lines:
        p1 = l[0]
        p5 = l[1]
        p2 = [p1[0] + 1/3*(p5[0] - p1[0]), p5[1] + 2/3*(p1[1] - p5[1])]
        p4 = [p1[0] + 2/3*(p5[0] - p1[0]), p5[1] + 1/3*(p1[1] - p5[1])]
        lengthOfLine = ((p1[0] - p5[0])**2 + (p1[1] - p5[1])**2)**(1/2)
        angleOfLineToX = math.tanh((p5[1] - p1[1])/(p5[0] - p1[0]))
        angleOfRaise =  angleOfLineToX + 5* math.pi / 3
        if (p5[0] > p1[0]):
            angleOfRaise = math.pi + angleOfLineToX - math.pi / 3
        p3 = [p4[0] + math.cos(angleOfRaise) * lengthOfLine / 3, p4[1] + math.sin(angleOfRaise) * lengthOfLine / 3] 
        newLines += [[p1, p2], [p2, p3], [p3, p4], [p4, p5]]
    return newLines

def drawLines(lines):
    for l in lines:
        a.penup()
        a.setpos(l[0][0], l[0][1])
        a.pendown()
        a.setpos(l[1][0], l[1][1])


##lines = [[[-300, -300], [0, 0]]]
##lines = [[[-400, -100], [400, 300]]]
lines = [[[-400, 0], [400, 0]]]
lines = fracLine(lines)
lines = fracLine(lines)
lines = fracLine(lines)
lines = fracLine(lines)
lines = fracLine(lines)
lines = fracLine(lines)



#print(lines)
drawLines(lines)


        
