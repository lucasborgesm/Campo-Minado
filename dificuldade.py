from tela import *


class Dificuldade(Tela):
    """
    Classe responsável pela interface do menu de escolha de dificuldade
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "interpreta_dificuldade", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por inicializar todas as variáveis necessárias e criar um objeto da classe Tela
        para criar a interface do menu de escolha de dificuladades

        Entrada: objeto da classe Dificuldade, objeto da classe Historico

        Saída: Nenhuma
        """
        self.hist = hist
        self.titulo = "Selecione a Dificuldade"
        self.opcoes = ("(1) Fácil", "(2) Médio", "(3) Difícil")

        Tela(self.titulo, self.opcoes, hist).__init__(self.titulo, self.opcoes, hist)
    
    def interpreta_dificuldade(self, escolha):
        """
        Método responsável por interpretar a opção de dificuldade escolhida e retornar o tamanho do campo e número de
        bombas que serão formadas

        Entrada: objeto da classe Dificuldade, int (representando a escolha)

        Saída: tuple, representando o tamanho e o número de bombas do campo
        """
        opcoes = {1: (4,2), 2: (15, 40), 3: (22, 99)}
        return opcoes[escolha]

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Dificuldade.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Dificuldade.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Dificuldade.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Dificuldade.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Dificuldade.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Dificuldade.__init__.__doc__
        manual["interpreta_dificuldade"] = Dificuldade.interpreta_dificuldade.__doc__
        manual["getManual"] = Dificuldade.getManual.__doc__
        manual["getAtributos"] = Dificuldade.getAtributos.__doc__
        manual["getMetodos"] = Dificuldade.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de dificuldades"
        manual["opcoes"] = "# Representa as opcoes da tela de dificuldades"
        return manual
