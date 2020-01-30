matriz= [[], [], []]

for f in range(0, 3):
    for d in range(0, 3):
        matriz[d].append(int(input('Digite um valor: ')))
        
print('-'*50)
print(f'[ {matriz[0][0]} ] [ {matriz[1][0]} ] [ {matriz[2][0]} ]')
print(f'[ {matriz[0][1]} ] [ {matriz[1][1]} ] [ {matriz[2][1]} ]')
print(f'[ {matriz[0][2]} ] [ {matriz[1][2]} ] [ {matriz[2][2]} ]')


# Outra maneira:
# matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 
# for l in range(0, 3):
    # for c in range(0, 3):
        # matriz2[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
# print('-'*50)
# for l in range(0, 3):
    # for c in range(0, 3):
        # print(f'[{matriz2[l][c]}]', end='')
    # print()