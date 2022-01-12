from criador_de_campo import *


class Campo:
    """
    Essa classe representa a funcionalidade do campo do jogo, sendo responsável por todas as mecânicas relacionadas
    diretamente com o que acontece no campo.
    """

    __atributos = {"tamanho", "n_bombas", "fechada", "bomba", "marcador", "campo", "mascara", "n_casas_abertas"}
    __metodos = {"__init__", "__str__", "abre_casa", "marca_casa", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, tamanho, n_bombas, fechada="\u25A1", bomba="b", marcador="\u2705"):
        """
        Inicializador responsável por criar todas as variáveis necessárias para a criação e funcionamento do campo e
        mascara do jogo Campo Minado

        Entrada: int, int, char, char, char, o primeiro representa o tamanho da matriz quadrada representando o campo
        do jogo, o segundo a quantidade de bombas que serão colocadas, o terceiro o símbolo responsável por representar
        as casas fechadas, o quarto o símbolo responsável por representar as bombas e o quinto o símbolo responsável
        por representar as casas marcadas

        Saída: Nenhuma
        """
        self.tamanho = tamanho
        self.n_bombas = n_bombas
        self.fechada = fechada
        self.bomba = bomba
        self.marcador = marcador
        self.campo = CriadorDeCampo().cria_campo(self.tamanho, self.n_bombas, self.bomba)
        self.mascara = CriadorDeCampo().cria_mascara(self.tamanho, self.fechada)
        self.n_casas_abertas = 0

    def __str__(self):
        """
        Esse método é responsável pela representação em string da mascara do jogo, pode ser usada também para
        representar o campo do jogo, com finalidade de ajudar o desenvolvedor

        Entrada: Nenhuma

        Saída: str, representando a mascara do jogo
        """
        # campo_de_retorno = self.campo
        campo_de_retorno = self.mascara
        campo_de_retorno_str = ""
        for i in campo_de_retorno:
            campo_de_retorno_str += "|\t"
            for aij in i:
                campo_de_retorno_str += f"{aij}\t"
            campo_de_retorno_str += "|\n"
        return campo_de_retorno_str

    def abre_casa(self, i, j):
        """
        Esse método é responsável por abrir uma casa no jogo do Campo Minado

        Entrada: int, int, o primeiro representando a coordenada das linhas e o segundo das colunas da casa que se
        deseja abrir

        Saída: Nenhuma
        """
        campo = self.campo
        mascara = self.mascara
        tamanho = self.tamanho
        bomba = self.bomba
        fechada = self.fechada
        marcador = self.marcador
        if mascara[i][j] == fechada or mascara[i][j] == marcador:
            mascara[i][j] = campo[i][j]
            self.n_casas_abertas += 1
            if campo[i][j] == 0:
                vizinhos = CriadorDeCampo().entorno(tamanho, i, j)
                for casa in vizinhos:
                    if campo[casa[0]][casa[1]] != bomba and mascara[casa[0]][casa[1]] == fechada \
                            or mascara[casa[0]][casa[1]] == marcador:
                        self.abre_casa(casa[0], casa[1])

    def marca_casa(self, i, j):
        """
        Esse método é responsável por marcar uma casa no jogo do Campo minado

        Entrada: int, int, o primeiro representando a coordenada das linhas e o segundo das colunas da casa que se
        deseja marcar

        Saída: bool, mostrando se a casa foi marcada ou não
        """
        mascara = self.mascara
        fechada = self.fechada
        marcador = self.marcador
        if mascara[i][j] == fechada:
            mascara[i][j] = marcador
        elif mascara[i][j] == marcador:
            mascara[i][j] = fechada
        else:
            return False
        return True

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Campo.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Campo.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Campo.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Campo.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Campo.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Campo.__init__.__doc__
        manual["__str__"] = Campo.__str__.__doc__
        manual["abre_casa"] = Campo.abre_casa.__doc__
        manual["marca_casa"] = Campo.marca_casa.__doc__
        manual["getManual"] = Campo.getManual.__doc__
        manual["getAtributos"] = Campo.getAtributos.__doc__
        manual["getMetodos"] = Campo.getMetodos.__doc__
        manual["tamanho"] = "# Representa o tamanho do campo do jogo"
        manual["n_bombas"] = "# Representa o número de bombas do jogo"
        manual["fechada"] = "# Representa as casas fechadas no campo"
        manual["bomba"] = "# Representa as bombas no campo"
        manual["marcador"] = "# Representa as marcações no campo"
        manual["campo"] = "# Representa o campo"
        manual["mascara"] = "# Representa a mascara do campo"
        manual["n_casas_abertas"] = "# Representa o número casas que já foram abertas"
        return manual
