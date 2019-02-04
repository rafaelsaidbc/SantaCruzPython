import main

estatisticas2016 = main.db.reference('resultados2016').get()
def estatisticas_2016():
    vitorias = derrotas = empates = gols_marcados = gols_sofridos = saldo_gols = 0
    #pega as keys e separa o dicionário resultante em chave e valor
    for keys in estatisticas2016.items():
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
    saldo_gols = gols_marcados - gols_sofridos

    print(f'Vitórias: {vitorias}\nEmpates: {empates}\nDerrotas: {derrotas}')
    print(f'Gols marcados: {gols_marcados}\nGols sofridos: {gols_sofridos}\nSaldo de gols: {saldo_gols}')

estatisticas_2016()

#Lista de artilheiros