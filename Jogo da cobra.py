# Importações de bibliotecas
import pygame # Adiciona o pygame para criar o jogo
import time # Adicionar um tempo no jogo
import random # Aleatorizar as comidas

# Inicializa os modulos do pygame
pygame.init()

# Cores do jogo (Fica do seu gosto)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Dimensões da tela
dis_width = 1000
dis_height = 600

# Criar a tela do jogo
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jogo da cobra by Rennanzin')

# Configurações do relogio para controlar a velocidade do jogo
clock = pygame.time.Clock()
snake_block = 10 # Tamanho do bloco da cobra
snake_speed = 15 # Velocidade da cobra

# Fontes
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para exibir a pontuação do jogador na tela
def Your_score(score):
    value = score_font.render("Seus Pontos: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Função para exivir mensagens na tela
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Função para exibir mensagens na tela
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Função principal do jogo
def gameLoop():
    game_over = False # Variável para controlar o fim do jogo
    game_close = False # Variável para controlar a tela de fim de jogo

    # Posições iniciais da cobra
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Variaveis de movimento da cobra
    x1_change = 0
    y1_change = 0

    # Lista para armazenar as posições da cobra
    snake_List = []
    Length_of_snake = 1 # Comprimento inicial da cobra

    # Gerar posição inicial aleatória para a comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over: # Loop principal do jogo

        while game_close == True: # Loop para a tela de fim de jogo
            dis.fill(blue)
            message("Você Perdeu! Pressione Q-Sair ou C-Jogar", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get(): # Captura os eventos do teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # Quando a tecla 'q' for pressionada o jogo vai fechar
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # Quando a telca 'c' for pressionada o jogo vai reiniciar
                        gameLoop()

        for event in pygame.event.get(): # Captura eventos do teclado e janela
            if event.type == pygame.QUIT: # Se o Jogador fechar a janela
                game_over = True
            if event.type == pygame.KEYDOWN: # Captura eventos de teclas pressionadas
                if event.key == pygame.K_LEFT: # Movimento para a esquerda com a seta pra direita
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_a: # Movimento para a esquerda com o a
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #Movimento para a direita com a seta pra direita
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_d: #Movimento para a direita com o d
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: # Movimento para cima com a seta pra cima
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_w: # Movimento para cima com o w
                    y1_change = -snake_block
                    x1_change = 0    
                elif event.key == pygame.K_DOWN: # Movimento para baixo com a seta pra baixo
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_s: # Movimento para baixo com o s
                    y1_change = snake_block
                    x1_change = 0
        # Verifica se a cobra bateu na parede
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) # Preenche o fundo com a cor azul (pode trocar a cor se quiser, só alterar no inicio do codigo a cor blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # Verifica se a cobra colidiu consigo mesma
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List) # Desenha o corpo da cobra
        Your_score(Length_of_snake - 1) # Atualiza a pontuação

        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed) # Controla a velocidade do jogo

    pygame.quit()
    quit() # Sair do jogo

# Iniciar o Jogo
gameLoop()
