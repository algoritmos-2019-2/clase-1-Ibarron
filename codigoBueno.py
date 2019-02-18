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

print ("A continuación se mostrará el codigo de la suma del numero que escriba")
sum = 0
Num = int(input( "Ingrese el numero: "))
for i in range (1, Num+1):
   sum= sum+i
   print (sum)
  

print ("Posterior se calculara los primeros n numero impares")
x= []
num = int(input("Numero final de la cadena: "))
for i in range (1,num):
    if (i %2 == 0): continue
    x.append (i)
print (x)


print ("Numero factorial de cualquier numero: ")
n = int (input ("Ingresa el numero: "))
factorial= 1
for i in range (1, n+1):
    factorial = factorial *i
print ( "El factorial es: ")
print (factorial)
	

print ("Imprimir los x numeros de la serie de Fibonacci")
x = int (input ("Inserte el valor de x: "))
def fib (x):
    a = 0
    b = 1
   
    for l in range (x):
        c = b + a
        a = b
        b = c
       
    return a
print (fib (x))
