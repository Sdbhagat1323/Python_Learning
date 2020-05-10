input_list = [5,6,2,10,15,20,2,1,6,9,3]


def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False
# generator but this case its not building a list 
#xyz = (i for i in input_list if dev_by_five(i))


# this is building  a list
#xyz = [] 
##	if div_by_five(i):
#		xyz.append(i)

#for i in xyz:
#	print(i)

#or 

#[print(i) for i in xyz]

#xyz = [i for i in input_list if div_by_five(i)]
#print(xyz)



#[[print(i, ii) for ii in range(5)] for i in range(5)]


#for i in range(5):
   #     for ii in range(5):
#                print(i,ii)

xyz  = ([[i, ii] for ii in range(5)] for i  in range(5))

print(xyz )

#for i in xyz:
   #     print(i)

print([i for i in xyz])






















