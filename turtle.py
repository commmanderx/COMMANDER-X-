from turtle import * 
from random import randint 
bgcolor('black') 
x = 4
speed(225) 
while x < 900: 
 r = randint(1,155) 
 g = randint(1,155)  
 b = randint(1,155) 
  
 colormode(255)  
 pencolor(r,g,b) 
 fd(10+ x) 
 rt (901)
 x = x+3
done()
