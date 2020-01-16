times = ('Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Atlético-PR', 'São Paulo',
         'Internacional', 'Corinthias', 'Bahia', 'Vasco da Gama', 'Góias',
         'Fortaleza', 'Atlético', 'Botaogo', 'Ceára SC', 'Cruzeiro', 'Fluminense',
         'CSA', 'Chapecoense', 'Avaí')

print(f'Lista de times do brasileirao: {times}')
print('-='*15)
print(f'Os 5 primeiros sao {times[:5]}')
print('-='*15)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense ocupa a posicao ', end='')
print(times.index('Chapecoense')+1)
