from math import *

def AdicionVectores(v1,v2):
    sumareales = n1[0] + n2[0]
    sumaimaginarios = n1[1] + n2[1]
    return sumareales, sumaimaginarios

def InversoVector(v1):
    productoreal= (n1[0]*n2[0]) + (-1*(n1[1]*n2[1]))
    productoimaginario= (n1[0]*n2[1]) + (n1[1]*n2[0])
    return productoreal, productoimaginario

def MultiplicacionVector(c,v1):
    restareales = n1[0] - n2[0]
    restaimaginarios = n1[1] - n2[1]
    return restareales, restaimaginarios

def AdicionMatrices(m1,m2):
    sumareales = n1[0] + n2[0]
    sumaimaginarios = n1[1] + n2[1]
    return sumareales, sumaimaginarios

def InversaMatriz(m1):
    productoreal= (n1[0]*n2[0]) + (-1*(n1[1]*n2[1]))
    productoimaginario= (n1[0]*n2[1]) + (n1[1]*n2[0])
    return productoreal, productoimaginario

def MultiplicacionMatriz(c,m1):
    restareales = n1[0] - n2[0]
    restaimaginarios = n1[1] - n2[1]
    return restareales, restaimaginarios

def TranspuestaMatrizVector(n1):
    conjugado = -1 * n2[1]
    dividiendoreal = (n1[0]*n2[0]) + (-1*(n1[1]*conjugado))
    dividiendoimaginario = (n1[0]*conjugado) + (n1[1]*n2[0])
    divisortotal = (n2[0]**2) - (-1*(n2[1]**2))
    return dividiendoreal, dividiendoimaginario, divisortotal

def ConjugadaMatrizVector(n1):
    numraiz = (n1[0]**2)+(n1[1]**2)
    modulo = sqrt(numraiz)
    isInt= int(modulo) == modulo
    if isInt == True:
        return (int(modulo))
    else:
        return numraiz

def AdjuntaMatrizVector(n1):
    conjugado = -1*n1[1]
    return n1[0], conjugado

def ProductoMatrices(m1,m2):
    fase = degrees(atan(n1[1]/n1[0]))
    if n1[0] >= 0 and n1[1] >= 0:
        return fase
    elif n1[0] < 0 and n1[1] < 0:
        fase = fase + 180
        return fase
    elif n1[0] < 0 and n1[1] >= 0:
        fase = 180 - (-1*fase)
        return fase
    else:
        fase = 360 - (-1*fase)
        return fase

def AccionMatrizVector(m1,v1):
    modulo = ModuloComplejos(n1)
    fase = FaseComplejos(n1)
    return modulo, fase

def ProductoInternoVectores(v1,v2):
    a = n1[0] * cos(radians(n1[1]))
    b = n1[0]* sin(radians(n1[1]))
    return a, b

def NormaVector(v1):
    conjugado = -1 * n2[1]
    dividiendoreal = (n1[0]*n2[0]) + (-1*(n1[1]*conjugado))
    dividiendoimaginario = (n1[0]*conjugado) + (n1[1]*n2[0])
    divisortotal = (n2[0]**2) - (-1*(n2[1]**2))
    return dividiendoreal, dividiendoimaginario, divisortotal

def DistanciaVectores(v1,v2):
    numraiz = (n1[0]**2)+(n1[1]**2)
    modulo = sqrt(numraiz)
    isInt= int(modulo) == modulo
    if isInt == True:
        return (int(modulo))
    else:
        return numraiz

def MatrizUnitaria(m1):
    conjugado = -1*n1[1]
    return n1[0], conjugado

def MatrizHermitiana(m1):
    fase = degrees(atan(n1[1]/n1[0]))
    if n1[0] >= 0 and n1[1] >= 0:
        return fase
    elif n1[0] < 0 and n1[1] < 0:
        fase = fase + 180
        return fase
    elif n1[0] < 0 and n1[1] >= 0:
        fase = 180 - (-1*fase)
        return fase
    else:
        fase = 360 - (-1*fase)
        return fase

def ProductoTensorVectores(v1,v2):
    modulo = ModuloComplejos(n1)
    fase = FaseComplejos(n1)
    return modulo, fase

def ProductoTensorMatrices(m1,m2):
    a = n1[0] * cos(radians(n1[1]))
    b = n1[0]* sin(radians(n1[1]))
    return a, b