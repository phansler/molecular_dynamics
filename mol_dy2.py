# Overview file

#import python classes
import numpy as np
import random as rn
import math

#import self produced classes
import forcemodule as fm
import initialmomenta as im
import initialpositionAD as ipAD
import initialpositionP as ipP

# independent parameters
dt = 1
l = 1.
N=32
gs = l*N**-(1./3.)
lpnum = 100
a=1

ICll = im.im(N)
partl,forces,ynum,xnum,znum = ipAD.ip(N,gs,l)
partl = ipP.ip(N,a)

print partl

# Updating postion, making use of force calculator

'''
for lp in range(lpnum):
	#print partl[0]
	forces = fm.calc_forces(partl,forces)
	for i in range(len(partl)):
		for z in range(3):
			partl[i][z] = partl[i][z] + ICll[i][z]*dt + (forces[i][z]/2)*dt**2
			ICll[i][z] = ICll[i][z] + forces[i][z]*dt
 '''

#print part_t,'=partt',len(part_t), partl,'=partl',len(partl)
