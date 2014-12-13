import pygame
from pygame.locals import *
from library.GameLibrary import SimpleGame
from core.Note import Note
from core.Score import Score
from core.UserInterface import UI
from threading import Thread


class DotPadGame(SimpleGame):

  BLACK = pygame.Color('black')
  WHITE = pygame.Color('white')
  RED = pygame.Color('red')
  GREY = pygame.Color('grey')
  WINDOW_SIZE = (1366, 768)
  FPS = 30


  def __init__(self):
    
    super(DotPadGame, self).__init__('DotPadGame [pre-alpha]', DotPadGame.WHITE, DotPadGame.WINDOW_SIZE, DotPadGame.FPS)


  def init(self):

   super(DotPadGame, self).init()
   global movie, movie_screen
   pygame.mixer.quit()
   movie = pygame.movie.Movie('o2.mpg')
   movie_screen = pygame.Surface(movie.get_size()).convert()
   movie.set_display(movie_screen)
   global notes, score, ui

   c4  = 60
   cs4 = 61
   d4  = 62
   ds4 = 63
   e4  = 64
   f4  = 65
   fs4 = 66
   g4  = 67
   gs4 = 68
   a4  = 69
   as4 = 70
   b4  = 71
   c5  = 72
   cs5 = 73
   d5  = 74
   ds5 = 75
   e5  = 76


   score = Score()

   ui = UI(self.font, score.get_score())

   notes = [ Note(1,-2745.30,0,g4),Note(1,-2854.93,0,g4),Note(2,-2985.85,0,fs4)
   ,Note(1,-3028.45,0,g4),Note(2,-3168.82,0,fs4),Note(1,-3255.58,0,g4),Note(3,-3342.46,0,d4)

   ,Note(4,-3486.82,0,g4),Note(4,-3530.26,0,g4),Note(4,-3573.70,0,g4),Note(3,-3736.60,0,fs4)
   ,Note(4,-3779.60,0,g4),Note(3,-3822.60,0,fs4),Note(4,-3912.60,0,g4) ,Note(4,-4010.50,0,g4)
  ,Note(3,-4108.00,0,fs4),Note(3,-4455.76,0,fs4),Note(4,-4510.18,0,g4),Note(3,-4554.10,0,fs4)

   ,Note(2,-4880.35,0,e4),Note(2,-5011.03,0,e4),Note(3,-5054.56,0,g4),Note(3,-5173.96,0,g4)
   ,Note(1,-5217.28,0,fs4),Note(2,-5315.20,0,e4),Note(1,-5402.38,0,fs4),Note(3,-5489.26,0,g4)

   ,Note(1,-5674.30,0,g4),Note(1,-5773.36,0,g4),Note(2,-5936.92,0,fs4),Note(1,-5980.36,0,g4)
   ,Note(2,-6088.78,0,fs4),Note(1,-6175.18,0,g4),Note(3,-6272.47,0,d4)

   ,Note(2,-6391.54,0,g4),Note(2,-6435.22,0,g4),Note(2,-6489.94,0,g4)

   ,Note(3,-6666.79,0,fs4),Note(2,-6710.89,0,g4),Note(2,-6819.79,0,fs4)
   ,Note(3,-6928.63,0,g4),Note(1,-7026.10,0,fs4) # chuuuuu 0.25

   ,Note(2,-7405.60,0,g4),Note(1,-7459.90,0,fs4),Note(3,-7547.02,0,e4),Note(1,-7657.60,0,fs4)
   ,Note(3,-7800.55,0,e4),Note(3,-7942.42,0,e4),Note(2,-7996.57,0,g4),Note(2,-8116.60,0,g4)
   ,Note(3,-8159.56,0,fs4),Note(3,-8256.85,0,e4),Note(1,-8344.39,0,fs4)


   ,Note(4,-8529.52,0,e4),Note(3,-8682.04,0,g4),Note(4,-8814.28,0,e4),Note(1,-8912.47,0,fs4)
   ,Note(3,-9010.54,0,g4),Note(1,-9097.90,0,fs4),Note(4,-9187.90,0,e4)

   ,Note(1,-10003.69,0,e4),Note(2,-10147.66,0,g4),Note(3,-10278.82,0,e4)
   ,Note(4,-10376.62,0,fs4),Note(2,-10463.35,0,g4),Note(3,-10560.52,0,a4),Note(3,-10647.28,0,e4)


   ,Note(1,-11417.11,0,d4),Note(3,-11472.46,0,e4),Note(2,-11613.94,0,fs4),Note(4,-11735.14,0,g4)
   ,Note(2,-11833.36,0,fs4),Note(1,-11931.10,0,d4),Note(1,-12028.57,0,d4),Note(1,-12114.58,0,d4)

   ,Note(3,-12200.95,0,b4),Note(3,-12355.81,0,b4),Note(2,-12399.76,0,a4),Note(1,-12519.76,0,b4)
   ,Note(4,-12563.32,0,g4),Note(3,-12650.44,0,b4),Note(2,-12749.35,0,a4),Note(1,-12848.38,0,fs4)
   ,Note(1,-12935.80,0,e4),Note(4,-13230.04,0,c5)


   ,Note(4,-13306.06,0,c5),Note(4,-13392.82,0,c5),Note(3,-13479.16,0,b4),Note(2,-13564.60,0,a4)
   ,Note(2,-13663.69,0,a4),Note(2,-13752.19,0,a4),Note(3,-13796.35,0,b4),Note(2,-13971.13,0,a4)
   
   ,Note(1,-14166.10,0,b4) #kimi 0.49
   ,Note(1,-14220.10,0,b4),Note(4,-14318.38,0,a4),Note(2,-14405.74,0,g4),Note(3,-14492.65,0,b4)
   ,Note(4,-14535.97,0,a4),Note(1,-14634.64,0,b4),Note(1,-14722.66,0,b4),Note(4,-14766.70,0,d5)
   ,Note(3,-14855.26,0,b4),Note(4,-14953.21,0,a4),Note(1,-15040.15,0,b4)
   ,Note(4,-15094.60,0,a4),Note(2,-15401.80,0,g4),Note(1,-15446.44,0,b4)

   ,Note(3,-15685.90,0,a4),Note(2,-15783.46,0,b4),Note(1,-15870.76,0,c5)
   ,Note(1,-15957.64,0,c5),Note(1,-16012.42,0,c5),Note(2,-16100.32,0,b4),Note(3,-16188.40,0,a4)
   ,Note(4,-16331.62,0,g4),Note(4,-16419.64,0,g4),Note(3,-16516.30,0,a4),Note(2,-16603.18,0,b4)
   ,Note(1,-16688.62,0,c5),Note(2,-16741.96,0,b4)


   ,Note(4,-17136.70,0,b4),Note(3,-17180.92,0,a4)
   ,Note(3,-17268.28,0,a4),Note(1,-17322.28,0,g4),Note(1,-17495.50,0,g4),Note(1,-17550.40,0,g4)
   ,Note(3,-17627.02,0,a4),Note(3,-17713.90,0,a4)

   ,Note(3,-17866.18,0,g4),Note(3,-17996.86,0,g4),Note(2,-17920.78,0,a4)
   ,Note(1,-18083.98,0,b4),Note(1,-18171.64,0,b4),Note(2,-18215.92,0,a4),Note(1,-18304.36,0,b4)
   ,Note(1,-18392.50,0,b4)

   ,Note(3,-18447.25,0,c5),Note(2,-18546.16,0,b4),Note(4,-18633.76,0,a4)
   ,Note(3,-18720.88,0,g4),Note(1,-18808.00,0,e4),Note(3,-18905.74,0,g4)
   ,Note(3,-18949.18,0,g4)

   ,Note(1,-19450.90,0,a4),Note(2,-19725.46,0,b4),Note(2,-19812.52,0,b4)
   ,Note(4,-19855.96,0,a4)


   ,Note(2,-20093.38,0,b4),Note(2,-20136.82,0,b4),Note(1,-20201.98,0,a4),Note(3,-20289.40,0,g4)
   ,Note(2,-20377.00,0,b4),Note(1,-20420.80,0,a4),Note(2,-20519.35,0,b4),Note(2,-20618.62,0,b4)
   ,Note(4,-20662.90,0,d5),Note(2,-20748.82,0,b4),Note(1,-20836.00,0,a4),Note(2,-20933.65,0,b4)
   ,Note(1,-20987.50,0,a4),Note(4,-21281.20,0,g4),Note(2,-21324.94,0,b4)


   ,Note(4,-21590.35,0,a4),Note(1,-21666.58,0,b4),Note(2,-21753.70,0,c5),Note(2,-21842.26,0,c5)
   ,Note(2,-21886.24,0,c5),Note(1,-21984.61,0,b4),Note(4,-22072.69,0,a4),Note(3,-22214.98,0,g4)
   ,Note(3,-22312.93,0,g4),Note(4,-22399.57,0,a4),Note(1,-22486.21,0,b4),Note(2,-22573.30,0,c5)
   ,Note(1,-22627.90,0,b4)


   ,Note(1,-23032.51,0,b4),Note(4,-23131.06,0,a4),Note(4,-23185.33,0,a4),Note(3,-23228.65,0,g4)
   ,Note(3,-23391.70,0,g4),Note(3,-23435.26,0,g4),Note(4,-23511.52,0,a4),Note(4,-23587.96,0,a4)
   ,Note(3,-23728.57,0,g4),Note(3,-23782.42,0,g4),Note(4,-23869.18,0,a4),Note(1,-23956.84,0,b4)
   ,Note(1,-24045.40,0,b4)

   ,Note(2,-24089.44,0,a4),Note(3,-24177.34,0,b4),Note(3,-24275.53,0,b4),Note(4,-24318.85,0,c5)
   ,Note(3,-24406.93,0,b4),Note(2,-24497.02,0,a4),Note(1,-24595.30,0,g4),Note(3,-24691.42,0,e4)
   ,Note(1,-24767.44,0,g4),Note(1,-24821.83,0,g4)

   ,Note(3,-25313.74,0,b4)
   ,Note(3,-25412.35,0,a4),Note(1,-25705.06,0,e4),Note(3,-25791.70,0,b4),Note(2,-25846.45,0,a4)
   ,Note(4,-25922.74,0,g4),Note(3,-26008.90,0,a4),Note(1,-26095.78,0,g4)
   ]
  

  def render(self,surface):

    #surface.blit(movie_screen,(180,40))
    self.surface.blit(movie_screen,(180,40))
    ui.render(self.surface, notes)

  def update(self):
    for note in notes:
      if (self.clock.get_fps() == 0):
        note.update(1./DotPadGame.FPS)
      else :
        note.update(1./self.clock.get_fps())
      score.update(note)
    ui.show_score(self.font, score.get_score())
    movie.play()

def main():
    game = DotPadGame()
    game.run()

if __name__ == '__main__':
    main()