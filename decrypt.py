from tabela import *
from cript import *

def main():
    # Entrada do usuário
    entrada = input("Digite os números criptografados separados por vírgula (ex: 41, 36, 128, 101): ")
    # Converte a entrada em uma lista de números inteiros
    numeros = list(map(int, entrada.split(', ')))
    # Agrupa os números em pares de dois
    pares_numeros = [numeros[i:i + 2] for i in range(0, len(numeros), 2)]
    
    # Descriptografar os pares de números
    pares_descriptografados = decrypt_pairs(pares_numeros, decod)
    texto_descriptografado = numbers_to_text(pares_descriptografados)

    print("Texto descriptografado:", texto_descriptografado)


if __name__ == "__main__":
    main()