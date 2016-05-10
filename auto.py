
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

width = 75
height = 52
nsteps = 12000
 
class Dir: up, right, down, left = range(4)
class Turn: left, right = False, True
class Color: white, black = '.', '#'
M = [[Color.white] * width for _ in range(height)]
 
x = width // 2
y = height // 2
dir = Dir.up
 
i = 0
while i < nsteps and 0 <= x < width and 0 <= y < height:
    turn = Turn.left if M[y][x] == Color.black else Turn.right
    M[y][x] = Color.white if M[y][x] == Color.black else Color.black
 
    dir = (4 + dir + (1 if turn else -1)) % 4
    dir = [Dir.up, Dir.right, Dir.down, Dir.left][dir]
    if   dir == Dir.up:    y -= 1
    elif dir == Dir.right: x -= 1
    elif dir == Dir.down:  y += 1
    elif dir == Dir.left:  x += 1
    else: assert False
    i += 1
 
print ("\n".join("".join(row) for row in M))
plt.show()


class Dir: norte, este, sur, oeste = range(4)
	class Color: blanco, negro = '.', '#'
	return dir.norte, color.negro


class Dir: norte, este, sur, oeste = range(4)
class giro: oeste, este = False, True
class Color: blanco, negro = 'w', 'k'
M = [[Color.blanco] * ancho for _ in range(alto)]
 
i = ancho// 2
j = alto // 2
dir = Dir.norte

n = 0
while n < nsteps and 0 <= i < ancho and 0 <= j < alto:
    		giro = giro.oeste 
		if M[j][i] == Color.negro else giro.este

    		M[j][i] = Color.blanco 
		if M[j][i] == Color.negro else Color.negro
 
    dir = (4 + dir + (1 if giro else -1)) % 4
    dir = [Dir.up, Dir.derecha, Dir.abajo, Dir.izquierda][dir]
    if   dir == Dir.norte:    j -= 1
    elif dir == Dir.este: i -= 1
    elif dir == Dir.sur:  j += 1
    elif dir == Dir.oeste:  i += 1
    else: assert False
    i += 1
 
print ("\n".join("".join(fila) for fila in M))
plt.plot (i, j)
plt.show()
