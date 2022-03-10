import numpy as np
from datetime import date
from historico import *


class Estatisticas:
    """
    Esta classe representa as informações necessárias para armazenar e disponibilizar as estatísticas para o usuário,
    guardando todas sua jogadas, como casas abertas e marcadas, em cada partida terminada de cada usuário.
    """

    __atributos = {"hist", "estatisticas"}
    __metodos = {"__init__", "salva_estatisticas", "carrega_estatisticas", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por criar os arquivos que irão armazenar os históricos

        Entrada: objeto da classe Estatistica, objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = hist
        self.estatistica = "estatistica.npy"
    
    def salva_estatisticas(self):
        """
        Método responsável por salvar as estatísticas necessárias através do histórico sempre que um jogo termina

        Entrada: objeto da classe Estatisticas

        Saída: Nenhuma
        """
        stat_nova = np.array([[f"{self.hist.retorna_nome()} {date.today()} {datetime.now().hour:02d}"
                               f":{datetime.now().minute:02d}", self.hist.retorna_jogadas()]], dtype=object)
        try:
            stat_antiga = np.load(self.estatistica, allow_pickle=True)
            stat = np.append(stat_antiga, stat_nova, axis=0)
        except FileNotFoundError:
            self.hist.armazena_log(f"{datetime.today()}\n"
                                   f"        FileNotFoundError"
                                   f"        Não existe nenhum arquivo de estatísticas."
                                   f"        Nenhuma estatística antiga foi carregada.")
            stat = stat_nova
        np.save(self.estatistica, stat)
    
    def carrega_estatisticas(self):
        """
        Método responsável por carregar as estatísticas

        Entrada: objeto da classe Estatisticas

        Saída: array
        """
        try:
            stat = np.load(self.estatistica, allow_pickle=True)
            return stat
        except FileNotFoundError:
            self.hist.armazena_log(f"{datetime.today()}\n"
                                   f"        FileNotFoundError"
                                   f"        Não existe nenhum arquivo de estatísticas."
                                   f"        Nenhuma estatística antiga foi carregada.")
            return np.array([False])
    
    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Estatisticas.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Estatisticas.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Estatisticas.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Estatisticas.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Estatisticas.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["salva_estatisticas"] = Estatisticas.salva_estatisticas.__doc__
        manual["carrega_estatisticas"] = Estatisticas.carrega_estatisticas.__doc__
        manual["getManual"] = Estatisticas.getManual.__doc__
        manual["getAtributos"] = Estatisticas.getAtributos.__doc__
        manual["getMetodos"] = Estatisticas.getMetodos.__doc__
        return manual
            
