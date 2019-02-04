import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
import resultados

#retornar a credencial de acesso ao Firebase, utilizando o arquivo json como chave de autenticação
def conexao_database():
    cred = credentials.Certificate('C:\\Users\\Usuario\\Documents\\Rafael\\Projetos\\SantaCruz\\santa-cruz-veterano-firebase-adminsdk-clhhp-2d5d4730e6.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://santa-cruz-veterano.firebaseio.com'})

conexao_database()
'''janela = Tk()
btn_resultados = Button(janela, width=40, text='Resultados')
btn_resultados.place(x=100, y=100)
btn_resultados.pack()
btn_calendario = Button(janela, width=40, text='Calendario')
btn_calendario.place(x=100, y=200)
btn_calendario.pack()
btn_estatisticas = Button(janela, width=40, text='Estatísticas')
btn_estatisticas.place(x=100, y=300)
btn_estatisticas.pack()
janela.title('Santa Cruz')
janela.geometry('400x400+200+200')
janela.mainloop()
'''
