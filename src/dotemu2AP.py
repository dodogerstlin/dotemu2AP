#!/bin/python3


import numpy as np
import glob

def sfix(infile):
  data = np.fromfile(infile, dtype='b')
  filelen = len(data)
  data = data.reshape((int(filelen/32), 32))
  outdata=np.zeros_like(data)
  for j in np.arange(8):
    outdata[:, j+16] = data[:, 4*j+0]
    outdata[:, j+24] = data[:, 4*j+1]
    outdata[:, j+ 0] = data[:, 4*j+2]
    outdata[:, j+ 8] = data[:, 4*j+3]
  return outdata.flatten()
  
sfixfile = glob.glob('*_game_sfix')[0]
sfixdata = sfix(sfixfile)
sfixdata.tofile("srom")
