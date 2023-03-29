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
  
####### TODO
#### check out http://i486.mods.jp/neogeo/tiles2crom.txt

	# for (i = 0; i < length; i += 0x80)
	# {
		# int y;
		# for (y = 0; y < 0x10; y++)
		# {
			# DWORD dstData = 0;
			# int x;
			# dstData = newSprites[i+(y*8)] + (newSprites[i+1+(y*8)]<<8) + (newSprites[i+2+(y*8)]<<16) + (newSprites[i+3+(y*8)]<<24);
			# for (x = 0; x < 8; x++)
			# {
				# if((dstData >> (x*4+3)) & 0x01) src[(i+0x43) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+2)) & 0x01) src[(i+0x41) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+1)) & 0x01) src[(i+0x42) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+0)) & 0x01) src[(i+0x40) | (y << 2)] |= (1 << x);
			# }
			# dstData = newSprites[i+4+(y*8)] + (newSprites[i+5+(y*8)]<<8) + (newSprites[i+6+(y*8)]<<16) + (newSprites[i+7+(y*8)]<<24);
			# for (x = 0; x < 8; x++)
			# {
				# if((dstData >> (x*4+3)) & 0x01) src[(i+0x03) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+2)) & 0x01) src[(i+0x01) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+1)) & 0x01) src[(i+0x02) | (y << 2)] |= (1 << x);
				# if((dstData >> (x*4+0)) & 0x01) src[(i+0x00) | (y << 2)] |= (1 << x);
			# }
		# }
	# }  
def tiles(infile, outfile="crom0"):
  data = np.fromfile(infile, dtype='b')
  filelen = len(data)
  outdata = np.zeros_like(data)
  dlen = 128
  for i in np.arange(int(filelen/dlen))*dlen:
    tmp = np.zeros(dlen)
    for y in np.arange(int(dlen/8)):
      dstData = data[i+(y*8)+0] <<  0 | data[i+(y*8)+1] <<  8 | data[i+(y*8)+2] << 16 | data[i+(y*8)+3] << 24
  outdata.flatten().tofile(outfile)
  return outdata.flatten()
  
  
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

