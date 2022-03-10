import matplotlib.pyplot as plt
import numpy as np
from tela import *


class MenuEstatisticas(Tela):
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
    
    def grafico_abertas_jogadas_partida(self, estatisticas):
        """
        Método responsável por criar o gráfico de casas abertas por jogadas, plotando as partidas salvas nas
        estatísticas

        Entrada: objeto da classe Estatisticas

        Saída: bool, representando se o gráfico foi plotado ou não
        """
        estatisticas = estatisticas.carrega_estatisticas()
        plotato = False
        if estatisticas.any():
            fig, ax = plt.subplots()
            ax.set_title("Casas abertas x Jogadas")
            plt.xlabel("Jogada")
            plt.ylabel("Quantidade de casas abertas")
            qtd_total_casas_abertas = []
            for partida in estatisticas:
                label = partida[0]
                jogadas = partida[1]
                n_jogadas, qtd_casas_abertas, casas_abertas, qtd_casas_marcadas, casas_marcadas = jogadas
                qtd_total_casas_abertas.append(qtd_casas_abertas)
                ax.plot(range(1, n_jogadas+1), casas_abertas, label=label)
            plt.ylim([0, max(qtd_total_casas_abertas) + 1])
            ax.legend()
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        else:
            print("\nNão existe nenhuma estatística salva")
            input("\nAperte enter para continuar\n")
        return plotato
    
    def grafico_marcadas_jogadas_partida(self, estatisticas):
        """
        Método responsável por criar o gráfico de casas marcadas por jogadas, plotando as partidas salvas nas
        estatísticas

        Entrada: objeto da classe Estatisticas

        Saída: bool, representando se o gráfico foi plotado ou não
        """
        estatisticas = estatisticas.carrega_estatisticas()
        plotato = False
        if estatisticas.any():
            fig, ax = plt.subplots()
            ax.set_title("Casas marcadas x Jogadas")
            plt.xlabel("Jogada")
            plt.ylabel("Quantidade de casas marcadas")
            qtd_total_casas_marcadas = []
            for partida in estatisticas:
                label = partida[0]
                jogadas = partida[1]
                n_jogadas, qtd_casas_abertas, casas_abertas, qtd_casas_marcadas, casas_marcadas = jogadas
                qtd_total_casas_marcadas.append(qtd_casas_marcadas)
                ax.plot(range(1, n_jogadas+1), casas_marcadas, label=label)
            plt.ylim([0, max(qtd_total_casas_marcadas) + 1])
            ax.legend()
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        else:
            print("\nNão existe nenhuma estatística salva")
            input("\nAperte enter para continuar\n")
        return plotato
    
    def grafico_abertas_marcadas_partida(self, estatisticas):
        """
        Método responsável por criar o gráfico de casas marcadas por casas abertas, plotando as partidas salvas nas
        estatísticas

        Entrada: objeto da classe Estatisticas

        Saída: bool, representando se o gráfico foi plotado ou não
        """
        estatisticas = estatisticas.carrega_estatisticas()
        plotato = False
        if estatisticas.any():
            fig, ax = plt.subplots()
            ax.set_title("Casas abertas x Casas Marcadas")
            plt.xlabel("Quantidade de casas marcadas")
            plt.ylabel("Quantidade de casas abertas")
            qtd_total_casas_marcadas = []
            qtd_total_casas_abertas = []
            for partida in estatisticas:
                label = partida[0]
                jogadas = partida[1]
                n_jogadas, qtd_casas_abertas, casas_abertas, qtd_casas_marcadas, casas_marcadas = jogadas
                qtd_total_casas_marcadas.append(qtd_casas_marcadas)
                qtd_total_casas_abertas.append(qtd_casas_abertas)
                ax.plot(casas_marcadas, casas_abertas, label=label)
            plt.xlim([0, max(qtd_total_casas_marcadas) + 1])
            plt.ylim([0, max(qtd_total_casas_abertas) + 1])
            ax.legend()
            plt.show()
            Tela.limpaTela()
            plotato = True
            input("Aperte enter para continuar")
        else:
            print("\nNão existe nenhuma estatística salva")
            input("\nAperte enter para continuar\n")
        return plotato

    @staticmethod
    def getAtributos():
            """
            Esta função estática (chamada sempre através de MenuEstatisticas.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
            """
            return MenuEstatisticas.__atributos

    @staticmethod
    def getMetodos():
            """
            Esta função estática (chamada sempre através de MenuEstatisticas.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
            """
            return MenuEstatisticas.__metodos

    @staticmethod
    def getManual():
            """
            Esta função estática (chamada sempre através de MenuEstatisticas.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

            (None) -> dict
            """
            manual = dict()
            manual["__init__"] = MenuEstatisticas.__init__.__doc__
            manual["grafico_abertas_jogadas"] = MenuEstatisticas.grafico_abertas_jogadas_partida.__doc__
            manual["grafico_marcadas_jogadas"] = MenuEstatisticas.grafico_marcadas_jogadas_partida.__doc__
            manual["grafico_abertas_marcadas"] = MenuEstatisticas.grafico_abertas_marcadas_partida.__doc__
            manual["getManual"] = MenuEstatisticas.getManual.__doc__
            manual["getAtributos"] = MenuEstatisticas.getAtributos.__doc__
            manual["getMetodos"] = MenuEstatisticas.getMetodos.__doc__
            manual["hist"] = "# Representa o historico"
            manual["titulo"] = "# Representa o titulo da tela de dificuldades"
            manual["opcoes"] = "# Representa as opcoes da tela de dificuldades"
            return manual
