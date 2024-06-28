"""Exercicio de escrita, criando um arquivo"""

"""
arquivo = open("palavras.txt", "w")#Criar e abrir arquivo no modo escrita. serve para ser utillizado
# quando não existe um arquivo


arquivo.write("Banana\n")
arquivo.write("Melancia\n")
arquivo.write("Morango\n")
arquivo.write("Manga\n")

arquivo.close()

o código acima serve para criar um arquivo, e adicionar itens nela
"""

arquivo = open("palavras.txt", "r")#abrir arquivo no modo leitura

# arquivo.read()#para ler o arquivo inteiro
# arquivo.close()#é necessário fechar para ler ele novamente.
# arquivo = open("palavras.txt", "r")
# print(arquivo.read())#aqui vai mostrar todo o arquivo

# for linha in arquivo:
# 	print(linha) #aqui vai mostrar os itens pulando uma linha

# linha = arquivo.readline().strip()#se caso aparece o \n colocar o strip, porque ele tira espaços em branco
# # e caracteres do python
# print(linha)
# arquivo.close()

#adicionando o conteudo do arquivo em uma lista

palavras = []

for linha in arquivo:
	linha = linha.strip()
	palavras.append(linha)

arquivo.close()

print(palavras)

# Exemplo com with
# arquivo = open("Palavra.txt", "r")
# palavras = logo.read()
# with open("Palavra.txt") as arquivo: #o comando WITH vai se encarregar de 
# 	# fechar o arquivo caso algum erro aconteça na hora da leitura do arquivo,
# 	# já o comando close() pode acontecer de não fechar o arquivo se caso ocorrer 
# 	#um erro grave, e com isso pode corromper o seu arquivo.
# 	for linha in arquivo:
# 		print(linha)