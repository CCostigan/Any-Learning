# Console app to help with mundane part of SFB
# Impulse chart, weapon tables, damage allocation

# https://www.starfleetgames.com/masterindex.shtml
# https://www.starfleetgames.com/SFB_Cadet_Rulebook.pdf
# https://www.starfleetgames.com/documents/FC_Reference_Card.pdf
# https://www.starfleetgames.com/sfb/sfin/EAF.pdf
# https://www.starfleetgames.com/sfb/sfin/HexMap4230.pdf

# https://www.starfleetgames.com/CadetTraining.shtml
# https://www.starfleetgames.com/documents/Cadet/Cadet%204/Federation%20CA%20cadet%20training%20v1.GIF

# https://www.starfleetgames.com/sfb/sfin/32_Impulse_Chart%20-%20COLOR.pdf

proportional_movement_chart = [
    #  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,  17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  3 ],
    [  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  2,  2,  2,  2,  2,  2,  0,  0,  3,  3,  3,  3,  3,  3,  3,  3,  4 ],
    [  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  2,  2,  2,  0,  0,  0,  0,  3,  3,  3,  3,  0,  0,  4,  4,  4,  4,  4,  4,  5 ],
    [  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  2,  2,  0,  0,  0,  3,  3,  3,  3,  0,  0,  4,  4,  4,  4,  0,  5,  5,  5,  5,  5,  6 ],
    [  0,  0,  0,  0,  1,  0,  0,  0,  0,  2,  0,  0,  0,  3,  3,  0,  0,  0,  4,  4,  4,  0,  5,  5,  5,  5,  0,  6,  6,  6,  6,  7 ],
    [  0,  0,  0,  1,  0,  0,  0,  2,  2,  0,  0,  3,  3,  0,  0,  4,  4,  4,  0,  5,  5,  5,  0,  6,  6,  6,  6,  7,  7,  7,  7,  8 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  4,  0,  0,  5,  5,  0,  0,  6,  6,  0,  7,  7,  7,  0,  8,  8,  8,  9 ],
    [  0,  0,  0,  0,  0,  2,  0,  0,  3,  0,  0,  0,  4,  0,  0,  5,  5,  0,  0,  6,  6,  0,  7,  7,  0,  8,  8,  8,  9,  9,  9, 10 ],
    [  0,  0,  1,  0,  0,  2,  0,  0,  3,  0,  0,  4,  0,  0,  5,  0,  0,  6,  6,  0,  7,  7,  0,  8,  8,  0,  9,  9,  0, 10, 10, 11 ],
    [  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  4,  0,  0,  5,  0,  6,  6,  0,  7,  7,  0,  8,  8,  9,  9,  9, 10, 10, 10, 11, 11, 12 ],
    [  0,  0,  0,  0,  2,  0,  0,  0,  0,  4,  0,  0,  5,  0,  6,  0,  0,  7,  0,  8,  8,  0,  9,  0, 10, 10,  0, 11, 11, 12, 12, 13 ],
    [  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  5,  0,  6,  0,  7,  7,  0,  8,  0,  9,  9, 10, 10,  0, 11, 11, 12, 12, 13, 13, 14 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  5,  0,  6,  0,  7,  0,  0,  8,  0,  9,  0, 10,  0, 11, 11, 12, 12, 13, 13, 14, 14, 15 ],
    [  0,  1,  0,  2,  0,  3,  0,  4,  0,  5,  0,  6,  0,  7,  0,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  0, 10,  0, 11,  0, 12,  0, 13,  0, 14,  0, 15,  0, 16, 17 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  6,  0,  7,  0,  8,  9,  0, 10,  0, 11,  0, 12,  0, 13, 14, 14, 15, 15, 16, 16, 17, 18 ],
    [  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  7,  0,  8,  0,  0, 10,  0, 11,  0, 12, 13, 13, 14,  0, 15, 16, 16, 17, 17, 18, 19 ],
    [  0,  0,  0,  0,  0,  0,  3,  0,  0,  5,  0,  6,  0,  8,  0,  9, 10, 11,  0, 12, 13,  0, 14, 15, 15, 16,  0, 17, 18, 18, 19, 20 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7,  0,  9,  0,  0, 11,  0, 12, 13,  0, 14, 15,  0, 16, 17, 17, 18, 19, 19, 20, 21 ],
    [  0,  0,  2,  0,  0,  4,  0,  0,  6,  0,  0,  8,  0,  0, 10, 11,  0, 12, 13,  0, 14, 15,  0, 16, 17,  0, 18, 19,  0, 20, 21, 22 ],
    [  0,  0,  0,  0,  0,  0,  5,  0,  0,  7,  0,  0,  9, 10,  0,  0, 12,  0,  0, 14, 15,  0, 16, 17,  0, 18, 19, 20, 20, 21, 22, 23 ],
    [  0,  0,  0,  3,  0,  0,  0,  6,  0,  0,  8,  9,  0,  0, 11, 12,  0, 13, 14, 15,  0, 16, 17, 18, 18, 19, 20, 21, 21, 22, 23, 24 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  7,  0,  0,  0, 10,  0,  0,  0, 13, 14,  0,  0, 16, 17,  0,  0, 19, 20, 21,  0, 22, 23, 24, 25 ],
    [  0,  0,  0,  0,  4,  0,  0,  0,  0,  8,  0,  0,  0, 11, 12, 13,  0,  0, 15, 16, 17,  0, 18, 19, 20, 21,  0, 22, 23, 24, 25, 26 ],
    [  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0, 14, 15, 16,  0,  0, 18, 19, 20, 21,  0, 22, 23, 24, 25, 26, 27 ],
    [  0,  0,  0,  0,  0,  0,  6,  7,  0,  0,  0,  0, 11, 12, 13, 14,  0,  0,  0, 17, 18, 19, 20, 21,  0, 22, 23, 24, 25, 26, 27, 28 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  8,  9,  0,  0,  0,  0,  0,  0, 15, 16, 17, 18, 19,  0,  0,  0, 22, 23, 24, 25, 26, 27, 28, 29 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11, 12, 13, 14, 15,  0,  0,  0,  0,  0, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 ],
    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 ],
]

