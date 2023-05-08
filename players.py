import csv

class Player:
    def __init__(self, lista):
        # Dados
        self.id = int(lista[0])
        self.nome = lista[1]
        self.idade = int(lista[3])
        self.foto = lista[6]
        self.nacionalidade = lista[7]
        self.posicao = lista[14]
        self.clube = lista[15]
        try:
            self.numero = int(lista[21])
        except:
            self.numero = 0
            #print(f'O player {self.nome} não tem número')
        self.pe_bom = lista[27]
        # Pontos
        self.velocidade = int(lista[33])
        self.chute = int(lista[34])
        self.passe = int(lista[35])
        self.drible = int(lista[36])
        self.defesa = int(lista[37])
        self.fisico = int(lista[38])
        self.gk_conducao = int(lista[68])
        self.gk_controle_mao = int(lista[69])
        self.gk_chute = int(lista[70])
        self.gk_pos = int(lista[71])
        self.gk_reflexo = int(lista[72])
        self.overall = int(lista[8])
        #self.overall = self.get_overall()
        self.gk_over = self.get_overall('GK')
        self.posicao_time = 'XX'
    
    def get_overall(self, posicao=None):
        if posicao == None: posicao = self.posicao
        if posicao == 'GK':
            med = (self.gk_conducao + self.gk_controle_mao +
                   self.gk_chute + self.gk_pos + self.gk_reflexo)// 5
        else:
            if posicao == 'CB': peso = (0.5, 2, 4.5, 3, 1.5, 0.5)
            elif posicao in ('LB', 'RB', 'LWB', 'RWB'): peso = (1,2.5, 3, 1.5, 2, 2)
            elif posicao == 'CDM': peso = (1.25, 2.5, 3.25, 2.5, 1.5, 1)
            elif posicao == 'CM': peso = (1.75, 3, 2.25, 2.25, 1.5, 1.25)
            elif posicao == 'CAM': peso = (2.5, 2.5, 1.5, 2, 1.5, 2)
            elif posicao in ('LM', 'RM'): peso = (1.75, 2.5, 1.25, 1.5, 2.5, 2.5)
            elif posicao in ('LW', 'RW'): peso = (2.5, 2, 0.5, 1.5, 2.75, 2.75)
            elif posicao == 'CF': peso = (3, 2.5, 1, 2, 1.5, 2)
            elif posicao == 'ST': peso = (4, 1.5, 0.5, 2.5, 2, 1.5)
            else: peso = (2,2,2,2,2,2)
            med = ((peso[0]*self.chute) + (peso[1]*self.passe) + (peso[2]*self.defesa) + 
                    (peso[3]*self.fisico) + (peso[4]*self.velocidade) + (peso[5]*self.drible)) //12
        return int(med)

    def get_player_info(self)->str:
        return "| {:<3} | {:<17} | {:<2} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} | {:<3} |".format(
            self.posicao_time, self.nome, self.overall, self.velocidade, self.chute, self.drible, 
            self.passe, self.defesa, self.fisico, self.gk_over, self.posicao)
        
      

with open ('players_fifa23.csv', 'r', newline='', 
           encoding='utf-8') as database:
    linhas = csv.reader(database)
    linhas = [linha for linha in linhas]
    args = linhas.pop(0)
    lista_players = [Player(i) for i in linhas]
   
        
        

    