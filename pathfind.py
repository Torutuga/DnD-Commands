import math

class Zone:
    def __init__(self, cor, bio, rel):
        self.cor = cor
        self.bio = bio
        self.rel = rel

class Node:
    def __init__(self, step, parent, position):
        self.step = step
        self.parent = parent
        self.position = position

def Actions(z, posible):
  coors = [(-3,-2),(0,-4),(3,-2),(-3,2),(0,4),(3,2)]
  for c in coors:
    pos = (z.cor[0]+c[0], z.cor[1]+c[1])
    for p in z.rel:
      if p.cor == pos and p.bio == 'water':
        posible.append(p)

cors = []
for col in range(2, 17, 3):
    for row in range(2, 16, 4):
        if col%2 != 0:
            if row >= 16-2:
                pass
            else:
                cors.append((col, row+2))
        else:
            cors.append((col, row))

print(cors)
zones = []
for x in cors:
    if x == (8,10):
        zones.append(Zone(x, 'peaks', []))
    if x == (5,8) or x == (5,4) or x == (8,2):
        zones.append(Zone(x, 'water', []))
    else:
        zones.append(Zone(x, 'flats', []))

for x in zones:
    for p in cors:
        dst = math.sqrt(pow(x.cor[0]-p[0], 2) + pow(x.cor[1]-p[1], 2))
        if dst > 0 and dst <= 4:
            x.rel.append(p)
        if len(x.rel) >= 6:
            break

center = (int(17/2), int(16/2))
def distance(z):
    global center
    return math.sqrt(pow(z.cor[0]-center[0], 2) + pow(z.cor[1]-center[1], 2))

#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################

def Search(zones):
    frontier = []
    explore = []
    pos = []
    lap = 0

    for z in zones:
        if z.bio == 'peaks':
            frontier.append(Node(0, None, z.cor))
            z.bio == 'peaksU'
            break

    run = True
    while run:
        if not frontier:
            run = False
        lap += 1

    frontier.sort(reverse=True, key=distance)
    node = frontier.pop()

    if node.position

