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
dt = 0.001
N=4
lpnum = 100
a=1
l = ((N/4)**(1./3.))*2*a
gs = l*N**-(1./3.)



ICll = im.im(N) #np.zeros((N,3),dtype = float)
#partlf,forces,ynum,xnum,znum = ipAD.ip(N,gs,l)
partl,forces = ipP.ip(N,a)

#print partl

# Updating postion, making use of force calculator


for lp in range(lpnum):
	print partl[0]
	#print ICll[0]
	forces = fm.calc_forces(partl,forces,l)
	#print forces[0]
	for i in range(len(partl)):
		for z in range(3):
			ICll[i][z] = ICll[i][z] + forces[i][z]*dt
			#print ICll[i][z]
			partl[i][z] = partl[i][z] + ICll[i][z]*dt #+ #0*(forces[i][z]/2)*dt**2
			#print partl[i][z]
			while partl[i][z] < -l/2:
				partl[i][z] = partl[i][z] + l
				#print 'while1'
			while partl[i][z] > l/2:
				partl[i][z] = partl[i][z] - l
				#print 'while2'
			#print 'here'
			
print range(len(partl))

#print part_t,'=partt',len(part_t), partl,'=partl',len(partl)
