from graph import *
import math as m

#Небо

penColor(162,245,255)
penSize(5)
brushColor(162,245,255)
rectangle(0, 65, 900, 250)

#Море

penColor(66,30,224)
penSize(5)
brushColor(66,30,224)
rectangle(0, 250, 900, 340)


#Песок

penColor(239,246,4)
penSize(5)
brushColor(239,246,4)
rectangle(0, 340, 900, 460)


def ellipse2 (a, b, x0, y0):
    for x in range(-a, a):
        for y in range(-b, b):
            if(x**2/a**2 + y**2/b**2 <= 1):
                point(x+x0, y+y0)

penSize(0)
penColor("#eff604")
ellipse2(30, 45, 25, 369)
ellipse2(30, 45, 109, 369)
ellipse2(30, 45, 193, 369)
ellipse2(30, 45, 277, 369)
ellipse2(30, 45, 361, 369)
ellipse2(30, 45, 445, 369)
ellipse2(30, 45, 529, 369)
ellipse2(30, 45, 613, 369)
#Море 2
penSize(0)
penColor("#421ee0")
ellipse2(30, 45, 67, 303)
ellipse2(30, 45, 151, 303)
ellipse2(30, 45, 235, 303)
ellipse2(30, 45, 319, 303)
ellipse2(30, 45, 403, 303)
ellipse2(30, 45, 487, 303)
ellipse2(30, 45, 571, 303)
ellipse2(30, 45, 655, 303)

penSize(1)
penColor("#674cb6")
line(0, 335, 900, 335)
#Солнце
 
penColor(255,247,23)
brushColor(255,247,23)
circle(435, 125, 38)

for i in range(40):
    fi = (i - 0) / 4 * m.pi / 4
    polygon([(435 - 38 * m.sin(fi - .15), 125 - 38 * m.cos(fi - .15)),
             (435 - 38 * m.sin(fi + .15), 125 - 38 * m.cos(fi + .15)),
             (435 - 60 * m.sin(fi), 125 - 60 * m.cos(fi))])
#Облака

penSize(1)
penColor(180,180,180)
brushColor(255,255,255)
circle(125, 125, 16)
circle(147, 125, 16)
circle(112, 137, 16)
circle(134, 139, 16)
circle(158, 139, 16)
circle(169, 125, 16)
circle(178, 139, 16)


def ellipse (a, b, x0, y0):
    for x in range(-a, a):
        for y in range(-b, b):
            if(x**2/a**2 + y**2/b**2 <= 1):
                point(x+x0, y+y0)
def obvodka (a, b, x0, y0):
    for x in range(-a, a):
        for y in range(-b, b):
            if(x**2/a**2 + y**2/b**2 <= 1):
                if(x**2/a**2 + y**2/b**2 >= 0.90): 
                    point(x+x0, y+y0)
penSize(0)
penColor("#ffffff")
ellipse(25, 30, 260, 100)
penColor("#a5b7ba")
obvodka(25, 30, 260, 100)
penColor("#ffffff")
ellipse(25, 30, 290, 100)
penColor("#a5b7ba")
obvodka(25, 30, 290, 100)
penColor("#ffffff")
ellipse(25, 30, 225, 125)
penColor("#a5b7ba")
obvodka(25, 30, 225, 125)
penColor("#ffffff")
ellipse(25, 30, 260, 130)
penColor("#a5b7ba")
obvodka(25, 30, 260, 130)
penColor("#ffffff")
ellipse(25, 30, 295, 130)
penColor("#a5b7ba")
obvodka(25, 30, 295, 130)
penColor("#ffffff")
ellipse(25, 30, 320, 100)
penColor("#a5b7ba")
obvodka(25, 30, 320, 100)
penColor("#ffffff")
ellipse(25, 30, 330, 130)
penColor("#a5b7ba")
obvodka(25, 30, 330, 130)


