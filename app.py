import pygame
from botoes import Botao

def get_resolution()->tuple[tuple[int,int],str]: # Tupla da resolução e tupla do modo de janela
    # Inicialize o Pygame
    pygame.init()
    # Dimensões da janela
    largura = 800
    altura = 450
    janela = pygame.display.set_mode((largura, altura))

    # Background e Propriedades da tela
    background = pygame.image.load("media\\images\\background\\size_resolution.png").convert_alpha()
    background = pygame.transform.scale(background, (largura, altura))
    pygame.display.set_caption('BrasfootV2')
    try:
        icone = pygame.image.load("media\\images\\icons\\icon.png"
                                  ).convert_alpha()
        icone = pygame.transform.scale(icone, (16, 16))
    except Exception:
        print('Não foi possível carregar o ícone')
    pygame.display.set_icon(icone)
    sair = False
    lista_resolucoes = ["{:^{}}".format(i, 20) for i in ['720x1280', '1080x1920']]
    indice_resolucao = 0
    lista_modos = ["{:^{}}".format(i, 20) for i in ['Full Screen', 'Janela']]
    indice_modos = 0
    indice_variavel = 0
    res_color = (218,165,32)
    mod_color = (255, 255, 224)
    selecionar_resolucao = Botao(janela, 240, 220, 325,50,
                                 color=(218,165,32),
                                 label=(f'{lista_resolucoes[indice_resolucao]}',30,(0,0,0), 'center'),
    )
    selecionar_modo = Botao(janela, 240, 310, 325,50,
                                 color=(255, 255, 224),
                                 label=(f'{lista_modos[indice_modos]}',30,(0,0,0),'center'),
    )
    
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if indice_variavel%2:
                        indice_modos += 1
                    else:
                        indice_resolucao += 1

                if event.key == pygame.K_LEFT:
                    if indice_variavel%2:
                        indice_modos -= 1
                    else:
                        indice_resolucao -= 1
                        
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    indice_variavel = indice_variavel^1
                    res_color, mod_color= mod_color, res_color
                    

                if event.key in [pygame.K_KP_ENTER, pygame.K_BACKSPACE]:
                    resolucao = lista_resolucoes[indice_resolucao%len(lista_resolucoes)]
                    resolucao = resolucao.split('x')
                    return ((int(resolucao[0]), int(resolucao[1])), lista_modos[indice_modos%len(lista_modos)])
                
                
                if event.key == pygame.K_F4 and pygame.key.get_mods() & pygame.KMOD_ALT:
                    pygame.quit()
                    quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                if event.button == 1:
                    print("Botão do mouse pressionado na posição:", pygame.mouse.get_pos())
                if (272 < posicao[0] < 530) and (95 < posicao[1] < 146):
                    resolucao = lista_resolucoes[indice_resolucao%len(lista_resolucoes)]
                    resolucao = resolucao.split('x')
                    return ((int(resolucao[0]), int(resolucao[1])), lista_modos[indice_modos%len(lista_modos)])

            selecionar_resolucao.label[0] = lista_resolucoes[indice_resolucao%len(lista_resolucoes)]
            selecionar_resolucao.color = res_color
            
            selecionar_modo.label[0] = lista_modos[indice_modos%len(lista_modos)]
            selecionar_modo.color = mod_color

        #Atualizando ícones
        janela.blit(background, (0, 0))
        selecionar_resolucao.draw()
        selecionar_modo.draw()

        # Atualizando janela
        pygame.display.update()

if __name__ == "__main__":
    print(get_resolution())

