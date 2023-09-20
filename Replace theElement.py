num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

n = 50

lis = []

for i in num_list:
    update = i[:-1] + (n,)
    lis.append(update)
    
print(lis)    