penColor("#ffffff")
ellipse(20, 15, 50, 180)
penColor("#a5b7ba")
obvodka(20, 15, 50, 180)
penColor("#ffffff")
ellipse(20, 15, 75, 182)
penColor("#a5b7ba")
obvodka(20, 15, 75, 182)
penColor("#ffffff")
ellipse(20, 15, 35, 195)
penColor("#a5b7ba")
obvodka(20, 15, 35, 195)
penColor("#ffffff")
ellipse(20, 15, 60, 195)
penColor("#a5b7ba")
obvodka(20, 15, 60, 195)
penColor("#ffffff")
ellipse(20, 15, 80, 195)
penColor("#a5b7ba")
obvodka(20, 15, 80, 195)
penColor("#ffffff")
ellipse(20, 15, 100, 182)
penColor("#a5b7ba")
obvodka(20, 15, 100, 182)
penColor("#ffffff")
ellipse(20, 15, 103, 200)
penColor("#a5b7ba")
obvodka(20, 15, 103, 200)


#Зонтик Палка

penSize(6)
penColor(228, 131, 18)
line(90, 450, 90, 323)
####################
penSize(2)
penColor(228, 131, 18)
line(180, 450, 180, 360)

#Зонтик Шляпа
points = [(87, 290), (92, 290), (20, 323), (160, 323)]
penSize(2)
penColor(244, 80, 80)
brushColor(244, 80, 80)
polygon(points)
###################
points = [(179, 340), (181, 340), (150, 360), (210, 360)]
penSize(2)
penColor(244, 80, 80)
brushColor(244, 80, 80)
polygon(points)

#Зонтик Узоры на шляпе

penSize(1)
penColor(221, 73, 98)

line(92, 289, 92, 324)
line(87, 289, 87, 324)

penColor(50,50,50)
line(87, 290, 38, 324)
line(87, 290, 56, 324)
line(87, 290, 74, 324)

line(92, 290, 105, 324)
line(92, 290, 123, 324)
line(92, 290, 141, 324)

#################

penSize(1)
penColor(221, 73, 98)

line(179, 360, 179, 340)
line(181, 360, 181, 340)

penColor(50,50,50)
line(181, 340, 188, 360)
line(181, 340, 196, 360)
line(181, 340, 202, 360)

line(179, 340, 172, 360)
line(179, 340, 164, 360)
line(179, 340, 156, 360)

#Дно коробля

penSize(0)
penColor(60, 60, 60)
brushColor(188, 79, 1)
circle(250, 280, 25)

penSize(0)
penColor(66,30,224)
brushColor(66,30,224)
rectangle(225, 280, 280, 250)

penSize(1)
penColor(60, 60, 60)
line (225, 280, 300, 280)

penSize(1)
penColor(60, 60, 60)
brushColor(188, 79, 1)
rectangle(400, 305, 250, 280)

points = [(400, 305), (400, 280), (460, 280)]
polygon(points)

penSize(3)
penColor(0, 0, 0)
brushColor(255, 255, 255)
circle(410, 290, 7)
################

penSize(0)
penColor(60, 60, 60)
brushColor(188, 79, 1)
circle(70, 265, 15)

penSize(0)
penColor(66,30,224)
brushColor(66,30,224)
rectangle(55, 265, 86, 250)

penSize(1)
penColor(60, 60, 60)
line (55, 265, 70, 265)

penSize(1)
penColor(60, 60, 60)
brushColor(188, 79, 1)
rectangle(180, 280, 70, 265)

points = [(180, 280), (180, 265), (230, 265)]
polygon(points)

penSize(2)
penColor(0, 0, 0)
brushColor(255, 255, 255)
circle(190, 271, 4)


#Парус

penSize(6)
penColor(0, 0, 0)
line(300, 200, 300, 280)

penSize(1)
penColor(60, 60, 60)
brushColor(223, 214, 154)

points = [(300, 200),(320, 240), (360, 240)]
polygon(points)

points = [(300, 280), (320, 240), (360, 240)]
polygon(points)

#####################
penSize(3)
penColor(0, 0, 0)
line(120, 220, 120, 265)

penSize(1)
penColor(60, 60, 60)
brushColor(223, 214, 154)

points = [(120, 220),(130, 240), (150, 240)]
polygon(points)

points = [(120, 265), (130, 240), (150, 240)]
polygon(points)


run()
