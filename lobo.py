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

sair_rect  = pygame.Rect(520, 310, 240, 60)
start_rect = pygame.Rect(520, 240, 240, 60)
fonte = pygame.font.SysFont(None, 60)

COR_BOTAO = (70, 130, 180)
COR_HOVER = (100, 160, 210)
COR_TEXTO = (255, 255, 255)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if start_rect.collidepoint(event.pos):
                 estado="jogo"
                if sair_rect.collidepoint(event.pos):
                 running = False
    if estado == "menu":
       screen.blit(background, (0, 0))
       mouse_pos = pygame.mouse.get_pos()

       if start_rect.collidepoint(mouse_pos):
         pygame.draw.rect(screen, COR_HOVER, start_rect, border_radius=12)
       else:
         pygame.draw.rect(screen, COR_BOTAO, start_rect, border_radius=12)

         texto = fonte.render("START", True, COR_TEXTO)
         texto_rect = texto.get_rect(center=start_rect.center)
         screen.blit(texto, texto_rect)
         
       if sair_rect.collidepoint(mouse_pos):
         pygame.draw.rect(screen, COR_HOVER, sair_rect, border_radius=12)
       else:
         pygame.draw.rect(screen, COR_BOTAO, sair_rect, border_radius=12)

         texto_sair = fonte.render("SAIR", True, COR_TEXTO)
         screen.blit(texto_sair, texto_sair.get_rect(center=sair_rect.center))

    elif estado == "jogo":
       screen.fill((0, 150, 0))
       screen.blit(quadrado, (x, y))
    pygame.display.flip()
    teclas = pygame.key.get_pressed() # Para capturar o pressionamento das teclas de forma contínua
    if estado == "jogo":
       if teclas[pygame.K_LEFT]:   # tecla direcional esquerda está sendo pressionada?
         x = x - velocidade
       if teclas[pygame.K_RIGHT]:  # tecla direcional direita está sendo pressionada?
         x = x + velocidade
       if teclas[pygame.K_UP]:
         y = y - velocidade 
       if teclas[pygame.K_DOWN]:
         y = y + velocidade 
       if x < 0:
         x = 0
       if x > 1280 - 30:
         x = 1280 - 30

       if y < 0:
         y = 0
       if y > 720 - 30:
         y = 720 - 30       
     
    clock.tick(60)

pygame.quit()
