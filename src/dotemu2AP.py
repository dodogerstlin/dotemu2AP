#!/bin/python3


import numpy as np
import glob

def sfix(infile, outfile="srom"):
  data = np.fromfile(infile, dtype='b')
  filelen = len(data)
  data = data.reshape((int(filelen/32), 32))
  outdata = np.zeros_like(data)
  dlen = 8
  outdata[:, 16:16+8] = data[:, 0::4]
  outdata[:, 24:24+8] = data[:, 1::4]
  outdata[:, 0:0+8] = data[:, 2::4]
  outdata[:, 8:8+8] = data[:, 3::4]
  outdata.flatten().tofile(outfile)
  return outdata.flatten()
  

def z80(infile, outfile="m1rom"):
  data = np.fromfile(infile, dtype='b')
  outdata = data
  outdata.flatten().tofile(outfile)
  return outdata.flatten()
  

def m68k(infile, outfile="prom"):
  data = np.fromfile(infile, dtype='b')
  outdata = data
  outdata.flatten().tofile(outfile)
  return outdata.flatten()
  
  
def adpcm(infile, outfile="vroma0"):
  data = np.fromfile(infile, dtype='b')
  outdata = data
  outdata.flatten().tofile(outfile)
  return outdata.flatten()
  

 
## translated from js taken from cxx https://gist.github.com/cxx/81b9f45eb5b3cb87b4f3783ccdf8894f ################################################################################
def tiles(infile, outfile="crom0"):
  data = np.fromfile(infile, dtype='>u1')
  filelen = len(data)
  
  dlen = 128

  outdata = np.copy(data)

  for i in (np.arange(int(filelen/0x80))*0x80):

    tmp = np.zeros(dlen, dtype=int)

    for y in np.arange(0x10):
      dstData = data[i+(y*8)+0] <<  0 | data[i+(y*8)+1] <<  8 | data[i+(y*8)+2] << 16 | data[i+(y*8)+3] << 24
      
      for x in np.arange(int(8)):
        tmp[0x43 | y << 2] |= (dstData >> x*4+3 & 1) << 7-x
        tmp[0x41 | y << 2] |= (dstData >> x*4+2 & 1) << 7-x
        tmp[0x42 | y << 2] |= (dstData >> x*4+1 & 1) << 7-x
        tmp[0x40 | y << 2] |= (dstData >> x*4+0 & 1) << 7-x

      dstData = data[i+(y*8)+4] <<  0 | data[i+(y*8)+5] <<  8 | data[i+(y*8)+6] << 16 | data[i+(y*8)+7] << 24
      
      for x in np.arange(int(8)):
        tmp[0x03 | y << 2] |= (dstData >> x*4+3 & 1) << 7-x
        tmp[0x01 | y << 2] |= (dstData >> x*4+2 & 1) << 7-x
        tmp[0x02 | y << 2] |= (dstData >> x*4+1 & 1) << 7-x
        tmp[0x00 | y << 2] |= (dstData >> x*4+0 & 1) << 7-x
    outdata[i:i+dlen] = np.copy(tmp)
		
  outdata.flatten().tofile(outfile)
  return outdata.flatten()

# def tiles(infile, outfile="crom0"):
  # data = np.fromfile(infile, dtype='>u1')
  # filelen = len(data)
  # # data = data.reshape((int(filelen/0x80), 0x80))
  # data = data.reshape((0x80, int(filelen/0x80)))
  # dlen = 128

  # outdata = np.zeros_like(data)

  # for y in np.arange(0x10):
    # dstData = data[:, (y*8)+0] <<  0 | data[:, (y*8)+1] <<  8 | data[:, (y*8)+2] << 16 | data[:, (y*8)+3] << 24
  
  # for x in np.arange(int(8)):
    # outdata[:, 0x43 | y << 2] |= (dstData >> x*4+3 & 1) << 7-x
    # outdata[:, 0x41 | y << 2] |= (dstData >> x*4+2 & 1) << 7-x
    # outdata[:, 0x42 | y << 2] |= (dstData >> x*4+1 & 1) << 7-x
    # outdata[:, 0x40 | y << 2] |= (dstData >> x*4+0 & 1) << 7-x

  # dstData = data[:, (y*8)+4] <<  0 | data[:, (y*8)+5] <<  8 | data[:, (y*8)+6] << 16 | data[:, (y*8)+7] << 24
  
  # for x in np.arange(int(8)):
    # outdata[:, 0x03 | y << 2] |= (dstData >> x*4+3 & 1) << 7-x
    # outdata[:, 0x01 | y << 2] |= (dstData >> x*4+2 & 1) << 7-x
    # outdata[:, 0x02 | y << 2] |= (dstData >> x*4+1 & 1) << 7-x
    # outdata[:, 0x00 | y << 2] |= (dstData >> x*4+0 & 1) << 7-x
	
  # outdata.flatten().tofile(outfile)
  # return outdata.flatten()
    
  
sfixfile = glob.glob('*_game_sfix')[0]
sfix(sfixfile)
  
z80file = glob.glob('*_game_z80')[0]
z80(z80file)
  
m68kfile = glob.glob('*_game_m68k')[0]
m68k(m68kfile)
  
adpcmfile = glob.glob('*_adpcm')[0]
adpcm(adpcmfile)
  
tilefile = glob.glob('*_tiles')[0]
tiles(tilefile)

