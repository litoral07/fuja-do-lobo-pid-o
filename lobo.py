import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) 
clock = pygame.time.Clock()
running = True
estado="menu"

quadrado = pygame.Surface([30, 30])
quadrado.fill((30, 30, 30))
rect_quadrado = quadrado.get_rect()

x = 100
velocidade =5   
y = 100
rect_quadrado.topleft = (x, y)

background = pygame.image.load("start.png").convert()
background = pygame.transform.scale(background, (1280, 720))

sair_rect  = pygame.Rect(520, 310, 240, 60)
start_rect = pygame.Rect(520, 240, 240, 60)
fonte = pygame.font.SysFont(None, 60)

COR_BOTAO = (150, 0, 0)
COR_HOVER = (255, 0, 0)
COR_TEXTO = (255, 255, 255)

tamanho = 60

labirinto =[
   [1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,1],
   [1,1,1,1,1,1,1,1,1,1,1,1]
]
blocos = []        # representas as paredes
rects_blocos = []  # rects dos blocos
for  col_i, linha in enumerate(labirinto):
  for linha_i, celula in enumerate(linha) :
    if labirinto[col_i][linha_i] == 1:
      bloco = pygame.Surface([tamanho, tamanho])
      bloco.fill((30, 30, 30))
      rect = bloco.get_rect()
      rect.topleft = (col_i*tamanho, linha_i*tamanho,)
      blocos.append(bloco)
      rects_blocos.append(rect)
pontos = 0
inicio = pygame.time.get_ticks()
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
         texto = fonte.render("START", True, COR_TEXTO)
         texto_rect = texto.get_rect(center=start_rect.center)
         screen.blit(texto, texto_rect)
       else:
         pygame.draw.rect(screen, COR_BOTAO, start_rect, border_radius=12)
          
         texto = fonte.render("START", True, COR_TEXTO)
         texto_rect = texto.get_rect(center=start_rect.center)
         screen.blit(texto, texto_rect)
         
       if sair_rect.collidepoint(mouse_pos):
         pygame.draw.rect(screen, COR_HOVER, sair_rect, border_radius=12)
         texto_sair = fonte.render("SAIR", True, COR_TEXTO)
         screen.blit(texto_sair, texto_sair.get_rect(center=sair_rect.center))
       else:
         pygame.draw.rect(screen, COR_BOTAO, sair_rect, border_radius=12)

         texto_sair = fonte.render("SAIR", True, COR_TEXTO)
         screen.blit(texto_sair, texto_sair.get_rect(center=sair_rect.center))

    elif estado == "jogo":
       screen.fill((0, 150, 0))
       #screen.blit(quadrado, (x, y))
       screen.blit(quadrado, rect_quadrado.topleft)
       for i, blc in enumerate(blocos):
           screen.blit(blc, rects_blocos[i].topleft)
           # desenhar bloco na tela
           
       tempo_atual = pygame.time.get_ticks()
       segundos = (tempo_atual - inicio) // 16

       pontos = segundos
       texto_pontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
       screen.blit(texto_pontos, (20, 20))

             

    pygame.display.flip()
    teclas = pygame.key.get_pressed() 
    if estado == "jogo":
       if teclas[pygame.K_LEFT]:   
         #x = x - velocidade
         rect_quadrado.left = rect_quadrado.left - velocidade
         for rec in rects_blocos:
            if rect_quadrado.colliderect(rec):
              x2=rec.right
              x3=rect_quadrado.left
              if x3 < x2:
                rect_quadrado.left = rect_quadrado.left + (x2 - x3)
       if teclas[pygame.K_RIGHT]:  
         rect_quadrado.left = rect_quadrado.left + velocidade
         for rec in rects_blocos:
            if rect_quadrado.colliderect(rec):
              x2=rec.left
              x3=rect_quadrado.right
              if x3 > x2:
                rect_quadrado.right = rect_quadrado.right + (x2 - x3)
       if teclas[pygame.K_UP]:
         rect_quadrado.top = rect_quadrado.top - velocidade
         for rec in rects_blocos:
            if rect_quadrado.colliderect(rec):
              x2=rec.bottom
              x3=rect_quadrado.top
              if x3 < x2:
                rect_quadrado.top = rect_quadrado.top + (x2 - x3) 
       if teclas[pygame.K_DOWN]:
         rect_quadrado.top = rect_quadrado.top + velocidade
         for rec in rects_blocos:
            if rect_quadrado.colliderect(rec):
              x2=rec.top
              x3=rect_quadrado.bottom
              if x3 > x2:
                rect_quadrado.bottom = rect_quadrado.bottom + (x2 - x3)
           
     
    clock.tick(60)

pygame.quit()
