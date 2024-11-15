# imagine a cuboid, cuboid is in quadrant 1 since x, y, z > 0
# input - 4 integers
# output array

x = int(input())
y = int(input())
z = int(input())
n = int(input())

def list_comprehensions(x, y, z, n):
    print( [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n] )


list_comprehensions(x, y, z, n)