import numpy as np
import itertools


def TTC(preferences,ownership):
    if (len(preferences) != len(ownership)):
        return -1

    mostPrefered = preferences[0,:]

    happilyOwned = ownership[ownership == mostPrefered]

    while len(happilyOwned)<len(ownership):
        mostPrefered = updateMostPrefered(mostPrefered,ownership,happilyOwned,preferences)

        ownership = updateOwnership(mostPrefered,ownership)

        happilyOwned = ownership[ownership == mostPrefered]

    return(ownership)

def updateMostPrefered(mostPrefered,ownership,happilyOwned,preferences):
        for i in range(len(mostPrefered)):
            if(mostPrefered[i] != ownership[i]):
                mostPrefered[i] = preferences[np.invert(np.isin(preferences[:,i],happilyOwned)),i][0]
        return(mostPrefered)

def updateOwnership(mostPrefered,ownership):
        for i in range(1,len(ownership)+1):
            listo = list(itertools.combinations(ownership,i))
            for j in listo:
                j = np.array(j)
                ownership[j] = identify_Cycles(mostPrefered[j],ownership[j])
        return(ownership)

def identify_Cycles(mostPreferedIdx,ownershipIdx):
    if (np.sort(mostPreferedIdx) == ownershipIdx).all():
        ownershipIdx = mostPreferedIdx
    return(ownershipIdx)
