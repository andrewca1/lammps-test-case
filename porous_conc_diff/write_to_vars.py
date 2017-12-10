import os.path
from pyDOE import * # To use Latin-Hypercube
from scipy.stats.distributions import norm
import numpy as np

# File name
fname = "vars.lmp"

# mean, dA, dB, dC, k
means = [2.0e-4, 2.0e-4, 2.0e-4, 2.0e-2]
stds = [1.0e-5, 1.0e-5, 1.0e-5, 1.0e-3]

# Generate design samples
N = 200
design = lhs(4, samples = N)

for i in range(4):
    # Transform into normal distributions with means and variance as above
    design[:, i] = norm(loc=means[i], scale=stds[i]).ppf(design[:,i])

# Create list to store results
cC_results = []
    
# Loop through each row to run LAMMPS code
for i in range(N):
    # Generate the string
    out_str = "variable dA equal {} \n variable dB equal {} \n variable dC equal {} \n variable k equal  {} \n".format(design[i,0], design[i,1], design[i,2], design[i,3])

    # If file exist, remove file
    if (os.path.isfile(fname)):
        os.remove(fname)
    
    # Write string to file
    text_file = open(fname, "w")
    text_file.write(out_str)
    text_file.close()

    # Check if output exists
    if (os.path.isfile("dump.last.xs")):
        os.remove("dump.last.xs")
    if (os.path.isfile("dump.last")):
        os.remove("dump.last")
    
    # Run LAMMPS
    os.system("./run.sh")

    # Read the output file
    out_data = np.loadtxt("dump.last.xs", skiprows=9)
    # Get the summation of the C concentration
    cC_results.append(np.mean(out_data[:,7]))

    # Some meaningless output
    print("JUST FINISHED {}!!!!!!!!!!!!!!\n".format(i))
    
# Save output
header_str = "DA,DB,DC,k,Cc"
L = np.c_[design, cC_results]
np.savetxt('uq.csv', L, delimiter=',', header=header_str)

