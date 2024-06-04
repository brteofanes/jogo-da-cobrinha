import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()



musica_de_fundo = pygame.mixer_music.load('Somewhere Fuse - French Fuse.mp3')
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.3)


barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

barulho_colisao.set_volume(5)


largura = 640 
altura = 480 
tela = pygame.display.set_mode((largura,altura))
imagem_fundo = pygame.image.load('jardim.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()
velocidade = 10
x_controle = velocidade
y_controle = 0


x_cobra = int(largura/2)
y_cobra = int(altura/2)


x_fruta = randint(40, 600)
y_fruta = randint(50, 430)


fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

pygame.display.set_caption('Jogo da cobra')

lista_cobra = []
tamanho_inicial = 15
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
#      XeY = x, y
#      XeY[0] = x
#      XeY[1] = y

        pygame.draw.rect(tela, (0,0,255), (XeY[0], XeY[1], 10, 10))
# 40, 40 tamanho da cabeça;
morreu = False

def reiniciar_jogo():
    global pontos, tamanho_inicial, x_cobra, y_cobra, lista_cobra, lista_de_posicoes, x_fruta, y_fruta, morreu
    pontos = 0
    tamanho_inicial = 15
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_de_posicoes = []
    x_fruta = randint(40, 600)
    y_fruta = randint(50, 430)
    morreu = False

while True:
    mensagem = f'P:{pontos}'
    texto_mesclada = fonte.render(mensagem, False, (255,255,255))

    relogio.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(imagem_fundo, (0,0))

    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            if x_controle == velocidade:
                pass
            else:
                x_controle = -velocidade
                y_controle = 0
        if event.key == K_RIGHT:
            if x_controle == -velocidade:
                pass
            else:
                x_controle = velocidade
                y_controle = 0
        if event.key == K_UP:
            if y_controle == velocidade:
                pass
            else:
                y_controle = -velocidade
                x_controle = 0
        if event.key == K_DOWN:
            if y_controle == -velocidade:
                pass
            else:
                y_controle = velocidade
                x_controle = 0
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle



    cobra = pygame.draw.rect(tela, (0,0,200), (x_cobra, y_cobra, 10, 10))


    fruta = pygame.draw.circle(tela, (200,0,0), (x_fruta, y_fruta), 10)
    

    if cobra.colliderect(fruta):

        x_fruta = randint(40, 600)
        y_fruta = randint(50, 430)   
        pontos = pontos + 1
        barulho_colisao.play()
        tamanho_inicial = tamanho_inicial + 1
    lista_de_posicoes = []
    lista_de_posicoes.append(x_cobra)
    lista_de_posicoes.append(y_cobra)
    
    lista_cobra.append(lista_de_posicoes)
    
    if lista_cobra.count(lista_de_posicoes) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        nota = 'Game Over! Pressione a tecla TAB para continuar'
        texto = fonte2.render(nota, True, (0,0,0))
        centralizado = texto.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_TAB:
                        reiniciar_jogo()
            centralizado.center = ((largura/2, altura/2))
            tela.blit(texto, centralizado)            
            pygame.display.update()



#   ATRAVESSANDO A TELA
    if x_cobra > largura:
        x_cobra = 0

    if x_cobra < 0:
        x_cobra = largura

    if y_cobra < 0:
        y_cobra = altura

    if y_cobra > altura:
        y_cobra = 0        


    if len(lista_cobra) > tamanho_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)


    tela.blit(texto_mesclada, (450, 40))


    pygame.display.update()