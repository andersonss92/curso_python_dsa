# -*- coding: utf-8 -*-
"""trabalhando-com-arquivos-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SBZWhRHGQkMn8WPfgHis9Otegnni6qmN

Automatizando o processo de gravação.
"""

fileName = input("Digite o nome do arquivo: ")

fileName = fileName + ".txt"

arq3 = open(fileName,"w")

arq3.write("Incluindo texto no arquivo criado.")

arq3.close()

arq3 = open(fileName, "r")

print(arq3.read())

arq3.close()

"""Abrindo um dataset em uma única linha"""

f = open("/arquivos-dsa/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

print(rows)

"""Contando as linhas do arquivo."""

f = open("/arquivos-dsa/salarios.csv", "r")

data = f.read()

rows = data.split("\n")

full_data = []

for row in rows:
  split_row = row.split(",")
  full_data.append(split_row)

count = 0
for row in full_data:
  count += 1 # é a mesma coisa que count = count + 1

print(count)

# Contando o número de colunas do arquivo

f = open("/arquivos-dsa/salarios.csv")
data = f.read()
row = data.split('\n')
full_data = []

for  row in rows:
  split_row = row.split(',')
  full_data.append(split_row)
  first_row = full_data[0]
count = 0

for column in first_row:
  count = count + 1

print(count)

"""Gravando arquivo pelo Jupyter Notebook"""

arq4 = open("/arquivos-dsa/teste.txt", "r")

arq4.read()

arq4.read()

arq4.seek(0)

arq4.seek(0)
arq4.readlines()

# Podemos usar o loop for para ler o arquivo

for line in open("/arquivos-dsa/teste.txt", "r"):
  print(line)

import pandas as pd
pd.__version__

file_name = "/arquivos-dsa/bynari.csv"

df = pd.read_csv(file_name)

df.head()

file2 = "/arquivos-dsa/salarios.csv"

df2 = pd.read_csv(file2)

df2.head()