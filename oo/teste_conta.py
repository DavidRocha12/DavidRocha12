import os

os.system("clear")

#aqui foi criado uma função, para criar contas e poder receber
#dados diferentes, e não ter a necessidade de repetir o código
def criar_conta(numero, titular, saldo, limite):
    """
    retorna dicionário conta.
    :param numero: str(numero).
    :param titular: str(nome).
    :param saldo: float.
    :param limite: float.
    :return dict de conta. 
    """
    conta = {"numero" : numero, "titular" : titular, "saldo" : saldo, "limite" : limite}
    return conta



def deposita(conta, valor):
    conta["saldo"] += valor
    #return conta #essa função não necessita o return


def saque(conta, valor):
    conta["saldo"] -= valor
    #return conta #essa conta não necessita o return


def extrato(conta):
    print(f"numero: {conta['numero']}\n saldo: {conta['saldo']}")


conta = criar_conta("123-4", "João", 120.0, 1000.0)

deposita(conta, 100)#acrescentando 100 no valor

extrato(conta)

saque(conta, 50)#tirando 50 do valor

extrato(conta)

#conta['saldo'] = -100
#print(conta)#aqui mostra que mesmo que tenha a função saca e deposita
# é possível modificar diretamente o valor de saldo, e o correto 
# é bloquear esse modo utilizando classe e obrigando ele alterar
# o valor somente com a função saca e deposita, diretamente 
# não vai ser possível modificar.
