def solution(a):
    
    tree_index = []
    people = []
    
    for i in range(len(a)):
        if a[i] == -1:
            tree_index.append(i)
        else:
            people.append(a[i])
            
    people.sort()
    for i in tree_index:
        people.insert(i,-1)
    return people 

