import main
from tkinter import *
'''
janela = Tk()
btn_estatisticas_2016 = Button(janela, width=40, text='Estatísticas 2016')
btn_estatisticas_2016.place(x=100, y=300)
btn_estatisticas_2016.pack()
btn_estatisticas_2017 = Button(janela, width=40, text='Estatísticas 2017')
btn_estatisticas_2017.place(x=100, y=300)
btn_estatisticas_2017.pack()
btn_estatisticas_2018 = Button(janela, width=40, text='Estatísticas 2018')
btn_estatisticas_2018.place(x=100, y=300)
btn_estatisticas_2018.pack()

janela.title('Estatísticas')
janela.geometry('300x300+200+200')
janela.mainloop()'''
estatisticas_2017 = main.db.reference('resultado').get()
def estatisticas():
    vitorias = 0
    derrotas = 0
    empates = 0
    #pega as keys e separa o dicionário resultante em chave e valor
    for keys in estatisticas_2017.items():
        #pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        #demenbra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            #obtém as informações dos resultados
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
            if chave == 'golsStaCruzAddResultado':
                gols_santa_cruz = valor
                if gols_santa_cruz > gols_adversario:
                    vitorias += 1
                elif gols_santa_cruz == gols_adversario:
                    empates += 1
                elif gols_santa_cruz < gols_adversario:
                    derrotas += 1
    print(f'Vitórias: {vitorias}\nEmpates: {empates}\nDerrotas: {derrotas}')

estatisticas()
#Gols marcados

#Gols sofridos

#Saldo de gols

#Lista de artilheiros