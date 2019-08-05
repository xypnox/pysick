def splitInversion(A, p, a, q):
    B = A[p:a]
    C = A[a:q]
    i, b, c = p, 0, 0
    inversions = 0

    while i < q:
        if b == len(B) or c == len(C):
            break
        elif B[b] < C[c]:
            A[i] = B[b]
            b += 1
        else:
            A[i] = C[c]
            c += 1
            inversions += a - p - b
        i += 1

    while c < len(C) and i < q:
        A[i] = C[c]
        i += 1
        c += 1
    while b < len(B) and i < q:
        A[i] = B[b]
        i += 1
        b += 1
    return inversions


def countInversion(A, p, q):
    a = (p+q)//2
    if p == a:
        return 0
    else:
        left = countInversion(A, p, a)
        right = countInversion(A, a, q)

    split = splitInversion(A, p, a, q)

    return left + right + split


Arr = []

with open('IntegerArray.txt') as f:
    for line in f:
        Arr.append(int(line))

# print(Arr)
inversions = countInversion(Arr, 0, len(Arr))
print(inversions)
