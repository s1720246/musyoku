#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 03:32:51 2018

@author: ks
"""

# setup the matplotlib graphics library and configure it to show figures inline in the notebook
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# make qutip available in the rest of the notebook
from qutip import *

# Problem parameters
wc = 1.0  * 2 * np.pi  # cavity frequency
wa = 1.0  * 2 * np.pi  # atom frequency
g  = 1.0  * 2 * np.pi # coupling strength
ga = 1.0  * 2 * np.pi

N = 5            # number of cavity fock states
use_rwa = False

# Set up the operators and the Hamiltonian
# operators
a    = tensor(destroy(N), qeye(2))
sm  = tensor(qeye(N), destroy(2))


na  = tensor(qeye(N), sigmaz())        # atom
nc  = tensor(destroy(N).dag() * destroy(N), qeye(2))   # cavity

# decoupled Hamiltonian
H0 = wc * nc + wa * na

# interaction Hamiltonian
if use_rwa:
    H1 = (a.dag() * sm + a * sm.dag())
else:
    H1 = (a.dag() + a) * (sm + sm.dag())
    
H = H0 + g * H1
p_energy, p_eigenstate = H.eigenstates()

# time list
#tlist = np.linspace(0, 10, 1001) * 2.0*np.pi

# diagonalized H
#diag_H = qdiags(full_energy, 0)

#-------------------------------

# parity oprtor of pol
parity_op = -tensor(((0+np.pi*1j)*destroy(N).dag() * destroy(N)).expm(), sigmaz())

# parity はんべつ

parity_op * full_eigenstate[0] + full_eigenstate[0]






