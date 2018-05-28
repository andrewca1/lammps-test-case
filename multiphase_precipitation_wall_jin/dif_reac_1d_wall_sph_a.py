import matplotlib.pyplot as plt
import numpy as np
import math

l = 1
n_eq = 32
h = l/n_eq
dx = h/4
rho = 1
m_0 = rho * dx**2
rho_m = m_0 * n_eq

dif = 1
k = 0.001

l_prime = 1
s_0 = 1
c_0 = 0.008
c_eq = 0.001

t = np.linspace(0,10000,10000)

# analytic solution to 1-d diffusion problem (moving reactive surface) [Tartakovsky, 2007]
s_t = (dif/k + l_prime) - np.sqrt((dif/k + l_prime - s_0)**2 - 2*dif*(c_0 - c_eq)*t/rho_m)

plt.plot(t,s_t,label='analytical')



# nfreq_s = input("Enter nfreq: ")
# nfreqfin_s = input("Enter last: ")

nfreq = 1000 #int(nfreq_s)
nfreqfin = 10000 #int(nfreqfin_s)

file_init = "dump."
file_end = ".dat"

fid = open(file_init+'0'+file_end,'r')

# Get number of atoms
for lines in range(0,4):
        num_atoms_s = fid.readline()
        
fid.close()
num_atoms = int(num_atoms_s)

x_dis =  []
t1 = []
curArr = []

# Loop over the dump files
for i in range (0,int(nfreqfin/nfreq)+1):
        x_dis.append([])
        t1.append([])
        x_dis[i] = 0.0
        t1[i] = nfreq*i
                
        tstep = str(i*nfreq)
        file_str = file_init+tstep+file_end
        curArr = np.loadtxt(file_str,skiprows=9)
                
        # Loop over the atoms in each dump file
        for j in range(0,num_atoms-1):
                cur_id = curArr[j][1]
                cur_x_dis = 1.0 - curArr[j][2]
                
                # Find solid particles fartherest from edge
                if(cur_id == 2 and cur_x_dis > x_dis[i]):
                        x_dis[i] = n_eq*cur_x_dis



plt.plot(t1,x_dis,'o',label='lammps')
plt.xlabel('time')
plt.ylabel('front position, S')
plt.grid()
plt.legend()
#plt.show()
plt.savefig("comp.png")
                                    
