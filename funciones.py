# Funciones se ejecutan solo cuando se llama "def"
# Se pueden llamar cuantas uno quiera 
# Estructura --> def "nombre de la funcion"():

# Sintaxis

# def mi_funcion():
#     instrucciones

# Tipos de funciones:

#!     Sin Argumentos y sin retornos

# def saludo():
#     print("Saludando a las personas")
# saludo() #* aqui se llama la funcion

#!     Sin Argumentos y con retornos

# def sumar():
#     num1 = int(input("ingrese valor: "))
#     num2 = int(input("ingrese valor: "))

#     num3 = num1 + num2

#     return num3

# print (sumar())

#!     Con Argumentos y sin retornos

# def sumar(num1, num2):

#     num3 = num1 + num2
#     print(f"La suma de {num1} + {num2} = {num3}")

# num1 = int(input("ingrese valor: "))
# num2 = int(input("ingrese valor: "))

# sumar(num1, num2)

#!     Con Argumentos y con retornos

# def sumar(a,b):

#     c=a+b
    
#     return c

# x = int(input("ingrese valor: "))
# y = int(input("ingrese valor: "))

# s = sumar(x,y)

# print(s)

#--------------------------
#* Otras funciones

# def varios_valores(*args): #* (*) esto se llama recibir párametros indeterminados por posición

#     for arg in args:

#         print(args)
#         print(type(args))

# varios_valores(4.5, "Buen día", [1,2,3,4,5])

# def varios_devoluciones():

#     return 1, 4.5, "Juan"

# s= varios_devoluciones()
# s= list(s)

# print(type(s))

#---------------------

# def resta(a=None, b=None):
#     if a == None or b == None:

#         print ("Error, faltan parámetros a la función")
#         return
#     return a - b

# resta()
