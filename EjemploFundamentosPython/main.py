print("Hola mundo")

numero:int = 45
print(numero)
numero1:int = 75
print(numero1)
numero2:int = 4.5
print(numero2)
esColombiano = True
print(esColombiano)


#operadores
num1 = 10
num2 = 8
suma = num1 + num2
print("la suma es: "+ str (suma))

q = 5
print(q > 4 and q < 9)

print(q > 5 or q < 10)

#relacionales
m = 45
n = 23
print(m == n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)
print(m != n)

#funciones
def miFuncion():
    print("Hola, soy Jefferson Roa")
miFuncion()

def mostrarNombre(nombre, apellido):
    print("Su nombre es: " + nombre + " " + apellido)
mostrarNombre("Jefferson", "Roa")



base = 7
altura = 4

def calcularAreaTriangulo(b, a):
    area = (b * a)/2
    return area
resultado = calcularAreaTriangulo(base, altura)
print("El area es: " + str (resultado))



#condicionales

edad = 23
if edad >= 18:
    print("usted es mayor de edad")
else:
    print("usted no es mayor de edad")

num3 = 200
num4 = 300

if num3 > num4:
    print("num3 es mayor que num4")
elif num3 == num4:
    print("num3 y num4 son iguales")
else:
    print("num3 es menor que num4")


#parametros end y sep
print("Texot de ejemplo", end =",")
print("Oscar","Carlos","Juan", sep=",")
print("Oscar","Carlos","Juan", sep="_", end="_Creditos_Libres_2.pdf")


#ciclos
#mientras
i = 0
while(i <= 6):
    print(i)
   #i = i + 1
    i += 1


frutas = ["Manzanas", "Banano", "Pera"]
for x in frutas:
    print(x)




