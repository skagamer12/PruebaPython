import math 
from itertools import count
squares = [1,2,3,4,5,6,7,8,9,10]

print(squares[2:4:9])

cubes = [i**2 for i in range(5)]

print(cubes)

# squares[8] = 64
# print(squares[3])
# squares[3] = 9
# print(squares[3])

nums = [1,12,3]

msg = "numeros: {0} {1} {2}".format(nums[0],nums[1],nums[2])
msg.join("Hola boludo")
print(msg)
msg.upper
a = "{x}, {y}".format(x=10, y=13)
print(a)
print(max(squares), min(squares))
print("Round")
print(sum(squares))

e=min([sum([11, 22]), max(abs(-30), 2)])
print(abs(30))


numb = "Esta wea es un string como input simonsssss"

txt = numb.split()

word=""

for i in range(len(txt)):
    if len(txt[i]) > len(word):
        word = txt[i]
print(word)

def add_fice(x):
    return x+5
n5 = [11,22,33,44,55]
result = list(filter(lambda x: x%2==0,nums))
print(result)
  #Wrap function normally 
def decor(func):
    def wrap():
        print("=====")
        func()
        
        print("=====")
    return wrap

def print_text():
    print("Halo tia ")

# decorated= decor(print_text)
# decorated()
@decor
def other_f():
    print("Sere decora o uppercase")

other_f()


#Sets 

num_set = {1,2,3,4,5}
word_set = set (["spam","eggs","sausage",2,3])

print( 3 in num_set)
print("spam" not in word_set)

num_set.add(-6)
num_set.remove(3)
#print(num_set)
    #combina
print(num_set | word_set)
    #que existan en both
print(num_set & word_set)
    #Lo que no hay en el primero pero si en el segundo 
print(num_set - word_set)
print(word_set-num_set)
    #creo que lo que no hay en ambos 
print(num_set ^ word_set)

num_set = {0,1,2,3 } & num_set
print(num_set)
     #Itertools




l=[0,1]
x=0
   #try factorial 
def fact(numf):
    global x
    global l
   
    if numf == 1:
        return l
    else:
        if x == 0:
            print(l[x])
            x=x+1
        l.append(l[x]+l[x-1])
        print(l[x])
        x=x+1
        return fact(numf-1)
    
fact(5)