import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
# from scipy.linalg import expm
# import scipy.sparse.linalg


class LocalisedSystem():
    ''' Anderson localised system with variables

    sites: number of sites in the system

    disorder: strength of disorder in the system, i.e. the average
    value of the diagonal elements (energy levels). These will be randomised.

    off_diags_magnitude: magnitude of the off-diagonal elements of the
    Hamiltonian, e.g. larger magnitude encourages transport of particles across
    sites.'''

    def __init__(self, sites=200, disorder=1, off_diags_magnitude=1):
        self.sites = sites
        self.disorder = disorder
        self.off_diags_magnitude = off_diags_magnitude

    def make_hamiltonian(self):
        """ Produces Hamiltonian of system. I.e. makes a (sites*sites)
        dimension matrix with randomised energy levels across the diagonal and
        the off-diagonal elements offset by 1 either side of the diagonal."""
        Ham = sp.sparse.lil_matrix((self.sites, self.sites), dtype=np.complex128)
        for i in range(self.sites):
            Ham[i, i] = np.random.rand(1, self.sites)[0, i]
            if i == 0:
                Ham[i, i + 1] = self.off_diags_magnitude
            elif i == self.sites - 1:
                Ham[i, i - 1] = np.conjugate(self.off_diags_magnitude)
            else:
                Ham[i, i + 1] = self.off_diags_magnitude
                Ham[i, i - 1] = np.conjugate(self.off_diags_magnitude)
        return Ham.tocsc()

    def find_low_energy_states(self):
        ''' Finds ground state and excited state of the system using an
        efficient algorithm on sparse matrix. Returns tensor of form T_ijk
        where i refers to energy number, and j, k indexes refer to the matrix
        of eigenvectors'''
        return sp.sparse.linalg.eigsh(self.make_hamiltonian(), k=2,
                                      sigma=-4, which='LM')

    def select_energies(self):
        '''Returns the energies of the lowest two energy levels'''
        return self.find_low_energy_states()[0]

    def select_eigenstates(self):
        '''Returns the eigenstates/kets of the lowest two energy levels'''
        return self.find_low_energy_states()[1]

    def select_ground_state(self):
        ''' Selects state with lowest energy i.e. ground state'''
        k = 1
        ind = np.argpartition(self.find_low_energy_states()[0], k)[:k]
        return ind

    def ground_state_ket(self):
        z = np.linspace(0, self.sites - 1, self.sites, dtype=int)
        return self.select_eigenstates()[z, self.select_ground_state()]

    def plot_ground_state(self):
        x = np.linspace(0, self.sites - 1, self.sites, dtype=int)
        plt.plot(x, np.real(self.ground_state_ket()) *
                 np.conjugate(self.ground_state_ket()))
        plt.show()
