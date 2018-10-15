
from TTC import TTC,updateMostPrefered,updateOwnership,identify_Cycles
import numpy as np
import itertools

num_agents = 5

preferences = np.ones((num_agents,num_agents))

for i in range(len(preferences)):
    listo = np.array(range(len(preferences)))
    np.random.shuffle(listo)
    preferences[:,i] = listo

listo = np.array(range(len(preferences)))
np.random.shuffle(listo)
ownership = np.array(range(len(preferences)))

print("Preferences Matrix: ")
print(preferences)
print("Initial Ownership: ")
print(ownership)
print("Optimized Ownership: ")
print(TTC(preferences,ownership))
