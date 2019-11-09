from graph import *


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

#Солнце
 
penColor(255,247,23)
brushColor(255,247,23)
circle(435, 125, 35)

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

#Зонтик Палка

penSize(6)
penColor(228, 131, 18)
line(90, 450, 90, 323)

#Зонтик Шляпа
points = [(87, 290), (92, 290), (20, 323), (160, 323)]
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




run()
