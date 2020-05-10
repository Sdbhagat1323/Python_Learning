

if (keys[k_RIGHT]):
    print("Right arrow pressed.")

# build window for game
from pygame.locals import *
import pygame
# build player size and its motion and speed
pygame.event.pump()
keys = pygame.key.get_pressed()


class player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x + self.speed

    def moveUp(self):
        self.y = self.y + self.speed

class App:
    windowWidth = 800
    windowheight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowheight), pygame.HWSURFACE)

        pygame.display.set_caption("Snake_Game")
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_excute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[k_RIGHT]):
                self.player.moveRight()

            if (Keys[k_LEFT]):
                self.player.moveLeft()

            if (keys[k_UP]):
                self.player.moveUp()

            if (keys[k_DOWN]):
                self.player.moveDown()

            if (key[k_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_excute()
