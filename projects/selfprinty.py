s = r"""
for i in range(2):
    if i == 0:
        print("s = \"\"\"" + s + "\"\"\"")
    else:
        print(s)
"""

for i in range(2):
    if i == 0:
        print("s = r\"\"\"" + s + "\"\"\"")
    else:
        print(s)
