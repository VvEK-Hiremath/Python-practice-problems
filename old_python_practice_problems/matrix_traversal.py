mat = list()
f = 1
for i in range(0,3):
    lst = list()
    for j in range(0,3):
        lst.append(f)
        f = f+1
    mat.append(lst)

def print_mat(lst):
    for i in range(0,3):
        for j in range(0,3):
            print(mat[i][j],end=" ")
        print()

print_mat(mat)