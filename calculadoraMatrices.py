'''
Proyecto: calculadora de matrices
Integrantes: Gabriel Vindas, Jose Pablo Murillo
Curso: Algebra lineal para computacion
Fecha de creacion: 8/03/2016
Ultima modificacion: 16/03/2016
Descripcion: una calculadora que hace operaciones de matrices entre 1 o 2 matrices
'''

##modulos importados
import tkinter #modulo para interfaces graficas
from tkinter import*



##Funciones para matrices
#Nombre:crearLista
#Entradas:cantidad de elementos
#Salidas:una lista nula
#Descripcion:Crea una serie de filas y la rellena de columnas nulas
def crearLista(n):
    lista = list()
    while n != 0:
        lista = lista + [[]]
        n = n - 1
    return lista

#Nombre:numFilas
#Entradas:matriz
#Salidas:cantidad de filas
#Descripcion:retorna largo de matriz
def numfilas(matriz):
    if matriz == []:
        return 0
    else:
        return len(matriz)

#Nombre:numcolumnas
#Entradas:matriz
#Salidas:cantidad de columnas
#Descripcion:retorna largo de fila
def numcolumnas(matriz):
    if matriz == []:
        return 0
    else:
        return len(matriz[0])



#Nombre:crearMatriz
#Entradas:cantidad de filas y columnas
#Salidas:una matriz vacia
#Descripcion: crea una serie de filas y luego llena cada fila de columnas
def crearMatriz(filas,columnas):
    matriz = crearLista(filas)
    for i in range(0,filas):
        matriz[i] = crearLista(columnas)
    return matriz

#Nombre:esCuadrada
#Entradas:una matriz
#Salidas:True o False
#Descripcion: Verfica si la cantidad de filas es igual a la cantidad de columnas fila por fila
def esCuadrada(matriz):
    if matriz == []:
        messagebox.showerror(None,"Debe ingresar la cantidad de filas y columnas")
        return
    dimension = tamano(matriz)
    filas = dimension[0]
    columnas = dimension[1]
    if filas != columnas:
        return False
    else:
        return True

#Nombre:estaVacia
#Entradas:una matriz
#Salidas:True o False
#Descripcion:Verifica entrada por entrada si hay un dato
def esVacia(matriz):
    if matriz == []:
        return True
    dimension = tamano(matriz)
    filas = dimension[0]
    columnas = dimension[1]
    for i in range(0,filas):
        for j in range(0,columnas):
            if matriz[i][j] == [] or matriz[i][j] == '':
                return True
    return False

#Nombre: soloNumeros
#Entradas:una matriz
#Salidas:True o False
#Descripcion: Verifica entrada por entrada si hay un numero
def soloNumeros(matriz):
    dimension = tamano(matriz)
    filas = dimension[0]
    columnas = dimension[1]
    for i in range(0,filas):
        for j in range(0,columnas):
            if type(eval(matriz[i][j]))!= int:
                return False
            elif type(eval(matriz[i][j])) == float:
                pass
    return True

#Nombre:tamano
#Entradas:una matriz
#Salidas:una lista [cantidad de fila, cantidad de columna]
#Descripcion:Recorre filas y incrementa contador, recorre cada fila y guarda cantidad de columnas
def tamano(matriz):
    cantFilas = 0
    cantColumnas  = len(matriz[0])
    for fila in matriz:
        cantFilas = cantFilas + 1
        if cantColumnas != len(fila):
            return []
        else:
            pass
    return [cantFilas,cantColumnas]

#Nombre:transpuesta
#Entradas:una matriz
#Salidas:matriz transpuesta
#Descripcion:cambia filas por columnas
def transpuesta(matriz):
    if matriz == []:
        return []
    else:
        filas = numfilas(matriz)
        columnas = numcolumnas(matriz)
        trans = crearMatriz(filas,columnas)
        for i in range(0,filas):
            for j in range(0,columnas):
                trans[j][i] = matriz[i][j]
        return trans

#Nombre:crearIdentidad
#Entradas:cantidad de filas y columnas
#Salidas:matriz matriz identidad
#Descripcion:crea matriz y pone 1 en diagonal y resto en 0
def crearIdentidad(filas,columnas):
    matriz = list(crearMatriz(filas,columnas))
    if not escuadrada(matriz):
        messagebox.showerror(None,"Matriz debe ser cuadrada")
        return
    for i in range(0,filas):
        for j in range(0,columnas):
            if i == j:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return matriz

#Nombre:eliminar
#Entradas:matriz, fila y columna
#Salidas:matriz resultante de eliminar fila y columna
#Descripcion:crea matriz resultado de eliminar fila y columna
def eliminar(matriz,fila,columna):
    resultado = list()
    cantfilas = numfilas(matriz)
    cantcolumnas= numcolumnas(matriz)
    for i in range(0,cantfilas):
        pila = list()
        for j in range(0,cantcolumnas):
            if i + 1 == fila or j + 1 == columna:
                pass
            else:
                pila.append(matriz[i][j])
        if pila == []:
            pass           
        elif [] in pila:
            while [] in pila:
                pila.remove([])
        else:
            resultado.append(pila)
    return resultado

#Nombre:menor
#Entradas:matriz, fila y columna
#Salidas:menor 
#Descripcion: crea una matriz despues de eliminar fila y columa
def menor(matriz,fila,columna):
    return eliminar(matriz,fila,columna)

#Nombre:cofactor
#Entradas:matriz, fila y columna
#Salidas:cofactor de matriz 
#Descripcion: usa formula para determinar el cofactor de matriz en fila y columna
def cofactor(matriz,fila,columna):
    global mostrar
    if mostrar:
        print("Cofactor de fila: " + str(fila) + " Columna: " + str(columna))
    suma = fila + columna
    signo = -1
    signo = signo**suma
    if mostrar:
        print("signo es: "+str(signo))
    men = menor(matriz,fila,columna)
    if mostrar:
        print("Su menor correspondiente es: ")
        for i in men:
            print(i)
        print("El cofactor es: "+ str(signo*determinante(men,fila)))
    return signo * determinante(men,fila)


