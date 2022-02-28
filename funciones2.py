def countDown(inicio):
    newArray=[]
    for i in range (inicio, -1, -1):
        newArray.append(i)
    return newArray


x = countDown(5)
print(x)


def imprimir_y_devolver(imprime, devuelve):
    print(imprime)

    return devuelve


y= imprimir_y_devolver(1, 2)
print(y)

def primero_mas_longitud(lista):
    sum= lista[0] + len(lista)
    return sum


j= primero_mas_longitud([1, 2, 3, 4, 5])
print(j)


def valores_mayores_que_el_segundo(arreglo):
    newList = []
    count = 0
    if len(arreglo) < 2:
        return False
    for i in range (0, len(arreglo)):
        if arreglo[i] > arreglo[1]:
            newList.append(arreglo[i])
            count += 1
    print (count)
            
    
    return (newList)
    
    


t = valores_mayores_que_el_segundo([5,2,3,2,1,4])
u = valores_mayores_que_el_segundo([3])
print (t)

def largo_y_valor(largo, valor):
    newArray2=[]
    for i in range (0, largo):
        newArray2.append(valor)
    return newArray2


o = largo_y_valor(4, 7)
print (o)
y= largo_y_valor(6, 2)
print (y)