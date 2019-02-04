import main
from tkinter import *

#busca os resultados na database do Firebase
calendario = main.db.reference('calendario').get()
#pega as keys e separa o dicionário resultante em chave e valor
for keys in calendario.items():
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
def janela_calendario():
    janela = Tk()
    janela.title('Santa Cruz - Próximos Jogos')
    janela.geometry('400x400+200+200')
    janela.mainloop()


janela_calendario()



#Ano

#Número do jogo

#data

#hora

#Santa Cruz x Adversário

#Local do jogo