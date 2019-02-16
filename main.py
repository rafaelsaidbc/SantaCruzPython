import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
from tkinter import *


# função para conectar a credencial de acesso ao Firebase, utilizando o arquivo json como chave de autenticação
def conexao_database():
    #cria a credencial necessária para acesso ao Firebase
    cred = credentials.Certificate('path')
    #inicializa a conexão com o Firebase, utilizando a credencial e o endereço do Firebase
    firebase_admin.initialize_app(cred, {
    'databaseURL' : 'site/firebase'})


#execução da função para conectar à database do Firebase
conexao_database()

# define a fonte dos textos dos botões
LARGE_FONT = ("Verdana", 12)


# função para obter os resultados do ano 2016
def obtendo_resultados_2016():
    dicionario_final = {}
    lista_resultados = []
    # pega as keys (da child no Firebase) e separa o dicionário resultante em chave e valor
    for keys in db.reference('resultados2016').get().items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # desmembra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'adversarioAddResultado':
                adversario = valor
            if chave == 'dataAddResultado':
                data_resultado = valor
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
            if chave == 'golsMarcadoresAddResultado':
                goleadores = valor
                if goleadores == '':
                    goleadores = 'Santa Cruz não balançou as redes'
            if chave == 'golsStaCruzAddResultado':
                gols_santa_cruz = valor
            if chave == 'idAddResultado':
                id_resultado = valor
                # adiciona os dados de resultados no dicionário dicionario_final
                dicionario_final['Jogo nº'] = id_resultado
                dicionario_final['Data'] = data_resultado
                dicionario_final['Santa Cruz'] = gols_santa_cruz
                dicionario_final['adversário'] = adversario
                dicionario_final['gols_adversário'] = gols_adversario
                dicionario_final['Goleadores'] = goleadores
                # faz uma cópia do dicionário, para ter os dados de cada jogo
                copia = dicionario_final.copy()
                # adiciona a cópia do dicionário na lista lista_resultados
                lista_resultados.append(copia)
                # limpa a cópia do dicionário para adicionar dados do próximo resultado
                copia = {}

    # janela de exibição dos resultados
    def janela_resultados2016():
        # define a janela como Toplevel, só será aberta quando o botão referente a ela for clicado
        resultados2016_janela = Toplevel()
        # define o título da janela
        resultados2016_janela.title('RESULTADOS 2016')
        # cria a variável t, do tipo Text, para armazenar os dados dos resultados a serem exibidos na janela
        t = Text(resultados2016_janela)
        # faz um for em cada dado dos resultados dos jogos e armazena em variáveis
        for elemento in lista_resultados:
            for item, valor in elemento.items():
                if item == 'Jogo nº':
                    id_jogo = 'Jogo nº ' + valor
                if item == 'Data':
                    data = 'Data: ' + valor
                if item == 'Santa Cruz':
                    santa_cruz = 'Santa Cruz ' + valor + ' x '
                if item == 'adversário':
                    adversario = ' ' + valor + ' '
                if item == 'gols_adversário':
                    gols_adversario = valor
                if item == 'Goleadores':
                    goleadores = 'Goleadores: ' + valor
                    # insere todos os dados de cada jogo na variável t, com a formatação aqui definida
                    t.insert(END,
                             id_jogo + '\n' + data + '\n' + santa_cruz + gols_adversario + adversario + '\n' + goleadores + '\n')
                    t.insert(END, '\n' + '*' * 50 + '\n\n')
        # empacota a variável t para ser executada
        t.pack()

    # execução da função que exibe a janela com os resultados
    janela_resultados2016()


