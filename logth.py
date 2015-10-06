from math import log10

# let us create header
hdr = 'log \t'
for hd in range(0, 10):
    hdr += repr(hd) + '\t'

for hd in range(10):
    hdr += repr(hd) + '  '

print('\n', hdr, '\n')

# this runs for every row
for row in range(100, 1000, 10):
    if row > 110:
        # This section for proper spacing
        if row % 100 == 00:
            print('\n')
        if row % 100 == 50:
            print()

    # this prints the rownum and pipe
    s = repr(row // 10) + '  |  '

    # finding mantissa
    for i in range(row, row + 10):
        # calculate the mantissa and round off to the 4 digits
        mantissa = round((log10(i) - int(log10(i))), 4)
        # add mantissa to string, while removing the decimal
        s = s + str(mantissa)[2:] + '\t'

    # finding mean diff
    for j in range(10):
        # calculate mean diff of xx5j where xx = rownum and
        # j represents the last digit for mantissa
        md = log10((row + 5) * 10 + j) - log10((row + 5) * 10)
        md = round(md * 10 ** 4)
        s = s + repr(md) + ' '
        # proper spacing of md
        if md / 10 < 1:
            s = s + ' '

    # output of a single row
    print(s)

# thnx message
print('\t <<The log program by cool Adi>>')
