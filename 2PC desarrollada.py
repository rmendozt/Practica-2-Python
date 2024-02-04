# PROBLEMA 1
def num_multiplos(lim_i,lim_f):
    if lim_f>lim_i:
        resultado=[]
        for n in range(lim_i,lim_f+1):
            if n%7 ==0 and n%5 ==0:
                resultado.append(n)

        return resultado
    raise ValueError("El límite inferior debe ser menor al límite superior.")
multiplos=num_multiplos(1500,2700)
print(multiplos)

#PROBLEMA 2
n=5
for i in range(1,n+1):
    for j in range(i):
        print("* ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("* ", end="")
    print()
# PROBLEMA 3
numeros=[]
par=impar=0
while True:
    deseo=str(input("Desea ingresar un número? : si o no"))
    if deseo=='si':
        n=int(input("Ingresa un número:"))
        if n%2==0:
            par+=1
            numeros.append(n)
        else:
            impar+=1            
            numeros.append(n)
    if deseo=='no': 
        break
print(numeros)
print(f"Cantidad de números pares: {par}")
print(f"Cantidad de números impares: {impar}")

#PROBLEMA 4
    nombres=[]
notas=[]
for x in range(4):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    nota1=int(input("Ingrese nota 1:"))
    nota2=int(input("Ingrese la nota 2:"))
    nota3=int(input("Ingrese la nota 3:"))
    notas.append([nota1,nota2,nota3])

for x in range(4):
    print(nombres[x],notas[x][-3],notas[x][-2],notas[x][-1])

#PROBLEMA 5
num=int(input("Ingresa cualquier número: "))
digito=int(input("Ingrese un solo dígito: "))
contador=0
while num>0:
    if digito==num % 10:
        contador+=1
    num=num//10
print(f"Cantidad de veces {digito} en el número: {contador}")

# PROBLEMA 6

def fibonacci(n):

    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(1,50):
    print(fibonacci(i))

 #   PROBLEMA 7
    
    def primo(numero):
    if numero==1:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2,numero):
            if numero %i==0:
                return False
            return True
for i in range(1,101):
        print(i,primo(i))
#PROBLEMA 8
def factorial (n):
    f = 1
    for i in range (2, n+1):
        f = f*i
    return (f)
#probamos con factorial de 5
factorial(5)

# PROBLEMA 9
texto = input("Escriba una operación : " )

vocales = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U','á','é','é','ó','ú')

for letra in vocales:
    texto = texto.replace(letra, "")

print (texto)

#PROBLEMA 10