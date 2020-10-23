from sys import argv
if len(argv) < 3:
    print('Not all args:\nUsage: [offset X] [offset Y] [file_name]')

X_OFFSET = float(argv[1])
Y_OFFSET = float(argv[2])
__OFFSET = [X_OFFSET, Y_OFFSET]
FILE_NAME = argv[3]
NEW_FILE_NAME = 'New_' + FILE_NAME


with open(FILE_NAME, 'r') as f:
    data = f.readlines()

new_data = []
for i, change in enumerate(['X', 'Y']):
    for l in data:
        try:
            start = l.index(change)
            stop = start + l[start:].index(' ')
            old_val = l[start + 1:stop]
            new_data.append(l.replace(old_val, str(float(old_val) + __OFFSET[i])))
        except:
            try:
                start = l.index(change)
                stop = start + l[start:].index('\n')
                old_val = l[start + 1:stop]
                new_data.append(l.replace(old_val, str(float(old_val) + __OFFSET[i])))
            except:
                new_data.append(l)
    data = new_data
    new_data = []
print('done')
with open(NEW_FILE_NAME, 'w') as f:
    f.writelines(data)
