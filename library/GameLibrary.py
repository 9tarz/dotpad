import pygame
from pygame.locals import *

  
class SimpleGame(object):
  
  def __init__(self, title, background_color, window_size = (640,480), fps = 60):
   
    self.title = title
    self.window_size = window_size
    self.fps = fps
    self.is_terminated = False
    self.background_color = background_color

  def terminate(self):
    self.is_terminated = True
  
  def __game_init(self):

    pygame.init()
    self.clock = pygame.time.Clock()
    self.surface = pygame.display.set_mode(self.window_size, pygame.FULLSCREEN|pygame.DOUBLEBUF)
    pygame.display.set_caption(self.title)
    self.font = pygame.font.SysFont("monospace", 40) 

  def __handle_events(self):
    for event in pygame.event.get():
      if event.type == KEYDOWN and event.key == K_ESCAPE:
        self.terminate()   
  
  def run(self):
    self.init()
    while not self.is_terminated :
      self.__handle_events()
      self.surface.fill(self.background_color)
      self.render(self.surface)
      self.update()
      pygame.display.update()
      self.clock.tick(self.fps)
      pygame.display.flip()   

  def init(self):

    self.__game_init()
  
  def update(self):
    pass

  def render(self, surface):
    pass



