#!/usr/bin/env python3.6


bool = [False, True]
print ('x\ty\tx or y')
#Tabla de verdad de 'or'
for x in bool:
    for y in bool:
        print (x,' ', y, ' ' , x or y)
print ()

#Tabla de verdad de 'and'
print ('x\ty\tx and y')
for x in bool:
        for y in bool:
            print (x, ' ',y,' ', x and y)
print ()

#Tabla de verdad de 'not'
print ('x\t falso x')
for x in bool:
    for y in bool:
        print (x,' ', not x)
print ()








