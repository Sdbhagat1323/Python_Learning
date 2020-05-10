x =  [1 , 2,  3, 4]
y = [7, 8, 9, 1]
z = ["a", "b", "c", "d"]

##for a, b in zip(x,y):
##         print(a, b )

print(zip (x,y,z))


for i in zip(x,y,z):
         print(i)

print('-------------------------------')

##convert zip_ to list_

print(list(zip(x, y, z)))

##convert zip_ to dict_

print(dict(zip(x, y)))


print('-------------------------------')