#####Operaciones

#Nombre:sumaMatrices
#Entradas:2 matrices
#Salidas:una matriz con suma de elemento por elemento de las matrices entrada
#en caso, de que se haga paso a paso, hace uno a la vez
#Descripcion: valida que ambas sean cuadradas y con datos luego suma
def sumaMatrices(matriz1,matriz2):
    global procesos
    procesos = list()
    if esVacia(matriz1) or esVacia(matriz2):
        messagebox.showerror(None,"Matrices invalidas")
        return
    elif not soloNumeros(matriz1) or not soloNumeros(matriz2):
        messagebox.showerror(None,"Las matrices deben tener solo datos numericos")
        return
    elif tamano(matriz1) != tamano(matriz2):
        messagebox.showerror(None,"Las matrices no son del mismo tamano")
        return
    else:
        dimension = tamano(matriz1)
        filas = dimension[0]
        columnas = dimension[1]
        resultado = crearMatriz(filas,columnas)
        for fila in range(0,filas):
            for columna in range(0,columnas):
                resultado[fila][columna] = int(matriz1[fila][columna]) + int(matriz2[fila][columna])
                procesos.append(["+",fila,columna])
        return resultado

def mostrarMatrizProceso(matriz):
    copia=matriz
    temp="|"
    imprimir=""
    while copia != []:
        for i in range(len(copia)):
            for j in range(len(copia[0])):
                temp=temp+"  "+str(copia[i][j])+"  "+"|"
            imprimir=imprimir+temp+"\n"
            temp="|"
        copia=[]
    print(imprimir)


#Nombre:esInvertible
#Entradas:una matriz
#Salidas: un True/False
#Descripcion: si determinante == 0 entonces es falso
def esInvertible(matriz):
    for i in range(1,len(matriz)+1):
        if determinante(matriz,i) == 0:
            return False
    return True

#Nombre:mCofactores
#Entradas:una matriz
#Salidas: matriz de cofactores
#Descripcion: calcula cofactor de cada fila y columna
def mcofactores(matriz):
    filas = numfilas(matriz)
    columnas = numcolumnas(matriz)
    cofactores = crearMatriz(filas,columnas)
    for i in range(0,filas):
        for j in range(0,columnas):
            cofactores[i][j] = matriz[i][j] * cofactor(matriz,i+1,j+1)
    return cofactores
            
            
    
#Nombre:restaMatrices
#Entradas:2 matrices
#Salidas:una matriz con resta de elemento por elemento de las matrices entrada
#en caso, de que se haga paso a paso, hace uno a la vez
#Descripcion: Recorre matriz elemento por elemento y hace resta de elementos
def restaMatrices(matriz1,matriz2):
    global procesos
    if esVacia(matriz1) or esVacia(matriz2):
        messagebox.showerror(None,"Ambas matrices deben estar llenas de datos")
        return
    elif not soloNumeros(matriz1) or not soloNumeros(matriz2):
        messagebox.showerror(None,"Las matrices deben tener solo datos numericos")
        return
    elif tamano(matriz1) != tamano(matriz2):
        messagebox.showerror(None,"Las matrices no son del mismo tamano")
        return
    else:
        dimension = tamano(matriz1)
        filas = dimension[0]
        columnas = dimension[1]
        resultado = crearMatriz(filas,columnas)
        for fila in range(0,filas):
            for columna in range(0,columnas):
                resultado[fila][columna] = int(matriz1[fila][columna]) - int(matriz2[fila][columna])
                procesos.append(["-",fila,columna])
        return resultado

#Nombre:determinante 
#Entradas:matriz, fila
#Salidas:determinante de matriz 
#Descripcion: usa formula de determinante, eliminando la primera fila y columna en caso de ser mayor de 3
def determinante(matriz,fila):
    if not esCuadrada(matriz):
        global mostrar
        messagebox.showerror(None,"Matriz debe ser cuadrada")
        return
    if mostrar:
        print("-----Calculando determinante de:")
        for i in matriz:
            print(i)
    resultado = matriz[:]
    if resultado == []:
        return 0
    elif numfilas(resultado) == 1 and numcolumnas(resultado) == 1:
        if mostrar:
            print("Determinante de una matriz '1x1' es su propio elemento")
        return int(resultado[0][0])
    elif numfilas(resultado) == 2 and numcolumnas(resultado) == 2:
        if mostrar:
            print("Determinante de una matriz '2x2' es el primer elemento por el ultimo menos el segundo elemento por su tercero")
        a = int(resultado[0][0])
        b = int(resultado[0][1])
        c = int(resultado[1][0])
        d = int(resultado[1][1])
        if mostrar:
            print("determinante de:")
            for i in matriz:
                print(i)
            print()
            print("=" + str(a) + "*" + str(d) + "-" + str(b) + "*" + str(c))
        return a*d - b*c
    else:
        resultado = 0
        cantcolumnas = numcolumnas(matriz)
        for j in range(0,cantcolumnas):
            if mostrar:
                print("Hay que hacer la suma de elementos por su cofactor correspondiente")
            resultado = resultado + (int(matriz[fila-1][j]) * cofactor(matriz,fila,j+1))
        return resultado

#Nombre:mcofactores 
#Entradas:matriz
#Salidas:matriz de cofactores
#Descripcion: calcula cofactores de cada fila y matriz
def mcofactores(matriz):
    global procesos,mostrar
    filas = numfilas(matriz)
    columnas = numcolumnas(matriz)
    cofactores = crearMatriz(filas,columnas)
    for i in range(0,filas):
        for j in range(0,columnas):
            cofactores[i][j] = matriz[i][j] * cofactor(matriz,i+1,j+1)
            if mostrar:
                print("Cofactor en fila: "+str(i+1) + " columna: " + str(j+1) + "es: " + str(cofactores[i][j]))
            procesos.append(["C",i,j])
    return cofactores

