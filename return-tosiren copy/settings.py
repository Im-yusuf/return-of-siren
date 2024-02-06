map_layout = [
    'X                                           ',
    'X                                           ',
    'X     C           XX      XX      XX        ',
    'XC    XX         X  X    X  X    X  X       ',
    'XX    XX         B              C           ',
    'X    CXX                      CC CC   G     ',
    'X    XXX  P   CS    S     S                 ',
    'XC     XXXXX  XX  XXXX    XX          X     ',
    'XX    CCXX     X  CXX    XXH X     S XXXX   ',
    'XXX   XXX       XXXX         XX   XXX       ',
    'XXXX       X    X XXC  X  CCCXX CXXXX       ',
    'XXXXXXXXXXXX  XXXXXXXX XXXXXX  XX  XXXX     ',]

map_layout2 = [
    'X                  XX      XX                 XX       XX    ',
    'X      CC         XXXX    XXXX               XXXX     XXXX   ',
    'X   C S                          C                           ',
    'X   XXXXXX                       XX                    G     ',
    'XC      XX                      XX         CC                ',
    'XX     CXX  S  X   S         S            C  C       XXXX    ',
    'X      XXX XXX XC XXX   X  XXXXX         X        X   XX     ',
    'XP  XX  XX  X  XX XXX  XX   XXX      S           XX   XX     ',
    'XXXXXX  XX  X  XC  CX XXX  CXXX     XXX   S  S  XXX   XX     ',
    'XXXXXX  XX  X  XXXXXXXXXX  XXXX     XXX XXXXXXXXXXX   XX     ',
    'XXXXXX  XX  X  XXXXXXXXXX   XXX     XXX XXXXXXXXXXX   XX     ',]

tile_size = 64
screen_width = 1470
screen_height =len(map_layout) * tile_size
map_layout3=[
  '                       ',
  '    X X  XXX  X X      ',
  '    XXX  X X  XPX      ',
  '     X   X X  X X      ',
  '     X   XXX  XXX      ',
  '                       ',
  '    X   X   X  X  X  X ',
  '    X  X X  X     XX X ',
  '    X X   X X  X  X XX ',
  '    XX     XX  X  X  X ',
  ]

 # '    X  X  X  
  #'    X X X X
  #'    XX   XX  
  #'    X     X  


# letters = ["a", "b", "c"]
levels = {1: map_layout3, 2: map_layout2, 3:map_layout}
