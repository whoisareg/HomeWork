#Bubble sort algorithm

list = [7, 9, 15, 8, 6]
for j in range(len(list)):  
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
print(list)