#Nombre:invertirCofactor 
#Entradas:matriz
#Salidas:matriz inversa
#Descripcion: usa formula de matriz inversa con matriz de cofactores
def invertirCofactor(matriz):
    global mostrar
    if determinante(matriz,1) == 0:
        messagebox.showinfo(None,"La matriz es singular")
        return
    else:
        filas = numfilas(matriz)
        columnas = numcolumnas(matriz)
        det = determinante(matriz,1)
        mcofactor = mcofactores(matriz)
        adjunta = transpuesta(mcofactor)
        if mostrar:
            print("-----Adjunta de la matriz-----")
            for i in adjunta:
                print(i)
        print("El resultado se puede ver en la ventana")
        return multiplicar(adjunta,1/det)

#Nombre:multiplicar 
#Entradas:matriz y numero
#Salidas:Matriz con cada entrada multiplicada por numero
#Descripcion:entrada por entrada multiplica por el numero
def multiplicar(matriz,numero):
    filas = numfilas(matriz)
    columnas = numcolumnas(matriz)
    for i in range(0,filas):
        for j in range(0,columnas):
            matriz[i][j] = numero * int(matriz[i][j])
            if matriz[i][j] == int(matriz[i][j]):
                matriz[i][j] = int(matriz[i][j])
    return matriz[:]


    

#Nombre:multiplicarmatrices
#Entradas:2 matrices
#Salidas: matriz producto
#Descripcion: usa formula de multiplicacion entre matrices
def multiplicamatrices(matriz1,matriz2):
    global procesos
    if numcolumnas(matriz1) != numfilas(matriz2):
        messagebox.showerror(None,'Error la cantidad de columnas de la primera matriz no es igual a la cantidad de filas de la segunda')
        return
    if esVacia(matriz1) or esVacia(matriz2):
        messagebox.showerror(None,"Las matrices no pueden estar vacias")
        return
    else:
        nfilas = numfilas(matriz1)
        ncolumnas = numcolumnas(matriz2)
        matrizresultado = crearMatriz(nfilas,ncolumnas)
        #lleno matriz resultado de 0
        for i in range(0,numfilas(matrizresultado)):
            for j in range(0,numcolumnas(matrizresultado)):
                matrizresultado[i][j] = 0

        #lleno de resultado de producto la matriz
        for i in range(0,nfilas):
            for j in range(0,ncolumnas):
                for k in range(0,len(matriz2)):
                    matrizresultado[i][j] = matrizresultado[i][j] + int(matriz1[i][k]) * int(matriz2[k][j])
                    procesos.append(["*",i,j])
        for elemento in procesos:
            if procesos.count(elemento) != 1:
                while procesos.count(elemento) != 1:
                    procesos.remove(elemento)
        return matrizresultado






#####Funciones para interfaz

#Nombre:mostrarMatriz
#Entradas:A o B
#Salidas:despliega matriz de filas y columnas seleccionadas por usuario
#Descripcion: Usa seleccion de usuario para determinar tamano de matriz a mostrar
def mostrarMatriz(entrada):
    global matrizEntradasA,matrizEntradasB
    global matrizA,matrizB,matrizResultado
    default = principal.cget('bg')

    labelResultado.grid_forget()
    for i in range(0,len(matrizResultado)):
        for j in range(0,len(matrizResultado[0])):
            matrizResultado[i][j].config(text="")
            matrizEntradasB[i][j].config(bg=default)
            matrizResultado[i][j].grid_forget()
        
    if entrada == "A":
        filas = entryEntrada1.get()
        if type(eval(filas)) != int:
            messagebox.showerror(None,"La cantidad de filas debe ser un numero entero")
            return
        elif int(filas) <= 0:
            messagebox.showerror(None,"La cantidad de filas debe ser mayor a 0")
            return
        elif int(filas) > 5:
            messagebox.showerror(None,"La cantidad de filas debe ser maximo 5")
            return
        else:
            columnas = entryEntrada12.get()
            if type(eval(columnas)) != int:
                messagebox.showerror(None,"La cantidad de columnas debe ser un numero entero")
                return
            elif int(columnas) <= 0:
                messagebox.showerror(None,"La cantidad de columnas debe ser mayor a 0")
                return
            elif int(columnas) > 5:
                messagebox.showerror(None,"La cantidad de columnas debe ser maximo 5")
                return
            else:
                for i in range(0,len(matrizResultado)):
                    for j in range(0,len(matrizResultado[0])):
                        matrizEntradasA[i][j].config(bg=default)
                        matrizEntradasA[i][j].grid_forget()
                posx = 3
                posy = 0
                for i in range(0,int(filas)):
                    for j in range(0,int(columnas)):
                        matrizEntradasA[i][j].delete(0,END)
                        matrizEntradasA[i][j].config(width=8)
                        matrizEntradasA[i][j].grid(row=posx,column=posy,columnspan=1)
                        posy = posy + 1
                    posx = posx + 1
                    posy = 0
                matrizA = list(crearMatriz(int(filas),int(columnas)))
    else:
        filas = entryEntrada2.get()
        if type(eval(filas)) != int:
            messagebox.showerror(None,"La cantidad de filas debe ser un numero entero")
            return
        elif int(filas) <= 0:
            messagebox.showerror(None,"La cantidad de filas debe ser mayor a 0")
            return
        elif int(filas) > 5:
            messagebox.showerror(None,"La cantidad maxima de filas es 5")
            return
        else:
            columnas = entryEntrada22.get()
            if type(eval(columnas)) != int:
                messagebox.showerror(None,"La cantidad de columnas debe ser un numero entero")
                return
            elif int(columnas) <= 0:
                messagebox.showerror(None,"La cantidad de columnas debe ser mayor a 0")
                return
            elif int(columnas) > 5:
                messagebox.showerror(None,"La cantidad de columnas debe ser maximo 5")
                return
            else:
                for i in range(0,len(matrizResultado)):
                    for j in range(0,len(matrizResultado[0])):
                        matrizEntradasB[i][j].config(bg=default)
                        matrizEntradasB[i][j].grid_forget()
                posx = 3
                posy = 7
                for i in range(0,int(filas)):
                    for j in range(0,int(columnas)):
                        matrizEntradasB[i][j].delete(0,END)
                        matrizEntradasB[i][j].config(width=8)
                        matrizEntradasB[i][j].grid(row=posx,column=posy,columnspan=1)
                        posy = posy + 1
                    posx = posx + 1
                    posy = 7
                matrizB = list(crearMatriz(int(filas),int(columnas)))
                    
