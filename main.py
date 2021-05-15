from os import truncate


def ler_arquivo():
    arquivo = open("usuarios.txt", "r")
    nomes = ler_nomes(arquivo)

    arquivo = open("usuarios.txt", "r")
    espaco = ler_espaco(arquivo)

    espaco_mb = []
    for line in espaco:
        espaco_mb.append(conversao_mb(line))

    soma = somar_elementos(espaco)

    total_usuarios = int(len(nomes))
    total_usuarios_mb = conversao_mb(soma / total_usuarios)



    novo_relatorio = open("relatorio.txt", "w")
    novo_relatorio.write(''
                         'ACME Inc.           Uso do espaco em disco pelos usuarios\n'
                         '------------------------------------------------------------------------\n'
                         'Nr.  Usuario        Espaco utilizado     % do uso\n')
    cont = 0
    for item in nomes:
        novo_relatorio.write(f'{cont+1}') and novo_relatorio.write(f" {item:>13}") and novo_relatorio.write(f" {espaco_mb[cont]:>18}") and novo_relatorio.write(f" {calculo_percentual(int(espaco[cont])):>13}\n")
        cont += 1

    novo_relatorio.write(f'\nEspaco total ocupado: {conversao_mb(str(soma))}\n')
    novo_relatorio.write(f'Espaco medio ocupado: {total_usuarios_mb}')










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

def conversao_mb(valor):
    a = (int(valor)/1000000)
    retorno = (f'{a:.2f} MB')
    return retorno

def calculo_percentual(valor):
    resultado = (100*(valor/2706966000))
    return (f'{resultado:.2f}%')

def somar_elementos(lista):
    soma = 0
    for numero in lista:
      soma += int(numero)
    return soma



if (__name__ == "__main__"):
    ler_arquivo()
