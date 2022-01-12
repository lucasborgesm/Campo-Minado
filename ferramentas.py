import os


class Ferramentas:
    """
        Esta super classe inclui todos os métodos que podem vir a ser úteis para a
        mecânica do jogo, independente das classes criadas para o jogo específico.
    """

    __atributos = {}
    __metodos = {"limpa_tela", "getAtributos", "getMetodos", "getManual"}

    @staticmethod
    def limpaTela():
        """
            Esta função limpa toda a tela do console do Windows. 
            Com isso, é possível dar 'refresh' na tela a ser desenhada.

            (None) -> (None)
        """
        os.system('cls')

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Ferramentas.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Ferramentas.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Ferramentas.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Ferramentas.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Ferramentas.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["limpaTela"] = Ferramentas.limpaTela.__doc__
        manual["getManual"] = Ferramentas.getManual.__doc__
        manual["getAtributos"] = Ferramentas.getAtributos.__doc__
        manual["getMetodos"] = Ferramentas.getMetodos.__doc__
        return manual
