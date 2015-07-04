from __future__ import print_function, division
import numpy as np
from scipy.misc import imsave

def spiral(Rows=400, Col=400, p=1):
  im = np.zeros([Rows,Col])
  x0, y0 = Rows/2, Col/2
  try:
    for theta in np.linspace(0,360,1000):
      p = p + p*theta/360
      im[int(x0+p*np.cos(theta)), int(y0+p*np.sin(theta))] = 255
  except: pass
  imsave('1.jpg', im)

if __name__=='__main__':
  spiral(Rows=400, Col=400)