import os

os.system("clear")

#exemplo de programa de banco financeiro par orientação a objeto,

#uma conta no banco,

# numero = "123-4"
# titular = "João"
# saldo = 120.0
# limite = 1000.0

# # representação de mais de uma conta

# numero2 = "123-5"
# titular2 = "José"
# saldo2 = 200.0
# limite2 = 1000.0 

# """ Com o crescimento do banco, o números de contas vai crescer, e com isso o
# programa vai ficar trabalhoso para fazer a manutenção.
# utilizando dicionário para acessar dados de uma conta expessifica:
# """

# conta = {"numero" : "123-4", "titular" : "João", "saldo" : 120.0, "limite" : 1000.0}

# # é possível acessar dados da conta pelo nome da chave

# print(conta["numero"])
# print(conta["titular"])

# #criando uma segunda conta:

# conta2 = {"numero" : "123-5", "titular" : "José", "saldo" : 200.0, "limite" : 1000.0}


#isolando o código em uma função:

#função criar conta, para criar várias contas:
def cria_conta(numero, titular, saldo, limite):
	conta = {"numero" : numero, "titular" : titular, "saldo" : saldo, "limite" : limite}
	return conta



conta1 = cria_conta("123-4", "João", 120.0, 1000.0)
conta2 = cria_conta("123-5", "José", 200.0, 1000.0)

print(conta1)
print(conta2)

print(conta1["numero"])
print(conta2["numero"])

def deposita(conta, valor):
	conta["saldo"] += valor
	return conta


def saque(conta, valor):
	conta["saldo"] -= valor
	return conta


def extrato(conta):
	print(f"numero: {conta['numero']} \n saldo: {conta['saldo']}")


deposita(conta1, 100.0)

extrato(conta1)

saque(conta1, 20.0)

extrato(conta1)





