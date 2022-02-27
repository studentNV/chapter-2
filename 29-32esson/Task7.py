#!/usr/bin/env python
def sky_piercing_spiral(sizeTable):
    dx, dy = 0, 1
    x, y = 0, 0
    arr = [[None] * sizeTable for _ in range(sizeTable)]
    for i in range(1, sizeTable * sizeTable + 1):
        arr[x][y] = i**2
        nx, ny = x + dx, y + dy
        if 0 <= nx < sizeTable and 0 <= ny < sizeTable and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy
    for i in arr:
        for j in i:
            print(j, end=' ')
        print(' ')


sky_piercing_spiral(5)
