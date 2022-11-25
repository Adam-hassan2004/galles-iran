#esercizio 1
import random
x=random.randrange(0,100)
y=random.randrange(0,100)
z=random.randrange(0,100)
if z<y and y < x:
    print(z, y , x)
if  z<x and x<y:
    print( z,y,x)
if x<y and y<z:
    print(z,y,x)    
if x<z and z<y:
    print(x,z,y)
if y<z and y<x:
    print(y,z,x)
if y<x and x<z:
    print(z,x,y)
#esercizio 2
print("¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤ø,¸¸,ø¤º°`°º¤ø,¸")
moto=["bmw", "yamaha","kawasaki","honda"]
auto=["ford","nissan","lambo","ferrari"]
lista=auto+moto
lista.sort()
print(lista)
