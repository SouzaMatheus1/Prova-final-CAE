array = []

#Matriz generator
def gerar_matriz(col):
  matriz = []
  pos = 0
  for i in range(6):
    lis_lin = []
    for i in col:
      i += pos
      lis_lin.append(i)
    pos += 1
    matriz.append(lis_lin)
  return matriz

#Array size
tam_list = int(input('Digite o tamanho da lista: '))
if tam_list < 5:
    #Min size - 5
  print('O tamanho minímo da lista é 5!')
else:
    #Show array size
  print(f'O tamanho da lista é: {tam_list}')
  for i in range(tam_list):
    numero = int(input('Insira um número entre 10 e 35 na lista: '))
    if numero < 10 or numero > 35:
      print('Valor inválido, tente novamente!')
      break
    else:
      array.append(numero)
      #Show the insert confirmation
      print(f"Número {numero} adicionado!")
  

#Show array
print('Array: ')
print(array)
matriz = gerar_matriz(array)

#Show matriz
print("Matriz: ")
for i in matriz:  
  print(i)
