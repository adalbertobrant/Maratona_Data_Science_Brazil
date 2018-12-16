# -*- coding: utf-8 -*-

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

Ganho_Hora,Numero_Horas = input("Qual o valor que você ganha por hora e quantas horas de trabalho faz no mês? ").split(" ")
Ganho_Hora = float(Ganho_Hora)
Numero_Horas = float(Numero_Horas)
print("Você trabalhou {0} horas e ganhou R$ {1:.1f} no mês, Viva  \o/".format(Numero_Horas, Ganho_Hora*Numero_Horas))
print("                                                          |")
print("                                                          /\\")