# função para obter os resultados do ano 2017
def obtendo_resultados_2017():
    dicionario_final = {}
    lista_resultados = []
    # pega as keys e separa o dicionário resultante em chave e valor
    for keys in db.reference('resultado').get().items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # demembra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'adversarioAddResultado':
                adversario = valor
            if chave == 'dataAddResultado':
                data_resultado = valor
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
            if chave == 'golsMarcadoresAddResultado':
                goleadores = valor
                if goleadores == '':
                    goleadores = 'Santa Cruz não balançou as redes'
            if chave == 'golsStaCruzAddResultado':
                gols_santa_cruz = valor
            if chave == 'idAddResultado':
                id_resultado = valor
                # adiciona os dados de resultados no dicionário dicionario_final
                dicionario_final['Jogo nº'] = id_resultado
                dicionario_final['Data'] = data_resultado
                dicionario_final['Santa Cruz'] = gols_santa_cruz
                dicionario_final['adversário'] = adversario
                dicionario_final['gols_adversário'] = gols_adversario
                dicionario_final['Goleadores'] = goleadores
                # faz uma cópia do dicionário, para ter os dados de cada jogo
                copia = dicionario_final.copy()
                # adiciona a cópia do dicionário na lista lista_resultados
                lista_resultados.append(copia)
                # limpa a cópia do dicionário
                copia = {}

    # janela de exibição dos resultados
    def janela_resultados2017():
        # define a janela como Toplevel, só será aberta quando o botão referente for clicado
        resultados2017_janela = Toplevel()
        # define o título da janela
        resultados2017_janela.title('RESULTADOS 2017')
        # cria a variável t, do tipo Text, para armazenar os dados dos resultados a serem exibidos na janela
        t = Text(resultados2017_janela)
        # faz um for em cada dado dos resultados dos jogos e armazena em variáveis
        for elemento in lista_resultados:
            for item, valor in elemento.items():
                if item == 'Jogo nº':
                    id_jogo = 'Jogo nº ' + valor
                if item == 'Data':
                    data = 'Data: ' + valor
                if item == 'Santa Cruz':
                    santa_cruz = 'Santa Cruz ' + valor + ' x '
                if item == 'adversário':
                    adversario = ' ' + valor + ' '
                if item == 'gols_adversário':
                    gols_adversario = valor
                if item == 'Goleadores':
                    goleadores = 'Goleadores: ' + valor
                    # insere todos os dados de cada jogo na variável t, com a formatação aqui definida
                    t.insert(END,
                             id_jogo + '\n' + data + '\n' + santa_cruz + gols_adversario + adversario + '\n' + goleadores + '\n')
                    t.insert(END, '\n' + '*' * 50 + '\n\n')
        # empacota a variável t para ser executada
        t.pack()

    # execução da função que exibe a janela com os resultados
    janela_resultados2017()


# função para obter os resultados do ano 2018
def obtendo_resultados_2018():
    dicionario_final = {}
    lista_resultados = []
    # pega as keys e separa o dicionário resultante em chave e valor
    for keys in db.reference('resultados2018').get().items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # demembra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'adversarioAddResultado':
                adversario = valor
            if chave == 'dataAddResultado':
                data_resultado = valor
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
            if chave == 'golsMarcadoresAddResultado':
                goleadores = valor
                if goleadores == '':
                    goleadores = 'Santa Cruz não balançou as redes'
            if chave == 'golsStaCruzAddResultado':
                gols_santa_cruz = valor
            if chave == 'idAddResultado':
                id_resultado = valor
                # adiciona os dados de resultados no dicionário dicionario_final
                dicionario_final['Jogo nº'] = id_resultado
                dicionario_final['Data'] = data_resultado
                dicionario_final['Santa Cruz'] = gols_santa_cruz
                dicionario_final['adversário'] = adversario
                dicionario_final['gols_adversário'] = gols_adversario
                dicionario_final['Goleadores'] = goleadores
                # faz uma cópia do dicionário, para ter os dados de cada jogo
                copia = dicionario_final.copy()
                # adiciona a cópia do dicionário na lista lista_resultados
                lista_resultados.append(copia)
                # limpa a cópia do dicionário
                copia = {}

    # janela de exibição dos resultados
    def janela_resultados2018():
        # define a janela como Toplevel, só será aberta quando o botão referente for clicado
        resultados2018_janela = Toplevel()
        # define o título da janela
        resultados2018_janela.title('RESULTADOS 2018')
        # cria a variável t, do tipo Text, para armazenar os dados dos resultados a serem exibidos na janela
        t = Text(resultados2018_janela)
        # faz um for em cada dado dos resultados dos jogos e armazena em variáveis
        for elemento in lista_resultados:
            for item, valor in elemento.items():
                if item == 'Jogo nº':
                    id_jogo = 'Jogo nº ' + valor
                if item == 'Data':
                    data = 'Data: ' + valor
                if item == 'Santa Cruz':
                    santa_cruz = 'Santa Cruz ' + valor + ' x '
                if item == 'adversário':
                    adversario = ' ' + valor + ' '
                if item == 'gols_adversário':
                    gols_adversario = valor
                if item == 'Goleadores':
                    goleadores = 'Goleadores: ' + valor
                    # insere todos os dados de cada jogo na variável t, com a formatação aqui definida
                    t.insert(END,
                             id_jogo + '\n' + data + '\n' + santa_cruz + gols_adversario + adversario + '\n' + goleadores + '\n')
                    t.insert(END, '\n' + '*' * 50 + '\n\n')
        # empacota a variável t para ser executada
        t.pack()

    # execução da função que exibe a janela com os resultados
    janela_resultados2018()


