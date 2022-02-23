from tela import Tela


class MenuInicial(Tela):
    """
    Essa classe é responsável pela interface do menu incial, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por criar a tela existente do menu inicial

        Entrada: objeto da classe MenuInicial, objeto da classe Historico

        Saída: Nenhuma
        """
        self.hist = hist
        self.titulo = "Bem Vindo ao Campo Minado"
        self.opcoes = ("(1) Novo Jogo", "(2) Carregar Jogo", "(3) Opções", "(4) Manual do Desenvolvedor",
                       "(5) Estatísticas")
        menu_inicial = Tela(self.titulo, self.opcoes, self.hist).__init__(self.titulo, self.opcoes, self.hist)

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de MenuInicial.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return MenuInicial.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de MenuInicial.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return MenuInicial.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de MenuInicial.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = MenuInicial.__init__.__doc__
        manual["getManual"] = MenuInicial.getManual.__doc__
        manual["getAtributos"] = MenuInicial.getAtributos.__doc__
        manual["getMetodos"] = MenuInicial.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual
