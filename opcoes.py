from tela import Tela


class Opcoes(Tela):
    """
    Essa classe é responsável pela interface do menu de opções, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por criar a tela existente do menu de opções

        Entrada: objeto da classe Opcoes, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.titulo = "Menu de opções"
        self.opcoes = ("(1)", "(2)", "(3)", "(4)", "(5)")
        menu_opcoes = Tela(self.titulo, self.opcoes, hist).__init__(self.titulo, self.opcoes, self.hist)

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Opcoes.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Opcoes.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Opcoes.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Opcoes.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Opcoes.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Opcoes.__init__.__doc__
        manual["getManual"] = Opcoes.getManual.__doc__
        manual["getAtributos"] = Opcoes.getAtributos.__doc__
        manual["getMetodos"] = Opcoes.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual
