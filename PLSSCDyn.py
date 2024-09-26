

def PLSSCDyn(T):
    n = len(T)
    L = [1]*(n)
    for i in range(1, n):
        for j in range(0, i):
            if T[j] < T[i]:
                L[i] = max(L[i], L[j] + 1)
    
    return max(L),L


T = [6 , 1 , 9 , 5 , 13 , 3 , 11 , 7 , 15 , 2 , 10 , 6 , 14 , 4 , 12 , 8 , 16 , 3 , 10]
print("Longueur de la plus logne sous liste croissante est : "+str(PLSSCDyn(T))+"\n")