# função para obter as estatísticas do ano de 2016
def estatisticas_2016():
    # cria uma lista vazia de artilheiros
    lista_artilheiros2016 = []
    # cria uma lista vazia com os nomes dos artilheiros
    artilharia_2016 = []
    # função para retornar as estatísticas de 2016
    vitorias = derrotas = empates = gols_marcados = gols_sofridos = saldo_gols = 0
    # importa os dados dos resultados de 2016 no Firebase
    estatisticas2016 = db.reference('resultados2016').get()
    # pega as keys e separa o dicionário resultante em chave e valor
    for keys in estatisticas2016.items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # desmembra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
                gols_sofridos += int(valor)
            if chave == 'golsStaCruzAddResultado':
                # faz as estatísticas de vitórias, empates, derrotas
                gols_santa_cruz = valor
                gols_marcados += int(valor)
                if gols_santa_cruz > gols_adversario:
                    vitorias += 1
                elif gols_santa_cruz == gols_adversario:
                    empates += 1
                elif gols_santa_cruz < gols_adversario:
                    derrotas += 1
            # adiciona os artilheiros de cada jogo à lista_artilheiros
            if chave == 'golsMarcadoresAddResultado':
                # separa os nomes por vírgula, strip() para remover possíveis espaços em branco entre os nomes
                lista_artilheiros2016.append(valor.split(','.strip()))
    saldo_gols = gols_marcados - gols_sofridos

    # função para a janela de estatísticas de 2016
    def janela_estatisticas2016():
        estatisticas2016_janela = Toplevel()
        estatisticas2016_janela.title("ESTATÍSTICAS 2016")
        t = Text(estatisticas2016_janela)
        t.insert(END, 'ESTATÍSTICAS DE 2016')
        t.insert(END, '\n')
        t.insert(END, 'Vitórias: ')
        t.insert(END, vitorias)
        t.insert(END, '\n')
        t.insert(END, 'Empates: ')
        t.insert(END, empates)
        t.insert(END, '\n')
        t.insert(END, 'Derrotas: ')
        t.insert(END, derrotas)
        t.insert(END, '\n')
        t.insert(END, 'Gols marcados: ')
        t.insert(END, gols_marcados)
        t.insert(END, '\n')
        t.insert(END, 'Gols sofridos: ')
        t.insert(END, gols_sofridos)
        t.insert(END, '\n')
        t.insert(END, 'Saldo de gols: ')
        t.insert(END, saldo_gols)
        t.insert(END, '\n\n')
        t.insert(END, 'ARTILHEIROS DE 2016\n')

        # função para desmembrar a lista_artilheiros por nome de jogador, independente do jogo em que marcou (até aqui era criada uma lista de artilheiros para cada jogo)
        def lista_de_artilheiros():
            # cria um índice para cada elemento, o elemento contém os nomes dos marcadores em cada jogo
            for indice, elemento in enumerate(lista_artilheiros2016):
                # pega cada nome de artilheiro de cada jogo e coloca na lista artilharia para ser contabilizado depois
                for goleador in elemento:
                    artilharia_2016.append(goleador.strip())

        # executa a função lista_de_artilheiros para criar uma lista com a artilharia
        lista_de_artilheiros()

        # função para armazenar na variável t os nomes e quantidade de gols marcados
        def artilharia2016():
            # ordena a lista artilharia por ordem alfabética
            artilharia_2016.sort()
            # pega cada nome na lista artilharia
            for nome in artilharia_2016:
                if nome == '':
                    continue
                else:
                    # armazena na variável t o nome do jogador e a quantidade de vezes em que parece na lista, resultando na quantidade de gols marcados no ano
                    t.insert(END, nome)
                    t.insert(END, ': ')
                    t.insert(END, artilharia_2016.count(nome))
                    t.insert(END, '\n')
                    # exclui os nomes que já foram catalogados da lista
                    while nome in artilharia_2016:
                        artilharia_2016.remove(nome)

        # execução da função artilharia2016
        artilharia2016()
        # empacota a variável t para ser executada
        t.pack()

    # executa a função janela_estatisticas2016
    janela_estatisticas2016()


