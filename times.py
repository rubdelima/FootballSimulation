from players import Player
import csv

def get_players()->list[Player]:
    with open ('players_fifa23.csv', 'r', newline='', 
           encoding='utf-8') as database:
        linhas = csv.reader(database)
        linhas = [linha for linha in linhas]
        args = linhas.pop(0)
        lista_players = [Player(i) for i in linhas]
        return lista_players

def get_teams()->dict:
    with open ('teams_fifa23.csv', 'r', newline='', 
               encoding='utf-8') as database:
        linhas = csv.reader(database)
        linhas = [linha for linha in linhas]
        args = linhas.pop(0)
        '''
        print(f"|{'N':<2}| {'Item':<15} | {'Valor':<15}|")
        for i in range(len(args)):
            print(f"|{i:<2}| {args[i]:<15} | {linhas[0][i]:<15}|")
        '''
        lista_teams = {}
        for i in linhas:
            try:
                lista_teams[i[0]] = Team(i, dict_teams_playerlist)
            except:
                try:
                    print(f'Erro ao adicionar o time {i[1]}')
                except:
                    print("Erro cabuloso dms, slc")
                    
        return lista_teams

lista_players = get_players()
dict_teams_playerlist = {}

class Team():
    def __init__(self, args:list, d_players_l:dict):
        self.id = args[0]
        self.nome = args[1]
        self.liga = args[2]
        self.players = d_players_l[self.nome]
        self.players.sort(key=lambda x : x.overall, reverse=True)
    
    def get_team_info(self)->None:
        print("-"*80)
        epacos = " "*(39-(len(self.nome)//2))
        print("|{}{}{}|".format(epacos, self.nome, epacos))
        print("-"*80)
        print("| {:<3} | {:<17} | {:<2} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} |".format(
            'POS', 'Nome', 'OV', 'VEL', 'FIN', 'DRI', 'PAS', 'DEF', 'FIS', 'GK', 'RPS'))
        [print(i.get_player_info()) for i in self.players]
        print("-"*80)
        
    def get_best_formations(self)->list:
        dict_formations = {
            'GK':[0,[]],  'CB': [0, []],
            'LB':[0, []], 'RB' : [0, []], 'LWB':[0, []], 'RWB' : [0, []],
            'CDM' : [0, []], 'CM' : [0, []], 'CAM' : [0, []],
            'LM' : [0, []], 'RM' : [0, []], 'LW' : [0, []], 'RW' : [0, []],
            'ST': [0, []], 'CF' : [0, []]
        }
        for i in self.players:
            dict_formations[i.posicao][0]+=1
            dict_formations[i.posicao][1].append(i)
        
        self.team_dict = dict_formations
        
        time_titular = [dict_formations['GK'][1][0]]
        formacao = [0,0,0,0,0,0,0]
        # LAT, ZAG, VOL, MC-MEI, MEI-ME-MD-SA, PONTAS,  SA-ATA, 
        while sum(formacao) < 10:
            if self.players[i].posicao == "GK":
                pass
            else:
                do = False
                if self.players[i].posicao in ('LB', 'RB', 'LWB', 'RWB') and formacao[0]<3:
                    do = True; zone = 0
                elif self.players[i].posicao == 'CB' and formacao[1]<4:
                    do = True; zone = 1
                elif self.players[i].posicao in ('CM', 'CDM') and formacao[2]<3:
                    do = True; zone = 2
                elif self.players[i].posicao in ('CM', 'CAM') and formacao[3]<4:
                    do = True; zone = 3
                elif self.players[i].posicao in ('CAM', 'LM', 'RM', 'CF') and formacao[4]<4:
                    do = True ; zone = 4
                elif self.players[i].posicao in ('LM', 'RM', 'LW', 'RW') and formacao[5]<2:
                    do = True ; zone = 5
                elif self.players[i].posicao in ('ST', 'CF') and formacao[6]<2:
                    do = True ; zone = 6
                
                if do:
                    self.players[i].posicao_time = self.players[i].posicao
                    formacao[zone] +=1
                    time_titular.append(self.players[i])
        
        self.time_titular = time_titular

        return [sum(formacao[:2]), sum(formacao[2:5]), sum(formacao[5:])]
        

for i in lista_players:
    if i.clube not in dict_teams_playerlist.keys():
        dict_teams_playerlist[i.clube] = [i]
    else:
        dict_teams_playerlist[i.clube].append(i)



if __name__ == '__main__':
    '''
    print("| {:<3} | {:<17} | {:<2} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} |".format(
            'POS', 'Nome', 'OV', 'VEL', 'FIN', 'DRI', 'PAS', 'DEF', 'FIS', 'GK', 'RPS'))
    for i in range(20):
        print(lista_players[i].get_player_info())
    '''
    times = get_teams()
    times['5'].get_team_info()
