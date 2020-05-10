# inheratance
#object oriented programming

import  pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blog World")
clock=pygame.time.Clock()

#we want to use operator on objects.
# blue_blob + red_blob

class BlueBlob(Blob):

         def  __init__(self, x_boundary, y_boundary):
                  Blob.__init__(self, BLUE, x_boundary, y_boundary)

         def __add__(self, other_blob):
                  if other_blob.color == RED:
                           self.size -= other_blob.size
                           other_blob.size -= self.size
                  elif other_blob.color == GREEN:
                           self.size += other_blob.size
                           other_blob.size += self.size
                  elif other_blob.color == BLUE:
                           pass
                  else:
                           raise Exception("Tried to combine one or multiple Blobs  of unsupported colors.")
                  

class RedBlob(Blob):

         def  __init__(self, x_boundary, y_boundary):
                  Blob.__init__(self, RED, x_boundary, y_boundary)                  
                  
class GreenBlob(Blob):

         def  __init__(self, x_boundary, y_boundary):
                  Blob.__init__(self, GREEN, x_boundary, y_boundary)



##         def move_fast(self):
##                  self.x += random.randrange(-7, 7)
##                  self.y +=  random.randrange(-7, 7)

def draw_environment(blob_list):
         game_display.fill(WHITE)
         
         for blob_dict in blob_list:
                  for blob_id in blob_dict :
                           blob = blob_dict[blob_id]
                           pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
                           blob.move()
                           blob.check_boundary()
                           

          
         pygame.display.update()
        
         
def main():
         blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
         red_blobs = dict(enumerate([RedBlob( WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
         green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

         #Manuallycheck the size operation one blob to check interactions.
         print("Blue blob size:{} Red blob size:{}".format(blue_blobs[0].size, red_blobs[0].size))
         blue_blobs[0] + red_blobs[0]
         print("Blue blob size:{} Red blob size:{}".format(blue_blobs[0].size, red_blobs[0].size))
         

         while True:
                  for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                  draw_environment([blue_blobs, red_blobs, green_blobs ])
                  clock.tick(60)

if __name__ == '__main__':
         main()


                  