def estatisticas_2017():
    # cria uma lista vazia de artilheiros
    lista_artilheiros2017 = []
    # cria uma lista vazia com os nomes dos artilheiros
    artilharia_2017 = []
    # função para retornar as estatísticas de 2017
    vitorias = derrotas = empates = gols_marcados = gols_sofridos = saldo_gols = 0
    # pega as keys e separa o dicionário resultante em chave e valor
    # importa os dados dos resultados de 2017 no Firebase
    estatisticas2017 = db.reference('resultado').get()
    for keys in estatisticas2017.items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # demenbra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
                gols_sofridos += int(valor)
            if chave == 'golsStaCruzAddResultado':
                # faz as estatísticas de vitórias, empates, derrotas
                gols_santa_cruz = valor
                gols_marcados += int(valor)
                if gols_santa_cruz > gols_adversario:
                    vitorias += 1
                elif gols_santa_cruz == gols_adversario:
                    empates += 1
                elif gols_santa_cruz < gols_adversario:
                    derrotas += 1
            # adiciona os artilheiros de cada jogo à lista_artilheiros
            if chave == 'golsMarcadoresAddResultado':
                # separa os nomes por vírgula, strip() para remover possíveis espaços em branco entre os nomes
                lista_artilheiros2017.append(valor.split(','.strip()))
    # estatísticas de gols marcados, sofridos e saldo
    saldo_gols = gols_marcados - gols_sofridos

    def janela_estatisticas2017():
        estatisticas2017_janela = Toplevel()
        estatisticas2017_janela.title("ESTATÍSTICAS 2017")
        t = Text(estatisticas2017_janela)
        t.insert(END, 'ESTATÍSTICAS DE 2017')
        t.insert(END, '\n')
        t.insert(END, 'Vitórias: ')
        t.insert(END, vitorias)
        t.insert(END, '\n')
        t.insert(END, 'Empates: ')
        t.insert(END, empates)
        t.insert(END, '\n')
        t.insert(END, 'Derrotas: ')
        t.insert(END, derrotas)
        t.insert(END, '\n')
        t.insert(END, 'Gols marcados: ')
        t.insert(END, gols_marcados)
        t.insert(END, '\n')
        t.insert(END, 'Gols sofridos: ')
        t.insert(END, gols_sofridos)
        t.insert(END, '\n')
        t.insert(END, 'Saldo de gols: ')
        t.insert(END, saldo_gols)
        t.insert(END, '\n\n')
        t.insert(END, 'ARTILHEIROS DE 2017\n')

        # função para desmembrar a lista_artilheiros por nome de jogador, independente do jogo em que marcou (até aqui era criada uma lista de artilheiros para cada jogo)
        def lista_de_artilheiros():
            # cria um indice para cada elemento, o elemento contém os nomes dos marcadores em cada jogo
            for indice, elemento in enumerate(lista_artilheiros2017):
                # pega cada nome de artilheiro de cada jogo e coloca na lista artilharia para ser contabilizado depois
                for goleador in elemento:
                    artilharia_2017.append(goleador.strip())

        # executa a função lista_de_artilheiros para criar uma lista com a artilharia
        lista_de_artilheiros()

        # função para armazenar na variável t os nomes e quantidade de gols marcados
        def artilharia2017():
            # ordena a lista artilharia por ordem alfabética
            artilharia_2017.sort()
            # pega cada nome na lista artilharia
            for nome in artilharia_2017:
                if nome == '':
                    continue
                else:
                    # armazena na variável t o nome do jogador e a quantidade de vezes em que parece na lista, resultando na quantidade de gols marcados no ano
                    t.insert(END, nome)
                    t.insert(END, ': ')
                    t.insert(END, artilharia_2017.count(nome))
                    t.insert(END, '\n')
                    # exclui os nomes que já foram catalogados da lista
                    while nome in artilharia_2017:
                        artilharia_2017.remove(nome)

        # execução da função artilharia2017
        artilharia2017()
        t.pack()

    janela_estatisticas2017()


