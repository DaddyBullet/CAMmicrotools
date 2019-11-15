import math

ROWS = 10
COLS = 10

INIT_X_OFFSET = 3.2
INIT_Y_OFFSET = 3.2

X_SPACING = 14.5
Y_SPACING = 14.5

DECIMALS = 2

# G52 X9.75 Y9.15
# M98 P10

ELEM_TO_COPY = 'g_codes_smart_helix.txt'

super_prog = ""

with open(ELEM_TO_COPY, 'r') as f:
    lines = f.readlines()
    for i in range(ROWS):
        for j in range(COLS):
            super_prog += 'G0 Z1\n'
            super_prog += 'G0 X{} Y{}\n'.format(round(INIT_X_OFFSET + i * X_SPACING, DECIMALS), round(INIT_X_OFFSET + j * Y_SPACING, DECIMALS))
            for l in lines:
                x_pos = l.find('X')
                if x_pos != -1:
                    x_val = float(l[x_pos + 1: x_pos + 1 + l[x_pos + 1:].find(' ')])
                    x_new_val = x_val + INIT_X_OFFSET + (i * X_SPACING)
                    l = l.replace('X' + str(x_val), 'X' + str(x_new_val))

                y_pos = l.find('Y')
                if y_pos != -1:
                    y_val = float(l[y_pos + 1: y_pos + 1 + l[y_pos + 1:].find(' ')])
                    y_new_val = y_val + INIT_Y_OFFSET + (j * Y_SPACING)
                    l = l.replace('Y' + str(y_val), 'Y' + str(y_new_val))

                super_prog += l

            super_prog += '\n'
        super_prog += '\n'

with open('g_matrix.txt', 'w') as f:
    f.writelines(super_prog)
