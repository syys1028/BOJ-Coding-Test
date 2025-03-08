T = int(input())  
N_list = [int(input()) for _ in range(T)]  

P = [0] * 101
P[1], P[2], P[3] = 1, 1, 1  

for i in range(4, 101):  
    P[i] = P[i-2] + P[i-3]  

for N in N_list:  
    print(P[N])