def estatisticas_2018():
    # cria uma lista vazia de artilheiros
    lista_artilheiros2018 = []
    # cria uma lista vazia com os nomes dos artilheiros
    artilharia_2018 = []
    # função para retornar as estatísticas de 2018
    vitorias = derrotas = empates = gols_marcados = gols_sofridos = saldo_gols = 0
    # pega as keys e separa o dicionário resultante em chave e valor
    # importa os dados dos resultados de 2018 no Firebase
    estatisticas2018 = db.reference('resultados2018').get()
    for keys in estatisticas2018.items():
        # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        # demenbra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            # obtém as informações dos resultados
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
                gols_sofridos += int(valor)
            if chave == 'golsStaCruzAddResultado':
                # faz as estatísticas de vitórias, empates, derrotas
                gols_santa_cruz = valor
                gols_marcados += int(valor)
                if gols_santa_cruz > gols_adversario:
                    vitorias += 1
                elif gols_santa_cruz == gols_adversario:
                    empates += 1
                elif gols_santa_cruz < gols_adversario:
                    derrotas += 1
            # adiciona os artilheiros de cada jogo à lista_artilheiros
            if chave == 'golsMarcadoresAddResultado':
                # separa os nomes por vírgula, strip() para remover possíveis espaços em branco entre os nomes
                lista_artilheiros2018.append(valor.split(','.strip()))
    # estatísticas de gols marcados, sofridos e saldo
    saldo_gols = gols_marcados - gols_sofridos

    def janela_estatisticas2018():
        estatisticas2018_janela = Toplevel()
        estatisticas2018_janela.title("ESTATÍSTICAS 2018")
        t = Text(estatisticas2018_janela)
        t.insert(END, 'ESTATÍSTICAS DE 2018')
        t.insert(END, '\n')
        t.insert(END, 'Vitórias: ')
        t.insert(END, vitorias)
        t.insert(END, '\n')
        t.insert(END, 'Empates: ')
        t.insert(END, empates)
        t.insert(END, '\n')
        t.insert(END, 'Derrotas: ')
        t.insert(END, derrotas)
        t.insert(END, '\n')
        t.insert(END, 'Gols marcados: ')
        t.insert(END, gols_marcados)
        t.insert(END, '\n')
        t.insert(END, 'Gols sofridos: ')
        t.insert(END, gols_sofridos)
        t.insert(END, '\n')
        t.insert(END, 'Saldo de gols: ')
        t.insert(END, saldo_gols)
        t.insert(END, '\n\n')
        t.insert(END, 'ARTILHEIROS DE 2018\n')

        # função para desmembrar a lista_artilheiros por nome de jogador, independente do jogo em que marcou (até aqui era criada uma lista de artilheiros para cada jogo)
        def lista_de_artilheiros():
            # cria um indice para cada elemento, o elemento contém os nomes dos marcadores em cada jogo
            for indice, elemento in enumerate(lista_artilheiros2018):
                # pega cada nome de artilheiro de cada jogo e coloca na lista artilharia para ser contabilizado depois
                for goleador in elemento:
                    artilharia_2018.append(goleador.strip())

        # executa a função lista_de_artilheiros para criar uma lista com a artilharia
        lista_de_artilheiros()

        # função para armazenar na variável t os nomes e quantidade de gols marcados
        def artilharia2018():
            # ordena a lista artilharia por ordem alfabética
            artilharia_2018.sort()
            # pega cada nome na lista artilharia
            for nome in artilharia_2018:
                if nome == '':
                    continue
                else:
                    # armazena na variável t o nome do jogador e a quantidade de vezes em que parece na lista, resultando na quantidade de gols marcados no ano
                    t.insert(END, nome)
                    t.insert(END, ': ')
                    t.insert(END, artilharia_2018.count(nome))
                    t.insert(END, '\n')
                    # exclui os nomes que já foram catalogados da lista
                    while nome in artilharia_2018:
                        artilharia_2018.remove(nome)

        # execução da função artilharia2016
        artilharia2018()
        t.pack()

    janela_estatisticas2018()


