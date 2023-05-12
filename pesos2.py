from times import get_players
from players import Player
import math
import xlsxwriter
from typing import List, Dict


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
                            if variacao < melhor_peso[0] and (i0 + i1 + i2 + i3 + i4 + i5)>0:
                                melhor_peso = [variacao, [i0, i1, i2, i3, i4, i5]]
                            
    print(f"Atualmente os melhores peso de {lista_jogadores[0].posicao} é {melhor_peso[1]} com uma variação de {melhor_peso[0]}")
    #condições de saída
    if dec == 1:
        return melhor_peso[1]
    else:
        return get_pesos(lista_jogadores,melhor_peso[1], dec-1)

def get_list_players_list(dicionario: Dict[str, List[Player]])->list[list[dict]]:
    lista = []
    for lista_j in dicionario.values():
        lista_aux = [
            {'Nome': i.nome, 'Chute': i.chute, 'Vel' : i.velocidade, 'Drible': i.drible,
                 'Passe': i.passe, 'Defesa': i.defesa, 'Fisico': i.fisico, 'Over': i.overall
        } for i in lista_j]
        lista.append(lista_aux)
    return lista

def gerar_planilha(dados:list, nome_arquivo:str, primeira_coluna:int=0):
    chaves = set().union(*dados)  # Obtém todas as chaves dos dicionários

    # Cria o arquivo XLSX
    workbook = xlsxwriter.Workbook(nome_arquivo)
    worksheet = workbook.add_worksheet()

    # Escreve o cabeçalho com as chaves
    col = primeira_coluna
    for chave in chaves:
        worksheet.write(0, col, chave)
        col += 1

    # Escreve os dados
    row = 1
    for dicionario in dados:
        col = primeira_coluna
        for chave in chaves:
            valor = dicionario.get(chave, '')  # Obtém o valor da chave ou uma string vazia se não existir
            worksheet.write(row, col, valor)
            col += 1

        row += 1

    workbook.close()

    print(f'Arquivo "{nome_arquivo}" criado com sucesso.')

def gerar_planila2(dados:list[list[dict]], nome_arquivo:str):
    chaves = dados[0][0].keys()
    # Cria o arquivo XLSX
    workbook = xlsxwriter.Workbook(nome_arquivo)
    worksheet = workbook.add_worksheet()
    
    for n, lista in enumerate(dados):
            # Escreve o cabeçalho com as chaves
        col = n*12
        for chave in chaves:
            worksheet.write(1, col, chave)
            col += 1

        # Escreve os dados
        row = 2
        for dicionario in lista:
            col = n*12
            for chave in chaves:
                valor = dicionario.get(chave, '')  # Obtém o valor da chave ou uma string vazia se não existir
                worksheet.write(row, col, valor)
                col += 1

            row += 1
    
    workbook.close()

    print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
    

if __name__ == '__main__':
    #*
    #for pos in dict_players.keys():
    #    bp = get_pesos(dict_players[pos], dec=1)
    #    print(f'A melhor combinação para a posição {pos} é {bp}')
    #    break
    #
    # Exemplo de uso
    listas = get_list_players_list(dict_players)
    gerar_planila2(listas, 'pesos2.xlsx')


