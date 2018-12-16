# -*- coding: utf-8 -*-

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7

Altura,Sexo = input("Olá, Entre a sua altura e seu sexo no seguinte formato\n Altura = x.xx  e sexo = F ou M\n Altura e sexo : ").split(" ")
Altura = float(Altura)
if Sexo == "F":
    print("Olá minha amiga seu peso ideal é = {0:.2f} Kg".format((62.1*Altura)-44.7))
elif Sexo =="M":
    print("Olá amigo seu peso ideal é = {0:.2f} Kg".format((72.7 * Altura) - 58))
else:
    print("Digite apenas F ou M para o sexo\n")
    Sexo = input("Entre o seu Sexo novamente: ")
    if Sexo == "F":
        print("Olá minha amiga seu peso ideal é = {0:.2f} Kg".format((62.1 * Altura) - 44.7))
    elif Sexo == "M":
        print("Olá amigo seu peso ideal é = {0:.2f} Kg".format((72.7 * Altura) - 58))
