"""
Modos de Abertura de arquivos: http://docs.python.org/3/library/functions.html#open

r -> Abre para leitura - padrão

w -> Abre para escrita - sobrescreve caso o arquivo ja exista

x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistError
        with open('university.txt', 'x') as arquivo:
            arquivo.write('Teste de conteúdo \n')

a -> Abrindo no modo 'a' (append), se o arquivo não existir será criado. Caso exista, o novo conteúdo será adicionado
SEMPRE no final do arquivo. Com o modo 'a' não controlamos o cursor.
        with open('frutas.txt', 'a') as arquivo:
            while True:
                fruta = input('Informe uma fruta ou digite "sair": ')
                if fruta != 'sair':
                    arquivo.write(fruta + '\n')
                else:
                    break

+ -> Abre para o modo atualização: r (read) w (writing) . (Temos o controle do cursor)
        with open('novo.txt', 'r+') as arquivo:
        arquivo.seek(0)
        arquivo.write('Tenta \n')
        arquivo.write('Fodase mano \n')
        arquivo.write('Eu sou um lixo \n')

"""
