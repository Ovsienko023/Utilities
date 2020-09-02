import pygame.midi
import time

pygame.midi.init()

player = pygame.midi.Output(0)
player.set_instrument(1)
player.note_on(60, 100)
time.sleep(0.5)

player.note_on(63, 100)
time.sleep(0.5)

player.note_on(66, 100)
time.sleep(1)
time.sleep(0.5)
######################
player.note_on(60, 100)
time.sleep(0.5)

player.note_on(63, 100)
time.sleep(0.5)

player.note_on(68, 100)
time.sleep(0.5)

player.note_on(66, 100)
time.sleep(0.5)
time.sleep(0.5)
#################
player.note_on(60, 100)
time.sleep(0.5)

player.note_on(63, 100)
time.sleep(0.5)

player.note_on(66, 100)
time.sleep(1)

player.note_on(63, 100)
time.sleep(0.5)

player.note_on(60, 100)
time.sleep(1)

del player
pygame.midi.quit()