import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) 
clock = pygame.time.Clock()
running = True

background = pygame.image.load("start.png").convert()
background = pygame.transform.scale(background, (1280, 720))

start_rect = pygame.Rect(520, 360, 240, 80)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 👆 clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botão esquerdo
                if start_rect.collidepoint(event.pos):
                    print("START clicado!")
  
    screen.blit(background, (0, 0))

  

    pygame.display.flip()

clock.tick(60)

pygame.quit()
