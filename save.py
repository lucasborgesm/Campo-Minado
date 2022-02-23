class Save:
    """
    Essa classe é responsável por armazenar o estado atual do jogo, incluindo todas as informações necessárias para que
    o jogo possa ser retomado no momento exato do save.
    """

    __atributos = {"hist", "save", "posicao_tamanho", "jogador_salvo"}
    __metodos = {"__init__", "salva_novo_jogo", "salva_jogada", "salva_jogador", "apaga_save", "getAtributos",
                 "getMetodos", "getManual"}

    def __init__(self, hist, jogador_salvo=True):
        """
        Inicializador responsável por criar o arquivo necessário para o salvamento do jogo.

        Entrada: objeto da classe Save, objeto da classe Historico, bool (dizendo se o jogador já foi salvo
        anteriormente ou não, por padrão True)

        Saída: Nenhuma
        """
        self.hist = hist
        self.save = "save.txt"
        self.posicao_tamanho = 5
        self.jogador_salvo = jogador_salvo
    
    def salva_novo_jogo(self, campo):
        """
        Método responsável por salvar o campo e o tamanho do jogo criado

        Entrada: objeto da classe Save, objeto da classe Campo

        Saída: Nenhuma
        """
        arquivo = open(self.save, "w")
        arquivo.write(str(campo.getTamanho()) + "\n")
        arquivo.write(campo.__str__())
        arquivo.close()
    
    def salva_jogada(self, modo, i, j):
        """
        Método responsável por salvar as jogadas

        Entrada: objeto da classe Save, str (representando o tipo de jogada), int (representando a coordenada da linha),
        int (representando a coordenada da coluna)

        Saída: Nenhuma
        """
        arquivo = open(self.save, "a")
        arquivo.write(modo + f"({i},{j})\n")
        arquivo.close()
    
    def salva_jogador(self, jogador):
        """
        Método responsável por salvar as informações do jogador

        Entrda: objeto da classe Save, objeto da classe Jogador

        Saída: Nenhuma
        """
        if self.jogador_salvo:
            arquivo_antigo = open(self.save)
            for i in range(self.posicao_tamanho):
                arquivo_antigo.readline()
            dados = arquivo_antigo.read()
        else:
            arquivo_antigo = open(self.save)
            dados = arquivo_antigo.read()
            self.jogador_salvo = True
        nick = jogador.getNick()
        nick = nick[: nick.find("\n")]
        informacoes_jogador = f"{nick}\n{jogador.getJogadas()}\n{jogador.getCasasAbertas()}\n{jogador.getCasasAbertasTotal()}\n{jogador.getCasasMarcadas()}\n"
        arquivo_novo = open(self.save, "w")
        arquivo_novo.write(informacoes_jogador + dados)
        arquivo_novo.close()
    
    def apaga_save(self):
        """
        Método responsável por apagar um save já existente

        Entrada: obejto da classe Save

        Saída: Nenhuma
        """
        open(self.save, "w").close()

    @staticmethod
    def getAtributos():
        """
        Esta função estática (chamada sempre através de Save.getAtributos()) retorna um
        conjunto com os nomes dos atributos desta classe.

        (None) -> set
        """
        return Save.__atributos

    @staticmethod
    def getMetodos():
        """
        Esta função estática (chamada sempre através de Save.getMetodos()) retorna um
        conjunto com os nomes dos métodos desta classe.

        (None) -> set
        """
        return Save.__metodos

    @staticmethod
    def getManual():
        """
        Esta função estática (chamada sempre através de Save.getManual()) retorna um
        dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

        (None) -> dict
        """
        manual = dict()
        manual["__init__"] = Opcoes.__init__.__doc__
        manual["salva_novo_jogo"] = Opcoes.salva_novo_jogo.__doc__
        manual["salva_jogada"] = Opcoes.salva_jogada.__doc__
        manual["salva_jogador"] = Opcoes.salva_jogador.__doc__
        manual["apaga_save"] = Opcoes.apaga_save.__doc__
        manual["getManual"] = Opcoes.getManual.__doc__
        manual["getAtributos"] = Opcoes.getAtributos.__doc__
        manual["getMetodos"] = Opcoes.getMetodos.__doc__
        manual["hist"] = "# Representa o historico"
        manual["save"] = "# Representa o save"
        manual["posicao_tamanho"] = "# Representa a posicao da linha que está salva o tamanho do campo"
        manual["jogador_salvo"] = "# Representa a informacao se o jogador já foi salvo anteriormente ou não"
        return manual
