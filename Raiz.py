def carregar_numeros(arquivo):
    """Lê o arquivo e devolve os números como inteiros."""
    with open(arquivo, 'r', encoding='utf-8') as f:
        return [int(linha.strip()) for linha in f if linha.strip()]


def pesquisa_binaria(lista, alvo, inicio=0):
    """Busca binária recursiva que retorna o índice real do elemento."""
    if len(lista) == 0:
        return None

    meio = len(lista) // 2
    valor_meio = lista[meio]

    if valor_meio == alvo:
        return inicio + meio

    # procurar na metade direita
    if valor_meio < alvo:
        return pesquisa_binaria(lista[meio + 1:], alvo, inicio + meio + 1)

    # procurar na metade esquerda
    return pesquisa_binaria(lista[:meio], alvo, inicio)


# -------------------------------------------------------
# Execução principal
# -------------------------------------------------------

arquivo = "numeros.txt"
numeros = carregar_numeros(arquivo)

alvo = int(input("Digite o número que deseja localizar: "))

posicao = pesquisa_binaria(numeros, alvo)

if posicao is not None:
    print(f"O número {alvo} está na posição {posicao}.")
else:
    print("Número não encontrado.")