#Nombre:cargarDatos
#Entradas:ninguna
#Salidas:ninguna
#Descripcion: carga datos ingresados por el usuario
def cargarDatos():
    global matrizEntradasA,matrizEntradasB,matrizA,matrizB
    operacion = int(op.get())
    if operacion == 1 or operacion == 2 or operacion == 3:
        for i in range(0,len(matrizA)):
            for j in range(0,len(matrizA[0])):
                matrizA[i][j] = matrizEntradasA[i][j].get()
        for i in range(0,len(matrizB)):
            for j in range(0,len(matrizB[0])):
                matrizB[i][j] = matrizEntradasB[i][j].get()
    elif operacion == 4:
        for i in range(0,numfilas(matrizB)):
            for j in range(0,numcolumnas(matrizB)):
                matrizB[i][j] = matrizEntradasB[i][j].get()
    else:
        for i in range(0,numfilas(matrizA)):
            for j in range(0,numcolumnas(matrizA)):
                matrizA[i][j] = matrizEntradasA[i][j].get()
        



#Nombre:Sumar
#Entradas:ninguna
#Salidas:la matriz resultado
#Descripcion: carga datos, hace validaciones y luego muestra un error o matriz resultado
def Sumar():
    labelResultado.grid_forget()
    cargarDatos()
    global matrizA,matrizB,matrizC
    global matrizResultado
    matrizC = (sumaMatrices(matrizA,matrizB))
    if matrizC == None:
        return
    labelResultado.grid(row=9,column=0)
    posx = 10
    posy = 0
    for i in range(0,len(matrizC)):
        for j in range(0,len(matrizC[0])):
            matrizResultado[i][j] = Label(text=str(matrizC[i][j]))
            matrizResultado[i][j].grid(row=posx,column=posy)
            posy = posy + 1
        posy = 0
        posx = posx + 1
        
#Nombre:Restar
#Entradas:ninguna
#Salidas:la matriz resultado
#Descripcion:carga datos, hace validaciones y muestra error o matriz resultado
def Restar():
    labelResultado.grid_forget()
    cargarDatos()
    global matrizA,matrizB,matrizC
    global matrizResultado
    matrizC = restaMatrices(matrizA,matrizB)
    if matrizC == None:
            return
    labelResultado.grid(row=9,column=0)
    posx = 10
    posy = 0
    for i in range(0,numfilas(matrizC)):
        for j in range(0,numcolumnas(matrizC)):
            matrizResultado[i][j] = Label(text=str(matrizC[i][j]))
            matrizResultado[i][j].grid(row=posx,column=posy)
            posy = posy + 1
        posy = 0
        posx = posx + 1

#Nombre:Multiplicar
#Entradas:ninguna
#Salidas: la matriz producto
#Descripcion:carga datos, hace validaciones y muestra error o matriz resultado
def Multiplicar():
    global matrizA,matrizB,matrizC
    global matrizResultado
    labelResultado.grid_forget()
    cargarDatos()
    matrizC = multiplicamatrices(matrizA,matrizB)
    if matrizC == None:
            return
    labelResultado.grid(row=9,column=0)
    posx = 10
    posy = 0
    for i in range(0,numfilas(matrizC)):
        for j in range(0,numcolumnas(matrizC)):
            matrizResultado[i][j] = Label(text=str(matrizC[i][j]))
            matrizResultado[i][j].grid(row=posx,column=posy)
            posy = posy + 1
        posy = 0
        posx = posx + 1

#Nombre:Multiplicark
#Entradas:ninguna
#Salidas: la matriz producto
#Descripcion:carga datos, hace validaciones y muesta error o matriz resultado
def multiplicark():
    labelResultado.grid_forget()
    global matrizB,matrizC
    global procesos
    cargarDatos()
    numero = entryEntrada1.get()
    try:
        numero = int(numero)
        filas = numfilas(matrizB)
        columnas = numcolumnas(matrizB)
        for i in range(0,filas):
            for j in range(0,columnas):
                matrizB[i][j] = numero * int(matrizB[i][j])
                procesos.append(["x",numero,i,j])
        labelResultado.grid(row=9,column=0)
        posx = 10
        posy = 0
        for i in range(0,len(matrizB)):
            for j in range(0,len(matrizB[0])):
                matrizResultado[i][j] = Label(text=str(matrizB[i][j]))
                matrizResultado[i][j].grid(row=posx,column=posy)
                posy = posy + 1
            posy = 0
            posx = posx + 1
    except ValueError:
        messagebox.showerror(None,"Debe ingresar un numero")
        return

#nombre:gauss
#Entradas: ninguna
#Salidas: matriz resultado
#Descripcion: llama a funcion de calcular inversa con gauss jordan
#nombre:gauss
#Entradas: ninguna
#Salidas: matriz resultado
#Descripcion: llama a funcion de calcular inversa con gauss jordan
def gauss():
    global matrizA,mostrar
    cargarDatos()
    for i in range(0,len(matrizA)):
        for j in range(0,len(matrizA[0])):
            matrizA[i][j] = int(matrizA[i][j])
    if mostrar:
        invert(matrizA)
    else:
        res = invert(matrizA)
        print("Resultado:")
        print(res)

