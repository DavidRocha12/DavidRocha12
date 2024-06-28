import os

os.system('clear')

# Variáveis e impressão

my_name = "David" #meu nome
my_age = 34 #minha idade
height = 1.72 #minha altura
centimetros = height * 100

my_weight = 80.0 #meu peso
my_eyes = "Castanhos" #meus olhos
my_teeth = "Brancos" #,meus dentes
my_hair = "Castanhos Escuros" #meu cabelo

print(f"Vamos falar sobre {my_name}.")
print(f"Ele tem {height} metros de altura.")
print(f"Ele tem {centimetros} centimetros de altura.")
print(f"Ele pesa {my_weight}kg.")
print("Na verdade isso não é muito pesado!.")
print(f"Ele tem olhos {my_eyes} e cabelos {my_hair}.")
print(f"Os dentes deles são {my_teeth}, mesmo tomando café.")

total = my_age + height + my_weight

print(f"Se eu somar sua idade que é {my_age},altura {height}, e peso {my_weight},\
 eu tenho um total de {total}.")
