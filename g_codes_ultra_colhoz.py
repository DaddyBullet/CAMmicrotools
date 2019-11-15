import math

INIT_X = 0
INIT_Y = 0
INIT_Z = 0

DEG = 10. * (math.pi / 180.) #incline degree
HEIGHT = 0.5
DIAMETR = 8.9
REVOLVES = 10
SPR = 20. #Step per revolve
MILL_D = 3.18
DECIMALS = 2
FILE_NAME = 'g_codes_smart_helix.txt'

parametr_arr = [INIT_X, INIT_Y, INIT_Z, DEG, HEIGHT, DIAMETR, REVOLVES, SPR, MILL_D, DECIMALS, FILE_NAME]

all_degs = []

for i in range(int(REVOLVES * SPR)):
    all_degs.append(((2 * math.pi) / SPR) * i)

def r(fi):
    return (DIAMETR/2) - (fi / (2 * math.pi * REVOLVES)) * HEIGHT * math.tan(math.pi/2 - DEG) - (MILL_D / 2)

def x(fi):
    return r(fi) * math.cos(fi)

def y(fi):
    return r(fi) * math.sin(fi)

def z(fi):
    return - HEIGHT * (fi / (2 * math.pi * REVOLVES))

for fi in all_degs:
    print(f'G01 X{round(x(fi),DECIMALS)} Y{round(y(fi),DECIMALS)} Z{round(z(fi),DECIMALS)}')
with open(FILE_NAME, 'w') as f:
    for fi in all_degs:
        f.writelines(f'G01 X{round(x(fi),DECIMALS)} Y{round(y(fi),DECIMALS)} Z{round(z(fi),DECIMALS)}\n')
