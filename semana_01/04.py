# -*- coding: utf-8 -*-

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = input ("Entre 4 notas bimestrais ").split()
soma = 0
i = 0
while i<4:
    soma = float(soma) + float(notas[i])
    print(soma)
    i = i+1
media = soma/i
print ("\nNota da prova 1ª = {0}\nNota da prova 2ª = {1}\nNota da prova 3ª = {2}\nNota da prova 4ª = {3}\n\nMedia Geral= {4:.2f}".format(notas[0],notas[1],notas[2],notas[3],media))