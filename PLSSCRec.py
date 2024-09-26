# Plus longue sous suite croissante  PLSSC

# Entrée: T tableau de n entiers
# Sortie 1:  Une PLSSC de T
# Sortie 2:  la longueur d'une PLSSC de T

# Example :

#       T = [6 , 1 , 9 , 5 , 13 , 3 , 11 , 7 , 15 , 2 , 10 , 6 , 14 , 4 , 12 , 8 , 16 , 3 , 10]
# Sortie 1: [    1                3        7            10                12       16         ]
# Ou      : [    1       5                 7            10       14                16         ]
# OU .....
 
# Sortie 2: 6 la taille de la plus longue sous suite croissante

# Allgorithme récursif

def PLSSCRec(T , n):
    if( n == 0 ):
        return 1 
    max = 0
    
    for i in range(0, n-2):
        
        if T[i] <= T[n-1]:
            
            x = PLSSCRec(T,i)
            
            if(x > max):
                max = x
    return 1 + max

T = [6 , 1 , 9 , 5 , 13 , 3 , 11 , 7 , 15 , 2 , 10 , 6 , 14 , 4 , 12 , 8 , 16 , 3 , 10]
n = len(T)
print("\n La longueur de la plus longue sous suite  de T est :  " +str(PLSSCRec(T,n))+"\n")
