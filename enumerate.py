# -*- coding: utf-8 -*-
"""enumerate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hNNskaeotA0Qdr6rzi4zrPtE6Sp9BJF2

Enumerate
"""

# cria lista.
seq = ['a','b','c']

enumerate(seq)

list(enumerate(seq))

# Imprimi os valores de  uma lista usando enumerate() e os seus respectivos indices.
for indice, valor in enumerate(seq):
  print(indice, valor)

for indice, valor in enumerate(seq):
  if indice >= 2:
    break
  else:
    print(indice, valor)

lista = ['Marketing', 'Tecnologia','Business']

for i, item in enumerate(lista):
  print(i, item)

for i, item in enumerate('Isso é uma String'):
  print(i, item)

for i, item in enumerate(range(10)):
  print(i, item)