#modules
import math, random, os, time, threading, pygame

#files
from settings import *
from  render  import *
from  Vector  import *

#App
class App:
    def __init__(self):
        #inicialization
        pygame.init()
        self.screen = pygame.display.set_mode(size, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.execute = True
        self.t = 0
        self.font = pygame.font.Font('consola.ttf', text_size)

    def run(self):
        #Set image
        logo = pygame.image.load("logo.png")
        pygame.display.set_icon(logo)
        #Loop
        while self.execute:
            self.t += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.execute = False

            #Input
            keys = pygame.key.get_pressed()  
            if keys[pygame.K_ESCAPE]:
                self.execute = False
            if keys[pygame.K_w]:
                camera_pos.x += speed
            if keys[pygame.K_s]:
                camera_pos.x -= speed

            #Drawing
            self.screen.fill('black')
            #Threads
            #tr = [0]*fragments
            #for i in range(fragments):
            #    tr[i] = threading.Thread(target = render, args = (self.screen, self.font, self.t, i, camera_pos,))
            #for i in range(fragments):
            #    tr[i].start()
            #for i in range(fragments):
            #    tr[i].join()
            #tr = ()
            render(self.screen, self.font, self.t, 1, camera_pos)
            pygame.display.flip()
            self.clock.tick()
            pygame.display.set_caption(f' CMD-GAME   FPS: {self.clock.get_fps() :.2f}')
            pygame.display.update()

#Run
if __name__ == '__main__':
    app = App()
    app.run()
pygame.quit()