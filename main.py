import html

def ler_arquivo():
    arquivo = open("usuarios.txt", "r")
    usuarios = montar_dic(arquivo)



    novo_relatorio = open("relatorio.txt", "w")
    novo_relatorio.write(''
                         'ACME Inc.           Uso do espaco em disco pelos usuarios\n'
                         '------------------------------------------------------------------------\n'
                         'Nr.  Usuario        Espaco utilizado     % do uso\n')



    a = int(input('Você deseja apresentar quantos usuários ? (Digite 0 Para sair)\n'))
    if (a > 0) and (a < len(usuarios)):
        cont = 0
        #relatório montado ordenando por ordem decrescente
        for item in sorted(usuarios, key = usuarios.get, reverse=True):
            novo_relatorio.write(f'{cont+1}') and novo_relatorio.write(f" {item:>13}") and novo_relatorio.write(f" {conversao_mb(usuarios[item]):>18}") and novo_relatorio.write(f" {calculo_percentual(usuarios[item]):>13}\n")
            cont += 1
            if cont == a:
                break


    soma = sum(usuarios.values())
    total_usuarios_mb = conversao_mb(soma / int(len(usuarios)))
    novo_relatorio.write(f'\nEspaco total ocupado: {conversao_mb(str(soma))}\n')
    novo_relatorio.write(f'Espaco medio ocupado: {total_usuarios_mb}')


def montar_dic(arquivo):
    usuarios = {}
    nomes = []
    espaco = []
    for line in arquivo:
        a = line.split()[0]
        b = int(line.split()[1])
        usuarios[a] = b
    arquivo.close()
    return usuarios

def conversao_mb(valor):
    a = (int(valor)/1000000)
    retorno = (f'{a:.2f} MB')
    return retorno

def calculo_percentual(valor):
    resultado = (100*(valor/2706966000))
    return (f'{resultado:.2f}%')


if (__name__ == "__main__"):
    ler_arquivo()
