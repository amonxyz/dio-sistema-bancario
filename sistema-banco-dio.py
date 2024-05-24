"""
somente depositos positivos

armazenar em uma variavel todos depositos

permitir 3 saques diarios

sem saldo exiba mensagem informando que não é possivel realizar o saque

operação de extrato mostrando saques e depositos no fim exibe saldo atual R$ xxx.xx"""

saldo = 0 
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

  menu = input("""
[d]epositar
[s]aque
[e]xtrato
[q]sair
""").lower()

  opcao = menu

  if opcao == 'd':
    dep = input('digite o valor do deposito: ') 
    if dep.replace('.', '', 1).isdigit():
      dep = float(dep)
      if dep > 0:
        saldo += dep
        extrato += f'deposito: R$ {dep:.2f}\n'
        print(f'seu deposito de {dep:.2f} foi realizado')
      else:
        print('deposite um valor positivo')
    else:
      print('digite apenas numeros')

  elif opcao == 's':
    if numero_saque >= LIMITE_SAQUES:
      print('limite de saques excedidos')
    else:
      saque = input('digite o valor do saque: ')
      if saque.replace('.', '', 1).isdigit():
        saque = float(saque)
        if saque > saldo:
          print('saldo insuficiente')
        elif saque > limite:
          print('você pode realizar saque de apenas R$ 500.00') 
        elif saque > 0:
          saldo -= saque
          extrato += f'saque: R$ {saque:.2f}\n'
          numero_saque += 1
          print(f'saque de R$ {saque:.2f} realizado com sucesso')
        else:
          print('o valor do saque deve ser positivo')
      else:
        print('digite apenas numeros')

  elif opcao == 'e':
    print('\n ---EXTRATO---')
    print('não foram realizadas movimentações' if not extrato else extrato)
    print(f"saldo atual: R$ {saldo:.2f}")
    print("---------------\n")

  elif opcao == 'q':
    print('até a próxima')
    break
  
  else:
    print('opção inválida, tente novamente')







