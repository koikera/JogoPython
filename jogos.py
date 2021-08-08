# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:32:54 2021

@author: legen
"""
import adivinhacao
import Forca

print("*****************************")
print("*****Escolha o seu jogo******")
print("*****************************")

print("(1) Forca (2) Adivinhacao")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    Forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhacao")
    adivinhacao.jogar()