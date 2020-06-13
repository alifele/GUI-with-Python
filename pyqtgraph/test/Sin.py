import numpy as np
import pyqtgraph as pg



t = np.arange(0,10,0.1)
y = np.sin(t)

pg.plot(t,y)
pg.show()
