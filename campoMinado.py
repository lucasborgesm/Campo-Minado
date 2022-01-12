"""
Esse programa consiste no jogo Campo Minado.

"A área de jogo consiste num campo de quadrados retangular. Cada quadrado pode ser revelado,
 e se o quadrado contiver uma mina, então o jogo acaba."
"O jogo é ganho quando todos os quadrados que não têm minas são revelados."
"Opcionalmente, o jogador pode marcar qualquer quadrado que acredita que contém uma mina."
Fonte : https://pt.wikipedia.org/wiki/Campo_minado

A partir dessa descrição breve do jogo, algumas opções podem ser escolhidas pelo usuário:
- Tamanho do campo (padrão 10)
- Número de bombas no campo (padrão 10)

O campo é composto por uma matriz com n linhas e n colunas, sendo o valor n igual ao tamanho do campo.
"""


# Document properties
__author__ = "Lucas_Borges_Menezes"
__copyright__ = "Copyright_2022"
__credits__ = __author__
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = __author__
__email__ = "lucasborgesm@poli.ufrj.br"
__status__ = "Production"


from interface_usuario import *
from ferramentas import *
from tela import *
from jogador import *
from campo import *


class CampoMinado:
    """
    Essa classe envolve todas as classes de forma a garantir a funcionalidade do jogo. Desse modo, todos as classes
    são conectadas garantindo o funcionamento das mecânicas do jogo, bem como criando métodos para isso.
    """

    __atributos = {"tamanho", "n_bombas"}
    __metodos = {"__init__", "__str__", "jogada", "verifica_situacao", "getAtributos", "getMetodos", "getManual"}

    def __init__(self, tamanho=10, n_bombas=10):
        """
        Esse método inicia um novo jogo a partir das duas configurações de tamanho do campo e número de bombas

        Entrada: int, int, representando o tamanho da matriz quadrada que o campo do jogo é representado e a quantidade
        de bombas que haverão na partida

        Saída: Nenhuma
        """
        pass

    def __str__(self):
        """
        Esse método, usado para representação em string, retorna uma string contendo todas as descrições de todos os
        métodos e atributos das classes.

        Entrada: Nenhuma

        Saída: str, representando em todas as descrições de todos os métodos e atributos das classes
        """
        saida = ""

        # Manual da classe CampoMinado
        manual_campo_minado = CampoMinado.getManual()
        saida += "MANUAL DA CLASSE CAMPOMINADO\n"
        for chave in manual_campo_minado:
            saida += f"{chave} : {manual_campo_minado[chave]}\n"
        saida += "\n"

        # Manual da classe Tela
        manual_tela = Tela.getManual()
        saida += 'MANUAL DA CLASSE TELA\n'
        for chave in manual_tela:
            saida += f"{chave} : {manual_tela[chave]}\n"
        saida += "\n"

        # Manual da classe Jogador
        manual_jogador = Jogador.getManual()
        saida += 'MANUAL DA CLASSE JOGADOR\n'
        for chave in manual_jogador:
            saida += f"{chave} : {manual_jogador[chave]}\n"
        saida += "\n"

        # Manual da classe Campo
        manual_campo = Campo.getManual()
        saida += 'MANUAL DA CLASSE CAMPO\n'
        for chave in manual_campo:
            saida += f"{chave} : {manual_campo[chave]}\n"
        saida += "\n"

        # Manual da classe Ferramentas
        manual_ferramentas = Ferramentas.getManual()
        saida += 'MANUAL DA CLASSE FERRAMENTAS\n'
        for chave in manual_ferramentas:
            saida += f"{chave} : {manual_ferramentas[chave]}\n"
        saida += "\n"

        # Manual da classe InterfaceUsuario
        manual_interface_usuario = InterfaceUsuario.getManual()
        saida += 'MANUAL DA CLASSE INTERFACEUSUARIO\n'
        for chave in manual_interface_usuario:
            saida += f"{chave} : {manual_interface_usuario[chave]}\n"
        saida += "\n"

        # Manual da classe CriadorDeCampo
        manual_criador_de_campo = CriadorDeCampo.getManual()
        saida += 'MANUAL DA CLASSE CRIADORDECAMPO\n'
        for chave in manual_criador_de_campo:
            saida += f"{chave} : {manual_criador_de_campo[chave]}\n"
        saida += "\n"

        return saida

    def jogada(self, jogador, pos_ij, abrir=True):
        """
        Esse método realiza uma jogada, abrindo ou marcando uma casa, e caso seja aberta, contabilizando a jogada para
        os dados do jogador daquela partida.
        """
        pass

    def verifica_situacao(self):
        """
        Verifica se o jogo foi terminado em vitória, retornando True, em derrota, retornando False, ou se ainda está
        acontecendo, retornando None.

        Entrada: Nenhuma

        Saída: bool, representando a situação da partida atual
        """
        pass

    def calcula_tempo(self):
        """
        Esse método é responsável por contabilizar o tempo da partida realizada pelo jogador

        Entrada: Nenhuma

        Saída: Tempo total da partida atual
        """
        pass

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de CampoMinado.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return CampoMinado.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de CampoMinado.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return CampoMinado.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de CampoMinado.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = CampoMinado.__init__.__doc__
        manual["__str__"] = CampoMinado.__str__.__doc__
        manual["jogada"] = CampoMinado.jogada.__doc__
        manual["verifica_situacao"] = CampoMinado.verifica_situacao.__doc__
        manual["calcula_tempo"] = CampoMinado.calcula_tempo.__doc__
        manual["getManual"] = CampoMinado.getManual.__doc__
        manual["getAtributos"] = CampoMinado.getAtributos.__doc__
        manual["getMetodos"] = CampoMinado.getMetodos.__doc__
        manual["tamanho"] = "# Representa o tamanho do campo do jogo"
        manual["n_bombas"] = "# Representa o número de bombas do jogo"
        return manual


def main():
    jogo = CampoMinado()
    menu_inicial = Tela("Bem Vindo ao Campo Minado", ("(1) Novo Jogo", "(2) Carregar Jogo", "(3) Opções",
                        "(4) Manual do Desenvolvedor", "(5) Estatísticas"))
    menu_inicial.desenha_tela()
    escolha = menu_inicial.getOpcaoEscolhida()
    if escolha == 4:
        print(jogo)
    else:
        print("Essa parte do jogo não está concluída")


if __name__ == "__main__":
    main()
