import pygame
from typing import Tuple

class Botao():
    def __init__(self,
                 janela:pygame.Surface, pos_x:int, pos_y:int,
                 size_x:int, size_y:int, image:str=None,
                 label:Tuple[str,int,Tuple[int,int,int],str]=(None, 0,(0,0,0),None), #texto, tamanho,rgb, alinhamento
                 color:Tuple[int,int,int]=None):
            self.janela = janela
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.size_x = size_x
            self.size_y = size_y
            self.image = image
            self.color = color
            if label is not None:
                label = list(label)
                if label[3] == 'center':
                    label[0] = "{:^{}}".format(str(label[0]), size_x//10)
                elif label[3] == 'right':
                    label[0] = "{:>{}}".format(str(label[0]), size_x//10)
                else:
                    label[0] = "{:<{}}".format(str(label[0]),size_x//10)
                    print(label[0])
            self.label = label
                    

    def draw(self):
        if self.color is not None:
            self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)
            pygame.draw.rect(self.janela, self.color, self.rect, border_radius=25)
        
        if self.image is not None:
            try:
                image = pygame.image.load("media\\images\\background\\514481.jpg").convert_alpha()
                image = pygame.transform.scale(image, (image.get_rect().width, image.get_rect().height))
                self.janela.blit(image, (self.pos_x, self.pos_y))
                pygame.display.update()
            except:
                print("Não foi possivel encontrar a imagem")
        
        if self.label[0] is not None:
            font = pygame.font.Font('media\\fonts\\font.ttf', self.label[1])
            text = font.render(str(self.label[0]), True, self.label[2])
            self.janela.blit(text, (self.pos_x, self.pos_y))
    
