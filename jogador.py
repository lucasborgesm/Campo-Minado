class Jogador:
    """
    Esta classe representa os dados do jogador do Campo Minado, guardando a quantidade de jogadas que ele já fez e
    também o tempo que ele tem naquela partida atual
    """

    __atributos = {"nick", "jogadas", "tempo_de_jogo"}
    __metodos = {"__init__", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, nick, jogadas=0, tempo_de_jogo=0):
        """
        Inicializador responsável por criar as variáveis que armazenam os dados do jogador

        Entrada: str, int, str, o primeiro representa o nome do jogador, o segundo o número de jogadas que ele fez até
        o momento e o terceiro um texto mostrando o tempo total

        Saída: Nenhuma
        """
        self.nick = nick  # Nome do jogador no jogo.
        self.jogadas = jogadas  # Quantidades de jogadas que o jogador realizou
        self.tempo_de_jogo = tempo_de_jogo  # Tempo que o jogador tem na mesma partida

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
        manual["getManual"] = Jogador.getManual.__doc__
        manual["getAtributos"] = Jogador.getAtributos.__doc__
        manual["getMetodos"] = Jogador.getMetodos.__doc__
        manual["nick"] = "# Representa o nome do jogador"
        manual["jogadas"] = "# Representa o número de jogadas do jogador"
        manual["tempo_de_jogo"] = "# Representa o tempo de jogo do jogador"
        return manual
