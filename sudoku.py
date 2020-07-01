"""
The input should be just like the example below:

6 4 2 1 8 3 5 9 7
3 1 9 5 2 7 6 8 4
5 8 7 9 4 6 3 2 1
8 9 4 2 6 5 7 1 3
7 3 6 8 1 9 2 4 5
2 5 1 7 3 4 9 6 8
4 6 5 3 9 1 8 7 2
1 7 8 6 5 2 4 3 9
9 2 3 4 7 8 1 5 6
Outputs: "Correct." or "Wrong."

"""

start = print("Type your sudoku board:")
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
f = list(map(int, input().split()))
g = list(map(int, input().split()))
h = list(map(int, input().split()))
i = list(map(int, input().split()))

rows = [a, b, c, d, e, f, g, h, i]


columns = []
for i in range(9):
    columns.append([
        rows[0][i],
        rows[1][i],
        rows[2][i],
        rows[3][i],
        rows[4][i],
        rows[5][i],
        rows[6][i],
        rows[7][i],
        rows[8][i]
        ])

squares = []

def squares_create():
    bigcol1=[]
    bigcol2=[]
    bigcol3=[]
    for i in range(9):
        for j in range(3):
            bigcol1.append(rows[i][j])
    for k in range(9):
        for j in range(3, 6):
            bigcol2.append(rows[k][j])
    for l in range(9):
        for j in range(6, 9):
            bigcol3.append(rows[l][j])
    squares.append(bigcol1[0:9])
    squares.append(bigcol1[9:18])
    squares.append(bigcol1[18:27])

    squares.append(bigcol2[0:9])
    squares.append(bigcol2[9:18])
    squares.append(bigcol2[18:27])
    
    squares.append(bigcol3[0:9])
    squares.append(bigcol3[9:18])
    squares.append(bigcol3[18:27])

squares_create()


def condition1(rows):
    if all(len(set(row)) == 9 for row in rows):
        return True
def condition2(columns):
    if all(len(set(column)) == 9 for column in columns):
        return True
def condition3(squares):
    if all(len(set(square)) == 9 for square in squares):
        return True
if (condition1(rows) == True and condition2(columns) == True and condition3(squares) == True):
    print("Correct.")
else:
    print("Wrong.")
    

