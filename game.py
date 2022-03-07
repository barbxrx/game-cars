import pygame
from random import randint

pygame.init()

x = 150
y = 20
pos_x = 20
pos_y = 800
pos_y_a = 800
pos_y_c = 800
timer = 0
tempo_segundo = 0

velocidade = 10
velocidade_outros = 13

fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carrored.png')
carro_verde = pygame.image.load('carrogreen.png')
carro_azul = pygame.image.load('carroblue.png')
carro_amarelo = pygame.image.load('carroyellow.png')

font = pygame.font.SysFont('arial black',20)
texto = font.render("TEMPO: ",True,(255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = 65,50

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('cars')

janela_aberta = True

while janela_aberta:
  pygame.time.delay(50)

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        janela_aberta = False

  comandos = pygame.key.get_pressed()
  if comandos[pygame.K_RIGHT] and x <= 290:
        x+= velocidade 
  if comandos[pygame.K_LEFT] and x >= 30:
        x-= velocidade
  
  if (pos_y <= -80) and (pos_y_a <= -80) and (pos_y_c <= -80) :
      pos_y = randint(800,2000)
      pos_y_a = randint(800,2000)
      pos_y_c = randint(800,2000)
      
  if (timer <20):
    timer +=1
  else:
    tempo_segundo +=1
    texto = font.render("TEMPO: "+str(tempo_segundo), True,(255,255,255), (0,0,0))
    timer = 0

  pos_y -= velocidade_outros
  pos_y_a -= velocidade_outros +10
  pos_y_c -= velocidade_outros + 4
        
  janela.blit(fundo,(0,0))
  janela.blit(carro,(x,y))
  janela.blit(carro_verde,(pos_x,pos_y))
  janela.blit(carro_amarelo,(pos_x + 130, pos_y_a))
  janela.blit(carro_azul,(pos_x + 280, pos_y_c))
  janela.blit(texto, pos_texto)


  pygame.display.update()

pygame.quit()