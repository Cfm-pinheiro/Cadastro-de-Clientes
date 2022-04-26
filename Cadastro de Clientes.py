# Cadastro simples de clientes

from datetime import datetime

nome = input('Digite o nome do Cliente ')

anonascimento = int(input('digite o ano de nascimento '))
mesnascimento = int(input('digite o mês de nascimento '))
dianascimento = int(input('digite o dia de nascimento '))

datanascimento = datetime(anonascimento,mesnascimento,dianascimento)
dataatual = datetime.now()
idadedocliente = dataatual - datanascimento


dias = idadedocliente.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30


endereco = input('Digite o Endereço ')
Telefone = input('Digite o Telefone ')

print('Cliente: {}\n Idade do Cliente: {} anos, {} Meses e {} dias\n Endereço: \n Telefone; {}'.format(nome, anos, meses, dias, endereco, Telefone))