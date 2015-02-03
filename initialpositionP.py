#Finding intial positions according to the PERRY algorithm

import numpy as np

def ip(ynum,xnum,gs):
	part_t = []
	for k in range(ynum):
		for j in range(ynum):
			for i in range(xnum):
				partx = (gs/2)*(2*i + ((j+k)%2)) +0.15
				party = (gs/2)*(np.sqrt(3)*(j+(1./3.)*(k%2))) +0.15
				partz = (gs/2)*((2.*np.sqrt(6)/3.)*k) +0.15
				part=[partx,party,partz]
				part_t.append(part)
			
#print part_t

	return part_t
