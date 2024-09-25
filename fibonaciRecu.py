# Problème fibonaçi
            # x=    0,1,2,3,4,5,6 ,7 ,8 ,9,10,11 ,12 ,13 ,14
# la suite fib(x) : 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,…
 
 #la récurrence
      # fib(0)  return 0
      # fib(1) return 1
      # fib(x) return fib(x-1) + fib(x-2)

# programme récursif
import time
def fibRecursif(x):
    if(x == 0):
        return 0
    elif(x == 1):
        return 1
    else:
        return fibRecursif(x-1) + fibRecursif(x-2)
    
n =38
start_time = time.time()
print("\n fibonaci de  " + str(n) +" = " +str( fibRecursif(n)))
end_time = time.time()
time_exec = end_time - start_time

print("\n Le temps d'exécution (Pg Rec) :" + str(time_exec) + "\n")
