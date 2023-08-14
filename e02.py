## Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro ##
## a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética.


tabela = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense',
                'Internacional', 'Bragantino-RD', 'Fortaleza', 'Athletico-PR', 'Athletico-MG',
                'São Paulo', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians',
                'Cuiabá', 'Goiáis', 'Vasco da gama', 'América-MG', 'Coritiba')


print("=" *15)
print(f"lista de times no Brasileirão :\n {tabela}")
print("=" *15)
print(f"Os primeiros 5 colocados : \n {tabela[0:5]}")
print("=" *15)
print(f"Os ultimos 5 colocados : \n {tabela[-4:]}")
print("=" *15)
print(f"Os times em ordem Alfabetica : \n {sorted(tabela)}")
print("=" *15)
print(f'Este time esta na possição {tabela.index("São Paulo")+1}')
