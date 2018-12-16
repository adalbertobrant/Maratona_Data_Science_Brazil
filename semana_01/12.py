# -*- coding: utf-8 -*-

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

Altura = float(input("Entre a sua Altura em metros x.xx = "))
print("Seu peso ideal é {0:.2f} kilos".format((72.7*Altura)-58))