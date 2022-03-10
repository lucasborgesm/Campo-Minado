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


from estatisticas import Estatisticas
from menu_estatisticas import *
from interface_usuario import *
from ferramentas import *
from menu_pause import *
from tela import *
from jogador import *
from campo import *
from menu_inicial import *
from opcoes import *
from historico import *
from interface_campo import *
from dificuldade import *
from confirma_novo_jogo import *
from save import *
from jogada import *
from load import *


class CampoMinado:
    """
    Essa classe envolve todas as classes de forma a garantir a funcionalidade do jogo. Desse modo, todos as classes
    são conectadas garantindo o funcionamento das mecânicas do jogo, bem como criando métodos para isso.
    """

    __atributos = {}
    __metodos = {"__init__", "__str__", "jogo", "jogada", "verifica_situacao", "calcula_tempo", "menu_inicial",
                 "novo_jogo", "carrega_jogo", "opcoes", "estatisticas", "redireciona_menu_inicial", "getAtributos",
                 "getMetodos", "getManual"}

    def __init__(self):
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

        # Manual da classe MenuEstatisticas
        manual_menu_estatisticas = MenuEstatisticas.getManual()
        saida += 'MANUAL DA CLASSE MENUESTATISTICAS\n'
        for chave in manual_menu_estatisticas:
            saida += f"{chave} : {manual_menu_estatisticas[chave]}\n"
        saida += "\n"

        # Manual da classe Estatisticas
        manual_estatisticas = Estatisticas.getManual()
        saida += 'MANUAL DA CLASSE ESTATISTICAS\n'
        for chave in manual_estatisticas:
            saida += f"{chave} : {manual_estatisticas[chave]}\n"
        saida += "\n"

        # Manual da classe InterfaceUsuario
        manual_interface_usuario = InterfaceUsuario.getManual()
        saida += 'MANUAL DA CLASSE INTERFACEUSUARIO\n'
        for chave in manual_interface_usuario:
            saida += f"{chave} : {manual_interface_usuario[chave]}\n"
        saida += "\n"

        # Manual da classe InterfaceCampo
        manual_interface_campo = InterfaceCampo.getManual()
        saida += 'MANUAL DA CLASSE INTERFACECAMPO\n'
        for chave in manual_interface_campo:
            saida += f"{chave} : {manual_interface_campo[chave]}\n"
        saida += "\n"

        # Manual da classe MenuPause
        manual_menu_pause = MenuPause.getManual()
        saida += 'MANUAL DA CLASSE MENUPAUSE\n'
        for chave in manual_menu_pause:
            saida += f"{chave} : {manual_menu_pause[chave]}\n"
        saida += "\n"

        # Manual da classe MenuInicial
        manual_menu_inicial = MenuInicial.getManual()
        saida += 'MANUAL DA CLASSE MENUINICIAL\n'
        for chave in manual_menu_inicial:
            saida += f"{chave} : {manual_menu_inicial[chave]}\n"
        saida += "\n"

        # Manual da classe Opcoes
        manual_opcoes = Opcoes.getManual()
        saida += 'MANUAL DA CLASSE OPCOES\n'
        for chave in manual_opcoes:
            saida += f"{chave} : {manual_opcoes[chave]}\n"
        saida += "\n"

        # Manual da classe Dificuldade
        manual_dificuldade = Dificuldade.getManual()
        saida += 'MANUAL DA CLASSE DIFICULDADE\n'
        for chave in manual_dificuldade:
            saida += f"{chave} : {manual_dificuldade[chave]}\n"
        saida += "\n"

        # Manual da classe ConfirmaNovoJogo
        manual_confirma_novo_jogo = ConfirmaNovoJogo.getManual()
        saida += 'MANUAL DA CLASSE CONFIRMANOVOJOGO\n'
        for chave in manual_confirma_novo_jogo:
            saida += f"{chave} : {manual_confirma_novo_jogo[chave]}\n"
        saida += "\n"

        # Manual da classe Jogada
        manual_jogada = Jogada.getManual()
        saida += 'MANUAL DA CLASSE JOGADA\n'
        for chave in manual_jogada:
            saida += f"{chave} : {manual_jogada[chave]}\n"
        saida += "\n"

        # Manual da classe Jogador
        manual_jogador = Jogador.getManual()
        saida += 'MANUAL DA CLASSE JOGADOR\n'
        for chave in manual_jogador:
            saida += f"{chave} : {manual_jogador[chave]}\n"
        saida += "\n"

        # Manual da classe Save
        manual_save = Save.getManual()
        saida += 'MANUAL DA CLASSE SAVE\n'
        for chave in manual_save:
            saida += f"{chave} : {manual_save[chave]}\n"
        saida += "\n"

        # Manual da classe Load
        manual_load = Load.getManual()
        saida += 'MANUAL DA CLASSE SAVE\n'
        for chave in manual_save:
            saida += f"{chave} : {manual_save[chave]}\n"
        saida += "\n"

        # Manual da classe Historico
        manual_historico = Historico.getManual()
        saida += 'MANUAL DA CLASSE HISTORICO\n'
        for chave in manual_historico:
            saida += f"{chave} : {manual_historico[chave]}\n"
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

    def jogo(self, campo, jogador, estatisticas, hist, save, jogo_salvo=False, pos_casas_abertas=[],
             pos_casas_marcadas=[]):
        """
        Método responsável por realizar o funcionamento principal do jogo

        Entrada: objeto da classe CampoMinado, objeto da classe Campo, objeto da classe Jogador,
        objeto da classe Estatistica, objeto da classe Historico, objeto da classe Save, bool (representando se o jogo
        jogado no exato momento já tinha sido salvo ou não, por padrão False), list (contendo todas as casas que foram
        abertas em um jogo salvo, por padrão []), list (contendo todas as casas que foram marcadas em um jogo salvo, por
        padrão [])

        Saída: Nenhuma
        """
        interface_campo = InterfaceCampo(campo, hist)
        jogada = Jogada(hist)
        menu_pause = MenuPause(hist)
        if jogo_salvo:
            for i, j in pos_casas_abertas:
                campo.abre_casa(i, j)
            for i, j in pos_casas_marcadas:
                campo.marca_casa(i, j)
        interface_campo.mostra_campo()
        while True:
            sair = self.jogada(campo, jogador, interface_campo, jogada, menu_pause, hist, save)
            if sair:
                menu_pause.mensagem_de_saida()
                break
            else:
                situacao = self.verifica_situacao(campo, hist)
                interface_campo.mostra_campo()
                if situacao == "derrota":
                    interface_campo.derrota()
                    estatisticas.salva_estatisticas()
                    save.apaga_save()
                    break
                if situacao == "vitoria":
                    interface_campo.vitoria()
                    estatisticas.salva_estatisticas()
                    save.apaga_save()
                    break

    def jogada(self, campo, jogador, interface_campo, jogada, menu_pause, hist, save):
        """
        Esse método realiza uma jogada, abrindo ou marcando uma casa, contabilizando a jogada para
        os dados do jogador daquela partida, para o histórico e para o save.

        Entrada: objeto da classe CampoMinado, objeto da classe Jogador, objeto da classe InterfaceCampo, objeto da
        classe Jogada, objeto da classe MenuPause, objeto da classe Historico, objeto da classe Save

        Saída: bool, representando se o usuário deseja sair do jogo ou não
        """
        opcoes = {1: campo.abre_casa, 2: campo.marca_casa}
        jogada.desenha_tela(False)
        while True:
            try:
                escolha = jogada.getOpcaoEscolhida()
                break
            except CommandError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        CommandError\n"
                                      f"        O comando digitado não faz parte das opções disponíveis.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("O comando digitado não faz parte das opções disponíveis.\n")
            except ValueError:
                hist.armazena_log(f"{datetime.today()}\n"
                                  f"        ValueError\n"
                                  f"        Digite o número entre parênses da opção desejada.\n"
                                  f"        O usuário foi perguntado novamente sobre sua escolha\n")
                print("Digite o número entre parênses da opção desejada.\n")
        sair = False
        if escolha != 3:
            while True:
                try:
                    i, j = interface_campo.pergunta_posicao()
                    break
                except PosicaoInvalida:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        PosicaoInvalida\n"
                                      f"        A posição dada é inválida, digite um número entre 1 e"
                                      f" {campo.getTamanho()}.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print(f"A posição dada é inválida, digite um número entre 1 e {campo.getTamanho()}.\n")
                except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        ValueError\n"
                                      f"        A posição dada é inválida, digite um número entre 1 e "
                                      f"{self.campo.getTamanho()}.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print(f"A posição dada é inválida, digite um número entre 1 e {self.campo.getTamanho()}.\n")
            jogador.aumenta_jogadas(1)
            hist.armazena_jogada_hist("j", i, j)
            if escolha == 1:
                save.salva_jogada("a", i, j)
                jogador.aumenta_abertas(1)
            else:
                hist.armazena_jogada_hist("m", i, j)
                save.salva_jogada("m", i, j)
                jogador.aumenta_marcadas(1)
            save.salva_jogador(jogador)
            opcoes[escolha](i, j)
        else:
            menu_pause.desenha_tela()
            while True:
                try:
                    if menu_pause.getOpcaoEscolhida() == 2:
                        sair = True
                        break
                except CommandError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        CommandError\n"
                                      f"        O comando digitado não faz parte das opções disponíveis.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("O comando digitado não faz parte das opções disponíveis.\n")
                except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite o número entre parênses da opção desejada.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("Digite o número entre parênses da opção desejada.\n")
        return sair

    def verifica_situacao(self, campo, hist):
        """
        Verifica se o jogo foi terminado em vitória, retornando True, em derrota, retornando False, ou se ainda está
        acontecendo, retornando None.

        Entrada: objeto da classe CampoMinado, objeto da classe Campo, objeto da classe Historico

        Saída: bool, representando a situação da partida atual
        """
        situacao = campo.verifica_derrota()
        if situacao == "":
            situacao = campo.verifica_vitoria()
        return situacao

    def menu_inicial(self, estatisticas, hist):
        """
        Método responsável por mostrar o menu inicial, tratar as interações com o usuário e redirecionar para o que for
        decidido

        Entrada: objeto da classe CampoMinado, objeto da classe Estatistica, objeto da classe Historico

        Saída: Nenhuma
        """
        menu_inicial = MenuInicial(hist)
        menu_inicial.desenha_tela()
        while True:
            try:
                escolha = menu_inicial.getOpcaoEscolhida()
                break
            except CommandError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        CommandError\n"
                                      f"        O comando digitado não faz parte das opções disponíveis.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("O comando digitado não faz parte das opções disponíveis.\n")
            except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite o número entre parênses da opção desejada.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("Digite o número entre parênses da opção desejada.\n")
        self.redireciona_menu_inicial(escolha, estatisticas, hist)

    def novo_jogo(self, estatisticas, hist, tamanho=False, n_bombas=False):
        """
        Método responsável por criar um novo jogo, criando todos os objetos de classe necessários, também perguntando se
        o usuário tem certeza que deseja criar um novo jogo, já que isso resultará em apagar seu save anterior

        Entrada: objeto da classe CampoMinado, objeto da classe Estatistica, objeto da classe Historico

        Saída: Nenhuma
        """
        confirma_novo_jogo = ConfirmaNovoJogo(hist)
        confirma_novo_jogo.desenha_tela()
        while True:
            try:
                continua = confirma_novo_jogo.getOpcaoEscolhida()
                break
            except CommandError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        CommandError\n"
                                      f"        O comando digitado não faz parte das opções disponíveis.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("O comando digitado não faz parte das opções disponíveis.\n")
            except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite o número entre parênses da opção desejada.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("Digite o número entre parênses da opção desejada.\n")
        confirma_novo_jogo.limpaTela()
        if continua == 1:
            hist.reinicia_historico()
            save = Save(hist, False)
            jogador = Jogador()
            jogador.setNome()
            hist.armazena_nome_jogador(jogador)
            if not tamanho:
                menu_dificuldades = Dificuldade(hist)
                menu_dificuldades.desenha_tela()
                while True:
                    try:
                        escolha = menu_dificuldades.getOpcaoEscolhida()
                        break
                    except CommandError:
                        hist.armazena_log(f"{datetime.today()}\n"
                                        f"        CommandError\n"
                                        f"        O comando digitado não faz parte das opções disponíveis.\n"
                                        f"        O usuário foi perguntado novamente sobre sua escolha\n")
                        print("O comando digitado não faz parte das opções disponíveis.\n")
                    except ValueError:
                        hist.armazena_log(f"{datetime.today()}\n"
                                        f"        ValueError\n"
                                        f"        Digite o número entre parênses da opção desejada.\n"
                                        f"        O usuário foi perguntado novamente sobre sua escolha\n")
                        print("Digite o número entre parênses da opção desejada.\n")
                tamanho, n_bombas = menu_dificuldades.interpreta_dificuldade(escolha)
                campo = Campo(tamanho, n_bombas, hist)
            else:
                campo = Campo(tamanho, n_bombas, hist)
            save.salva_novo_jogo(campo)
            save.salva_jogador(jogador)
            Ferramentas.limpaTela()
            self.jogo(campo, jogador, estatisticas, hist, save)
        else:
            self.menu_inicial(estatisticas, hist)

    def carrega_jogo(self, estatisticas, hist):
        """
        Esse método carrega um jogo salvo anteriormente, criando todos os objetos de classe necessários e redirecionando
        para o jogo

        Entrada: objeto da classe CampoMinado, objeto da casse Estatistica, objeto da classe Historico

        Saída: Nenhuma
        """
        load = Load(hist)
        try:
            carregado = load.carrega_campo_inicial()
        except ArquivoVazio:
            hist.armazena_log(f"{datetime.today()}\n"
                              f"        ArquivoVazio"
                              f"        O arquivo de save está vazio."
                              f"        O usuário foi levado novamente ao menu_principal")
            print("O arquivo de save está vazio.\n")
            input("Pressione enter para continuar\n")
            carregado = False
        except FileNotFoundError:
            hist.armazena_log(f"{datetime.today()}\n"
                                   f"        FileNotFoundError"
                                   f"        Não existe nenhum jogo salvo."
                                   f"        O usuário foi levado novamente ao menu_principal")
            print("Não existe nenhum jogo salvo.\n")
            input("Pressione enter para continuar\n")
            carregado = False
        if carregado:
            tamanho, n_bombas, campo = carregado
            nick, jogadas, casas_abertas, casas_abertas_total, casas_marcadas = load.carrega_jogador()
            jogador = Jogador(nick, jogadas, casas_abertas, casas_abertas_total, casas_marcadas)
            campo = Campo(tamanho, n_bombas, hist, campo)
            pos_casas_abertas, pos_casas_marcadas = load.carrega_casas_abertas_e_marcadas(load.carrega_jogadas())
            save = Save(hist)
            self.jogo(campo, jogador, estatisticas, hist, save, True, pos_casas_abertas,
                      pos_casas_marcadas=pos_casas_marcadas)
        else:
            self.menu_inicial(estatisticas, hist)

    def opcoes(self, estatisticas, hist):
        """
        Esse método é reponsável por todo o menu de opções, tratando a interação com o usuário e redirecionando para o
        que for necessário

        Entrada: objeto da classe CampoMinado, objeto da classe Estatistica, objeto da casse Historico

        Saída: Nenhuma
        """
        menu_opcoes = Opcoes(hist)
        opcoes = {1: menu_opcoes.altera_dificuldades, 2: self.menu_inicial}
        menu_opcoes.desenha_tela()
        while True:
            try:
                escolha = menu_opcoes.getOpcaoEscolhida()
                break
            except CommandError:
                hist.armazena_log(f"{datetime.today()}\n"
                                  f"        CommandError\n"
                                  f"        O comando digitado não faz parte das opções disponíveis.\n"
                                  f"        O usuário foi perguntado novamente sobre sua escolha\n")
            except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite o número entre parênses da opção desejada.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("Digite o número entre parênses da opção desejada.\n")
            print("O comando digitado não faz parte das opções disponíveis.\n")
        if escolha != 2:
            while True:
                try:
                    tamanho, n_bombas = opcoes[escolha]()
                    self.novo_jogo(estatisticas, hist, tamanho=tamanho, n_bombas=n_bombas)
                    break
                except ValorTamanhoInvalido:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        ValorTamanhoInvalido\n"
                                      f"        Digite um número maior do que 1.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("\nDigite um número maior do que 1.\n")
                except ValorNumeroDeBombasInvalido:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        ValorNumeroDeBombasInvalido\n"
                                      f"        Digite um número maior do que 0 e menor do que o tamanho do campo"
                                      f" ao quadrado.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("\nDigite um número maior do que 0 e menor do que o tamanho do campo ao quadrado.\n")
                except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite um número inteiro.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("\nDigite um número inteiro.\n")
        else:
            opcoes[escolha](estatisticas, hist)

    def estatisticas(self, estatisticas, hist):
        """
        Método responsável por todo o menu de estatisticas, tratando a interação com o usuário e redirecionando para o
        que for necessário

        Entrada: objeto da classe CampoMinado, objeto da classe Estatistica, objeto da classe Historico
        """
        menu_estatisticas = MenuEstatisticas(hist)
        opcoes = {1: menu_estatisticas.grafico_abertas_jogadas_partida,
                  2: menu_estatisticas.grafico_marcadas_jogadas_partida,
                  3: menu_estatisticas.grafico_abertas_marcadas_partida,
                  4: self.menu_inicial}
        menu_estatisticas.desenha_tela()
        while True:
            try:
                escolha = menu_estatisticas.getOpcaoEscolhida()
                break
            except CommandError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                      f"        CommandError\n"
                                      f"        O comando digitado não faz parte das opções disponíveis.\n"
                                      f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("O comando digitado não faz parte das opções disponíveis.\n")
            except ValueError:
                    hist.armazena_log(f"{datetime.today()}\n"
                                    f"        ValueError\n"
                                    f"        Digite o número entre parênses da opção desejada.\n"
                                    f"        O usuário foi perguntado novamente sobre sua escolha\n")
                    print("Digite o número entre parênses da opção desejada.\n")
        if escolha != 4:
            plotado = opcoes[escolha](estatisticas)
            if not plotado:
                self.menu_inicial(estatisticas, hist)
        else:
            opcoes[escolha](estatisticas, hist)

    def redireciona_menu_inicial(self, escolha, estatisticas, hist):
        """
        Método responsável por redirecionar o usuário após escolher uma das opções do menu para qualquer opção
        selecionada

        Entrada: objeto da classe CampoMinado, int (representando a escolha), objeto da classe Estatistica, objeto da
        classe Historico
        """
        opcoes = {1: self.novo_jogo, 2: self.carrega_jogo, 3: self.opcoes, 4: self, 5: self.estatisticas}
        if escolha != 4:
            opcoes[escolha](estatisticas, hist)
        else:
            print(opcoes[escolha])
            input("\nPressione enter para voltar para o menu inicial\n")
            self.menu_inicial(estatisticas, hist)

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
        manual["jogo"] = CampoMinado.jogo.__doc__
        manual["jogada"] = CampoMinado.jogada.__doc__
        manual["verifica_situacao"] = CampoMinado.verifica_situacao.__doc__
        manual["menu_inicial"] = CampoMinado.menu_inicial.__doc__
        manual["novo_jogo"] = CampoMinado.novo_jogo.__doc__
        manual["carrega_jogo"] = CampoMinado.carrega_jogo.__doc__
        manual["opcoes"] = CampoMinado.opcoes.__doc__
        manual["estatisticas"] = CampoMinado.estatisticas.__doc__
        manual["redireciona_menu_inicial"] = CampoMinado.redireciona_menu_inicial.__doc__
        manual["getManual"] = CampoMinado.getManual.__doc__
        manual["getAtributos"] = CampoMinado.getAtributos.__doc__
        manual["getMetodos"] = CampoMinado.getMetodos.__doc__
        return manual


def main():
    jogo = CampoMinado()
    hist = Historico()
    estatisticas = Estatisticas(hist)
    jogo.menu_inicial(estatisticas, hist)


if __name__ == "__main__":
    main()
