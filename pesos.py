from players import Player
from times import get_players
from threading import Thread
import time

running = True

i0 = 0; i1 = 0; i2 = 0; i3 = 0; i4 = 0; i5 = 1

tempo_inicial = time.time()

positions = {
    'CB' : [100000000000000,  [0,0,0,0,0,0]],
    'LB' : [100000000000000,  [0,0,0,0,0,0]],
    'CM' : [100000000000000,  [0,0,0,0,0,0]],
    'CDM' : [100000000000000, [0,0,0,0,0,0]],
    'CAM' : [100000000000000, [0,0,0,0,0,0]],
    'LM' : [100000000000000,  [0,0,0,0,0,0]],
    'LW' : [100000000000000,  [0,0,0,0,0,0]],
    'CF' : [100000000000000,  [0,0,0,0,0,0]],
    'ST' : [100000000000000,  [0,0,0,0,0,0]],
}


def print_pesos():
    while running:
        print('Tempo e pesos atuais', end=' ')
        print(abs(int(tempo_inicial - time.time())), i0, i1, i2, i3, i4, i5)
        a = i0*(10**5) + i1*(10**4) + i2*(10**3) + i3*(10*2) + i4*(10*1) + i5
        print(f'Operações {a} de 10^6 total de {(a/10**6)*100}%')
        for i in positions.keys():
            print(i, positions[i])
        time.sleep(600)
    
def get_overall(self, posicao):
        if posicao == 'CB': peso = positions['CB'][1]
        elif posicao in ('LB', 'RB', 'LWB', 'RWB'): peso = positions['LB'][1]
        elif posicao == 'CDM': peso = positions['CDM'][1]
        elif posicao == 'CM': peso = positions['CM'][1]
        elif posicao == 'CAM': peso = positions['CAM'][1]
        elif posicao in ('LM', 'RM'): peso = positions['LM'][1]
        elif posicao in ('LW', 'RW'): peso = positions['LW'][1]
        elif posicao == 'CF': peso = positions['CF'][1]
        elif posicao == 'ST': peso = positions['ST'][1]
        else: peso = (2,2,2,2,2,2)
        med = ((peso[0]*self.chute) + (peso[1]*self.passe) + (peso[2]*self.defesa) + 
                (peso[3]*self.fisico) + (peso[4]*self.velocidade) + (peso[5]*self.drible)) //12
        return int(med)

t = Thread(target=print_pesos)
t.start()
players_list = get_players()
players_list.sort(key=lambda x :x.overall, reverse=True)
players_list = players_list[:200]


while i0 < 11:
    while i1 < 11:
        while i2 < 11:
            while i3 < 11:
                while i4 < 11:
                    while i5 < 11:
                        dp = {}
                        for player in players_list:
                            if player.posicao in dp.keys():
                                dp[player.posicao] += abs(
                                    player.overall - ((
                                        (i0*player.velocidade) + (i1*player.chute) + (i2*player.passe)
                                        + (i3*player.drible ) + (i4*player.defesa) + (i5*player.fisico)
                                    )/(i0+i1+i2+i3+i4+i5))
                                )
                            else:
                                dp[player.posicao] = abs(
                                    player.overall - ((
                                        (i0*player.velocidade) + (i1*player.chute) + (i2*player.passe)
                                        + (i3*player.drible ) + (i4*player.defesa) + (i5*player.fisico)
                                    )/(i0+i1+i2+i3+i4+i5))
                                )
                        if dp['CB' ]< positions['CB'][0]  : positions['CB'] = [dp['CB' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['LB' ]< positions['LB'][0]  : positions['LB'] = [dp['LB' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['CM' ]< positions['CM'][0]  : positions['CM'] = [dp['CM' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['CDM']< positions['CDM'][0]  : positions['CDM'] = [dp['CDM' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['CAM']< positions['CAM'][0] : positions['CAM']= [dp['CAM'], [i0, i1, i2, i3, i4, i5]]
                        if dp['LM' ]< positions['LM'][0]  : positions['LM'] = [dp['LM' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['LW' ]< positions['LW'][0]  : positions['LW'] = [dp['LW' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['LW' ]< positions['LW'][0]  : positions['LW'] = [dp['LW' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['ST' ]< positions['ST'][0]  : positions['ST'] = [dp['ST' ], [i0, i1, i2, i3, i4, i5]]
                        if dp['CF' ]< positions['CF'][0]  : positions['CF'] = [dp['CF' ], [i0, i1, i2, i3, i4, i5]]
                        i5 += 1
                    i4 += 1
                    i5 = 0
                i3 += 1
                i4 = 0
            i2 += 1
            i3 = 0
        i1 += 1
        i2 = 0
    i0 += 1
    i1 = 0

running = False

with open('pesos.txt', 'w') as f:
    print(abs(int(tempo_inicial - time.time())), i1, i2, i3, i4, i5)
    print("|{:<3}|{:<7}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|".format(
        'Pos', 'Desvio', 'VEL', 'FIN', 'PAS', 'DRI', 'DEF', 'FIS'))
    for i in positions.keys():
        print("|{:<3}|{:<7}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|".format(
        i, round(positions[i][0],2), positions[i][1][0], positions[i][1][1], positions[i][1][2],
        positions[i][1][3], positions[i][1][4], positions[i][1][5]), file=f)
        print(i, positions[i])
    print("|{:<20}|{:<3}|{:<7}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|".format(
        'Nome', 'POS', 'Desvio' , 'OVO', 'OVG','VEL', 'FIN', 'PAS', 'DRI', 'DEF', 'FIS'), file=f)
    for player in players_list:
        ov = get_overall(player, player.posicao)
        print("|{:<20}|{:<3}|{:<7}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|{:<3}|".format(
        player.nome, player.posicao , ov - player.overall, player.overall,ov,
        player.velocidade, player.chute, player.passe, player.drible, player.defesa, player.drible), file=f)
        
    print(f'Finalizado em {(time.time() - tempo_inicial)//60} minutos')
    print(f'Finalizado em {(time.time() - tempo_inicial)//60} minutos', file=f)
