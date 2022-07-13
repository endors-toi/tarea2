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
        string = "C1:NomC1-C2:NomC2-C3:NomC3"
        #string = input("ERROR: No pueden haber identificadores repetidos. Reingrese los datos:\n")
        
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
    return string, aux

# Ingreso de string 1 (nombres de coaliciones)
string1 = "C1:NomC1-C2:NomC2-C2:NomC3"
string1, coaliciones = validarRepetidos(string1, ":", "-")

# Ingreso de string 2 (nombres de partidos)
string2 = "P1=NomP1,P2=NomP2,P3=NomP3,P4=NomP4"
string2, partidos = validarRepetidos(string2, "=", ",")

# Ingreso de string 3 (conformación de coaliciones)
string3 = "C1:P1,P1;C2:P2,P3;C3:P4"

var = ""
I = -1 ; K = 0
dupC = "" ; dupP = ""
while K != -1:
    K = string3.find(":", I+1)

    coa = string3[I+1:K]
    if coa not in dupC:
        dupC += coa
    else:
        print("error: duplicado")
    
    #print(coa)
    
    I = string3.find(";", K+1)
    if I != -1:
        par = string3[K+1:I]
        #print(par)
    else:
        par = string3[K+1:]
        #print(par)
    
    
    # SEPARAR par Y COMPROBAR EXISTENCIA Y DUPLICADOS
    
    if coa not in coaliciones:
        print("error: no existe")
    
    if I == -1:
        break


# Ingreso de string 4 (votos)
string4 = "P1$P1$P2$P2$P3$P3$P2$P2$P3$P1$P3$P3$P4"

I = -1 ; K = 0 ; error = 0 ; erroneo = ""
while K != -1:
    K = string4.find("$", I+1)
    if K != -1:
        var = string4[I+1:K]
    else:
        var = string4[I+1:]        

    if var not in partidos:
        error = 1
        erroneo = var
        break
    
    if K != -1:
        I = string4.find("$", K+1)
        if I != -1:
            var = string4[K+1:I]
        else:
            var = string4[K+1:]

        if var not in partidos:
            error = 1
            erroneo = var
            break
    
    if I == -1 or K == -1:
        break

while error == 1:
    string4 = input(f"ERROR: El código de partido {erroneo} no existe. Reingrese votos:\n")
    I = -1 ; K = 0 ; error = 0
    while K != -1:
        K = string4.find("$", I+1)
        if K != -1:
            var = string4[I+1:K]
        else:
            var = string4[I+1:]        
    
        if var not in partidos:
            error = 1
            erroneo = var
            break
        
        if K != -1:
            I = string4.find("$", K+1)
            if I != -1:
                var = string4[K+1:I]
            else:
                var = string4[K+1:]
    
            if var not in partidos:
                error = 1
                erroneo = var
                break

        if I == -1 or K == -1:
            break

# Cálculo de votos por partido

count = "" ; var = ""
for x in partidos:
    if x == "/":
        count += str(string4.count(var)) + "/"
        var = ""
    else:
        var += x
            
# Cálculo de votos por coalición

# Crear menú funcional para acceder a cada paso

