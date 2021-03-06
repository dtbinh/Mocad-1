import sys
sys.path.append('.')

from Simulateur.core.SMA import SMA
from Simulateur.core.View import View
from Simulateur.core.Environment import Environment
from Simulateur.particles.Particle import Particle
import time

GRIDSIZEX = 100
GRIDSIZEY = 100

TICKSNB = 0
PARTICLENB = 300

TOR = False


v = View(800/GRIDSIZEX,800/GRIDSIZEY)

e = Environment(GRIDSIZEX, GRIDSIZEY, TOR)

s = SMA(e,v,0 ,TICKSNB, 0.1)

for i in range(PARTICLENB):
	p = Particle(e, s)
	p.addRandomToEnv()

v.drawWidgets(s.env)
s.run()
v.update()
time.sleep(0.1)
