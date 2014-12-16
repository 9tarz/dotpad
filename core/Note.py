import time
import numpy
import pyaudio
import fluidsynth
import pygame
from pygame.locals import *
from threading import Thread

class Note(object):
	
  def __init__(self, row, y , track, sound_note):

    self.row = row
    self.y = y

    self.rect = (60*self.row, self.y,  60, 20)

    self.is_hit = False
    self.track = track
    self.sound_note = sound_note

  def get_rect(self):
    return self.rect

  def get_y(self):
    return self.y

  def delete(self):
    self.y = 1000

  def hit(self):
    self.is_hit = True

  def update(self, delta):

    self.y += 300*delta

    self.rect = (60*self.row, self.y, 60, 20)

  def render(self,surface):

    pygame.draw.rect(surface, pygame.Color('white'), self.rect)

  def play(self):

    SoundKeyThread(self).start()

  def play_sound(self):
    
    self.sound_arr = []
    self.fl = fluidsynth.Synth()
    self.sfid = self.fl.sfload("sound/KawaiStereoGrand.sf2")
    self.pa = pyaudio.PyAudio()
    self.strm = self.pa.open(

        format = pyaudio.paInt16,
        channels = 2, 
        rate = 44100, 
        output = True)

    self.fl.program_select(0, self.sfid, 0, 0)

    self.fl.noteon(self.track, self.sound_note, 127)

    # Chord is held for 2 seconds
    self.sound_arr = numpy.append(self.sound_arr, self.fl.get_samples(44100 * 1))

    self.fl.noteoff(self.track, self.sound_note)

    # Decay of chord is held for 1 second
   # self.sound_arr = numpy.append(self.sound_arr, self.fl.get_samples(44100 * 1))

    self.fl.delete()

    self.samps = fluidsynth.raw_audio_string(self.sound_arr)

    self.strm.write(self.samps)

    self.strm.close()

    self.pa.terminate()

class SoundKeyThread(Thread):
    def __init__(self,note):

        Thread.__init__(self)
        self.note = note
 
    def run(self):

        Note.play_sound(self.note)