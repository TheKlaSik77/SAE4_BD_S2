#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

"""
Prends en paramètre une liste de données
"""
def moyenne(data):   
    n = len(data)
    moy = np.sum(data)/n
    return moy

def variance(data):  
    l = []
    for i in data:
        l.append(i*i)
    var = moyenne(l) - moyenne(data)**2
    return var

def ecartType(data):
    
    return np.sqrt(variance(data))


def visu_histo(data, s):
    moy = moyenne(data)
    sig = ecartType(data)
    # visualisation de l'histogramme :
    plt.figure()
    plt.hist(data, bins=20, density=True, edgecolor='k')
    plt.title('histogramme de %s , moy = %1.3f,  $\sigma$ = %1.3f' \
              % (s, moy, sig))
        
        
def recupererListeDataParLigne(ligne):
    
    fichier = open('fichier_28',"r")
    line = fichier.readline()
    listelignes = []
    
    while line:
        listelignes.append(line)
        line = fichier.readline()
    

    
    data = listelignes[ligne - 1]
    data = data.split(";")
    
    data = [float(d) for d in data]
    
    fichier.close()
    
    return data
    
    
data = recupererListeDataParLigne(0)

print("Moyenne : " + str(moyenne(data)))
print("Ecart-Type : " + str(ecartType(data)))
visu_histo(data, 'X')
