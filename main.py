def ler_arquivo():

    arquivo = open("usuarios.txt", "r")
    nomes = ler_nomes(arquivo)

    arquivo = open("usuarios.txt", "r")
    espaco = ler_espaco(arquivo)

    print(nomes)
    print(espaco)












def ler_nomes(arquivo):

    nomes = []
    for line in arquivo:
        a = line.split()[0]
        nomes.append(a)
    arquivo.close()
    return nomes

def ler_espaco(arquivo):

    espaco = []
    for line in arquivo:
        a = line.split()[1]
        espaco.append(a)
    arquivo.close()
    return espaco


if (__name__ == "__main__"):
    ler_arquivo()