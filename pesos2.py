from times import get_players
from players import Player
import math

#gerar lista de jogadores
list_players = get_players()

#dividir os jogadores por suas posições
dict_players = {}
for player in list_players:
    if player.posicao not in dict_players.keys():
        dict_players[player.posicao] = [player]
    else:
        dict_players[player.posicao].append(player)
        
# Restringindo para apenas 100 playres por posição
for l_player in dict_players.keys():
    dict_players[l_player] = dict_players[l_player][:100]

def get_range(n:int)->tuple[int,int]:
    dec = int(math.log10(n))
    return ((n-(10**dec)), (n+(10**dec)))

def get_pesos(lista_jogadores:list[Player], lp:list[int]=[1,1,1,1,1,1], dec:int=3)->list[int]:
    # criando lista de desvio e de pesos
    melhor_peso = [1000000000, [0,0,0,0,0,0]]
    lp = [10 if i==0 else i*10 for i in lp]
    # encontrando os melhores pesos
    for i0 in range(*get_range(lp[0])):
        for i1 in range(*get_range(lp[1])):
            for i2 in range(*get_range(lp[2])):
                for i3 in range(*get_range(lp[3])):
                    for i4 in range(*get_range(lp[4])):
                        for i5 in range(*get_range(lp[5])):
                            variacao = 0
                            for player in lista_jogadores:
                                try:
                                    # somo a variação o valor absoluto de (over - media ponderada)
                                    variacao += abs(player.overall - ((
                                        (i0*player.velocidade) + (i1*player.chute) + (i2*player.passe)
                                        + (i3*player.drible ) + (i4*player.defesa) + (i5*player.fisico)
                                    )/(i0 + i1 + i2 + i3 + i4 + i5)))
                                except ZeroDivisionError:
                                    pass
                            # se a minha variação, for menor que a minha melhor variação atual, eu atualizo os pesos e menor variação
                            if variacao < melhor_peso[0]: melhor_peso = [variacao, [i0, i1, i2, i3, i4, i5]]
                            
    print(f"Atualmente os melhores peso de {lista_jogadores[0].posicao} é {melhor_peso[1]} com uma variação de {melhor_peso[0]}")
    #condições de saída
    if dec == 1:
        return melhor_peso[1]
    else:
        return get_pesos(lista_jogadores,melhor_peso[1], dec-1)

if __name__ == '__main__':
    for pos in dict_players.keys():
        bp = get_pesos(dict_players[pos], dec=1)
        print(f'A melhor combinação para a posição {pos} é {bp}')
        break
