# let us create header
hdr = 'alog \t '
for hd in range(0, 10):
    hdr += repr(hd) + '\t '

for hd in range(10):
    hdr += repr(hd) + '  '

print(hdr, '\n')


for row in range(0, 100):
    if row > 9:
        # This section for proper spacing
        if row % 10 == 0:
            print('\n')
    if row % 10 == 5:
        print()

    s = repr(row)
    if row < 10:
        s += ' '
    s += '  |\t'
    for i in range(0, 10):
        x = round((10 ** ((row * 10 + i) * 10 ** (-3))) * 10 ** 3)
        s = s + repr(x) + '\t'
    for j in range(10):
        x = round(((10 ** ((row * 100 + 50 + j) * 10 ** (-4))) - (10 ** ((row * 10 + 5) * 10 ** (-3)))) * 10 ** 3)
        s = s + ' ' + repr(x)
        if x < 10:
            s += ' '
    print(s)
