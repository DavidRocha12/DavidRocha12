import random

def imprime_mensagem_abertura():
	print("*" * 30)
	print(f"{"Bem vindo ao jogo da forca":*^30}" )
	print("*" * 30)

def carrega_palavra_secreta():
	arquivo = open("Palavra.txt", "r")
	palavra = []
	for linha in arquivo:
		linha = linha.strip()
		palavra.append(linha)

	arquivo.close()

	numero = random.randrange(0, len(palavra))

	palavra_secreta = palavra[numero].upper()
	return palavra_secreta
	

def inicializa_letras_acertadas(palavra_secreta):
	return ["_" for letra in palavra_secreta]



def pede_chute():
	chute = input("Qual a letra? ")
	chute = chute.strip().upper()
	return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
	posicao = 0
	for letra in palavra_secreta:
		if chute == letra:
			letras_acertadas[posicao] = letra
		posicao += 1


def imprime_mensagem_perdedor(palavra_secreta):
	print("Puxa! você foi enforcado!")
	print(f"A palavra era {palavra_secreta}")


def imprime_mensagem_vencedor():
	print("Parabéns, você ganhou!!!")


# arquivo = open("Palavra.txt", "w")#o w não vai repetir as palavras, ele  apaga
# e acrecenta novamente
# arquivo.write("Banana\n")
# arquivo.write("Melancia\n")
# arquivo.write("Morango\n")
# arquivo.write("Manga\n")
# arquivo.close()

def jogar():
	imprime_mensagem_abertura()

	palavra_secreta = carrega_palavra_secreta()

	letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

	print(letras_acertadas)

	enforcou = False
	acertou = False
	erro = 0
	while (not enforcou and not acertou):

		chute = pede_chute()

		if chute in palavra_secreta:
			marca_chute_correto(chute, letras_acertadas, palavra_secreta)
		else:
			erro += 1

		enforcou = erro == 6
		acertou = "_" not in letras_acertadas

		print(letras_acertadas)

	if acertou:
		imprime_mensagem_vencedor()
	else:
		imprime_mensagem_perdedor(palavra_secreta)


jogo = jogar()


