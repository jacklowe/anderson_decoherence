# anderson_decoherence

Since Anderson localisation (https://en.wikipedia.org/wiki/Anderson_localization) is a quantum effect it relies on quantum coherence, this project analyses what happens to such localised states when coherence is lost i.e. under decoherence/dephasing. The aim is therefore to evolve the system in a non-unitary manner.

Specifically the module (anderson_decoherence.py) contains a class of an Anderson localised system with methods that construct the Hamiltonian, diagonalise the Hamiltonian to obtain and plot ground state. 

May add methods that perform statistics over an ensemble of ground states to analyse effects of changing parameters in Hamiltonian e.g. disorder strength W and those that evolve system in a non-unitary way thus introducing decoherence. 

# Background

The Hamiltonian may be written 

<a href="https://www.codecogs.com/eqnedit.php?latex=H&space;=&space;\sum_i\(&space;\epsilon_i&space;|i><i|&space;&plus;&space;\mu|i&plus;1><i|&space;&plus;&space;\mu|i><i&plus;1|\)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H&space;=&space;\sum_i\(&space;\epsilon_i&space;|i><i|&space;&plus;&space;\mu|i&plus;1><i|&space;&plus;&space;\mu|i><i&plus;1|\)" title="H = \sum_i\( \epsilon_i |i><i| + \mu|i+1><i| + \mu|i><i+1|\)" /></a>

which can be represented as an i dimensional square matrix with energies on the diagonal and hopping elements on the off-diagonal representing transport from site i to i+1 etc.

We distribute the energy levels according to

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\epsilon_i)&space;=&space;\frac{1}{W}\Theta(W-\frac{\epsilon_i}{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\epsilon_i)&space;=&space;\frac{1}{W}\Theta(W-\frac{\epsilon_i}{2})" title="P(\epsilon_i) = \frac{1}{W}\Theta(W-\frac{\epsilon_i}{2})" /></a>

i.e. a flat distribution. We can also use a Gaussian distribution

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\epsilon_i)&space;=&space;\frac{1}{\sqrt{2\pi\sigma^2}}\exp{(-\epsilon_i^2/2\sigma^2)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\epsilon_i)&space;=&space;\frac{1}{\sqrt{2\pi\sigma^2}}\exp{(-\epsilon_i^2/2\sigma^2)}" title="P(\epsilon_i) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp{(-\epsilon_i^2/2\sigma^2)}" /></a>

note that W and the standard deviation here represent the disorder strength in the system. This can be viewed heuristically as the amount of randomness in the system. The higher the disorder strength the more sharply localised the states are in space. If the disorder strength is too large, when evolved the eigenstate may not spread at all and remain localised.

This is interesting because the eigenstates are *localised*, i.e. under unitary transformations such as evolution in time the eigenstate does not move. For dimensions less than 3 P.W. Anderson showed *all* eigenstates of the system are localised. Here we work in d=1 so all our eigenstates are localised.  

# Non-unitary evolution

Typically in quantum mechanics we are interested in unitary evolution in time. I.e. that given by the Schroedinger equation. However in this case since our state is temporally and spatially localised the Schroedinger equation evolution has no effect on the eigenstate (they commute). 

Evolution given by the Schroedinger equation preserves quantum-coherence. We are interested in the situation where such coherence is lost. Typically this is viewed as a coupling between the system and environment and may be viewed as a quantum-to-classical transition.

How do we represent this non-unitary time evolution here?
