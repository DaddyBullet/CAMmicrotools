import math

INIT_X_OFFSET = 9.75
INIT_Y_OFFSET = 9.75

X_SPACING = 14.5
Y_SPACING = 14.5

ROWS = 20
COLS = 10

P_NUM = '10'

XY_OFFSETS = []

for i in range(ROWS):
    for j in range(COLS):
        XY_OFFSETS.append([INIT_X_OFFSET + (X_SPACING * (j if i % 2 == 0 else COLS - 1 - j)) , INIT_Y_OFFSET + (Y_SPACING * i)])

lines = ''
for offset in XY_OFFSETS:
    lines += 'G52 X{} Y{}\n'.format(offset[0], offset[1])
    lines += 'M98 P{}\n\n'.format(P_NUM)
with open('g_subprog_matrix.txt', 'w') as f:
    f.writelines(lines)
