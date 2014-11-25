import pygame
from pygame.locals import *
from Note import Note

class Score(object):

  def __init__(self):
    self.score = 0

  def get_score(self):
    return int(self.score)

  def note_collide(self, note):
    judment_line = []
    for i in range (1,5):
      judment_line.append(Rect(60*i,  625,   60,   143))

    for i in range (0,4):
      if judment_line[i].colliderect(note.get_rect()) and not note.is_hit :
        if pygame.key.get_pressed()[K_d] and i  == 0:
          note.hit()
          note.play()
          self.score += 100
        elif pygame.key.get_pressed()[K_f] and i == 1:
          note.hit()
          note.play()
          self.score += 100
        elif pygame.key.get_pressed()[K_j] and i == 2:
          note.hit()
          note.play()
          self.score += 100
        elif pygame.key.get_pressed()[K_k] and i == 3:
          note.hit()
          note.play()
          self.score += 100

  def update(self, note):
    self.note_collide(note)
