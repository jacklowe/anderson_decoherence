# anderson_decoherence

Since Anderson localisation is a quantum effect it relies on quantum coherence, therefore this project analyses what happens to such localised states when coherence is lost i.e. under decoherence/dephasing.

Specifically the module contains a class of Anderson localised system with methods that construct the Hamiltonian, diagonalise the Hamiltonian to obtain and plot ground state. 

Will add methods that perform statistics over an ensemble of ground states to analyse effects of changing parameters in Hamiltonian e.g. disorder strength W and those that evolve system in a non-unitary way thus introducing decoherence. 

The Hamiltonian may be written 

<a href="https://www.codecogs.com/eqnedit.php?latex=H&space;=&space;\sum_i\(&space;\epsilon_i&space;|i><i|&space;&plus;&space;\mu|i&plus;1><i|&space;&plus;&space;\mu|i><i&plus;1|\)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H&space;=&space;\sum_i\(&space;\epsilon_i&space;|i><i|&space;&plus;&space;\mu|i&plus;1><i|&space;&plus;&space;\mu|i><i&plus;1|\)" title="H = \sum_i\( \epsilon_i |i><i| + \mu|i+1><i| + \mu|i><i+1|\)" /></a>
