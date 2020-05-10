

def add_wrapping(item):
         def wrapped_item():
                  return "A Wrapped up box of  {}" .format(str(item()))
         return wrapped_item

                  
         


@ add_wrapping
def new_gpu():
         return "A new tesla GPU"

print(new_gpu())
