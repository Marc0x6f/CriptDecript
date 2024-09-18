from tabela import *

def agrupar_pares(mensagem):
    mensagem =mensagem.upper()
    #transforma char em numeros
    numeros = [tabela[char] for char in mensagem if char in tabela]
    #agrupa os pares
    pares = []
    for i in range(0, len(numeros), 2):
        if i+1 < len(numeros):
            pares.append([numeros[i], numeros[i+1]])
        else:
            pares.append([numeros[i], 0]) # # Caso o último caractere fique sozinho, adiciona 0

    return pares

def format_numbers(numbers):
    """Formata a lista de números para uma string legível."""
    return ', '.join(f"{int(num)}" for num in numbers)

def encrypt_pairs(pares, cod):
    #Criptografa os pares de números usando a matriz de codificação
    criptografado = []
    for par in pares:
        matriz_par = np.array(par).reshape(2, 1)
        resultado = np.dot(cod, matriz_par)
        criptografado.extend(resultado.flatten())
    return criptografado



def decrypt_pairs(pares, decod):
    """Descriptografa os pares de números usando a matriz inversa."""
    descriptografado = []
    for par in pares:
        matriz_par = np.array(par).reshape(2, 1)
        resultado = np.dot(decod, matriz_par)
        resultado = resultado.flatten().astype(int)
        descriptografado.extend(resultado)
    return descriptografado


def numbers_to_text(numbers):
    """Converte uma lista de números de volta em uma string usando a tabela."""
    reverse_tabela = {v: k for k, v in tabela.items()}
    texto = ''.join(reverse_tabela.get(int(round(num)), '?') for num in numbers)
    return texto

#Mensagem
usrinput = input(str("digite sua mensagem: "))
pares_numeros = agrupar_pares(usrinput)


#Criptografa
pares_criptografados = encrypt_pairs(pares_numeros, cod)
formatted_result = format_numbers(pares_criptografados)
print("Números criptografados:", formatted_result)
