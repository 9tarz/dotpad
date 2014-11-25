import pygame
from pygame.locals import *
from library.GameLibrary import SimpleGame
from core.Note import Note
from core.Score import Score
from core.UserInterface import UI


class DotPadGame(SimpleGame):

  BLACK = pygame.Color('black')
  WHITE = pygame.Color('white')
  RED = pygame.Color('red')
  GREY = pygame.Color('grey')
  WINDOW_SIZE = (1366, 768)


  def __init__(self):
    
    super(DotPadGame, self).__init__('DotPadGame [pre-alpha]', DotPadGame.WHITE, DotPadGame.WINDOW_SIZE)


  def init(self):

   super(DotPadGame, self).init()

   global notes, score, ui

   score = Score()

   ui = UI()

   notes = [Note(1,0,0,67),Note(2,100,0,70),Note(3,200,0,61),Note(4,300,0,77),Note(1,-100,0,75),Note(2,-150,0,75),Note(3,-200,0,61),Note(4,-250,0,67),Note(1,-400,0,71),Note(1,-425,0,73),Note(2,-450,0,75),Note(2,-475,0,75),Note(3,-500,0,75),Note(3,-525,0,75),Note(4,-550,0,75)]
   #notes = [ Note(1,0,0,67), Note(3,-100,0,70)]
  
  def render(self,surface):

    ui.render(self.surface, notes)

  def update(self):
    for note in notes:
      note.update()
      score.update(note)
    ui.show_score(self.font, score.get_score())

def main():

   game = DotPadGame()
   game.run()

if __name__ == '__main__':
  main()


