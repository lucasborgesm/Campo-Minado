from tela import Tela


class ConfirmaNovoJogo(Tela):
    """
    Classe responsável pela interface de confirmar novo jogo, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por inicializar todas as variáveis necessárias e criar um objeto da classe Tela
        para criar a interface do menu de confirmar um novo jogo

        Entrada: objeto da classe ConfirmaNovoJogo, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.titulo = "Começar um novo jogo irá apagar seu save antigo.\nTem certeza que deseja continuar?"
        self.opcoes = ("(1) Continuar", "(2) Voltar")
        Tela(self.titulo, self.opcoes, hist).__init__(self.titulo, self.opcoes, hist)

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de ConfirmaNovoJogo.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return ConfirmaNovoJogo.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de ConfirmaNovoJogo.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return ConfirmaNovoJogo.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de ConfirmaNovoJogo.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = ConfirmaNovoJogo.__init__.__doc__
        manual["getManual"] = ConfirmaNovoJogo.getManual.__doc__
        manual["getAtributos"] = ConfirmaNovoJogo.getAtributos.__doc__
        manual["getMetodos"] = ConfirmaNovoJogo.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de confirmar um novo jogo"
        manual["opcoes"] = "# Representa as opcoes da tela de confirmar um novo jogo"
        return manual
