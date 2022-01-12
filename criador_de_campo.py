from random import randint


class CriadorDeCampo:
    """
    Essa classe representa os métodos necessários para a criação de um campo e máscara do jogo Campo Minado
    """

    __atributos = {}
    __metodos = {"inicializa_campo", "verifica_posicoes_livres", "spawna_bombas", "entorno", "atualiza_vizinhos",
                 "cria_campo", "cria_mascara", "getAtributos", "getMetodos", "getManual"}

    @staticmethod
    def inicializa_campo(tamanho):
        """
        Função responsável por inicializar uma matriz quadrada com um tamanho passado como parâmetro, e 0 em todas as
        posições

        Entrada: int, representando o tamanho da matriz

        Saída: list, representando uma matriz quadrada com 0 em todas as posições
        """
        campo = []
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                linha.append(0)
            campo.append(linha)
        return campo

    @staticmethod
    def verifica_posicoes_livres(campo):
        """
        Função responsável por encontrar todas as casas vazias da matriz, que nesse caso são as casas que possuem
        valor 0

        Entrada: list, representando a matriz

        Saída: list, com todas as coordenadas das posições vazias
        """
        posicoes_vazias = []
        pos_i = 0
        pos_j = 0
        for i in campo:
            for aij in i:
                if aij == 0:
                    posicoes_vazias.append((pos_i, pos_j))
                pos_j += 1
            pos_j = 0
            pos_i += 1
        return posicoes_vazias

    @staticmethod
    def spawna_bombas(campo, n_bombas, bomba):
        """
        Função responsável por posicionar numa matriz, uma quantidade determinada de item repetidos aleatóriamente,
        como exemplo no jogo campo minado, posicionar aleatóriamente o símbolo que representa a bomba

        Entrada: list, int, char, o primeiro representando a matriz, o segundo o número de símbolos e o terceiro o
        símbolo que se deseja colocar

        Saída: Nenhuma
        """
        posicoes_vazias = CriadorDeCampo().verifica_posicoes_livres(campo)
        for k in range(n_bombas):
            posicao = randint(0, len(posicoes_vazias) - 1)
            i, j = posicoes_vazias[posicao]
            campo[i][j] = bomba
            posicoes_vazias.remove(posicoes_vazias[posicao])

    @staticmethod
    def entorno(tamanho, linha, coluna):
        """
        Função responsável por encontrar os elementos de uma matriz quadrada no entorno de uma coordenada passada
        como parâmetro

        Entrada: int, int, int, representando primeiro o tamanho da matriz quadrada, depois a coordenada da linha e por
        último a coordenada da coluna

        Saída: list, contendo as coordenadas de todos os vizinhos
        """
        linhas = [linha]
        colunas = [coluna]
        if linha > 0:
            linhas = linhas + [linha - 1]
        if linha + 1 < tamanho:
            linhas = linhas + [linha + 1]
        if coluna > 0:
            colunas = colunas + [coluna - 1]
        if coluna + 1 < tamanho:
            colunas = colunas + [coluna + 1]
        vizinhos = []
        for i in linhas:
            for j in colunas:
                vizinhos = vizinhos + [(i, j)]
        vizinhos.remove((linha, coluna))
        return vizinhos

    @staticmethod
    def atualiza_vizinhos(campo, tamanho, bomba):
        """
        Função responsável por atualizar um elemento em uma matriz quadrada, colocando como valor o número de vezes
        que o simbolo passado como parâmetro aparece como entorno daquele elemento

        Entrada: list, int, char, o primeiro sendo a matriz quadrada, o segundo o tamanho da matriz e o terceiro
        o símbolo de interesse

        Saída: Nenhuma
        """
        for i in range(tamanho):
            for j in range(tamanho):
                if campo[i][j] != bomba:
                    casas_vizinhas = CriadorDeCampo().entorno(tamanho, i, j)
                    for casa in casas_vizinhas:
                        if campo[casa[0]][casa[1]] == bomba:
                            campo[i][j] = campo[i][j] + 1

    @staticmethod
    def cria_campo(tamanho, n_bombas, bomba):
        """
        Função responsável por criar uma matriz quadrada colocando aleatóriamente um determinado número de símbolos,
        passado como parâmetro, e marcando nas casas vazias o número de vezes que aquele símbolo aparece no entrono
        dessa casa

        Entrada, int, int, char, primeiro representando o tamanho da matriz quadrada, depois o número de simbolos que
        serão colocados e por último o símbolo

        Saída: list, contendo a matriz representando o campo
        """
        campo = CriadorDeCampo().inicializa_campo(tamanho)
        CriadorDeCampo().spawna_bombas(campo, n_bombas, bomba)
        CriadorDeCampo().atualiza_vizinhos(campo, tamanho, bomba)
        return campo

    @staticmethod
    def cria_mascara(tamanho, fechada):
        """
        Função responsável por criar uma matriz quadrada, com um determinado tamanho, utilizando um mesmo símbolo em
        todas as posições

        Entrada: int, char, primeiro representando o tamanho da matriz quadrada, depois o símbolo que será utilizado

        Saída: list, contendo a matriz representando a mascara
        """
        mascara = []
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                linha.append(fechada)
            mascara.append(linha)
        return mascara

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Ferramentas.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return CriadorDeCampo.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de CriadorDeCampo.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return CriadorDeCampo.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de CriadorDeCampo.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["inicializa_campo"] = CriadorDeCampo.inicializa_campo.__doc__
        manual["verifica_posicoes_livres"] = CriadorDeCampo.verifica_posicoes_livres.__doc__
        manual["spawna_bombas"] = CriadorDeCampo.spawna_bombas.__doc__
        manual["entorno"] = CriadorDeCampo.entorno.__doc__
        manual["atualiza_vizinhos"] = CriadorDeCampo.atualiza_vizinhos.__doc__
        manual["cria_campo"] = CriadorDeCampo.cria_campo.__doc__
        manual["cria_mascara"] = CriadorDeCampo.cria_mascara.__doc__
        manual["getAtributos"] = CriadorDeCampo.getAtributos.__doc__
        manual["getMetodos"] = CriadorDeCampo.getMetodos.__doc__
        manual["getManual"] = CriadorDeCampo.getManual.__doc__
        return manual