def invert(X):
    global mostrar
    #copy X to avoid altering input
    X = X[:]

    #Get dimensions of X
    rows = len(X)
    cols = len(X[0])

    #Get the identity matrix and append it to the right of X
    #This is done because our row operations will make the identity into the inverse
    identity = make_identity(rows,cols)
    for i in range(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in range(0,cols):
        if mostrar:
            print("En columna {0} y fila {1}".format(j,i))
            print("Matriz: ")
        mostrarMatrizProceso(X)
##        print("Identidad: ")
##        mostrarMatrizProceso(identity)
        #Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)
        #If everything is zero, increment the columns
        if zero_sum==0:
            if j==cols:
                return X
            messagebox.showinfo(None,"Matriz es singular.")
            return
        #If X[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            X = swap_row(X,i,first_non_zero)
            mostrarMatrizProceso(X)
        #Divide X[i] by X[i][j] to make X[i][j] equal 1
        X[i] = [m/X[i][j] for m in X[i]]
        mostrarMatrizProceso(X)

        #Rescale all other rows to make their values 0 below X[i][j]
        for q in range(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in range(0,len(scaled_row))]
                mostrarMatrizProceso(X)
        #If either of these is true, we have iterated through the matrix, and are done
        if i==rows or j==cols:
            break
        i+=1

    #Get just the right hand matrix, which is now our inverse
    for i in range(0,rows):
        X[i] = X[i][cols:len(X[i])]
    if mostrar:
        print("Inversa: ")
        mostrarMatrizProceso(X)

    return X

def check_for_all_zeros(X,i,j):
    non_zeros = []
    first_non_zero = -1
    for m in range(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero

def swap_row(X,i,p):
    if mostrar:
        print("f"+str(i)+"<->"+"f"+str(p))
    X[p], X[i] = X[i], X[p]
    return X

def make_identity(r,c):
    identity = []
    for i in range(0,r):
        row = []
        for j in range(0,c):
            elem = 0
            if i==j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return identity

#Nombre:determinar 
#Entradas:ninguna
#Salidas:determinante de una matriz
#Descripcion:usa formula de calcular determinante
def determinar():
    global matrizA
    cargarDatos()
    labelResultado.grid_forget()
    if len(matrizA) != len(matrizA[0]):
        messagebox.showerror(None,"La matriz debe ser cuadrada")
        return
    else:
        det = determinante(matrizA,1)
        print("El determinante es: " + str(det))
        

#nombre:inversacofactor
#Entradas: ninguna
#salidas: matriz inversa
#Descripcion: usa forma de calcular inversa con matriz de cofactores
def inversacofactor():
    global matrizA,matrizC
    labelResultado.grid_forget()
    if len(matrizA) != len(matrizA[0]):
        messagebox.showerror(None,"La matriz debe ser cuadrada")
        return
    cargarDatos()
    for i in range(0,numfilas(matrizA)):
        for j in range(0,numcolumnas(matrizA)):
            matrizA[i][j] = int(matrizA[i][j])
    matrizC = invertirCofactor(matrizA)
    if matrizC == None:
            return
    else:
        labelResultado.grid(row=9,column=0)
        posx = 10
        posy = 0
        for i in range(0,numfilas(matrizC)):
            for j in range(0,numcolumnas(matrizC)):
                matrizResultado[i][j] = Label(text=str(matrizC[i][j]))
                matrizResultado[i][j].grid(row=posx,column=posy)
                posy = posy + 1
            posy = 0
            posx = posx + 1
    
    
    


        
#Nombre:seleccionarOperacion
#Entradas:ninguna
#Salidas:despliega widgets en ventana para operacion seleccionada
#Descripcion: Usa seleccion de usuario para determinar que widgets mostrar
def seleccionarOperacion():
    global procesos,indice
    default = principal.cget('bg')
    indice = 0
    procesos = list()
    operacion = int(op.get())
    cOperacion.grid(row=9,column=5,columnspan=2)
    bOperacion.grid(row=8,column=5,columnspan=2)
    lOperacion.grid_forget()
    lOperacion2.grid_forget()
    for i in range(0,len(matrizResultado)):
        for j in range(0,len(matrizResultado[0])):
            matrizResultado[i][j].config(bg=default)
            matrizResultado[i][j].grid_forget()
        labelResultado.grid_forget()
        
        #desaparezco, en caso de haber, las matrices entrada
    for i in range(0,len(matrizEntradasA)):
        for j in range(0,len(matrizEntradasA[0])):
            matrizEntradasA[i][j].delete(0,END)
            matrizEntradasA[i][j].grid_forget()
            matrizEntradasB[i][j].delete(0,END)
            matrizEntradasB[i][j].grid_forget()
    if operacion == 1 or operacion == 2 or operacion ==3:            
        #aparezco widgets de entrada1
        labelEntrada1.config(text="Seleccione las filas y columnas de la matriz A")
        labelEntrada1.grid(row=0,column=0,columnspan=5)
        entryEntrada1.delete(0,END)
        entryEntrada1.insert(END,"filas")
        entryEntrada1.grid(row=1,column=0,columnspan=2)
        entryEntrada12.delete(0,END)
        entryEntrada12.insert(END,"columnas")
        entryEntrada12.grid(row=1,column=2,columnspan=3)
        bGenerar1.config(text="Crear matriz",command=lambda entrada="A":mostrarMatriz(entrada))
        bGenerar1.grid(row=2,column=0,columnspan=5)
        if operacion == 1:
            bOperacion.config(text="Sumar",command=Sumar)
        elif operacion == 2:
            bOperacion.config(text="Restar",command=Restar)
        else:
            bOperacion.config(text="Multiplicar",command=Multiplicar)

        #aparezco widgets de entrada2
        labelEntrada2.config(text="Seleccione las filas y columnas de la matriz B")
        labelEntrada2.grid(row=0,column=7,columnspan=5)
        entryEntrada2.delete(0,END)
        entryEntrada2.insert(END,"filas")
        entryEntrada2.grid(row=1,column=7,columnspan=2)
        entryEntrada22.delete(0,END)
        entryEntrada22.insert(END,"columnas")
        entryEntrada22.grid(row=1,column=8,columnspan=3)
        bGenerar2.config(command=lambda entrada="B":mostrarMatriz(entrada))
        bGenerar2.grid(row=2,column=8,columnspan=3)
        
    elif operacion == 4:
        #desaparezco widgets de entrada1
        labelEntrada1.config(text="Ingrese un numero")
        labelEntrada1.grid(row=0,column=0)
        entryEntrada1.delete(0,END)
        entryEntrada1.insert(END,"numero")
        entryEntrada1.grid(row=1,column=0,columnspan=2)
        bGenerar1.grid_forget()
        entryEntrada12.delete(0,END)
        entryEntrada12.grid_forget()
        labelEntrada2.config(text="")
        labelEntrada2.grid_forget()
        entryEntrada2.delete(0,END)
        entryEntrada2.grid_forget()
        entryEntrada2.delete(0,END)
        entryEntrada22.grid_forget()
        bGenerar2.grid_forget()
        bOperacion.config(text="Multiplicar",command=multiplicark)
        

        #aparezco widgets de entrada2
        labelEntrada2.config(text="Seleccione las filas y columnas de la matriz A")
        labelEntrada2.grid(row=0,column=7,columnspan=5)
        entryEntrada2.delete(0,END)
        entryEntrada2.insert(END,"filas")
        entryEntrada2.grid(row=1,column=7,columnspan=3)
        entryEntrada22.delete(0,END)
        entryEntrada22.insert(END,"columnas")
        entryEntrada22.grid(row=1,column=8,columnspan=2)
        bGenerar2.config(command=lambda entrada="B":mostrarMatriz(entrada))
        bGenerar2.grid(row=2,column=8,columnspan=3)
        
    elif operacion == 5 or operacion ==6 or operacion == 7:
        #aparezco widgets de entrada1
        labelEntrada1.config(text="Seleccione las filas y columnas de la matriz B")
        labelEntrada1.grid(row=0,column=0,columnspan=5)
        entryEntrada1.delete(0,END)
        entryEntrada1.insert(END,"filas")
        entryEntrada1.grid(row=1,column=0,columnspan=2)
        entryEntrada12.delete(0,END)
        entryEntrada12.insert(END,"columnas")
        entryEntrada12.grid(row=1,column=2,columnspan=3)
        bGenerar1.config(text="Crear matriz",command=lambda entrada="A":mostrarMatriz(entrada))
        bGenerar1.grid(row=2,column=0,columnspan=5)
        bOperacion.config(text="Calcular")
        if operacion == 5:
            bOperacion.config(command=gauss)
        elif operacion == 6:
            bOperacion.config(command=inversacofactor)
        else:
            bOperacion.config(command=determinar)


        #desaparezco widgets de entrada2
        labelEntrada2.grid_forget()
        entryEntrada2.delete(0,END)
        entryEntrada2.grid_forget()
        entryEntrada22.delete(0,END)
        entryEntrada22.grid_forget()
        bGenerar2.grid_forget()
        bGenerar2.grid_forget()
        
        
        

#Nombre:mostrarFlechas
#Entradas:ninguna
#Salidas:despliega flechas para hacer operacion paso a paso
#Descripcion: Usa seleccion de usuario para mostrar flechas      
def mostrarFlechas():
    opcion = pasoApaso.get()
    global procesos,indice,mostrar
    indice = 0
    lOperacion.grid_forget()
    lOperacion2.grid_forget()
    lOperacion.grid_forget()
    mostrar = False
    if opcion == 0:
        procesos = list()
        flecha1.grid_forget()
        flecha2.grid_forget()
    else:
        flecha1.grid(row=10,column=5)
        flecha2.grid(row=10,column=6)
        lOperacion.grid(row=11,column=5,columnspan=2)
        lOperacion2.grid(row=12,column=5,columnspan=2)
        mostrar = True

#Nombre:Siga
#Entradas:ninguna
#Salidas:muestra que elemenentos de las matrices estan involucrados en la operacion
#Descipcion:Hace siguiente operacion de lista de procesos
def siga():
    global procesos,matrizEntradasA,matrizEntradasB,matrizResultado
    global indice,matrizC
    if procesos == []:
        messagebox.showinfo(None,"Primero debe hacer la operacion")
        return
    elif indice == len(procesos):
        messagebox.showinfo(None,"Ya se han mostrado todos los pasos")
        indice = indice - 1
        return
    else:
        operacion = procesos[indice][0]
        default = principal.cget('bg')
        
    lOperacion.grid(row=9,column=5,columnspan=2)
    lOperacion2.config(text="")
    lOperacion2.grid_forget()
    flecha1.config(state=NORMAL)
    if operacion == "+" or operacion == "-":
        fila = procesos[indice][1]
        columna = procesos[indice][2]
        if indice != 0:
            anterior = procesos[indice-1]
            filaanterior = anterior[1]
            columnaanterior = anterior[2]
            matrizEntradasA[filaanterior][columnaanterior].config(bg=default)
            matrizEntradasB[filaanterior][columnaanterior].config(bg=default)
            matrizResultado[filaanterior][columnaanterior].config(bg=default)
            matrizResultado
            matrizEntradasA[fila][columna].config(bg="Yellow")
            matrizEntradasB[fila][columna].config(bg="Red")
            matrizResultado[fila][columna].config(bg="Orange")
            elementoA = matrizEntradasA[fila][columna].get()
            elementoB = matrizEntradasB[fila][columna].get()
            elementoC = str(matrizC[fila][columna])
            texto = elementoA + operacion + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
        else:
            matrizEntradasA[fila][columna].config(bg="Yellow")
            matrizEntradasB[fila][columna].config(bg="Red")
            matrizResultado[fila][columna].config(bg="Orange")
            elementoA = matrizEntradasA[fila][columna].get()
            elementoB = matrizEntradasB[fila][columna].get()
            elementoC = str(matrizC[fila][columna])
            texto = elementoA + operacion + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
    elif operacion =="*":
        if indice == 0:
            actual = procesos[indice]
            fila = actual[1]
            columna = actual[2]
            texto = ""
            listaString = list()
            columnas = int(columnas1.get())
            for j in range(0,columnas):
                matrizEntradasA[fila][j].config(bg="Yellow")
                elemento = matrizEntradasA[fila][j].get()
                listaString.append("("+elemento+"*")
            filas = int(filas2.get())
            listaString2 = list()
            for i in range(0,filas):
                matrizEntradasB[i][columna].config(bg="Red")
                elemento = matrizEntradasB[i][columna].get()
                listaString2.append(elemento+")")
            matrizResultado[fila][columna].config(bg="Orange")
            elementoC = str(matrizC[fila][columna])               
            for pos in range(0,len(listaString)):
                texto = texto + listaString[pos] + listaString2[pos] + "+"
            texto = texto[:-1]
            texto = texto + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
        else:
            actual = procesos[indice]
            fila = actual[1]
            columna = actual[2]
            texto = ""
            anterior = procesos[indice-1]
            filaanterior = anterior[1]
            columnaanterior = anterior[2]
            listaString = list()
            columnas = int(columnas1.get())
            for j in range(0,columnas):
                matrizEntradasA[filaanterior][j].config(bg=default)
                matrizEntradasA[fila][j].config(bg="Yellow")
                elemento = matrizEntradasA[fila][j].get()
                listaString.append("("+elemento+"*")
                
            filas = int(filas2.get())
            listaString2 = list()
            for i in range(0,filas):
                matrizEntradasB[i][columnaanterior].config(bg=default)
                matrizEntradasB[i][columna].config(bg="Red")
                elemento = matrizEntradasB[i][columna].get()
                listaString2.append(elemento+")")

            matrizResultado[filaanterior][columnaanterior].config(bg=default)
            matrizResultado[fila][columna].config(bg="Orange")
            elementoC = str(matrizC[fila][columna])
            
            for pos in range(0,len(listaString)):
                texto = texto + listaString[pos] + listaString2[pos] + "+"
            texto = texto[:-1]
            texto = texto + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
    elif operacion == "x":
        if indice == 0:
            actual = procesos[indice]
            numero = str(actual[1])
            fila = actual[2]
            columna = actual[3]
            matrizEntradasB[fila][columna].config(bg="Red")
            matrizResultado[fila][columna].config(bg="Orange")
            elementoB = matrizEntradasB[fila][columna].get()
            elementoC = str(matrizB[fila][columna])
            texto = numero + "x" + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
        else:
            actual = procesos[indice]
            numero = str(actual[1])
            fila = actual[2]
            columna = actual[3]
            anterior = procesos[indice-1]
            filaanterior = anterior[2]
            columnaanterior = anterior[3]
            matrizEntradasB[filaanterior][columnaanterior].config(bg=default)
            matrizResultado[filaanterior][columnaanterior].config(bg=default)
            matrizResultado[fila][columna].config(bg="Orange")
            matrizEntradasB[fila][columna].config(bg="Red")
            elementoB = matrizEntradasB[fila][columna].get()
            elementoC = str(matrizB[fila][columna])
            texto = numero + "x" + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice + 1
            return
    else:
        messagebox.showinfo(None,"Esta operacion no se puede ver en esta ventana, por favor veala en la consola")
        return
                               
 #Nombre:atras
#Entradas:ninguna
#Salidas:muestra que elemenentos de las matrices estan involucrados en la operacion previa
#Descipcion:Hace anterior operacion de lista de procesos       
def atras():
    global procesos,matrizEntradasA,matrizEntradasB,matrizResultado
    global indice
    lOperacion2.config(text="")
    lOperacion2.grid_forget()
    original = principal.cget('bg')
    if indice == 0 or indice == 1:
        flecha1.config(state=DISABLED)
        matrizEntradasA[0][0].config(bg=original)
        matrizEntradasB[0][0].config(bg=original)
        matrizResultado[0][0].config(bg=original)
        indice = indice - 1
        return
    elif procesos == []:
        messagebox.showinfo(None,"No se ha hecho ninguna operacion")
        return
    else:
        operacion = procesos[indice-1][0]

        if operacion == "-" or operacion == "+":
            anterior = procesos[indice-1]
            filaanterior = procesos[indice-2][1]
            columnaanterior = procesos[indice-2][2]
            fila = procesos[indice-1][1]
            columna = procesos[indice-1][2]
            
            matrizEntradasA[fila][columna].config(bg=original)
            matrizEntradasB[fila][columna].config(bg=original)
            matrizResultado[fila][columna].config(bg=original)
            matrizEntradasA[filaanterior][columnaanterior].config(bg="Yellow")
            matrizEntradasB[filaanterior][columnaanterior].config(bg="Red")
            matrizResultado[filaanterior][columnaanterior].config(bg="Orange")
            elementoA = matrizEntradasA[filaanterior][columnaanterior].get()
            elementoB = matrizEntradasB[filaanterior][columnaanterior].get()
            elementoC = str(matrizC[filaanterior][columnaanterior])
            texto = elementoA + operacion + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice - 1
            return

        elif operacion == "*":
            texto = ""
            if indice == 1:
                for i in range(0,numfilas(matrizA)):
                    matrizEntradasB[i][0].config(bg="Red")
                    matrizEntradasB[0][0].config(bg="Red")
                for j in range(0,numcolumnas(matrizB)):
                    matrizEntradasA[0][j].config(bg="Yellow")
                    matrizEntradasA[0][0].config(bg="Yellow")
                indice = indice - 1
                return

            anterior = procesos[indice-1]
            filaanterior = procesos[indice-2][1]
            columnaanterior = procesos[indice-2][2]
            fila = procesos[indice-1][1]
            columna = procesos[indice-1][2]

            listaString = list()
            listaString2 = list()

            columnas = int(columnas1.get())
            for j in range(0,columnas):
                matrizEntradasA[fila][j].config(bg=original)
                matrizEntradasA[filaanterior][j].config(bg="Yellow")
                elemento = matrizEntradasA[filaanterior][j].get()
                listaString.append("("+elemento+"*")
                
            filas = int(filas2.get())
            listaString2 = list()
            for i in range(0,filas):
                matrizEntradasB[i][columna].config(bg=original)
                matrizEntradasB[i][columnaanterior].config(bg="Red")
                elemento = matrizEntradasB[i][columnaanterior].get()
                listaString2.append(elemento+")")

            matrizResultado[filaanterior][columnaanterior].config(bg="Orange")
            matrizResultado[fila][columna].config(bg=original)
            elementoC = str(matrizC[filaanterior][columnaanterior])

            for pos in range(0,len(listaString)):
                texto = texto + listaString[pos] + listaString2[pos] + "+"
            texto = texto[:-1]
            texto = texto + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice - 1
        elif operacion == "x": 
            actual = procesos[indice-1]
            numero = str(actual[1])
            fila = actual[2]
            columna = actual[3]
            anterior = procesos[indice-2]
            filaanterior = anterior[2]
            columnaanterior = anterior[3]
            matrizEntradasB[fila][columna].config(bg=original)
            matrizResultado[fila][columna].config(bg=original)
            matrizResultado[filaanterior][columnaanterior].config(bg="Orange")
            matrizEntradasB[filaanterior][columnaanterior].config(bg="Red")
            elementoB = matrizEntradasB[filaanterior][columnaanterior].get()
            elementoC = str(matrizB[filaanterior][columnaanterior])
            texto = numero + "x" + elementoB + "=" + elementoC
            lOperacion2.config(text=texto)
            lOperacion2.grid(row=11,column=5,columnspan=2)
            indice = indice - 1
            return
        else:
            messagebox.showinfo(None,"Esta operacion no puede ser vista en esta ventana, por favor vea la consola")
            return
            
            
                        

            

            
            
                
            
            
            

            
            
            
        
    
        

                                    

##Variables declaradas
matrizA = list() #donde voy a guardar valores de primera matriz
matrizB = list() #donde voy a guardar valores de segunda matriz
matrizC = list() #Matriz de resultado de operacion
matrizEntradasA = list(crearMatriz(5,5)) #matriz interfaz
matrizEntradasB = list(crearMatriz(5,5)) #matriz interfaz
matrizResultado = list(crearMatriz(5,5)) #matriz interfaz
indice = 0 #indice en operaciones efectuadas
procesos = list() #donde guarda historial de operaciones
mostrar = False


##Interfaz grafica
principal = tkinter.Tk()

##variables para trabajar con interfaces
op = IntVar()
pasoApaso = IntVar()
numero = StringVar()
filas1 = StringVar()
filas2 = StringVar()
columnas1 = StringVar()
columnas2 = StringVar()

##Objetos para diseno
#Entrada 1
principal.title("Calculadora matrices")#titulo de ventana
l1 = Label(principal,text="Entrada 1",font=("Times New Roman",14))
bGenerar1 = Button(principal,text="Crear matriz")
labelEntrada1 = Label()
entryEntrada1 = Entry(principal,textvariable=filas1)
entryEntrada12 = Entry(principal,textvariable=columnas1)

#Lista de operaciones
l2 = Label(principal,text="Seleccione una operacion:")
l2.grid(row=0,column=5)
r1 = Radiobutton(principal,value=1,text="Sumar",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r1.grid(row=1,column=5,columnspan=2)
r2 = Radiobutton(principal,value=2,text="Restar",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r2.grid(row=2,column=5,columnspan=2)
r3 = Radiobutton(principal,value=3,text="Multiplicar matrices",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r3.grid(row=3,column=5,columnspan=2)
r4 = Radiobutton(principal,value=4,text="Multiplicar matriz por numero",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r4.grid(row=4,column=5,columnspan=2)
r5 = Radiobutton(principal,value=5,text="Inversa (Gauss Jordan)",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r5.grid(row=5,column=5,columnspan=2)
r6 = Radiobutton(principal,value=6,text="Inversa (matriz de cofactores)",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r6.grid(row=6,column=5,columnspan=2)
r7 = Radiobutton(principal,value=7,text="Determinante",font=("Times New Roman",14),variable=op,command=seleccionarOperacion,compound=CENTER)
r7.grid(row=7,column=5,columnspan=2)

bOperacion = Button(principal)

cOperacion = Checkbutton(principal,text="Paso a paso",variable=pasoApaso,command=mostrarFlechas)
flecha1 = Button(principal,text="<-",state=DISABLED,command=atras)
flecha2 = Button(principal,text="->",command=siga)
lOperacion = Label(principal,text="Operacion efectuada")
lOperacion2 = Label(principal)
    

#Entrada 2
l3 = Label(principal,text="Seleccione tipo de entrada 2",font=("Times New Roman",14))
bGenerar2 = Button(principal,text="Crear matriz")
labelEntrada2 = Label(principal)
entryEntrada2 = Entry(principal,textvariable=filas2)
entryEntrada22 = Entry(principal,textvariable=columnas2)

labelResultado  = Label(text="Resultado de operacion")

#matriz grafica
for fila in range(0,5):
    for columna in range(0,5):
        matrizEntradasA[fila][columna] = Entry(principal)       
        matrizResultado[fila][columna] = Label(principal)       
        matrizEntradasB[fila][columna] = Entry(principal)



