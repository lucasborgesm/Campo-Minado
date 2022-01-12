import os
os.system("color")


class InterfaceUsuario:
    """
    Esta super classe inclui todos os métodos e atributos que são úteis para qualquer
    interface que pode ser feita com o usuário.

    Em partes adaptado de https://www.codegrepper.com/code-examples/python/python+ansi+colors
    Acesso em 02/01/2022
    """

    __atributos = {"tabelaCaracteres", "pref", "reset", "black", "red", "green", "yellow", "blue", "magenta", "cyan",
                   "white"}
    __metodos = {"__init__", "str_ansi", "print", "getAtributos", "getMetodos", "getManual"}

    def __init__(self):
        """
        Inicializador da classe. Inicializa um dicionario que associa os indices de 0 a
        255 (inclusive) a todos os primeiros 256 caracteres que o cmd do windows reconhece.
        Tambem seta os atributos das cores ANSI. Eles são úteis para escrever caracteres
        coloridos.

        Adaptado de https://www.codegrepper.com/code-examples/python/python+ansi+colors
        Acesso em 02/01/2022

        Entrada: Nenhuma

        Saída: Nenhuma
        """
        self.tabelaCaracteres = {x: chr(x) for x in range(256)}
        self.pref = "\033["
        self.reset = f"{self.pref}0m"
        self.black = "30m"
        self.red = "31m"
        self.green = "32m"
        self.yellow = "33m"
        self.blue = "34m"
        self.magenta = "35m"
        self.cyan = "36m"
        self.white = "37m"

    def str_ansi(self, text, color=None, is_bold=False):
        """
        Retorna a string 'text' na cor setada por 'color' e 'is_bold'.

        Entrada: str, str, bool, o primeiro representa o texto, o segundo a cor em inglês e o terceiro se o texto que
        se deseja escrever será em negrito ou não

        Saída: str, com as características desejadas
        """
        if color.upper() == "BLACK":
            color = self.black
        elif color.upper() == "RED":
            color = self.red
        elif color.upper() == "GREEN":
            color = self.green
        elif color.upper() == "YELLOW":
            color = self.yellow
        elif color.upper() == "BLUE":
            color = self.blue
        elif color.upper() == "MAGENTA":
            color = self.magenta
        elif color.upper() == "CYAN":
            color = self.cyan
        else:
            color = self.white
        return f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset

    def print(self, text, color=None, is_bold=False):
        """
        Printa na tela a string 'text' na cor setada por 'color' e 'is_bold'.

        Entrada: str, str, bool, o primeiro representa o texto, o segundo a cor em inglês e o terceiro se o texto que
        se deseja imprimir será em negrito ou não

        Saída: Nenhuma
        """
        if color.upper() == "BLACK":
            color = self.black
        elif color.upper() == "RED":
            color = self.red
        elif color.upper() == "GREEN":
            color = self.green
        elif color.upper() == "YELLOW":
            color = self.yellow
        elif color.upper() == "BLUE":
            color = self.blue
        elif color.upper() == "MAGENTA":
            color = self.magenta
        elif color.upper() == "CYAN":
            color = self.cyan
        else:
            color = self.white
        print(f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset)

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Tela.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return InterfaceUsuario.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Tela.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return InterfaceUsuario.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de InterfaceUsuario.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = InterfaceUsuario.__init__.__doc__
        manual["str_ansi"] = InterfaceUsuario.str_ansi.__doc__
        manual["print"] = InterfaceUsuario.print.__doc__
        manual["getManual"] = InterfaceUsuario.getManual.__doc__
        manual["getAtributos"] = InterfaceUsuario.getAtributos.__doc__
        manual["getMetodos"] = InterfaceUsuario.getMetodos.__doc__
        manual["tabelaCaracteres"] = "# Representa todos os primeiros 256 caracteres que o cmd do windows reconhece"
        manual["pref"] = "# Representa a primeira parte do código para mudar a cor dos textos"
        manual["reset"] = "# Representa o código para retornar as configurações do texto para padrão"
        manual["black"] = "# Representa o código para tornar a cor do texto preta"
        manual["red"] = "# Representa o código para tornar a cor do texto vermelha"
        manual["green"] = "# Representa o código para tornar a cor do texto verde"
        manual["yellow"] = "# Representa o código para tornar a cor do texto amarela"
        manual["blue"] = "# Representa o código para tornar a cor do texto azul"
        manual["magenta"] = "# Representa o código para tornar a cor do texto magenta"
        manual["cyan"] = "# Representa o código para tornar a cor do texto ciana"
        manual["white"] = "# Representa o código para tornar a cor do texto branca"
        return manual
