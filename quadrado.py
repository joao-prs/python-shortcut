import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado Colorido")

# Definir a cor do quadrado (vermelho no exemplo)
cor_quadrado = (255, 0, 0)

# Definir as coordenadas e dimensões do quadrado
x, y, lado = 100, 100, 200

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpar a tela
    janela.fill((255, 255, 255))

    # Desenhar o quadrado na tela
    pygame.draw.rect(janela, cor_quadrado, (x, y, lado, lado))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame (geralmente, isso não será alcançado no loop acima)
pygame.quit()