proportional_movement_chart_16 = [  # WIP
  [  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0  ],
  [  2,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0  ],
  [  3,  2,  2,  2,  2,  2,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0  ],
  [  4,  3,  3,  3,  3,  3,  0,  2,  2,  2,  0,  0,  1,  1,  0,  0  ],
  [  5,  4,  4,  4,  0,  3,  3,  0,  0,  2,  0,  0,  0,  0,  0,  0  ],
  [  6,  5,  5,  0,  4,  4,  0,  3,  3,  0,  2,  0,  0,  1,  0,  0  ],
  [  7,  6,  6,  5,  5,  0,  4,  0,  0,  3,  0,  2,  0,  0,  0,  0  ],
  [  8,  7,  7,  6,  6,  5,  5,  4,  4,  0,  3,  0,  2,  0,  1,  0  ],
  [  9,  8,  0,  7,  0,  6,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0  ],
  [ 10,  9,  8,  7,  0,  6,  0,  5,  4,  0,  3,  0,  0,  0,  0,  0  ],
  [ 11, 10,  9,  0,  8,  7,  0,  6,  0,  0,  4,  0,  0,  2,  0,  0  ],
  [ 12, 11, 10,  9,  8,  7,  0,  6,  5,  0,  0,  3,  0,  0,  0,  0  ],
  [ 13, 12, 11, 10,  0,  0,  8,  7,  0,  0,  0,  4,  0,  0,  0,  0  ],
  [ 14, 13, 12, 11, 10,  9,  0,  0,  7,  6,  5,  0,  0,  0,  0,  0  ],
  [ 15, 14, 13, 12, 11, 10,  9,  8,  0,  0,  0,  0,  0,  0,  0,  0  ],
  [ 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1  ],
]


#  https://www.starfleetgames.com/sfb/sfin/DAC.pdf
damage_chart = [
    [ "A","B","C","D","E","F","G","H","I","J","K","L","M" ],
    [ "BRDG", "FLAG", "SENS", "DCON", "AHUL", "LWEN", "TRAN", "TRAC", "SHUT", "LABS", "FHUL", "RWEN", "EXD" ],
    [ "DRON", "PHAS", "IMPL", "LWEN", "RWEN", "AHUL", "Shut", "DCon", "CWEN", "LABS", "BTTY", "PHAS", "EXD" ],
    [ "PHAS", "Tran", "RWEN", "IMPL", "FHul", "AHUL", "LWEN", "AxPR", "LABS", "TRAN", "PROB", "CWEN", "EXD" ],
    [ "RWEN", "AHUL", "CARG", "BTTY", "SHUT", "TORP", "LWEN", "IMPL", "RWEN", "TRAC", "PROB", "ANYW", "EXD" ],
    [ "FHUL", "IMPL", "LABS", "LWEN", "SENS", "TRAC", "SHUT", "RWEN", "PHAS", "TRAN", "BTTY", "ANYW", "EXD" ],
    [ "CARG", "FHUL", "BATT", "CWEN", "SHUT", "AxPR", "LABS", "PHAS", "AWEN", "PROB", "AHUL", "ANYW", "EXD" ],
    [ "AHUL", "AxPR", "SHUT", "RWEN", "SCAN", "TRAC", "LABS", "LWEN", "PHAS", "TRAN", "BTTY", "ANYW", "EXD" ],
    [ "LWEN", "FHUL", "CARG", "BTTY", "LABS", "DRON", "RWEN", "IMPL", "LWEN", "TRAC", "PROB", "ANYW", "EXD" ],
    [ "PHAS", "TRAC", "LWEN", "IMPL", "AHUL", "FHUL", "RWEN", "AxPR", "LABS", "TRAN", "PROB", "CWEN", "EXD" ],
    [ "TORP", "PHAS", "IMPL", "RWEN", "LWEN", "FHUL", "TRAC", "DCON", "CWEN", "LABS", "BTTY", "PHAS", "EXD" ],
    [ "AUXC", "EMBR", "SCAN", "PROB", "FHUL", "RWEN", "TRAN", "SHUT", "TRAC", "LABS", "AHUL", "LWEN", "EXD" ],
]

global speeds
speeds=[]

def get_speeds():
  reading=False
  speeds = []
  print(f"Enter speeds for this turn")
  while reading:
    pass

def fire_weapons():
    print(f"FIRING WEAPONS")


import pygame

pygame.init()
# Create a tiny window to capture keyboard focus
screen = pygame.display.set_mode((100, 100))

print("Got here")
running = True
while running:

  for i,ii in enumerate(proportional_movement_chart):
    # print(f"impulse:{i} - {ii}")
    movers=""
    for j,k in enumerate(ii):
      if k!=0:
        movers+=f"S:{j}#{k} "
    print(f"impulse:{i} - {movers}")

    waiting = True
    while waiting:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          # print(f"Key pressed: {pygame.key.name(event.key)} {event.dict}")
          if 'unicode' in event.dict.keys() and event.dict['unicode'] == ' ':
            waiting=False
          if 'unicode' in event.dict.keys() and event.dict['unicode'] == 'w':
            fire_weapons()
            waiting=False
          if 'unicode' in event.dict.keys() and event.dict['unicode'] == 'q':
            waiting=False
            runnint=False

pygame.quit()
















































