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


   c2  = 47
   c3  = 48
   cs3 = 49
   d3  = 50
   ds3 = 51
   e3  = 52
   f3  = 53
   fs3 = 54
   g3  = 55
   gs3 = 56
   a3  = 57
   as3 = 58
   b3  = 59
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
   f5  = 77
   fs5 = 78
   g5  = 79
   gs5 = 80
   a5  = 81
   as5 = 82
   b5  = 83
   c6  = 84


   score = Score()

   ui = UI(self.font, score.get_score())

   notes = [ Note(1,-2745.30,0,g4),Note(1,-2854.93,0,g4),Note(1,-2985.85,0,fs4)
   ,Note(1,-3028.45,0,g4),Note(1,-3168.82,0,fs4),Note(1,-3255.58,0,g4),Note(1,-3342.46,0,d4)

   ,Note(1,-3486.82,0,g4),Note(1,-3530.26,0,g4),Note(1,-3573.70,0,g4),Note(1,-3736.60,0,fs4)
   ,Note(1,-3779.60,0,g4),Note(1,-3822.60,0,fs4),Note(1,-3912.60,0,g4) ,Note(1,-4010.50,0,g4)
  ,Note(1,-4108.00,0,fs4),Note(1,-4455.76,0,fs4),Note(1,-4510.18,0,g4),Note(1,-4554.10,0,fs4)

   ,Note(1,-4880.35,0,e4),Note(1,-5011.03,0,e4),Note(1,-5054.56,0,g4),Note(1,-5173.96,0,g4)
   ,Note(1,-5217.28,0,fs4),Note(1,-5315.20,0,e4),Note(1,-5402.38,0,fs4),Note(1,-5489.26,0,g4)

   ,Note(3,-5674.30,0,g4),Note(1,-5773.36,0,g4),Note(1,-5936.92,0,fs4),Note(1,-5980.36,0,g4)
   ,Note(1,-6088.78,0,fs4),Note(1,-6175.18,0,g4),Note(2,-6272.47,0,d4)

   ,Note(1,-6391.54,0,g4),Note(1,-6435.22,0,g4),Note(1,-6489.94,0,g4)

   ,Note(2,-6666.79,0,fs4),Note(1,-6710.89,0,g4),Note(1,-6819.79,0,fs4)
   ,Note(1,-6928.63,0,g4),Note(2,-7026.10,0,fs4) # chuuuuu 0.25

   ,Note(1,-7405.60,0,c2),Note(1,-7459.90,0,c2),Note(1,-7547.02,0,c2),Note(1,-7657.60,0,c2)
   ,Note(1,-7800.55,0,c2),Note(1,-7942.42,0,c2),Note(1,-7996.57,0,c2),Note(1,-8116.60,0,c2)
   ,Note(1,-8159.56,0,c2),Note(1,-8256.85,0,c2),Note(1,-8344.39,0,c2),Note(1,-8529.52,0,c2)
   ,Note(1,-8682.04,0,c2),Note(1,-8814.28,0,c2),Note(1,-8912.47,0,c2),Note(1,-9010.54,0,c2)
   ,Note(1,-9097.90,0,c2),Note(1,-9187.90,0,c2),Note(1,-10147.66,0,c2),Note(1,-10278.82,0,c2)
   ,Note(1,-10376.62,0,c2),Note(1,-10463.35,0,c2),Note(1,-10550.26,0,c2),Note(1,-10637.59,0,c2)
   ,Note(1,-11417.11,0,c2),Note(1,-11472.46,0,c2),Note(1,-11613.94,0,c2),Note(1,-11735.14,0,c2)
   ,Note(1,-11833.36,0,c2),Note(1,-11931.10,0,c2),Note(1,-12028.57,0,c2),Note(1,-12114.58,0,c2)
   ,Note(1,-12200.95,0,c2),Note(1,-12355.81,0,c2),Note(1,-12399.76,0,c2),Note(1,-12519.76,0,c2)
   ,Note(1,-12563.32,0,c2),Note(1,-12650.44,0,c2),Note(1,-12749.35,0,c2),Note(1,-12848.38,0,c2)
   ,Note(1,-12935.80,0,c2),Note(1,-13230.04,0,c2),Note(1,-13306.06,0,c2),Note(1,-13392.82,0,c2)
   ,Note(1,-13479.16,0,c2),Note(1,-13564.60,0,c2),Note(1,-13663.69,0,c2),Note(1,-13752.19,0,c2)
   ,Note(1,-13796.35,0,c2),Note(1,-13971.13,0,c2),Note(1,-14166.10,0,c2),Note(1,-14220.10,0,c2)
   ,Note(1,-14318.38,0,c2),Note(1,-14405.74,0,c2),Note(1,-14492.65,0,c2),Note(1,-14535.97,0,c2)
   ,Note(1,-14634.64,0,c2),Note(1,-14722.66,0,c2),Note(1,-14766.70,0,c2),Note(1,-14855.26,0,c2)
   ,Note(1,-14953.21,0,c2),Note(1,-15040.15,0,c2),Note(1,-15094.60,0,c2),Note(1,-15401.80,0,c2)
   ,Note(1,-15446.44,0,c2),Note(1,-15685.90,0,c2),Note(1,-15783.46,0,c2),Note(1,-15870.76,0,c2)
   ,Note(1,-15957.64,0,c2),Note(1,-16012.42,0,c2),Note(1,-16100.32,0,c2),Note(1,-16188.40,0,c2)
   ,Note(1,-16331.62,0,c2),Note(1,-16419.64,0,c2),Note(1,-16516.30,0,c2),Note(1,-16603.18,0,c2)
   ,Note(1,-16688.62,0,c2),Note(1,-16741.96,0,c2),Note(1,-17136.70,0,c2),Note(1,-17180.92,0,c2)
   ,Note(1,-17268.28,0,c2),Note(1,-17322.28,0,c2),Note(1,-17495.50,0,c2),Note(1,-17550.40,0,c2)
   ,Note(1,-17627.02,0,c2),Note(1,-17713.90,0,c2),Note(1,-17866.18,0,c2),Note(1,-12312,0,c2)
   ,Note(1,-17996.86,0,c2),Note(1,-17920.78,0,c2)
   ,Note(1,-18083.98,0,c2),Note(1,-18171.64,0,c2),Note(1,-18215.92,0,c2),Note(1,-18304.36,0,c2)
   ,Note(1,-18392.50,0,c2),Note(1,-18447.25,0,c2),Note(1,-18546.16,0,c2),Note(1,-18633.76,0,c2)
   ,Note(1,-18720.88,0,c2),Note(1,-18808.00,0,c2),Note(1,-18905.74,0,c2),Note(1,-18949.18,0,c2)
   ,Note(1,-19450.90,0,c2),Note(1,-19725.46,0,c2),Note(1,-19812.52,0,c2),Note(1,-19855.96,0,c2)
   ,Note(1,-20093.38,0,c2),Note(1,-20136.82,0,c2),Note(1,-20201.98,0,c2),Note(1,-20289.40,0,c2)
   ,Note(1,-20377.00,0,c2),Note(1,-20420.80,0,c2),Note(1,-20519.35,0,c2),Note(1,-20618.62,0,c2)
   ,Note(1,-20662.90,0,c2),Note(1,-20748.82,0,c2),Note(1,-20836.00,0,c2),Note(1,-20933.65,0,c2)
   ,Note(1,-20987.50,0,c2),Note(1,-21281.20,0,c2),Note(1,-21324.94,0,c2),Note(1,-21590.35,0,c2)
   ,Note(1,-21666.58,0,c2),Note(1,-21753.70,0,c2),Note(1,-21842.26,0,c2),Note(1,-21886.24,0,c2)
   ,Note(1,-21984.61,0,c2),Note(1,-22072.69,0,c2),Note(1,-22214.98,0,c2),Note(1,-22312.93,0,c2)
   ,Note(1,-22399.57,0,c2),Note(1,-22486.21,0,c2),Note(1,-22573.30,0,c2),Note(1,-22627.90,0,c2)
   ,Note(1,-23032.51,0,c2),Note(1,-23131.06,0,c2),Note(1,-23185.33,0,c2),Note(1,-23228.65,0,c2)
   ,Note(1,-23391.70,0,c2),Note(1,-23435.26,0,c2),Note(1,-23511.52,0,c2),Note(1,-23587.96,0,c2)
   ,Note(1,-23728.57,0,c2),Note(1,-23782.42,0,c2),Note(1,-23869.18,0,c2),Note(1,-23956.84,0,c2)
   ,Note(1,-24045.40,0,c2),Note(1,-24089.44,0,c2),Note(1,-24177.34,0,c2),Note(1,-24275.53,0,c2)
   ,Note(1,-24318.85,0,c2),Note(1,-24406.93,0,c2),Note(1,-24497.02,0,c2),Note(1,-24595.30,0,c2)
   ,Note(1,-24691.42,0,c2),Note(1,-24767.44,0,c2),Note(1,-24821.83,0,c2),Note(1,-25313.74,0,c2)
   ,Note(1,-25412.35,0,c2),Note(1,-25705.06,0,c2),Note(1,-25791.70,0,c2),Note(1,-25846.45,0,c2)
   ,Note(1,-25922.74,0,c2),Note(1,-26008.90,0,c2),Note(1,-26095.78,0,c2)
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