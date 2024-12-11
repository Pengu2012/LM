Matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(Matrix)

Number = Matrix[1][1]

print(Number)
#Number of rows
print(len(Matrix))
#Number of colums
print(len(Matrix[0]))

for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        print(Matrix[i][j], end = " ")
    print()
    