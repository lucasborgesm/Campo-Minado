import matplotlib.pyplot as plt
import numpy as np
from tela import *


class Estatisticas(Tela):
    """
    Classe responsável por coletar dados salvos do histórico e tratá-los para exibir gráficos mostrando as estatíticas
    das partidas jogadas.
    """

    __atributos = {"hist", "titulo", "opcoes"}
    __metodos = {"__init__", "retorna_estatisticas", "grafico_abertas_jogadas", "grafico_marcadas_jogadas",
                 "grafico_abertas_marcadas", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, hist):
        """
        Inicializador responsável por inicializar as variáveis necessárias e criar um objeto da classe Tela para criar
        a interface do menu de estatísticas

        Entrada: objeto da classe Estatisticas, objeto da classe Historico

        Saída: Nenhuma
        """
        self.hist = hist
        self.titulo = "Estatísticas"
        self.opcoes = ("(1) Casas abertas x Jogadas", "(2) Casas marcadas x Jogadas",
                       "(3) Casas marcadas x Casas abertas", "(4) Voltar")
        Tela(self.titulo, self.opcoes, self.hist).__init__(self.titulo, self.opcoes, self.hist)
    
    # def salva_estatisticas(self):
    #     """
    #     Método responsável por salvar as informações necessárias para as estatísticas através do numpy
    #
    #     Entrada: objeto da classe Estatisticas
    #
    #     Saída: Nenhuma
    #     """
    #     n_jogadas, qtd_casas_abertas, total_qtd_casas_abertas, qtd_casas_marcadas, total_qtd_casas_marcadas = self.hist.retorna_jogadas()
    #     casas_abertas = np.array(total_qtd_casas_abertas)
    #     np.save("casas_abertas.npy", casas_abertas)
    #     casas_marcadas = np.array(total_qtd_casas_marcadas)
    #     np.save("casas_marcadas.npy", casas_marcadas)
    #     jogadas = np.array(i for i in range(1, n_jogadas + 1))
    #     np.save("jogadas.npy", jogadas)

    def retorna_estatisticas(self):
        """
        Método responsável por retornar as informações necessárias para as estatíticas retiradas do histórico

        Entrada: objeto da classe Estatisticas

        Saída: tuple, contendo as informações das casas apertas, casas marcadas e jogadas
        """

        retorno = self.hist.retorna_jogadas()
        if retorno:
            n_jogadas, qtd_casas_abertas, total_qtd_casas_abertas, qtd_casas_marcadas, total_qtd_casas_marcadas = retorno
            casas_abertas = np.array(total_qtd_casas_abertas)
            casas_marcadas = np.array(total_qtd_casas_marcadas)
            jogadas = np.array([i for i in range(1, n_jogadas + 1)])
            return casas_abertas, casas_marcadas, jogadas
        else:
            return False

    # def carrega_estatisticas(self):
    #     """
    #     Método responsável por carregar as informações anteriormente salvas das estatísticas
    #
    #     Entrada: objeto da classe Estatisticas
    #
    #     Saída: tuple, contendo as informações das casas apertas, casas marcadas e jogadas
    #     """
    #     casas_abertas = np.load("casas_abertas.npy")
    #     casas_marcadas = np.load("casas_marcadas.npy")
    #     jogadas = np.load("jogadas.npy")
    #     return casas_abertas, casas_marcadas, jogadas
    
    def grafico_abertas_jogadas(self):
        """
        Método responsável por criar o gráfico de casas abertas por jogadas

        Entrada: objeto da classe Estatisticas

        Saída: Nenhuma
        """
        estatisticas = self.retorna_estatisticas()
        plotato = False
        if estatisticas:
            casas_abertas, casas_marcadas, jogadas = estatisticas
            fig, ax = plt.subplots()
            ax.plot(jogadas, casas_abertas)
            ax.set_xticks(range(0, jogadas[-1] + 1))
            ax.set_yticks(range(0, casas_abertas[-1] + 1))
            plt.xlim(0, jogadas[-1] + 1)
            plt.ylim(0, casas_abertas[-1] + 1)
            ax.set_title("Casas abertas x Jogadas")
            plt.xlabel("Jogada")
            plt.ylabel("Quantidade de casas abertas")
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        return plotato
    
    def grafico_marcadas_jogadas(self):
        """
        Método responsável por criar o gráfico de casas marcadas por jogadas

        Entrada: objeto da classe Estatisticas

        Saída: Nenhuma
        """
        estatisticas = self.retorna_estatisticas()
        plotato = False
        if estatisticas:
            casas_abertas, casas_marcadas, jogadas = estatisticas
            fig, ax = plt.subplots()
            ax.plot(jogadas, casas_marcadas)
            ax.set_xticks(range(0, jogadas[-1] + 1))
            ax.set_yticks(range(0, casas_marcadas[-1] + 1))
            plt.xlim(0, jogadas[-1] + 1)
            plt.ylim(0, casas_marcadas[-1] + 1)
            ax.set_title("Casas marcadas x Jogadas")
            plt.xlabel("Jogada")
            plt.ylabel("Quantidade de casas marcadas")
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        return plotato
    
    def grafico_abertas_marcadas(self):
        """
        Método responsável por criar o gráfico de casas marcadas por casas abertas

        Entrada: objeto da classe Estatisticas

        Saída: Nenhuma
        """
        estatisticas = self.retorna_estatisticas()
        plotato = False
        if estatisticas:
            casas_abertas, casas_marcadas, jogadas = estatisticas
            fig, ax = plt.subplots()
            ax.plot(casas_abertas, casas_marcadas)
            ax.set_xticks(range(0, casas_abertas[-1] + 1))
            ax.set_yticks(range(0, casas_marcadas[-1] + 1))
            plt.xlim(0, casas_abertas[-1] + 1)
            plt.ylim(0, casas_marcadas[-1] + 1)
            ax.set_title("Casas marcadas x Casas abertas")
            plt.xlabel("Quantidade de casas abertas")
            plt.ylabel("Quantidade de casas marcadas")
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        return plotato

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
            manual["__init__"] = Estatisticas.__init__.__doc__
            manual["retorna_estatisticas"] = Estatisticas.retorna_estatisticas.__doc__
            manual["grafico_abertas_jogadas"] = Estatisticas.grafico_abertas_jogadas.__doc__
            manual["grafico_marcadas_jogadas"] = Estatisticas.grafico_marcadas_jogadas.__doc__
            manual["grafico_abertas_marcadas"] = Estatisticas.grafico_abertas_marcadas.__doc__
            manual["getManual"] = Estatisticas.getManual.__doc__
            manual["getAtributos"] = Estatisticas.getAtributos.__doc__
            manual["getMetodos"] = Estatisticas.getMetodos.__doc__
            manual["hist"] = "# Representa o historico"
            manual["titulo"] = "# Representa o titulo da tela de dificuldades"
            manual["opcoes"] = "# Representa as opcoes da tela de dificuldades"
            return manual
