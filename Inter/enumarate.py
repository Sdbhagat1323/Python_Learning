example = ["left", "righ ", "up","down"]


for i in range(len(example)):
         print(i , example[i])


print('-------------------------------')

# Enumerate>:
for i, j in enumerate(example):
         print(i, j)
print('-------------------------------')

new_dic = dict(enumerate(example))
print(new_dic)

print('-------------------------------')


[print(i,  j) for i, j in enumerate(new_dic)]
