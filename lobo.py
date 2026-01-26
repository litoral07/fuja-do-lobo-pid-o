import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) 
clock = pygame.time.Clock()
running = True
estado="menu"

quadrado = pygame.Surface([30, 30])
quadrado.fill((30, 30, 30))

x = 50       	# coordenada x do quadrado
velocidade = 10   # velocidade de movimentação do quadrado
y = 200

background = pygame.image.load("start.png").convert()
background = pygame.transform.scale(background, (1280, 720))

start_rect = pygame.Rect(520, 260, 240, 80)            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if start_rect.collidepoint(event.pos):
                 estado="jogo"

        if estado == "menu":
           screen.blit(background, (0, 0))

        elif estado == "jogo":
          screen.fill((255, 255, 255))
          screen.blit(quadrado, (x, y))
        pygame.display.flip()
    teclas = pygame.key.get_pressed() # Para capturar o pressionamento das teclas de forma contínua
    if teclas[pygame.K_LEFT]:   # tecla direcional esquerda está sendo pressionada?
      x = x - velocidade
    if teclas[pygame.K_RIGHT]:  # tecla direcional direita está sendo pressionada?
      x = x + velocidade
    if teclas[pygame.K_UP]:
      y = y - velocidade 
    if teclas[pygame.K_DOWN]:
       y = y + velocidade      
     
clock.tick(60)

pygame.quit()
