"""Para definirmos uma função em python utilizamos o camando def, veja um 
exemplo abaixo de uma função para calcular espaço e tempo:
"""

def velocidade(espaço, tempo):#velocidade nome da função, espaço e tempo entre
	#parenteses parametros que a função vai receber.
	v = espaço / tempo
	print(f"velocidade: {v} m/s.")


velocidade(100, 20)

# resultado:

# 5.0 m/s

#podemos ter funções sem parametros, veja um exemplo abaixo:

def diz_oi():
	print("Oi!")


diz_oi()

#resultado:

#Oi!

#Os parâmetros podem ser obrigatórios ou opcionais, mas para ser opcional
# é necessário atribuir um valor padrão a ele, ppor exemplo, None ou 0, veja 
# o exemplo abaixo:

def dados(nome, idade = None):
	print(f"Nome: {nome}.")
	if idade is not None:
		print(f"Idade: {idade}.")
	else:
		print("Idade: Não informada.")


dados("João", 20)

dados("Maria")


def dados_2(nome, idade = 0):
	print(f"Nome: {nome}.")
	if idade > 0:
		print(f"Idade: {idade}.")
	else:
		print("Idade: Não informada.")


dados_2("João", 20)

dados_2("Maria")

#ambos as funções recebem os mesmos resultado, mesmo que um seja None e o outro
# 0, como parametros padrão. 
#é possível passar somente idade, mas teriamos que especificar o parâmetro, e nesse
# caso também é necessário fazer o nome virar um parâmetro padrão como None

def dados_3(nome = None, idade = None):
	if nome is not None:
		print(f"Nome: {nome}.")
	else:
		print("Nome: Sem nome!")

	if idade is not None:
		print(f"Idade: {idade}.")
	else:
		print("Idade: Não informada.")


dados_3("João", 20)
dados_3(idade = 30)

#acima nos resultados vai mostrar as repectivas mensagem o primeiro chamado
# vai mostrar nome e idade e o proximo sem nome e idade.

#Retornando multiplos valores

def velocidade_media(distancia, tempo):
	velocidade = distancia / tempo
	return velocidade


print(velocidade_media(100, 20))
print(velocidade_media(150, 22))
print(velocidade_media(200, 30))
print(velocidade_media(50, 3))

# Números arbitrários de parâmetros(*args)
	
#Váriáveis mágicas do python: *args e **kwargs

#*args pode receber vários parametros em uma função, veja o exemplo abaixo:

def teste(arg, *args):
	print(f"primeiro argumento normal: {arg}")
	for arg in args:
		print(f"Outro argumento: {arg}")


teste("Python", "é", "muito", "legal", "!")

#é possível receber listas e tuplas, veja o exemplo abaixo:

print()

lista = ["é", "muito", "legal"]
teste("python", *lista)

print()

tupla = ("é", "muito", "legal")
teste("python", *tupla)

print(*tupla)# o * executa um empacotamento e a função faz o desempacotamento
# nesse caso a função print.

#Número arbitrário de chaves(**kwargs)

#O kwargs é utilizado para manipular argumentos nomeados em uma função, 
# argumentos nomeados é o dicionário, que carrega a chave e o valor.
# Veja o exemplo abaixo:

def minha_funcao(**kwargs):
	for key, value in kwargs.items():
		print("{0} = {1}".format(key, value))


minha_funcao(nome = "Caelum")

print()

dicionario = {"nome" : "João", "Idade" : 25}
minha_funcao(**dicionario)

