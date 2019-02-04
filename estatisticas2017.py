import main

estatisticas2017 = main.db.reference('resultado').get()
artilharia = []

def estatisticas_2017():
    vitorias = derrotas = empates = gols_marcados = gols_sofridos = saldo_gols = 0
    #pega as keys e separa o dicionário resultante em chave e valor
    for keys in estatisticas2017.items():
        #pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
        dados = keys[1]
        #demenbra o dicionário da variável dados em chave e valor
        for chave, valor in dados.items():
            #obtém as informações dos resultados
            if chave == 'golsAdversarioAddResultado':
                gols_adversario = valor
                gols_sofridos += int(valor)
            if chave == 'golsStaCruzAddResultado':
                gols_santa_cruz = valor
                gols_marcados += int(valor)
                if gols_santa_cruz > gols_adversario:
                    vitorias += 1
                elif gols_santa_cruz == gols_adversario:
                    empates += 1
                elif gols_santa_cruz < gols_adversario:
                    derrotas += 1
            if chave == 'golsMarcadoresAddResultado':
                artilharia.append(valor.split(', '))
    saldo_gols = gols_marcados - gols_sofridos

    print(f'Vitórias: {vitorias}\nEmpates: {empates}\nDerrotas: {derrotas}')
    print(f'Gols marcados: {gols_marcados}\nGols sofridos: {gols_sofridos}\nSaldo de gols: {saldo_gols}')

estatisticas_2017()

#Lista de artilheiros
gols_rafael = 0
#pega a lista de artilharia (todos os jogos do ano) e desmembra resultado em uma lista de goleadores de cada jogo
for goleadores_jogo in artilharia:
    #pega cada nome de jogador na lista de goleadores de cada jogo
    for jogador in goleadores_jogo:
        if jogador == 'Rafael':
            gols_rafael += 1
print(f'Rafael: {gols_rafael}')