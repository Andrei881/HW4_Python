# Задача 1
# from random import randint

# with open('output.txt','w') as fw:
#     for i in range (10): fw.write(str(randint(1,1000))+',')

# with open('output.txt','r') as fr:
#     a=fr.readline().split(',')
#     a.pop()
# print (sorted(map(int, a)))

# Задача 2
def unique(a):
    return list(set(a))

print(unique([1, 5, 2, 3, 4, 6, 1, 7]))

