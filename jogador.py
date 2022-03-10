class Jogador:
    """
    Esta classe representa os dados do jogador do Campo Minado, guardando a quantidade de jogadas que ele já fez e
    também o tempo que ele tem naquela partida atual.
    """

    __atributos = {"nick", "jogadas", "casas_abertas", "casas_abertas_total", "casas_marcadas" "tempo_de_jogo"}
    __metodos = {"__init__", "getNick", "getJogadas", "getCasasAbertas", "getCasasAbertasTotal", "getCasasMarcadas",
                 "aumenta_jogadas", "aumenta_abertas", "aumenta_abertas_total", "aumenta_marcadas", "setNome",
                 "getAtributos", "getMetodos", "getManual"}

    def __init__(self, nick="", jogadas=0, casas_abertas_jogador=0, casas_abertas_total=0, casas_marcadas=0,
                 tempo_de_jogo=0):
        """
        Inicializador responsável por criar as variáveis que armazenam os dados do jogador

        Entrada: objeto da classe, Jogador, str, int, str, o primeiro representa o nome do jogador, o segundo o número
         de jogadas que ele fez até
        o momento e o terceiro um texto mostrando o tempo total

        Saída: Nenhuma
        """
        self.nick = nick  # Nome do jogador no jogo.
        self.jogadas = jogadas  # Quantidades de jogadas que o jogador realizou
        self.casas_abertas_jogador = casas_abertas_jogador # Quantidades de casas abertas pelo jogador
        self.casas_abertas_total = casas_abertas_total # Quantidades de casas abertas no total, pelo jogo e jogador
        self.casas_marcadas = casas_marcadas # Quantidade de casas marcadas pelo jogador
        self.tempo_de_jogo = tempo_de_jogo  # Tempo que o jogador tem na mesma partida
    
    def getNick(self):
        """
        Método responsável por retornar o nome do jogador

        Entrada: objeto da classe Jogador

        Saída: str, nome do jogador
        """
        return self.nick
    
    def getJogadas(self):
        """
        Método responsável por retornar o número de jogadas do jogador

        Entrada: objeto da classe Jogador

        Saída: int, número de jogadas
        """
        return self.jogadas

    def getCasasAbertas(self):
        """
        Método responsável por retornar o número de casas abertas

        Entrada: objeto da classe Jogador

        Saída: int, número de casas abertas
        """
        return self.casas_abertas_jogador
    
    def getCasasAbertasTotal(self):
        """
        Método responsável por retornar o número de casas abertas no total, contando com as abertas recursivamente

        Entrada: objeto da classe Jogador

        Saída: int, número de casas abertas no total
        """
        return self.casas_abertas_total
    
    def getCasasMarcadas(self):
        """
        Método responsável por retornar o número de casas marcadas

        Entrada: objeto da classe Jogador

        Saída: Nenhuma
        """
        return self.casas_marcadas

    def aumenta_jogadas(self, n):
        """
        Método responsável por aumentar o número de jogadas

        Entrada: objeto da classe Jogador, int

        Saída: Nenhuma
        """
        self.jogadas += n
    
    def aumenta_abertas(self, n):
        """
        Método responsável por aumentar o número de casas abertas

        Entrada: objeto da classe Jogador, int

        Saída: Nenhuma
        """
        self.casas_abertas_jogador += n
    
    def aumenta_abertas_total(self, n):
        """
        Método responsável por aumentar o número de casas abertas no total

        Entrada: objeto da classe Jogador, int

        Saída: Nenhuma
        """
        self.casas_abertas_total += n
    
    def aumenta_marcadas(self, n):
        """
        Método responsável por aumentar o número de casas marcadas

        Entrada: objeto da classe Jogador, int

        Saída: Nenhuma
        """
        self.casas_marcadas += n

    def setNome(self):
        """
        Método responsável por alterar o nome do jogador

        Entrada: objeto da classe Jogador

        Saída: Nenhuma
        """
        nome = input("\nQual o nome do jogador? ")
        self.nick = nome

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Jogador.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Jogador.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Jogador.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Jogador.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Jogador.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Jogador.__init__.__doc__
        manual["getNick"] = Jogador.getNick.__doc__
        manual["getJogadas"] = Jogador.getJogadas.__doc__
        manual["getCasasAbertas"] = Jogador.getCasasAbertas.__doc__
        manual["getCasasAbertasTotal"] = Jogador.getCasasAbertasTotal.__doc__
        manual["getCasasMarcadas"] = Jogador.getCasasMarcadas.__doc__
        manual["aumenta_jogadas"] = Jogador.aumenta_jogadas.__doc__
        manual["aumenta_abertas"] = Jogador.aumenta_abertas.__doc__
        manual["aumenta_abertas_total"] = Jogador.aumenta_abertas_total.__doc__
        manual["aumenta_marcadas"] = Jogador.aumenta_marcadas.__doc__
        manual["setNome"] = Jogador.setNome.__doc__
        manual["getManual"] = Jogador.getManual.__doc__
        manual["getAtributos"] = Jogador.getAtributos.__doc__
        manual["getMetodos"] = Jogador.getMetodos.__doc__
        manual["nick"] = "# Representa o nome do jogador"
        manual["jogadas"] = "# Representa o número de jogadas do jogador"
        manual["casas_abertas_jogador"] = "# Quantidades de casas abertas pelo jogador"
        manual["casas_abertas_total"] = "# Quantidades de casas abertas no total, pelo jogo e jogador"
        manual["casas_marcadas"] = "# Quantidade de casas marcadas pelo jogador"
        manual["tempo_de_jogo"] = "# Representa o tempo de jogo do jogador"
        return manual
