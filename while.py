# -*- coding: utf-8 -*-
"""while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RS2fkLK6x1_pGIqKDKDGCK7Ujm0LfSUv
"""

# usando o loop while para imprimir os numeros de 0 a 9:
counter = 0
while counter <10:
  print(counter)
  counter = counter + 1

# Também é possível usar a claúsula else para encerrar o loop while
x=0
while x<10:
  print('O valor de x nessa iteração é: ', x)
  print(' x ainda é menor que 10, somando 1 a x.')
  x += 1

else:
  print('Loop concluído!')

"""Pass, break e Continue"""

counter=0
while counter <100:
  if counter==4:
    break
  else:
    pass
  print(counter)
  counter = counter+1

for verificador in 'Python':
  if verificador == 'h':
    continue
  print(verificador)

# while e for juntos
for i in range(2,30):
  j = 2
  counter = 0
  while j < i:
    if i % j == 0:
      counter = 1
      j = j + 1
    else:
      j = j + 1
  if counter == 0:
    print(str(i) + " é um número primo.")
    counter = 0
  else:
    counter = 0