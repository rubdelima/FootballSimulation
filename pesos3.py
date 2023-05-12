from times import get_players
from players import Player
import time

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
    
# função que retorna a variância
def get_variance(lista_jogadores:list[Player], lp:list[float], sub:tuple[int,float]=None)->float:
    if sub is not None:
        lp[sub[0]] = sub[1]
    variacao = 0
    for player in lista_jogadores:
        try:
            # somo a variação o valor absoluto de (over - media ponderada)
            variacao += abs(player.overall - ((
                (lp[0]*player.velocidade) + (lp[1]*player.chute) + (lp[2]*player.passe)
                + (lp[3]*player.drible ) + (lp[4]*player.defesa) + (lp[5]*player.fisico)
            )/sum(lp)))
                            
        except ZeroDivisionError:
            pass
    return variacao

#função para pegar o peso inicial
def get_in_peso(lista_jogadores:list[Player])->list[int]:
    lista_pesos = [0,0,0,0,0,0]
    over_geral = 0
    for player in lista_jogadores:
        lista_pesos[0]+=player.velocidade; lista_pesos[1] += player.chute; lista_pesos[2] += player.passe
        lista_pesos[3]+=player.drible; lista_pesos[4]+=player.defesa; lista_pesos[5]+=player.fisico
        over_geral+= player.overall
    lista_pesos = [(abs(over_geral-lista_pesos[i]))**(-1) for i in range(len(lista_pesos))]
    correcao = 2/(min(lista_pesos))
    lista_pesos = [i*correcao for i in lista_pesos]
    return lista_pesos

#funcao_divide
def get_pesos(lista_jogadores:list[Player],lp:list[int]=None)->tuple[list[float],float]:
    if lp is None:
        lp = get_in_peso(lista_jogadores)
    variacao_inicial = get_variance(lista_jogadores, lp)
    for i in range(len(lp)):
        lp[i], variacao_inicial = get_best_peso(lista_jogadores, lp, i, variacao_inicial)
    return (lp, variacao_inicial)

def get_best_peso(lista_jogadores:list[Player], lp:list[int], p_pos:int, var_ini:int)->tuple[float, float]:
    lp_sup = []
    lp_inf = []
    for j in range(len(lp)):
        if j == p_pos : lp_sup.append(lp[j]+1); lp_inf.append(lp[j]-1)
        else: lp_inf.append(lp[j]); lp_sup.append(lp[j])
    var_sup = get_variance(lista_jogadores, lp_sup)
    var_inf = get_variance(lista_jogadores, lp_inf)
    minimo = min(var_ini, var_inf, var_sup)
    try:
        if minimo == var_inf:
            if lp[p_pos] - 2 >=0:
                return (lp_inf[p_pos], minimo)
            lp[p_pos] -= 2
            return get_best_peso(lista_jogadores, lp, p_pos, minimo)
        elif minimo == var_sup:
            lp[p_pos] += 2
            return get_best_peso(lista_jogadores, lp, p_pos, minimo)
        else:
            return (lp[p_pos], minimo)
    except RecursionError:
        return (lp[p_pos], minimo)

if __name__ == "__main__":
    dict_pesos = {}
    for lista in dict_players.values():
        tempo_i = time.time()
        pesos, variancia = get_pesos(lista)
        pesos = [round(i,2) for i in pesos]
        dict_pesos[lista[0].posicao] = pesos
        print(f'Os melhores pesos para a posicao {lista[0].posicao} é {pesos} com variancia de {variancia}')
        print(f'Para concluir a posicao {lista[0].posicao} durou: {time.time() - tempo_i}')
    
    print("|{:<3}|{:<6}|{:<6}|{:<6}|{:<6}|{:<6}|{:<6}|".format(
        'POS', 'VEL', 'FIN', 'PAS', 'DRI', 'DEF', 'FIS'
    )) 
    for pos in dict_pesos.keys():
        print("|{:<3}|{:<6}|{:<6}|{:<6}|{:<6}|{:<6}|{:<6}|".format(pos, *dict_pesos[pos])) 