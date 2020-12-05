#!/bin/python3
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = [100,0,0]
o = [255,115,0]
y = [255,217,0]
g = [0,255,0]
b = [0,0,255]
n = [106,84,128]
p = [89,0,94]





'''
[] = 대괄호, {} =  중괄 호 , () = 소  괄  호 

'''


my_rainbow =  [
  r,r,r,r,r,r,r,r,
  r,o,o,o,o,o,o,o,
  r,y,y,y,y,y,y,y,
  g,g,g,g,g,g,g,g,
  r,b,b,b,b,b,b,b,
  n,n,n,n,n,n,n,n,
  p,p,p,p,p,p,p,p,
  p,p,p,p,p,p,p,p
  ]

sense.set_pixels(my_rainbow)


