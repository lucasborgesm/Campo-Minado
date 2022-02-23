from tela import *


class MenuPause(Tela):
    """
    Classe responsável pela interface do menu de pause, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "mensagem_de_saida", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por inicializar as variáveis necessárias e criar um objeto da classe Tela para a
        interface do menu de pause

        Entrada: objeto da classe MenuPause, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.titulo = "Menu de Pause"
        self.opcoes = ("(1) Retomar", "(2) sair")
        Tela(self.titulo, self.opcoes, self.hist).__init__(self.titulo, self.opcoes, self.hist)
    
    def mensagem_de_saida(self):
        """
        Método responsável pela mensagem de saída do jogo

        Entrada: objeto da classe MenuPause

        Saída: Nenhuma
        """
        print("\nVocê escolheu sair do jogo.\n")

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de MenuPause.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return MenuPause.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de MenuPause.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return MenuPause.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de MenuPause.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = MenuPause.__init__.__doc__
        manual["mensagem_de_saida"] = MenuPause.mensagem_de_saida.__doc__
        manual["getManual"] = MenuPause.getManual.__doc__
        manual["getAtributos"] = MenuPause.getAtributos.__doc__
        manual["getMetodos"] = MenuPause.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual
