import main

resultados = main.db.reference('resultados2018').get()
for keys in resultados.items():
    dados = keys[1]
    for chave, valor in dados.items():
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


