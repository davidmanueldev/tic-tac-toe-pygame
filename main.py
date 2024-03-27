import pygame

pygame.init()

# Crear la ventana p
screen = pygame.display.set_mode((450,450))
# titulo para mi juego gozu
pygame.display.set_caption("3 en raya gaaa")
# Cargar recursos estaticos para nuestro juegozu
fondo = pygame.image.load('static/tictactoe_background.png')
circulo = pygame.image.load('static/circulo.png')
equis = pygame.image.load('static/x.png')
# Escalar las imagenes pq estan muy grandes
fondo = pygame.transform.scale(fondo, (450,450))
circulo = pygame.transform.scale(circulo, (125,125))
equis = pygame.transform.scale(equis, (125,125))
# Hacer una matriz bidimensional de tuplas donde estaran las coordenadas de los elementos(X y O y fondo)
# TODO: NO dejarlo para después
coordenadas = [[(40,0),(165,0),(290,0)],
               [(40,175),(165,175),(290,175)],
               [(40,300),(165,300),(290,300)]]

# Matriz para almacenar jugadas
tablero = [['','',''],
           ['','',''],
           ['','',''],]

# Almacenar el turno del jugador actual
turno = 'X' # La X arranca
game_over = False # Controlar el estado del juego, por defecto no ha terminado
reloj = pygame.time.Clock() # El clock para facilitar el establecer los frames del juego
# Verificar en cada iteración las interacciones con un game_loop
while not game_over:
  reloj.tick(30) # Para que se quede en 30FPS en todos los casos
  # Eventos dentro del juego
  for event in pygame.event.get(): #Captura los eventos de interación anterior
    if event.type == pygame.QUIT:
      game_over = True
  # Toca graficar los elementos
  screen.blit(fondo, (0,0)) # TODO: Quitar lo estático
  screen.blit(circulo, (40,50))
  screen.blit(equis, (165,165))
  #Actualizar la pantalla(screen)
  pygame.display.update()

  #! Warning: pygame.quit() dejar esto dentro del while, o sea que a la primera sale del juego :,v

pygame.quit()