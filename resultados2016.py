import main
from tkinter import *

#busca os resultados na database do Firebase
resultados = main.db.reference('resultados2016').get()

def obtendo_resultados_2016():
    #pega as keys e separa o dicionário resultante em chave e valor
    for keys in resultados.items():
        #pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        #demenbra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            #obtém as informações dos resultados
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
                print('Jogo nº: ', valor)
                print('Data: ', data_resultado)
                print('Santa Cruz ' + gols_santa_cruz + ' x ' + gols_adversario + ' ' + adversario)
                print('Goleadores: ' + goleadores)
        print('*'*40)

#cria a janela para exibir os resultados
def janela_resultados_2016():
    janela = Toplevel()
    janela.title('Santa Cruz - Resultados de 2016')
    janela.geometry('400x400+200+200')
    janela.mainloop()

obtendo_resultados_2016()
janela_resultados_2016()

