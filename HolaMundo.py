
import requests
import math
#import hola2.py 

#print(num:=input("Contraseña bro: "))

lst = [1,2,3,4]



if 12 in lst:
	print("12 si rifa")
	#Enlugar de llaves se usan TABS---- 	----
else:
	print("No en la lst")
for i in range (4):
	print(lst[i])

a = list(range(3,15,3))
print(a)
numbers = [1,2,3,4,5,6]

def imprimi_lago(func, x,y):
	print("Im a function dude con parametro de una funcion" )
	print(func(x,y))
	"""
	Normaly this is used to explain CODE
	But I'll use it to coment code that i will not use XD
	"""
def second(a,b):
	return a+b

imprimi_lago(second,1,2)

def func(x):
	res =0
	for i in range(4):
		res+=i
	return res
print(func(4))

def f_c(c):
	print(9/5*c+32)



		#CICLO WHILE realiza diferentes actividades 

while True:
	s = int(input("""\nBOludo hace loq ue quieras
1-Exit 
2-Hola Mundo
3-Critica constructiva
4-Operacion con dos numeros
5-Listas
6-Functions
7-Exceptions
8-Open Files Boludo
9- List, Dictionary and Tuples from other Class
"""))
	if s==1:
		break
	elif s==2:
		print("Hola mundo")
	elif s==3:
		print("""Quisas no diveaste bien, pero considero
			que deberias tmar en cuenta los sums del enemigo
			antes de hacerlo""")
	elif s==4:
		operation = int(input(""""Type the operation
			1-suma
			2-resta
			3-multiplicar"""))
		if operation == 1:
			x = int(input("Number 1:"))
			y = int(input("Number 2:"))
			print("Resultado suma: ", x+y)
		if operation == 2:
			x = int(input("Number 1:"))
			y = int(input("Number 2:"))
			print("Resultado suma: ", x-y)
		if operation == 3:
			x = int(input("Number 1:"))
			y = int(input("Number 2:"))
			print("Resultado suma: ", x*y)
	elif s==5:
		print("Tines esta lista [1,2,3,4,5,6]\n1-AGREGAR ELEMENTO AL FINAL \n2-iNSERTAR NUMERO DONDE SEA \n3-recorrer lista")
		
		do = int(input())
		if do ==1:
			print(numbers)
			add = int(input())
			numbers.append(add)
			print(numbers)
		if do ==2:
			print(numbers)
			index = int(input())
			num = int(input())
			numbers.insert(index,num)
			print(numbers)
		if do ==3:
			for lsta in numbers:
				print(lsta) 
	elif s==6:
		print(""""Funciones que podes correr 
1-Grados centigrados to Farenheit
2-Funcion dentro de otra funcion
""")
		func = int(input())
		if func == 1:
			cel = int(input("Grados centidragos: "))
			f_c(cel)
		elif func ==2:
			imprimi_lago(second,1,2)
	elif s==7:
		print("""Welcome to Exceptions
Here you can fail, but dont care 
This module is about that XD
1-EXEPTION VALUE error
2-Division entre 0
""")
		e=int(input("¿Que exceptions qeures que salga?"))

		if e==1:
			try:
				print("2"+1)
			except TypeError:
				print("Che no podes sumar un string y un en entero, pelotudooo\n")
		elif e==2:
			try:
				num1 = 8
				num2 =0
				print(num1/num2)
			except ZeroDivisionError:
				print("No carnal esto no se puede hacer como que 8 entre 0?")
			finally:
				print("Esta wea se ejecuta de ahuevo si falla o no")
	elif s==8:
		print("""Che boludo aqui manejas Archivos que te apetece hacer?
1-Abrir arhivo
2-leer archivo
3-Agregar algo a un archivo 
3-Binary, creo abre imagens y sonidos o weas
""")
		f=int(input("Escoge alguna cosa"))
		
		if f==1:
			print("SobreEscribir en un archivo")
			with open("OpenFilesPython.txt", "w") as f:
				f.write("Esta wea se agregara al archivo")
				f.close()

				f=open("OpenFilesPython.txt", "r")
				print(f.read())
			f.close()

		elif f==2:
			index=1
			lenfile=0
			
			file= open("OpenFilesPython.txt", "r")
		
			lenfile = len(open("OpenFilesPython.txt").readlines())
			
			for  line in file.readlines():
			
				if index == lenfile:
					print(line[0]+str(len(line)))	
				else:
					print(line[0]+str(len(line)-1))
				index+=1
			file.close()
		elif f==3:
			print("Agregar algo al arhivo")
			file=open("waifu.jpg", "a")
			file.close()
	elif s==9:
		print("Creo que esto es dictionarys tuples y sabe que mas listas :v y el none ")
		print("1-NONE \n2-List \n3.Dictionary \n4-Listas")
		l = int(input("La reconcha weon que queres apreder? /O·O/"))
		if l == 1:
			print("You chose NONE")
			print("This wea supose to be like an EMPY osea que si no hay nada pues us none para comprobar que no esta vacio XD ")
			foo = print("a")

			if foo is not None:
				print("Theres nothing to read dude")
			else:
				print("Si contiene algo ese weon")
		if l == 2:
			print("Dictionarios bro")
			print("TO define a Dictionary you need to do it between { } ")
			ages = {"Juan": 24, "Dian":12, "Lola": 14}
			print(ages)
			print(ages["Dian"])
	
