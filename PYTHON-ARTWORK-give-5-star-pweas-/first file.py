from turtle import *
screen = Screen()
screen.setup(width=1200, height=800)
screen.screensize(2000, 1500) 
tom = Turtle()
tom.speed(0)
tom.width(1)
tom.shape('turtle')
tom.color('#779163')
tom.pu()
tom.goto(-150, 300)
tom.pd()
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()
tom.right(90)
tom.forward(25)
tom.left(90)
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()


def square(c):
    tom.color(c)
    tom.begin_fill()
    for count in range(4):
        tom.forward(25)
        tom.right(90)
    tom.end_fill()

def jump(l):
    tom.pu()
    tom.forward(l)
    tom.pd()

for count in range(12):
    square('#8E9B63')
    jump(50)

tom.pu()
tom.backward(600)
tom.right(90)
tom.forward(25)
tom.left(90)
tom.pd()
tom.color('#779163')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()

for count in range(6):
    jump(25)
    square('#8E9B63')
    jump(25)
    square('#9F9B63')
    jump(25)
    square('#8E9B63')
    jump(25)

jump(-600)
tom.right(90)
tom.pu()
tom.forward(25)
tom.left(90)
tom.pd()

tom.color('#8E9B63')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()

jump(25)
square('#9F9B63')
for count in range(3):
    jump(50)
    square('#9F9B63')

jump(50)
square('#3B292A')
for count in range(6):
    square('#3B292A')
    jump(25)
    

square('#9F9B63')
jump(50)
for count in range(3):
    
    square('#9F9B63')
    jump(50)
square('#9F9B63')
jump(25)

tom.pu()
tom.backward(600)
tom.right(90)
tom.forward(25)
tom.left(90)

tom.pd()
tom.color('#9F9B63')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()


jump(25)
square('#9F9F81')
jump(50)
square('#8E9B63')

jump(50)
square('#9F9F81')
jump(50)
square('#8E9B63')

for count in range(6):
    jump(25)
    square('#3B292A')

jump(25)
square('#291515')

jump(25)
square('#3B292A')

jump(50)

square('#9F9F81')

jump(50)
square('#8E9B63')
jump(50)
square('#9F9F81')
jump(50)
square('#8E9B63')

tom.pu()
tom.backward(600-25)
tom.right(90)
tom.forward(25)
tom.left(90)
tom.pd()

tom.color('#9F9B63')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()


square('#9F9F81')
jump(50)
square('#9F9F81')
jump(50)
square('#9F9F81')
jump(50)
square('#9F9F81')  
jump(25)


for count in range(2):
    square('#3B292A')
    jump(25)

for count in range(4):
    square('#C79F5B')
    jump(25)


for count in range(2):
    square('#3B292A')
    jump(25)

square('#291515')
jump(25)

square('#3B292A')
jump(50)

for count in range(3):
    square('#9F9F81')
    jump(50)

tom.pu()
tom.right(90)
tom.forward(25)
tom.left(90)
tom.backward(600)
tom.pd()

tom.color('#9F9B63')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()


for count in range(2):
    square('#63775B')
    jump(25)

jump(25)
square('#9F9F81')
jump(50)
square('#9F9F81')
jump(50)
    


square('#3B292A')
jump(25)
square('#3B1D16')

for count in range(4):
    jump(25)
    square('#E5C263')

jump(25)
square('#C79F5B')
jump(25)
square('#291515')
jump(25)
square('#3B292A')

for count in range(2):
    jump(25)
    square('#291515')


for count in range(3):
    jump(50)
    square('#9F9F81')

tom.pu()
tom.backward(600-25)
tom.right(90)
tom.forward(25)
tom.left(90)
tom.pd()


tom.color('#63775B')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()
    
square('#3B5B5B')
jump(100)
square('#9F9F81')
jump(25)
square('#9F9F81')
jump(25)
square('#3B292A')
jump(25)
square('#3B1D16')
jump(25)
for count in range(6):
    square('#E5C263')
    jump(25)
square('#3B1D16')
jump(25)
for count in range(3):
    square('#291515')
    jump(25)
jump(50)

square('#9F9F81')

for count in range(3):
    jump(25)
    square('#9F9F81')

tom.pu()
tom.backward(600-25)
tom.right(90)
tom.forward(25)
tom.left(90)

tom.color('#63775B')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()

square('#3B5B5B')
jump(75)

square('#818D79')
jump(75)

square('#3B292A')
jump(25)

square('#3B1D16')
jump(25)

for count in range(6):
    square('#E5C263')
    jump(25)

square('#3B1D16')
jump(25)
for count in range(3):
    square('#291515')
    jump(25)

jump(75)

for count in range(3):
    square('#9F9F81')
    jump(25)

tom.pu()
tom.backward(600)
tom.right(90)
tom.forward(25)
tom.left(90)
tom.pd()


tom.color('#818D79')
tom.begin_fill()
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(600)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.end_fill()

square('#3B5B5B')
jump(75)

square('#63775B')
jump(25)
square('#63775B')
jump(25)
square('#3B5B5B')
jump(25)


square('#3B292A')
jump(25)
square('#3B1D16')
jump(25)




for count in range(6):
    square('#E5C263')
    jump(25)


square('#3B1D16')
jump(25)
square('#3B1D16')
jump(25)
square('#291515')
jump(25)
square('#291515')
jump(25)

jump(75)

square('#8D9581')
jump(25)
square('#8D9581')
jump(25)
square('#8D9581')
jump(25)















done()


