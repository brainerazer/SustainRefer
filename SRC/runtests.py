#!/usr/bin/python3

import itertools
import gensafeprime
import subprocess
import shlex

from math import ceil, log, exp

BITS = [50, 55, 60]
CONFS = {'1': 'hostfile_1', '2': 'hostfile_2', '4': 'hostfile_4'}
BOUND_FACTORS = [1, 2, 4, 8, 16]

COMMANDLINE = "mpirun --hostfile {} -np {} ./bachelor_main {} {} {}"

def L(a,c,N):
    z = ceil(exp(c*log(N) ** a*log(log(N)) ** (1-a)))
    if z % 2:
        z += 1
    return ceil(z)

for bits, factor in itertools.product(BITS, BOUND_FACTORS):
    prime = gensafeprime.generate(bits)
    default_bound = L(0.5, 0.5, prime)
    for workers, hostfile in CONFS.items():
        cmdline = COMMANDLINE.format(hostfile, workers, bits, prime, ceil(factor * default_bound))
        print("---------------------------------")
        print('# ', cmdline)
        out = subprocess.check_output(shlex.split(cmdline), universal_newlines=True)
        print(out)
        print("---------------------------------")
        print()
        with open('out_{}_{}_{}'.format(bits, workers, factor), 'w') as f:
            f.write(out)