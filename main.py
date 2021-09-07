

def ler_arquivo():
    arquivo = open("usuarios.txt", "r")
    usuarios = montar_dic(arquivo)
    pagina = open("index.html", "w")
    pagina.write("<html lang=\"pt-BR\">\n")
    pagina.write("<head><title>Relatorio de Usuarios</title></head>\n")


    novo_relatorio = open("relatorio.txt", "w",encoding="utf-8")
    novo_relatorio.write(''
                         'ACME Inc.           Uso do espaço em disco pelos usuários\n'
                         '------------------------------------------------------------------------\n'
                         'Nm.    Usuário      Espaço utilizado     % do uso\n')



    a = int(input('Você deseja apresentar quantos usuários ? (Digite 0 Para sair)\n'))
    if (a > 0) and (a <= len(usuarios)):
        cont = 0
        #relatório montado ordenando por ordem decrescente
        for item in sorted(usuarios, key = usuarios.get, reverse=True):
            novo_relatorio.write(f'{cont+1}') and novo_relatorio.write(f" {item:>13}") \
            and novo_relatorio.write(f" {conversao_mb(usuarios[item]):>18}") \
            and novo_relatorio.write(f" {calculo_percentual(usuarios[item]):>13}\n")
            cont += 1
            if cont == a:
                break
    print('Relatório criado')

    soma = sum(usuarios.values())
    total_usuarios_mb = conversao_mb(soma / int(len(usuarios)))
    novo_relatorio.write(f'\nEspaço total ocupado: {conversao_mb(str(soma))}\n')
    novo_relatorio.write(f'Espaço médio ocupado: {total_usuarios_mb}')
    novo_relatorio.close()


    conteudo = open("relatorio.txt","r")
    pagina.write("<body><pre><center><h1>\n")
    for linhas in conteudo.readlines():
        pagina.write(linhas)
    pagina.write("\n</h1></center></pre></body>")


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
