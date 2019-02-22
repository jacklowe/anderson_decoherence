"""Module that implements Anderson localisation along with various methods,
mainly concerned with evolving the system non-unitarily."""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.sparse.linalg
from scipy.linalg import expm


class System():
    "System object that represents the Anderson localisation system."
    def __init__(self, sites=200, disorder=1, off_diags_magnitude=1):
        self.sites = sites
        self.disorder = disorder
        self.off_diags_magnitude = off_diags_magnitude

    def hamiltonian(self):
        """Produces Hamiltonian of system, which is a sites*sites
        dimensional matrix with randomised energy levels across the diagonal."""
        h_matrix = sp.sparse.lil_matrix((self.sites, self.sites),
                                        dtype=np.complex128)

        # Assigning the elements of the matrix manually
        for i in range(self.sites):
            h_matrix[i, i] = np.random.rand(1, self.sites)[0, i]
            if i == 0:
                h_matrix[i, i + 1] = self.off_diags_magnitude
            elif i == self.sites - 1:
                h_matrix[i, i - 1] = np.conjugate(self.off_diags_magnitude)
            else:
                h_matrix[i, i + 1] = self.off_diags_magnitude
                h_matrix[i, i - 1] = np.conjugate(self.off_diags_magnitude)
        return h_matrix.tocsc()

    def low_energy_states(self):
        """Finds ground and excited state of the system using an
        efficient algorithm on sparse matrix. Returns tensor T_ijk where i
        refers to energy number, and j, k indexes refer to the matrix
        of eigenvectors"""
        return sp.sparse.linalg.eigsh(self.hamiltonian(), k=2,
                                      sigma=-4, which='LM')

    def energies(self):
        "Returns the energies of the lowest two energy levels"
        return self.low_energy_states()[0]

    def eigenstates(self):
        "Returns the eigenstates/kets of the lowest two energy levels"
        return self.low_energy_states()[1]

    def ground_state_index(self):
        "Selects state with lowest energy i.e. ground state"
        return np.argpartition(self.low_energy_states()[0], 1)[:1]

    def ground_state_ket(self):
        "Constructs ground state ket/vector"
        return self.eigenstates()[:, self.ground_state_index()]

    def site_vector(self):
        "Makes site number vector for x vals when plotting"
        return np.linspace(0, self.sites - 1, self.sites, dtype=int)

    def plot_ground_state(self):
        "Plots ground state of anderson localised system"
        plt.plot(self.site_vector(), np.absolute(self.ground_state_ket()))
        plt.show()

    def density_matrix(self):
        "Constructs pure state density matrix of ground state"
        return sp.outer(np.conjugate(self.ground_state_ket()).T,
                        self.ground_state_ket())

    def delta_t(self, total=3, num_steps=30):  # put this in trotter decomp method
        "Returns small time-step interval delta_t"
        return total / num_steps

    def propagator(self):
        "Constructs unitary evolution operator (i.e. U = exp{-iHt})"
        return expm(-1j * self.hamiltonian() * self.delta_t()).toarray()

    def trotter_decomposition(self, decay_rate=0.1):
        "Construct matrix for trotter decomposition"
        alpha = [i * decay_rate for i in range(self.sites)]
        gamma = np.zeros((self.sites, self.sites))
        for i in range(self.sites):
            upper_diags = np.diag(np.ones(self.sites - i) *
                                  np.exp(-self.delta_t() * alpha[i]), i)
            gamma += upper_diags
            if i != 0:
                lower_diags = np.diag(np.ones(self.sites - i) *
                                      np.exp(-self.delta_t() * alpha[i]), -i)
                gamma += lower_diags
        return gamma

    def evolve_ground_state(self):
        "Evolve ground state with decoherence using trotter and propagator"
        pass

    def plot_evolution(self):
        "Show time evolution of state with decoherence visually"
        pass