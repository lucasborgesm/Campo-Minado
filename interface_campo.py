from tela import *


class InterfaceCampo(Tela):
    """
    Classe responsável pela interface do campo, mostrando o campo e todas as suas alterações
    """

    __atributos = {"hist", "campo"}
    __metodos = {"__init__", "mostra_campo", "pergunta_posicao", "derrota", "vitoria", "getAtributos", "getMetodos",
                 "getManual"}

    def __init__(self, campo, hist):
        """
        Inicializador responsável por definir todas as variáveis necessárias

        Entrada: objeto da classe InterfaceCampo, objeto da classe Campo, objeto da classe Historico

        Saída: Nenhuma
        """
        self.hist = hist
        self.campo = campo

    def mostra_campo(self):
        """
        Método responsável por utilizar a representação em string do campo e tratá-la para ter maior interatividade
        visual

        Entrada: objeto da classe InterfaceCampo

        Saída: Nenhuma
        """
        self.limpaTela()
        campo_de_retorno = self.campo.getMascara()
        campo_de_retorno_str = ""
        pos_j = 0
        ciano = "\033[1;36m"
        azul = "\033[1;34m"
        verde = "\033[0;32m"
        vermelho = "\033[1;31m"
        reset = "\033[0;0m"
        for i in campo_de_retorno:
            for aij in i:
                if pos_j == 0:
                    campo_de_retorno_str += "|\t"
                if type(aij) == int:
                    if aij == 0:
                        campo_de_retorno_str += verde + f"{aij}" + reset + "\t"
                        pos_j += 1
                    else:
                        campo_de_retorno_str += azul + f"{aij}" + reset + "\t"
                        pos_j += 1
                elif aij == self.campo.getBomba():
                    campo_de_retorno_str += vermelho + f"{aij}" + reset + "\t"
                    pos_j += 1
                elif aij == self.campo.getFechada():
                    campo_de_retorno_str += ciano + f"{aij}" + reset + "\t"
                    pos_j += 1
                else:
                    campo_de_retorno_str += ciano + f"{aij}" + reset + "\t"
                    pos_j += 1
                if pos_j >= len(campo_de_retorno):
                    pos_j = 0
            campo_de_retorno_str += "|\n"
        print(campo_de_retorno_str)

    def pergunta_posicao(self):
        """
        Método responsável por interagir com o usuário e receber a posição desejada para uma jogada

        Entrada: objeto da classe InterfaceCampo

        Saída: tuple, com as coordenadas desejadas
        """
        print("\nDigite a posição da casa, primeiro a linha, depois a coluna")
        while True:
            try:
                i = int(input("\nQual a linha?\n"))
                if i > self.campo.getTamanho() or i < 1:
                    raise PosicaoInvalida
                j = int(input("\nQual a coluna?\n"))
                if j > self.campo.getTamanho() or j < 1:
                    raise PosicaoInvalida
                return i - 1, j - 1
            except ValueError:
                self.hist.armazena_log(f"Value Error|Digite um número representando a posição, começando a contar de cima pra baixo e da esquerda para direita|"
                                        f"{datetime.today()}\n")
                print("Digite um número representando a posição, começando a contar de cima pra baixo e da esquerda para direita")
            except PosicaoInvalida:
                self.hist.armazena_log(f"PosicaoInvalida|A posição dada é inválida, digite um número entre 1 e {self.campo.getTamanho()}|"
                                        f"{datetime.today()}\n")
                print(f"A posição dada é inválida, digite um número entre 1 e {self.campo.getTamanho()}")

    def derrota(self):
        """
        Método responsável pela mensagem de derrota

        Entrada: objeto da classe InterfaceCampo

        Saída: Nenhuma
        """
        print("\n")
        print("        88                                                             ")
        print("        88                                                             ")
        print("        88                                                             ")
        print("        88,dPPYba,   ,adPPYba,   ,adPPYba,  88,dPYba,,adPYba,          ")
        print("        88P'    '8a a8'     '8a a8'     '8a 88P'   '88'    '8a         ")
        print("        88       d8 8b       d8 8b       d8 88      88      88         ")
        print("        88b,   ,a8' '8a,   ,a8' '8a,   ,a8' 88      88      88         ")
        print("        8Y'Ybbd8''   `'YbbdP''   `'YbbdP''  88      88      88         ")
        print("\n")
        print("\n")
        print("                              SINTO MUITO                              ")
        print("                              VOCÊ PERDEU                              ")
        print("\n")


    def vitoria(self):
        """
        Método responsável pela mensagem de vitória

        Entrada: objeto da classe InterfaceCampo

        Saída: Nenhuma
        """
        print("\n")
        print("              88                                                       ")
        print("              ''              ,d                                       ")
        print("                              88                                       ")
        print("  8b       d8 88  ,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba, 8b       d8  ")
        print("  `8b     d8' 88 a8'     ''   88   a8'     '8a 88P'   'Y8 `8b     d8'  ")
        print("   `8b   d8'  88 8b           88   8b       d8 88          `8b   d8'   ")
        print("    `8b,d8'   88 '8a,   ,aa   88,  '8a,   ,a8' 88           `8b,d8'    ")
        print("      '8'     88  `'Ybbd8''   'Y888 `'YbbdP''  88             Y88'     ")
        print("                                                              d8'      ")
        print("                                                             d8'       ")
        print("\n")
        print("     ___________                                                       ")
        print("    '._==_==_=_.'                                                      ")
        print("    .-\:       /-.                                                     ")
        print("   | (|:.     |) |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ")
        print("    '-|:.     |-'           ================PARABÉNS===============    ")
        print("      \::.    /             ==============VOCÊ VENCEU!=============    ")
        print("       '::. .'              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ")
        print("         ) (                                                           ")
        print("       _.' '._                                                         ")
        print("       '''''''                                                         ")
        print("\n")

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de InterfaceCampo.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return InterfaceCampo.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de InterfaceCampo.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return InterfaceCampo.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de InterfaceCampo.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = InterfaceCampo.__init__.__doc__
        manual["mostra_campo"] = InterfaceCampo.mostra_campo.__doc__
        manual["pergunta_posicao"] = InterfaceCampo.pergunta_posicao.__doc__
        manual["derrota"] = InterfaceCampo.derrota.__doc__
        manual["vitoria"] = InterfaceCampo.vitoria.__doc__
        manual["getManual"] = InterfaceCampo.getManual.__doc__
        manual["getAtributos"] = InterfaceCampo.getAtributos.__doc__
        manual["getMetodos"] = InterfaceCampo.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["campo"] = "# Representa o campo"
        return manual



class PosicaoInvalida(Exception):
    """
    Erro para quando a posição do campo dada for inválida
    """
    pass
