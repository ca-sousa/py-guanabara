dados = []
boletim = []
media = opt = 0

while True:
    dados.append(input('Digite o nome do Aluno: '))
    dados.append(int(input('Digite a primeira nota: ')))
    dados.append(int(input('Digite a segunda nota: ')))
    opt = input('Deseja continuar? [S/N] ').upper()

    boletim.append(dados[:])
    dados.clear()

    if opt == 'N':
        break

print('-'*50)
print('BOLETIM')
print('NOME -------- MEDIA --------- NP1 ------- NP2')
for c in range(0, len(boletim)):
        media = (boletim[c][1] + boletim[c][2])/2
        print(f'{boletim[c][0]} -------- {media} --------- {boletim[c][1]} ------- {boletim[c][2]}')
