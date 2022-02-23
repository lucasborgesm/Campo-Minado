from criador_de_campo import *


class Campo:
    """
    Essa classe representa a funcionalidade do campo do jogo, sendo responsável por todas as mecânicas relacionadas
    diretamente com o que acontece no campo.
    """

    __atributos = {"hist", "tamanho", "n_bombas", "fechada", "bomba", "marcador", "campo", "mascara"}
    __metodos = {"__init__", "__str__", "abre_casa", "marca_casa", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, tamanho, n_bombas, hist, campo=None):
        """
        Inicializador responsável por criar todas as variáveis necessárias para a criação e funcionamento do campo e
        mascara do jogo Campo Minado

        Entrada: objeto da classe Campo, int, int, char, char, char, o primeiro representa o tamanho da matriz quadrada representando o campo
        do jogo, o segundo a quantidade de bombas que serão colocadas, o terceiro o símbolo responsável por representar
        as casas fechadas, o quarto o símbolo responsável por representar as bombas e o quinto o símbolo responsável
        por representar as casas marcadas

        Saída: Nenhuma
        """
        self.hist = hist
        self.tamanho = tamanho
        self.n_bombas = n_bombas
        self.fechada = "\u25A1"
        self.bomba = "b"
        self.marcador = "\u2705"
        if campo == None:
            self.campo = CriadorDeCampo().cria_campo(self.tamanho, self.n_bombas, self.bomba)
        else:
            self.campo = campo 
        self.mascara = CriadorDeCampo().cria_mascara(self.tamanho, self.fechada)

    def __str__(self):
        """
        Esse método é responsável pela representação em string do campo do jogo, pode ser usada também para
        representar a mascara do jogo, com finalidade de ajudar o desenvolvedor

        Entrada: objeto da classe Campo

        Saída: str, representando a mascara do jogo
        """
        campo_de_retorno = self.campo
        # campo_de_retorno = self.mascara
        campo_de_retorno_str = ""
        for i in campo_de_retorno:
            for aij in i:
                campo_de_retorno_str += f"{aij}"
            campo_de_retorno_str += "\n"
        return campo_de_retorno_str

    def abre_casa(self, i, j):
        """
        Esse método é responsável por abrir uma casa no jogo do Campo Minado

        Entrada: objeto da classe Campo, int, int, o primeiro representando a coordenada das linhas e o segundo das colunas da casa que se
        deseja abrir

        Saída: Nenhuma
        """
        self.hist.armazena_jogada_hist("a", i, j)
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

        Entrada: objeto da classe Campo, int, int, o primeiro representando a coordenada das linhas e o segundo das colunas da casa que se
        deseja marcar

        Saída: bool, mostrando se a casa foi marcada ou não
        """
        mascara = self.mascara
        fechada = self.fechada
        marcador = self.marcador
        if mascara[i][j] == fechada:
            mascara[i][j] = marcador
            self.hist.armazena_jogada_hist("m", i, j)
        elif mascara[i][j] == marcador:
            mascara[i][j] = fechada
            self.hist.armazena_jogada_hist("m", i, j)
        else:
            return False
        return True
    
    def verifica_derrota(self):
        """
        Esse método é responsável por verificar se o jogo acabou em derrota ou não, indentificando se alguma bomba
        foi aberta

        Entrada: objeto da classe Campo

        Saída: str, representando se a situação do jogo é derrota ou não
        """
        situacao = ""
        for i in self.mascara:
            for aij in i:
                if aij == self.bomba:
                    situacao = "derrota"
        return situacao
    
    def verifica_vitoria(self):
        """
        Método responsável por verificar se o jogo acabou em vitória ou não, indentificando se todas as casas vazias
        foram abertas

        Entrada: objeto da classe Campo

        Saída: str, representando se a situação do jogo é vitória ou não
        """
        situacao = ""
        if self.n_casas_abertas == (self.tamanho**2 - self.n_bombas):
            situacao = "vitoria"
        return situacao
    
    def getMascara(self):
        """
        Método responsável por retornar a máscara

        Entrada: objeto da classe Campo

        Saída: list, representando a máscara
        """
        return self.mascara
    
    def getBomba(self):
        """
        Método responsável por retornar o símbolo da bomba

        Entrada: objeto da classe Campo

        Saída: str, representando a bomba
        """
        return self.bomba

    def getFechada(self):
        """
        Método responsável por retornar o símbolo da casa fechada

        Entrada: objeto da classe Campo

        Saída: str, representando a casa fechada
        """
        return self.fechada
    
    def getTamanho(self):
        """
        Método responsável por retornar o tamanho do campo

        Entrada: objeto da classe Campo

        Saída: int, representando o tamanho do campo
        """
        return self.tamanho

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
        manual["verifica_derrota"] = Campo.verifica_derrota.__doc__
        manual["verifica_vitoria"] = Campo.verifica_vitoria.__doc__
        manual["getMascara"] = Campo.getMascara.__doc__
        manual["getBomba"] = Campo.getBomba.__doc__
        manual["getFechada"] = Campo.getFechada.__doc__
        manual["getTamanho"] = Campo.getTamanho.__doc__
        manual["getManual"] = Campo.getManual.__doc__
        manual["getAtributos"] = Campo.getAtributos.__doc__
        manual["getMetodos"] = Campo.getMetodos.__doc__
        manual["hist"] = "# Representa o histórico do jogo"
        manual["tamanho"] = "# Representa o tamanho do campo do jogo"
        manual["n_bombas"] = "# Representa o número de bombas do jogo"
        manual["fechada"] = "# Representa as casas fechadas no campo"
        manual["bomba"] = "# Representa as bombas no campo"
        manual["marcador"] = "# Representa as marcações no campo"
        manual["campo"] = "# Representa o campo"
        manual["mascara"] = "# Representa a mascara do campo"
        manual["n_casas_abertas"] = "# Representa o número casas que já foram abertas"
        return manual
