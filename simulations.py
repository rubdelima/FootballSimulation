import random
from objects import Time
from itertools import combinations
import matplotlib.pyplot as plt

zonas = ['gol2', 'def1', 'meio1', 'meio', 'meio2', 'def2', 'gol1']

def vantagem(t1:int, t2:int) -> int:
    t3 = t1 + (t1-t2)*5
    if t3<0:
        t3 = t1
    return t3

def alg2(t1:Time, t2: Time, zone: int)->int:
    if zone == 3: z1 = t1.meio; z2 = t2.meio
    elif zone == 2: z1 = (t1.meio + t1.defesa)//2; z2 = (t2.meio + t2.ataque)//2
    elif zone == 1: z1 = t1.defesa ; z2 = t2.ataque
    elif zone == 4: z1 = (t1.meio + t1.ataque)//2; z2 =(t2.meio + t2.defesa)//2
    elif zone == 5: z1 = t1.ataque ; z2=t2.defesa
    meio = 2*(z1+z2) - (abs(z1-z2)*10)
    z1 =  vantagem(z1,z2)
    z2 =  vantagem(z2,z1)
    try:
        a = random.randint(0,(z1+z2+meio))
    except:
        print()
        a = random.randint(0,(z1+z2))
    if a < z1: return 1
    elif z1 <= a < z1+z2: return -1
    else: return 0
    
def simulation(time1: Time, time2:Time):
    time1_p = 0
    time2_p = 0
    zone = 3
    for i in range(90):
        zone += alg2(time1,time2, zone)
        if zonas[zone] == 'gol1':
            time1_p += 1
            zone = 3
        elif zonas[zone] == 'gol2':
            time2_p += 1
            zone = 3
    return (time1_p,time2_p)

def graph_simulation(time1: Time, time2: Time, rounds:int):
    valores_c = []
    for i in range(rounds):
        a, b = simulation(time1, time2)
        valores_c.append(a-b)
        ocorrencias = {}
    for c in valores_c:
        if c in ocorrencias:
            ocorrencias[c] += 1
        else:
            ocorrencias[c] = 1

    # Ordena o dicionário pelo valor de c em ordem decrescente
    ocorrencias = {k: v for k, v in sorted(ocorrencias.items(), key=lambda item: item[0], reverse=True)}

    # Cria o gráfico de barras
    valores = list(ocorrencias.values())
    nomes = list(map(str, ocorrencias.keys()))
    plt.bar(nomes, valores)
    plt.title('Gráfico de Barras')
    plt.xlabel('Valor de c')
    plt.ylabel('Ocorrências')
    plt.show()
 
def get_rounds(lista: list): # Lista de objetos da Classe Time
    a  = list(combinations(lista, 2))
    lista_b =[(i[1], i[0]) for i in a]
    a.extend(lista_b)
    return a


def simulate_league(lista: list, rounds:int=1):
    for i in range(rounds):
        liga = get_rounds(lista)
        for i, j in enumerate(liga):
            b = simulation(j[0], j[1])
            if b[0] > b[1]: j[0].vitorias +=1; j[1].derrotas +=1
            elif b[1] > b[0]: j[1].vitorias +=1; j[0].derrotas +=1
            else: j[0].empates +=1; j[1].empates +=1
            j[0].gols_pro += b[0];j[0].gols_contra += b[1]
            j[1].gols_pro += b[1];j[1].gols_contra += b[0]
        lista.sort(key=lambda t: (t.get_pontos(), t.gols_pro - t.gols_contra), reverse=True)
        [k.clear() for k in lista]
        lista[0].titulos_liga +=1

    lista.sort(key=lambda t: (t.titulos_liga, t.pontos_totais), reverse=True)
    for i in lista:
        print(f'{i.nome:<15} {i.titulos_liga:<5} {i.pontos_totais:<8}')
    
if __name__ == "__main__":
    pass
    