# classe principal do programa
class SantaCruz(tk.Tk):
    # cria a inicialização da janela principal
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # cria o container para colocar os widgets
        container = tk.Frame(self)
        # localização do container
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # cria um dicionário vazio para colocar os frames
        self.frames = {}

        # para cada Frame das janelas do programa
        for F in (PaginaInicial, PaginaCalendario, PaginaResultados, PaginaEstatisticas):
            # coloca o frame no container
            frame = F(container, self)
            # define que o frame será o atual
            self.frames[F] = frame
            # localização do frame
            frame.grid(row=0, column=0, sticky="nsew")
        # exibe o frame na janela inicial do programa
        self.show_frame(PaginaInicial)

    # função para mostrar cada frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PaginaInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Santa Cruz", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Calendário",
                           command=lambda: controller.show_frame(PaginaCalendario))
        button.pack()

        button2 = tk.Button(self, text="Resultados",
                            command=lambda: controller.show_frame(PaginaResultados))
        button2.pack()

        button3 = tk.Button(self, text="Estatísticas", command=lambda: controller.show_frame(PaginaEstatisticas))
        button3.pack()


class PaginaCalendario(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Calendário", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Cadastrar', command=lambda: controller.show_frame())
        button1.pack()

        button2 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(PaginaInicial))
        button2.pack()


class PaginaResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Resultados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Resultados 2016",
                            command=obtendo_resultados_2016)
        button1.pack()

        button2 = tk.Button(self, text="Resultados 2017",
                            command=obtendo_resultados_2017)
        button2.pack()

        button3 = tk.Button(self, text="Resultados 2018",
                            command=obtendo_resultados_2018)
        button3.pack()

        button4 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(PaginaInicial))
        button4.pack()


class PaginaEstatisticas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Estatísticas", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Estatísticas 2016",
                            command=estatisticas_2016)
        button1.pack()

        button2 = tk.Button(self, text="Estatísticas 2017",
                            command=estatisticas_2017)
        button2.pack()

        button3 = tk.Button(self, text="Estatísticas 2018",
                            command=estatisticas_2018)
        button3.pack()

        button4 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(PaginaInicial))
        button4.pack()


# execução da classe Santa Cruz, a classe principal do programa
app = SantaCruz()
app.mainloop()
