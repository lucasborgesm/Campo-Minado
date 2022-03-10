from tela import Tela
from datetime import datetime


class Opcoes(Tela):
    """
    Essa classe é responsável pela interface do menu de opções, herdando a classe Tela
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "altera_dificuldades", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por criar a tela existente do menu de opções

        Entrada: objeto da classe Opcoes, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.titulo = "Menu de opções"
        self.opcoes = ("(1) Jogar Campo Personalizado", "(2) Voltar")
        Tela(self.titulo, self.opcoes, hist).__init__(self.titulo, self.opcoes, self.hist)
    
    def altera_dificuldades(self):
        """
        Método responsável por criar uma dificuldade personalizada para jogar em um campo personalizado

        Entrada: objeto da classe Opcoes

        Saída: int (representando o tamanho do campo), int (representando o número de bombas do campo)
        """
        while True:
            print("\nQual será o tamanho do campo? (Precisa ser maior do que 1)\n")
            tamanho = input()
            tamanho = int(tamanho)
            if tamanho <= 1:
                raise ValorTamanhoInvalido
            break
        while True:
            print("\nQual será a quantidade de bombas?\n")
            n_bombas = input()
            n_bombas = int(n_bombas)
            if n_bombas <= 0 or n_bombas >= tamanho**2:
                raise ValorNumeroDeBombasInvalido
            break
        print("\nCampo personalizado criado\n")
        input("Aperte enter para começar o jogo")
        return tamanho, n_bombas

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
        manual["altera_dificuldades"] = Opcoes.__init__.__doc__
        manual["getManual"] = Opcoes.getManual.__doc__
        manual["getAtributos"] = Opcoes.getAtributos.__doc__
        manual["getMetodos"] = Opcoes.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["titulo"] = "# Representa o titulo da tela de jogada"
        manual["opcoes"] = "# Representa as opcoes da tela de jogada"
        return manual


class ValorTamanhoInvalido(Exception):
    """
    Erro para quando o valor do tamanho passado for inválido
    """
    pass


class ValorNumeroDeBombasInvalido(Exception):
    """
    Erro para quando o valor do número de bombas passado for inválido
    """
    pass
