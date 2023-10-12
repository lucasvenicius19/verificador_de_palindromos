print("Verificador de palindromos.")

# Pedir ao usuario que forneca a frase ou palavra
frase_original = input("Digite a frase que deseja verificar sem acentos e sem pontuação: ")

# Convertendo todos os caracteres para letras minúsculas
frase = frase_original.lower()

# Removendo espaços entre as palavras
frase = frase.replace(" ", "")

# Removendo os espaços em branco
frase = frase.strip()

# Criando uma lista com a frase fornecida pelo usuário
lista_frase = list(frase)

# Invertendo a frase
lista_invertida = list(lista_frase)
lista_invertida.reverse()

if lista_frase == lista_invertida:
    print("A frase: ", frase_original, "é um palíndromo.")
else:
    print("A frase: ", frase_original, "não é um palíndromo.")
