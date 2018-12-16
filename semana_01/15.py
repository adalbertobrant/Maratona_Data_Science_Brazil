# -*- coding: utf-8 -*-
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$
#
#     Obs.: Salário Bruto - Descontos = Salário Líquido.

G_H,N_H = input("Qual o valor que você ganha por hora e quantas horas de trabalho faz no mês? ").split(" ")
G_H = float(G_H)
N_H = float(N_H)
Salario_Bruto = G_H * N_H
IR = Salario_Bruto * 11/100
INSS = Salario_Bruto * 8/100
SIND = Salario_Bruto * 5/100
Salario_Liquido = Salario_Bruto - IR -INSS -SIND


print("\n+ Salário Bruto : R$ {0:.2f}\n  - IR (11%) : R$ {1:.2f}\n  - INSS (8%) : R$ {2:.2f}\n  - Sindicato ( 5%) : R$ {3:.2f}\n= Salário Liquido : R$ {4:.2f}".format(Salario_Bruto,IR,INSS,SIND,Salario_Liquido))



