A = range(0x61, 0x61+25)
B = [119, 101, 95, 119, 105, 108, 108, 95, 109, 105, 115, 115, 95, 121, 111, 117, 95, 112, 114, 111, 99, 102, 115, 46, 46]
C = [41546, 8619, 53491, 12367, 19810, 56577, 60086, 27970, 20573, 9151, 3554, 50732, 45063, 30800, 48142, 44842, 8366, 10332, 53130, 7242, 28114, 45541, 46379, 9801, 10691]
ans = [66767, 74378, 98601, 96720, 115270, 59426, 95089, 80703, 115942, 59188, 58826, 82702, 108504, 102446, 102655, 64693, 89909, 70993, 101607, 53330, 102259, 59728, 64083, 66997, 103118]
perm = [21, 3, 24, 9, 18, 19, 0, 4, 20, 1, 22, 11, 2, 7, 16, 10, 5, 13, 14, 17, 6, 12, 15, 8, 23][::-1]
aans = [0 for i in range(25)]
for i in range(25):
    aans[perm[i]] = ans[i]

M1 = Matrix(IntegerRing(), 5, 5)
for i in range(5):
    for j in range(5):
        M1[i, j] = A[i * 5 + j]

M2 = Matrix(IntegerRing(), 5, 5)
for i in range(5):
    for j in range(5):
        M2[i, j] = B[i * 5 + j]

M3 = Matrix(IntegerRing(), 5, 5)
for i in range(5):
    for j in range(5):
        M3[i, j] = C[i * 5 + j]

M4 = Matrix(IntegerRing(), 5, 5)
for i in range(5):
    for j in range(5):
        M4[i, j] = aans[i * 5 + j]

print (M4 - M3) * M2^-1
