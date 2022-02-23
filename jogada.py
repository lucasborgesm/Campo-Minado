from tela import *


class Jogada(Tela):
    """
    Classe responsável pela interface de jogada, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por inicializar as variáveis necessárias e criar um objeto da classe Tela para a
        interdace do menu de jogada

        Entrada: objeto da classe Jogada, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.titulo = "Jogada"
        self.opcoes = ("(1) Abre casa", "(2) Marca/Desmarca casa", "(3) Menu")
        Tela(self.titulo, self.opcoes, self.hist).__init__(self.titulo, self.opcoes, self.hist)

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Jogada.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Jogada.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Jogada.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Jogada.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Jogada.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Jogada.__init__.__doc__
        manual["getManual"] = Jogada.getManual.__doc__
        manual["getAtributos"] = Jogada.getAtributos.__doc__
        manual["getMetodos"] = Jogada.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual