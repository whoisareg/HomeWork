def solution(a):
    arr = []
    suM1 = 0
    suM2 = 0
    x = a[::2]
    y = a[1::2]
    
    for i in x:
        suM1 += i
    arr.append(suM1)  
    
    for j in y:
        suM2 += j
    arr.append(suM2)      
        
    print(arr)    
solution([50, 60, 60, 45, 70])    
   
        