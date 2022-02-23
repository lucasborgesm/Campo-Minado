from datetime import datetime
from logging import exception


class Historico:
    """
    Esta classe representa o histórico de ações que o usuário fez, guardando todas sua jogadas, como casas abertas e
    marcada. Além disso, também armazena o histórico de erros, o log.
    """

    __atributos = {"hist", "log"}
    __metodos = {"__init__", "reinicia_historico", "armazena_nome_jogador", "armazena_jogada_hist", "armazena_log",
                 "retorna_nome", "retorna_jogadas", "getAtributos", "getMetodos", "getManual"}

    def __init__(self):
        """
        Inicializador responsável por criar os arquivos que irão armazenar os históricos

        Entrada: objeto da classe Historico

        Saída: Nenhuma
        """

        self.hist = "historico.txt"
        self.log = "log.txt"
    
    def reinicia_historico(self):
        """
        Método responsável por apagar todo o histórico

        Entrada: objeto da classe Historico

        Saída: Nenhuma
        """
        open("historico.txt", "w").close()
    
    def armazena_nome_jogador(self, jogador):
        """
        Método responsável por armazenar o nome do jogador no histórico

        Entrada: objeto da classe Historico, objeto da classe Jogador

        Saída: Nenhuma
        """
        arquivo = open(self.hist, "w")
        arquivo.write(jogador.getNick() + "\n")
        arquivo.close()

    def armazena_jogada_hist(self, modo, i, j):
        """
        Método responsável por armazenar as jogadas no histórico

        Entrada: objeto da classe Historico, str (representando o tipo da jogada), int (representando a coordenada da
        linha), int (representando a coordenada da coluna)

        Saída: Nenhuma
        """
        arquivo = open(self.hist, "a")
        arquivo.write(modo + f"({i},{j})\n")
        arquivo.close()

    def armazena_log(self, erro):
        """
        Método responsável por armazenar o log

        Entrada: objeto da classe Historico, str (detalhando o erro)

        Saída: Nenhuma
        """
        arquivo = open(self.log, "a")
        arquivo.write(erro)
        arquivo.close()
    
    def retorna_nome(self):
        """
        Método responsável por retornar o nome do jogador do histórico

        Entrada: objeto da classe Historico

        Saída: str, contendo o nome
        """
        arquivo = open(self.hist)
        linhas = arquivo.readlines()
        nome = linhas[0]
        arquivo.close()
        return nome

    def retorna_jogadas(self):
        """
        Método responsável por retornar as jogadas salvas no histórico

        Entrada: objeto da classe Historico

        Saída: tuple, contendo as informações das jogadas, das casas abertas e das casas marcadas
        """
        try:
            arquivo = open(self.hist)
            linhas = arquivo.readlines()
            n_linhas = sum(linhas)
            if n_linhas == 0:
                raise ArquivoVazio
            jogadas = linhas[1:]
            qtd_casas_abertas = 0
            total_qtd_casas_abertas = []
            qtd_casas_marcadas = 0
            total_qtd_casas_marcadas = []
            n_jogadas = 0
            for jogada in jogadas:
                if jogada[0] == "a":
                    qtd_casas_abertas += 1
                elif jogada[0] == "m":
                    qtd_casas_marcadas += 1
                total_qtd_casas_abertas.append(qtd_casas_abertas)
                total_qtd_casas_marcadas.append(qtd_casas_marcadas)
                n_jogadas += 1
            return n_jogadas, qtd_casas_abertas, total_qtd_casas_abertas, qtd_casas_marcadas, total_qtd_casas_marcadas
        except FileNotFoundError:
            self.armazena_log(f"{datetime.today()}\n"
                                   f"        FileNotFoundError\n"
                                   f"        Não houve nenhum jogo anterior para ver as estatíticas.\n"
                                   f"        O usuário foi levado novamente ao menu_principal\n")
            print("Não houve nenhum jogo anterior para ver as estatíticas.\n")
            input("Pressione enter para continuar\n")
        except ArquivoVazio:
            self.armazena_log(f"{datetime.today()}\n"
                                   f"        FileNotFoundError"
                                   f"        Não houve nenhum jogo anterior para ver as estatíticas.\n"
                                   f"        O usuário foi levado novamente ao menu_principal\n")
            print("Não houve nenhum jogo anterior para ver as estatíticas.\n")
            input("Pressione enter para continuar\n")
        return False

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Historico.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Historico.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Historico.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Historico.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Historico.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Historico.__init__.__doc__
        manual["reinicia_historico"] = Historico.reinicia_historico.__doc__
        manual["armazena_nome_jogador"] = Historico.armazena_nome_jogador.__doc__
        manual["armazena_jogada_hist"] = Historico.armazena_jogada_hist.__doc__
        manual["armazena_log"] = Historico.armazena_log.__doc__
        manual["retorna_nome"] = Historico.retorna_nome.__doc__
        manual["retorna_jogadas"] = Historico.retorna_jogadas.__doc__
        manual["getManual"] = Historico.getManual.__doc__
        manual["getAtributos"] = Historico.getAtributos.__doc__
        manual["getMetodos"] = Historico.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["log"] = "# Representa o log"
        return manual
    

class ArquivoVazio(Exception):
    """
    Erro para quando o arquivo passado estiver vazio
    """
    pass
