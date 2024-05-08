def solution(n):
    
    ticketNum = str(n)
    a = 0
    for i in ticketNum[:len(ticketNum)//2:]:
        a += int(i)
    b = 0
    for j in ticketNum[len(ticketNum)//2::]:
         b += int(j)
    if a == b:
        return True
    return False

        
   