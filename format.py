'''nombre = input("ingresa tu  nombre : ")
edad =  input("ingresa tu edad : ")
print("hola", nombre, "su edad es",edad, "años") # print("leyenda",variable,"leyenda",variable) PRESTAR ATENCION A LAS COMAS DESPUES DE LA VARIABLE SI VA A SEGUIR PRINTEANDO 
print("hola {} tu edad es {}".format(nombre,edad)) # se abre llaves (alt+123) donde iria la variable y al cerrar las "" del print .FORMAT(VARIABLE1,VARIABLE2)
# booleanos verdadero o falso'''



'''verdadero = True 
falso = False
num1 = 500
num2 = 1000
print(num1> num2) #devuelve true o false 
cadena = "Estoy mostrando los metodos booleanos para los srtings"
print(cadena.startswith("E")) #startswith = arranca con? T o F 
print(cadena.endswith("E")) #startswith = arranca con? T o F 
print(cadena.isupper("")) #isupper= si esta todo en mayuscula
print(cadena.islower("")) #islower = si esta todo en minuscula'''

'''IF / ELSE 
edad =  input("ingrese su edad : ")
edad = int(edad) #debe pasar de string a int (input es string)#
if edad >= 18 : 
    print ("mayor de edad")
else:
    print ("no eres mayor de edad")'''

'''ELIF
letra = input ("ingrese una vocal : ")
if letra == "a":
    print("esta vocal es la a")
elif letra == "e":
    print("es la vocal e")
elif letra == "i":
    print("es la vocal i")
elif letra == "o":
    print("es la vocal o")
elif letra == "u":
    print("es la vocal u")'''


''' CONDICIONALES ANIDADOS
edad = input ("ingrese se edad")
edad = int (edad)
nombre = input ("ingrese su nombre")
if nombre == "mateo" :
    if edad >= 18 :
        print("es mayor de edad y su nombre es el corercto")
    else : 
        print("su nomnre es correcto pero no es mayor de edad")''' 
    

'''ESTRUCURA DE DATOS
lista = ['python', 120, 'nombre', 4.14, 6.28] #se crean con [] y son editables.
print(lista[3])
lista[0] = "MATEO"
print(lista[0])'''

'''lista = [ 1,2,3,4,5,6,7,8,9]
print(lista[0:5])
print(lista[0:])
print(lista[:6])'''

'''#METODOS DE LISTA 
lista = [1,2,3,4,5] #agg mas dartos a la lista 
lista.append(6) #NOMBRE.APPEND(VALOR QUE QUIERO AGG)

lista.append('MATEO') #PARA AGG CARACTS SE PONE COMILLA SIMPLE 'QWERTY'

print(lista[0:])

#AGREGAR UN DATO EN POSICION DETERMINADA
lista = [1,2,3,4,5]
lista.insert(2, 'hola') #NOMBRELISTA.INSEET(POSICION,DATO)
print(lista[0: ])

#CUANTOS ELEMENTOS X HAY EN UNA LISTA 
lista = [1,2,3,4,5,2,6,5,1,7,9,5,2,5]
print(lista.count(5)) #nnombrelista.count(valor que quiero averiguar)
print(lista.index(4)) #averigua cual es la posicion de la primera vez que aparece el valor del()
lista1=[7,4,1,2,5,8,2.4, 5, 9,6,3]
lista1.sort() #nombre.sort acomoda los valores de menor a mayor
print(lista1[0: ])
lista.sort()
print(lista[0: ])
lista.reverse() #nombre.reverse ordena los valores de menor a mayor. 
print(lista[0:])'''

'''#EDITAR O ELIMINAR UN DATO 
lista1=[7,4,1,2,5,8,2.4, 5, 9,6,3]
lista1[3] = "mateo" #PARA MODIFICAR EL DATO EN UN ESPACIO EN ESPECIFICO 
print(lista1[3]) 
lista1.pop() #elimina el ultimo valor de la lista
print(lista1[0:4]) 
lista1.remove('mateo') #nombre.remove(valor o dato que quiero eliminar de la lista(elimina el primero que encuentra))
print(lista1[0:4]) 
lista = [1,2,3,4,5,2,6,5,1,7,9,5,2,5]
lista.remove(5)
print(lista[0: ])'''
 
'''lista = [1,2,3]
lista2 = [4,5,6]
lista3= lista + lista2 
print(lista3[0: ]) #devuelve la union de ambas listas 
lista4= []
edad = int(input("ingrese su edad"))
lista4.append(edad)
print(lista4[0:])
print("su edad es ",lista4[0])

#ejercicio 
leje = [20,50,"curso","python",3.14]
print(leje[0: ])
primer = int(input("ingrese un valor"))
segundo = int(input("ingrese otro valor"))
leje[0]= primer
leje[1]= segundo
print(leje[0: ])'''

'''#diccionarios AGREGAR Y MODIFICAR  
diccionarios = { 'usuario': "mateo" , 'contrasena' : 1414  } #diccionario = {'clave' : "valor ó xxxx" , 'clave2' : "qwerty"} LA CALVE NO SE PUEDE REPETIR//  SE SEPARA EN COMAS  
print(diccionarios)

#elementos direccionarois 
diccionario1 = { 'nombre': "Mateo", 'apellido' : "Barranco" , 'estatura' : 1.80} 
print(diccionario1)
print(diccionario1.keys()) # LLAVE = CLAVE = KEYSS
print(diccionario1.values())

print(diccionario1["nombre"]) # entre corchetes la clave y imprime el valor al que estas llamando 
diccionario1["peso"] = "73 kg" #PARA AGREGAR UNA CLAVE Y UN VALOR 
print(diccionario1)'''

 
'''#METODOS EN DICCIONAROS 
diccionario =  {1 : 2 , 2 : 3, 3 : 4}
diccionario2 =  {1 : 21 , 2 : 3, 3 : 4}


diccionario.pop(3) # elimina la  calve que se ingresa en el parentesis 
print(diccionario)
diccionario.clear() #borra todo el diccionario 

print(diccionario2.get(1)) #diccionario.get() trae el VALOR  de la clave que se ingresa en el parentesis

diccionario2.setdefault( 4 , 5) #setdefault(llave , valor) agrega al final del diccionario una llave y valor nuevos
print(diccionario2)

diccionario3 = { 4 : 5, 14 : 5 , 10 : "messi", }
print(diccionario3)
diccionario2.update(diccionario3)
print(diccionario2)'''

#CONJUNTOS 
conjunto = { 1,2,3,4,5} #pueden crearse con llaves 
'''print(conjunto)
conjunto2 = set(( 5,4,3,2,1)) #la funcion set crea conjuntos
conjunto3 = { 1,1,2,2,3,4,5,5,6}
lista = [ 1,1,2,2,3,4,5,5,6]
print(lista)
print(conjunto3) #los conjuntos no imprimen valores repetidos 
conjunto.add(20) #añade el dato al final del conjunto 
print(conjunto)
conjunto.pop()#elimina un valor al azar del conjunto 
conjunto.update([11,22,33]) #agrega el valor o la lista al conjunto indicado
print(conjunto)
conjunto.update([1414])
print(conjunto)'''

#TUPLAS "SUS DATOS MO PUEDEN CAMBIAR, ACTUALIZAR, BORRAR" 
tupla = 1,2,3,4,5
tupla2 = (7,8,9,4,5,6) #puede ir o no con parentesis 
print(tupla2[3]) 
print(tupla[0:4])
print(tupla2 + tupla2)


