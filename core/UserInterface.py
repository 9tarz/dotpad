import pygame
from pygame.locals import *

class UI(object):

  BLACK = pygame.Color('black')
  WHITE = pygame.Color('white')
  RED = pygame.Color('red')
  GREY = pygame.Color('grey')


  def __init__(self,font, score):
    
    self.score_image = font.render("Score = %d" % score, 0, UI.BLACK)

  def show_score(self, font, score):

    self.score_image = font.render("Score = %d" % score, 0, UI.BLACK)

  def render(self, surface, notes):

    pygame.draw.rect(surface, UI.RED, (0, 0, 60, 768))
    pygame.draw.rect(surface, UI.BLACK, (60, 0, 240, 625))
    for i in range(1,5):
      pygame.draw.line(surface, UI.WHITE, (60*i, 0), (60*i, 768))
    pygame.draw.line(surface, UI.WHITE, (60, 625), (300, 625), 9)
    for note in notes:
      note.render(surface)
    pygame.draw.rect(surface, UI.GREY, (60, 625, 240, 768))
    surface.blit(self.score_image, (1000,10))
