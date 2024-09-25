# programmation dynamique 

# Consiste a sauvgarder les résultat deja calculer et les utilisé pour calculer la valeur suivante 

import time
def fibDynamique(x):
    tab = [0]*(x+1)
    tab[0] = 0
    tab[1] = 1
    for i in range(2 , x+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[x]


n =38
start_time = time.time()
print("\n fibonaci de " + str(n) +" = " +str( fibDynamique(n)))
end_time = time.time()
time_exec = end_time - start_time

print("\n Le temps d'exécution (Pg Dy) :" + str(time_exec) + "\n")