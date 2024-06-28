class Conta:
    def __init__(self, numero, titular, saldo, limite):
        #O método __init__ é responsável por inicializar o objeto.
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #O primeiro parametro é sempre sua própria instância, e por
    # convenção é chamado de self, nesse caso self é a variável 
    # que a classe vai ser chamada, nesse  caso: conta.titular.

    def deposita(self, valor):
        self.saldo += valor
    
    #método com retorno:
    def saca(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente!")
            return False
        else:
            self.saldo -= valor
            return True

    
    def extrato(self):
        print(f"Número: {self.numero} \nSaldo: {self.saldo}")


#conta = Conta()
#print(type(conta))#visualisando o tipo de arquivo, aqui vai mostrar
# class __main__.conta, se chamar o módulo em outro arquivo, vai
# mostrar o nome do arquivo, mais a classe, class conta.Conta
