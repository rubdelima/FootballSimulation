from players import Player
from times import Team, get_teams, get_players
import urllib.request
from pygoogle_image import image as pi

def baixar_imagem(url:str, pasta:str, nome:str)->None:
    caminho_arquivo = '".data/images/'+ pasta + '/' + nome + '.png'
    try:
        with urllib.request.urlopen(url) as response:
            with open(caminho_arquivo, 'wb') as arquivo:
                arquivo.write(response.read())
        print("Imagem baixada com sucesso!")
    except Exception as e:
        print("Falha ao baixar a imagem:", str(e))

def get_ligas(nome_liga:str=None)->dict:
    dict_leagues = {}
    times = get_teams()
    for team in times.values():
        if team.liga not in dict_leagues.keys():
            dict_leagues[team.liga] = [team]
        else:
            dict_leagues[team.liga].append(team)
    if nome_liga is None: return dict_leagues
    else:
        try:
            return dict_leagues[nome_liga]
        except KeyError:
            print(f'Não existe a liga {nome_liga} no dataset')

if __name__ == '__main__':
    premier_league = get_ligas('English Premier League (1)')
    for club in premier_league:
        print(f'Baixando imagens de {club.nome}', end=' ')
        pi.download(f"PL {club.nome} FC Logo", limit=1)