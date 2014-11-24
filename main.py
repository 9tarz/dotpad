import pygame
from pygame.locals import *
from gamelib import SimpleGame
from note import Note
from score import Score


class DotPadGame(SimpleGame):

  BLACK = pygame.Color('black')
  WHITE = pygame.Color('white')
  RED = pygame.Color('red')
  GREY = pygame.Color('grey')
  WINDOW_SIZE = (1366,768)


  def __init__(self):
    
    super(DotPadGame, self).__init__('DotPadGame [pre-alpha]', DotPadGame.WHITE, DotPadGame.WINDOW_SIZE)

  def init(self):

   super(DotPadGame, self).init()

   global notes, score

   score = Score()

   #score_image = self.font.render("Score = %d" % score.get_score() , 0, DotPadGame.BLACK)

   notes = [Note(1,0,0,67),Note(2,100,0,70),Note(3,200,0,61),Note(4,300,0,77),Note(1,-100,0,75),Note(2,-150,0,75),Note(3,-200,0,61),Note(4,-250,0,67),Note(1,-400,0,71),Note(1,-425,0,73),Note(2,-450,0,75),Note(2,-475,0,75),Note(3,-500,0,75),Note(3,-525,0,75),Note(4,-550,0,75)]
   #notes = [ Note(1,0,0,67), Note(3,-100,0,70)]
  
  def render(self,surface):

    pygame.draw.rect(self.surface, DotPadGame.RED, (0,  0,   60,   768))
    pygame.draw.rect(self.surface, DotPadGame.BLACK, (60,  0,   240,   625))
    for i in range(1,5):
      pygame.draw.line(self.surface, DotPadGame.WHITE, (60*i, 0), (60*i, 768))
    pygame.draw.line(self.surface, DotPadGame.WHITE, (60, 625), (1366, 625), 9)
    for note in notes:
      note.render(surface)
    pygame.draw.rect(self.surface, DotPadGame.GREY, (60,  625,   240,   768))
    surface.blit(score_image, (1000,10))

  def update(self):
    global score_image
    for note in notes:
      note.update()
      score.update(note)
    score_image = self.font.render("Score = %d" % score.get_score() , 0, DotPadGame.BLACK)

def main():

   game = DotPadGame()
   game.run()

if __name__ == '__main__':
  main()


