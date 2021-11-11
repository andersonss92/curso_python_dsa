# -*- coding: utf-8 -*-
"""if-elif-else.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bze50AhnCZEaxb3DVxKzGWw2JDBiRvz0
"""

# Condicional If
if 5 > 2:
  print("Python funciona!")

# If e Else
if 5 > 2:
  print("Python funciona!")
else:
  print("Algo está errado.")

6 > 3

3 > 7

4 < 8

4 >= 4

if 5 == 5:
  print("Testando Python!")

if True:
  print("Parece que Python funciona.")

# Atenção com a sintaxe.
if 4 > 3:
  print("Tudo funciona.")

"""Condicionais Aninhadas"""

idade = 18
if idade > 17:
  print("Você já pode dirigir!")

nome = "Bob"
if idade > 13:
  if nome == "Bob":
    print("Ok, Bob! Você está autorizado a entrar")
  else:
    print("Desculpe! Você não pode entrar.")

nome = "Bob"
idade = 13
if idade >= 13 and nome == "Bob":
  print("Ok, Bob! Você está autorizado a entrar.")

idade = 12
nome = "Bob"
if (idade >= 13) or (nome == "Bob"):
  print("Ok, Bob! Você está autorizado a entrar.")

"""Elif:"""

dia = "terça"
if dia =="segunda":
  print("Hoje fará sol.")
else:
  print("Hoje vai chover.")

if dia == "Segunda":
  print("Hoje fará sol!")
elif dia == "Terça":
  print("Hoje vai chover.")
else:
  print("Sem previsão do tempo para o dia selecionado")

"""Operadores Lógicos"""

idade = 18
nome = "Anderson"
if idade > 17:
  print("Você pode dirigir.")

idade = 18
if idade > 17 and nome == "Anderson":
  print("Autorizado!")

# Usando mais de uma condição na cláusula if:

disciplina = input("Digite o nome da disciplina: ")
nota_final = input("Digite a nota final (entre 0 e 100): ")

if disciplina == "Geografia" and nota_final >= "70":
  print("Você foi aprovado!")
else:
  print("Lamento, acho que você precisa estudar mais!")