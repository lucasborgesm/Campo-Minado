from datetime import datetime


class Load:
    """
    Essa classe é responsável por carregar o estado antigo do jogo, incluindo todas as informações necessárias para que
    o jogo possa ser retomado no momento exato do save.
    """

    __atributos = {"hist", "load", "posicao_tamanho"}
    __metodos = {"__init__", "carrega_campo_inicial", "carrega_jogadas", "carrega_casas_abertas_e_marcadas",
                 "carrega_jogador", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por ler o arquivo necessário para carregar o jogo.

        Entrada:

        Saída:
        """
        self.hist = hist
        self.load = "save.txt"
        self.posicao_tamanho = 5
    
    def carrega_campo_inicial(self):
        """
        Método responsável por carregar o campo do save

        Entrada: objeto da classe Load

        Saída: tuple, contendo o tamanho, o número de bombas e o campo
        """
        try:
            arquivo = open(self.load)
            linhas = arquivo.readlines()
            tamanho = int(linhas[self.posicao_tamanho])
            n_bombas = 0
            campo_str = linhas[self.posicao_tamanho + 1: tamanho + self.posicao_tamanho + 1]
            campo = []
            for linha in campo_str:
                linha_campo = []
                for i in range(tamanho):
                    aij = linha[i]
                    if aij == "b":
                        linha_campo.append(aij)
                        n_bombas += 1
                    else:
                        linha_campo.append(int(aij))
                campo.append(linha_campo)
            arquivo.close()
            return tamanho, n_bombas, campo
        except IndexError:
            self.hist.armazena_log(f"{datetime.today()}\n"
                                   f"        IndexError"
                                   f"        Não existe nenhum jogo salvo."
                                   f"        O usuário foi levado novamente ao menu_principal")
            print("Não existe nenhum jogo salvo.\n")
            input("Pressione enter para continuar\n")
            return False

    
    def carrega_jogadas(self):
        """
        Método responsável por carregar todas as jogadas feitas de um save

        Entrada: objeto da classe Load

        Saída: str, contendo as informações de jogadas
        """
        arquivo = open(self.load)
        linhas = arquivo.readlines()
        tamanho = int(linhas[self.posicao_tamanho])
        jogadas = linhas[self.posicao_tamanho + tamanho + 1:]
        return jogadas
    
    def carrega_casas_abertas_e_marcadas(self, jogadas):
        """
        Método responsável por tratar o str com informações de jogadas

        Entrada: objeto da classe Load, str (contendo as jogadas)

        Saída: tuple, contendo as coordenadas de casas abertas e marcadas
        """
        pos_casas_abertas = []
        pos_casas_marcadas = []
        for jogada in jogadas:
            virgula = jogada.index(",")
            parentese_final = jogada.index(")")
            i = int(jogada[2: virgula])
            j = int(jogada[virgula + 1: parentese_final])
            if jogada[0] == "a":
                pos_casas_abertas.append((i, j))
            elif jogada[0] == "m":
                pos_casas_marcadas.append((i, j))
        return pos_casas_abertas, pos_casas_marcadas
    
    def carrega_jogador(self):
        """
        Método responsável por carregar as informações de um jogador de um save

        Entrada: objeto da classe Load

        Saída: tuple, contendo todas as informações do jogador
        """
        arquivo = open(self.load)
        linhas = arquivo.readlines()
        nick = linhas[0]
        jogadas = int(linhas[1])
        casas_abertas = int(linhas[2])
        casas_abertas_total = int(linhas[3])
        casas_marcadas = int(linhas[4])
        arquivo.close()
        return nick, jogadas, casas_abertas, casas_abertas_total, casas_marcadas

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Load.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Load.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Load.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Load.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Load.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Load.__init__.__doc__
        manual["carrega_campo_inicial"] = Load.carrega_campo_inicial.__doc__
        manual["carrega_jogadas"] = Load.carrega_jogadas.__doc__
        manual["carrega_casas_abertas_e_marcadas"] = Load.carrega_casas_abertas_e_marcadas.__doc__
        manual["carrega_jogador"] = Load.carrega_jogador.__doc__
        manual["getManual"] = Load.getManual.__doc__
        manual["getAtributos"] = Load.getAtributos.__doc__
        manual["getMetodos"] = Load.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual
