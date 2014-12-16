import pygame
from pygame.locals import *

class UI(object):

  BLACK = pygame.Color('black')
  WHITE = pygame.Color('white')
  RED = pygame.Color('red')
  GREY = pygame.Color('grey')
  BLUE = pygame.Color('blue')


  def __init__(self,font, score):
    
    self.score_image = font.render("Score : %.2f " % score, 0, UI.WHITE)

  def show_score(self, font, score):

    self.score_image = font.render("Score : %.2f " % score, 0, UI.WHITE)

  def render(self, surface, notes):

    pygame.draw.rect(surface, UI.RED, (0, 0, 60, 768))
    pygame.draw.rect(surface, UI.BLACK, (60, 0, 240, 625))

    for note in notes:
      note.render(surface)

    pygame.draw.rect(surface, UI.GREY, (60, 625, 240, 768))
    if pygame.key.get_pressed()[K_d]:
      pygame.draw.rect(surface, UI.BLUE, (60*1, 0 , 60, 768))
    elif pygame.key.get_pressed()[K_f]:
      pygame.draw.rect(surface, UI.RED, (60*2, 0 , 60, 768))
    elif pygame.key.get_pressed()[K_j]:
      pygame.draw.rect(surface, UI.BLUE, (60*3, 0 , 60 , 768))
    elif pygame.key.get_pressed()[K_k]:
      pygame.draw.rect(surface, UI.RED, (60*4, 0 , 60 , 768))
    for i in range(1,5):
      pygame.draw.line(surface, UI.WHITE, (60*i, 0), (60*i, 768))

    pygame.draw.line(surface, UI.WHITE, (60, 625), (300, 625), 9)

    surface.blit(self.score_image, (1000,50))
