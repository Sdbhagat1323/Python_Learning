# built your own generator
##
##
##def simple_gen():
##         yield "oh"
##         yield "Hello"
##         yield "there"
##
##for i in simple_gen():
##         print(i)
##
##print('-------------------------------')



CORRECT_COMBO = (3, 8, 2)

##for c1 in range(10):
##         for c2 in range(10):
##                  for c3 in range(10):
##                           if (c1, c2, c3) == CORRECT_COMBO:
##                                    print("Found the corrent combo: {}".format((c1, c2, c3)) )
##                                    break
##                           print(c1, c2, c3)
##
##

## this is lot of code
##got_it = False
##for c1 in range(10):
##         if  got_it:
##                  break
##         for c2 in range(10):
##                  if got_it:
##                           break
##                  for c3 in range(10):
##                           if (c1, c2, c3) == CORRECT_COMBO:
##                                    print("Found the corrent combo: {}".format((c1, c2, c3)))
##                                    got_it = True
##                                    break
##                           print(c1, c2, c3)



# Now we build Generator

CORRECT_COMBO = (3, 8, 2)


def combo_gen():
         for c1 in range(10):
                  for c2 in range(10):
                           for c3 in range(10):
                                    yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
         print(c1, c2, c3)
         if (c1, c2, c3) == CORRECT_COMBO:
                  print("Found the corrent combo: {}".format((c1, c2, c3)))
                  break
         print(c1, c2, c3)






























                           

                           
