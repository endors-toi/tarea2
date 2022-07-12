"""
REGLAS:
  - No usar split()
  - No usar listas
  - Se asume que los códigos de identificación van en MAYÚSCULAS
  - Respetar formato para cada string (están en el PDF)
  - Se pueden definir funciones para tareas repetitivas (como validaciones)
  - Las entradas de strings en el código final son inputs, pero para ir probando usamos un string fijo que respete el formato. CAMBIAR A INPUT CUANDO FUNCIONE.
"""

def validarRepetidos(string, sep1, sep2):
    sw = 1
    aux = ""
    var = ""
    error = 0
    for x in string:
        if x == sep1:
            sw = 0
            if var not in aux:
                aux += var + "/"
                var = ""
            else:
                error = 1
                break
        elif x == sep2:
            sw = 1
        elif sw == 1:
            var += x
    while error == 1:
        string = input("ERROR: No pueden haber identificadores repetidos. Reingrese los datos:\n")
        
        sw = 1
        aux = ""
        var = ""
        error = 0
        for x in string:
            if x == sep1:
                sw = 0
                if var not in aux:
                    aux += var + "/"
                    var = ""
                else:
                    error = 1
                    break
            elif x == sep2:
                sw = 1
            elif sw == 1:
                var += x
    return aux

# Ingreso de string 1 (nombres de coaliciones)
string1 = "C1:NomC1-C2:NomC2-C3:NomC3"
coaliciones = validarRepetidos(string1, ":", "-")

# Ingreso de string 2 (nombres de partidos)
string2 = "P1=NomP1,P2=NomP2,P3=NomP3,P4=NomP4"
partidos = validarRepetidos(string2, "=", ",")

# Ingreso de string 3 (conformación de coaliciones)
string3 = "C1:P1,P1;C2:P2,P3;C3:P4"

"""
J = string3.find(":")

L = -1
c += string3[L+1:J]

K = string3.find(",")
p += string3[J+1:K]

L = string3.find(";")
"""


# Ingreso de string 4 (votos)
string4 = "P1$P1$P2$P2$P5$P3$P2$P2$P3$P1"

var = ""
L = -1
K = 0
while K != -1:
    K = string4.find("$", L+1)
    var = string4[L+1:K]
    if var not in partidos:
        error = 1
    var = ""
    L = K
    



count = "" ; var = ""
for x in partidos:
    if x == "/":
        count += string4.count(var) + "/"
        var = ""
    else:
        var += x

# Cálculo de votos por partido

# Cálculo de votos por coalición

# Crear menú funcional para acceder a cada paso