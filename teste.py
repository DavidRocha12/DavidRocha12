from conta import Conta

import os 

os.system("clear")


conta = Conta("123-4", "João", 120.0, 1000.0)
##print(type(conta))#mostrando tipo de variável, aqui vai mostrar
# que conta é uma classe.

# conta.titular = "João"#exemplo acessando sem ter definido parâmetros
print(conta.titular)
#conta.saldo = 120.0
print(conta.saldo)
#conta.saldo = 100.0
#
# print(conta.número, conta.titular, conta.saldo, conta.limite)
conta.deposita(20.0)
conta.extrato()

conta.saca(15.0)
conta.extrato()

print()

#Objetos são acessados por referẽncia:
conta_2 = Conta("123-5", "David", 120.0, 1000.0)
print(conta_2.saldo)
#A variável conta é uma variável para associar a um objeto e, 
# essa variável não guarda um objeto, e sim uma maneira de acessa-lo
# chamada de referência(self)

#O correto é dizer que conta_2 se refere á um objeto, conta_2 é uma
#variável de referência.
#O correto é dizer que tenho uma referência conta_2 do objeto
#tipo Conta.

conta_3 = conta_2 #conta_3 passa a fazer referência para o mesmo 
# objeto conta_2

print(conta_3.saldo)

conta_2.deposita(100.0)
print(conta_2.saldo)

conta_3.deposita(30.0)
print(conta_3.saldo)

print(id(conta_2))
print(id(conta_3))
# aqui vai mostrar que as duas variáveis referênciam o mesmo 
#objeto conta.
print(id(conta_2) == id(conta_3))
print(conta_2 == conta_3)
#vai mostrar que é True, que são o mesmo objeto

conta_2 = Conta("123-5", "David", 120.0, 1000.0)
conta_3 = Conta("123-5", "David", 120.0, 1000.0)
if conta_2 == conta_3:
    print("Contas iguais!")

print(id(conta_2))
print(id(conta_3))
# o print acima vai mostra que agora essa váriáver se referência
# tem ids diferentes,por mais que são contas identicas

#No caso acima os valores são iguais, mas são objetos diferentes,
# nesse caso a condição if é False.
#Para saber se o dois objetos tem o mesmo conteúdo é necessário
#comparar atributo por atributo, mais a frente vai ser mostrado
#uma solução eficaz para esse assunto.