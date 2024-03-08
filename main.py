def cpf_repetido(cpf):
  with open('pessoas.txt', 'r') as arquivo:
    for linha in arquivo:
      partes = linha.split(';')
      if cpf == partes[1]:
        return True
    return False

'''
nome
cpf
endereco
qntd telefones
telefones
'''
def inserir():
  nome = input("Nome: ")
  cpf = input("CPF: ")

  if cpf_repetido(cpf):
    print(f'\nERRO! CPF repetido.\nTente inserir "{nome}" novamente.\n')
    return

  endereco = input("Endereço: ")

  qntd_telefones = int(input("Quantos telefones inserir: "))
  telefones = []
  for i in range(qntd_telefones):
    tel = input(f'Telefone {i+1}: ')
    telefones.append(tel)

  with open('pessoas.txt', 'a') as arquivo:
    arquivo.write(f'{nome};{cpf};{endereco};{qntd_telefones};{telefones}\n')

  print("\nOperação realizada com sucesso.\n")

def listar():
  with open('pessoas.txt', 'r') as arquivo:
    conteudo = arquivo.read()

    if conteudo == "":
      print("Lista vazia!\n")
      return

    print("LISTA DE PESSOAS:\n" + '-'*30)
    for linha in conteudo.splitlines():
      partes = linha.split(';')

      print(f'Nome: {partes[0]}')
      print(f'CPF: {partes[1]}')
      print(f'Endereço: {partes[2]}')
      telefones_individuais = partes[4].strip('[]').replace("'", "").split(', ')
      for i in range(int(partes[3])):
        print(f'Telefone {i+1}: {telefones_individuais[i]}')
      print("-"*30)
      
  print("")

def buscar_cpf():
  cpf = input("Digite o CPF a ser procurado: ")
  print("")

  with open('pessoas.txt', 'r') as arquivo:
    for linha in arquivo:
      partes = linha.split(';')
      if cpf == partes[1]:
        print("PESSOA LOCALIZADA:\n" + '-'*30)
        print(f'Nome: {partes[0]}')
        print(f'CPF: {partes[1]}')
        print(f'Endereço: {partes[2]}')
        telefones_individuais = partes[4].strip('[]\n').replace("'", "").split(', ')
        for i in range(int(partes[3])):
          print(f'Telefone {i+1}: {telefones_individuais[i]}')
        print('-'*30 + "\n")
        return

  print("CPF não localizado.\n")


def buscar_telefone():
  tel = input("Digite o telefone a ser buscado: ")
  print("")

  with open('pessoas.txt', 'r') as arquivo:
    for linha in arquivo:
      partes = linha.split(';')
      telefones_individuais = partes[4].strip('[]\n').replace("'", "").split(', ')
      
      for i in range(int(partes[3])):
        if tel == telefones_individuais[i]:
          print("PESSOA LOCALIZADA:\n" + '-'*30)
          print(f'Nome: {partes[0]}')
          print(f'CPF: {partes[1]}')
          print(f'Endereço: {partes[2]}')
          for i in range(int(partes[3])):
            print(f'Telefone {i+1}: {telefones_individuais[i]}')
          print('-'*30 + "\n")
          return

  print("Telefone não encontrado.\n")

def remover():
  cpf = input("Digite o CPF da pessoa a ser removida: ")
  print("")
  flag = False
  
  with open('pessoas.txt', 'r+') as arquivo:
    aux = []
    for linha in arquivo:
      partes = linha.split(';')
      if cpf == partes[1]:
        flag = True
        continue
      else:
        aux.append(linha)

  if flag is True:
    print(f'Operação realizada com sucesso.\n')
    with open('pessoas.txt', 'w') as arquivo:
      arquivo.writelines(aux)
  else:
    print("CPF não encontrado!\n")
  

while True:
  print("MENU")
  print("1 - Inserir pessoa")
  print("2 - Listar pessoas cadastradas")
  print("3 - Buscar pessoa por CPF")
  print("4 - Buscar pessoa por telefone")
  print("5 - Remover pessoa por CPF")
  print("6 - Sair\n")

  val = int(input("Digite a opção desejada: "))
  print("")

  if val == 1:
    inserir()
  elif val == 2:
    listar()
  elif val == 3:
    buscar_cpf()
  elif val == 4:
    buscar_telefone()
  elif val == 5:
    remover()
  elif val == 6:
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida\n")
