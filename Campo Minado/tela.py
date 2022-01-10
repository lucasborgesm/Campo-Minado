from interface_usuario import *
from ferramentas import *


class Tela(InterfaceUsuario):
    """
    Esta classe representa a tela que é mostrada ao usuário. Todas as possíveis telas
    usadas são objetos da classe Tela ou de subclasses dela.
    """

    __atributos = {"titulo", "opcoes"}
    __metodos = {"__init__", "__str__", "menu_inicial", "menu_de_pause", "menu_save_load", "menu_opcoes",
                 "menu_estatisticas", "pinta_campo", "tela_vitoria", "tela_derrota", "desenha_tela",
                 "getOpcaoEscolhida", "getManual", 'getAtributos', 'getMetodos'}

    def __init__(self, titulo, opcoes):
        """
        Inicializador da classe, definindo o titulo e as opcoes

        Entrada: str, iter, o primeiro representando o nome da tela que será apresentada e o segundo um iterável com
        todas as opções que serão disponibilizadas

        Saída: Nenhuma
        """
        InterfaceUsuario().__init__()
        self.titulo = titulo
        self.opcoes = opcoes

    def __str__(self):
        """
        Esse método é responsável pela representação em string.

        Entrada: Nenhuma

        Saída: str, representando o que será enviado para a tela
        """
        tela_str = ""
        tela_str += f"{self.titulo}\n\n"
        for opcao in self.opcoes:
            tela_str += f"{opcao}\n"
        return tela_str

    def desenha_tela(self):
        """
        Esta função atualiza a tela no console após ocorrer alguma modificação,
        limpando a tela e em seguida printando sua versão em string.

        Entrada: Nenhuma

        Saída: Nenhuma
        """
        Ferramentas.limpaTela()
        print(self)

    def getOpcaoEscolhida(self):
        """
        Esta função lê a opção escolhida pelo usuário a partir do console e retorna
        a escolha.

        Entrada: Nenhuma

        Saída: int, representando a opção escolhida na tela pelo usuário
        """
        escolha = int(input())
        if escolha not in range(len(self.opcoes) + 1):
            print("Essa opção não é válida")
            self.getOpcaoEscolhida()
        return escolha

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Tela.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return __atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Tela.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return __metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Tela.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Tela.__init__.__doc__
        manual["__str__"] = Tela.__str__.__doc__
        manual["desenhaTela"] = Tela.desenha_tela.__doc__
        manual["getOpcaoEscolhida"] = Tela.getOpcaoEscolhida.__doc__
        manual["getManual"] = Tela.getManual.__doc__
        manual["getAtributos"] = Tela.getAtributos.__doc__
        manual["getMetodos"] = Tela.getMetodos.__doc__
        manual["titulo"] = "# Representa o título da tela"
        manual["opcoes"] = "# Representa a lista de opções do usuário"
        return manual
