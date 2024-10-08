import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()

# Crear la ventana p
screen = pygame.display.set_mode((450,450))
# titulo para mi juego gozu
pygame.display.set_caption("3 en raya gaaa")
# Cargar recursos estaticos para nuestro juegozu
fondo = pygame.image.load('static/board.jpeg')
# fondo = pygame.image.load('static/board2.png') # Fondo alternativo
circulo = pygame.image.load('static/circulito.png')
equis = pygame.image.load('static/equis.png')
# Escalar las imagenes pq estan muy grandes
fondo = pygame.transform.scale(fondo, (450,450))
circulo = pygame.transform.scale(circulo, (110,110))
equis = pygame.transform.scale(equis, (110,110))
# Hacer una matriz bidimensional de tuplas donde estaran las coordenadas de los elementos(X y O y fondo)
# TODO: NO dejarlo para después
coordenadas = [[(42,40),(170,40),(300,40)],
               [(42,175),(170,175),(300,175)],
               [(42,300),(170,300),(300,300)]]

# Matriz para almacenar jugadas
tablero = [['','',''],
           ['','',''],
           ['','',''],]

# Almacenar el turno del jugador actual
turno = 'X' # La X arranca
game_over = False # Controlar el estado del juego, por defecto no ha terminado
reloj = pygame.time.Clock() # El clock para facilitar el establecer los frames del juego

def graficar_board():
  screen.blit(fondo, (0,0))
  for fila in range(3):
    for columna in range(3):
      # Logica de verificar elementos
      if tablero[fila][columna] == 'X':
        dibujar_x(fila,columna)
      elif tablero[fila][columna] == 'O':
        dibujar_circulo(fila, columna)

def dibujar_x(fila, columna):
  screen.blit(equis, coordenadas[fila][columna])

def dibujar_circulo(fila, columna):
  screen.blit(circulo, coordenadas[fila][columna])

def verificar_ganador():
  for i in range(3):
    if tablero[i][0] == tablero[i][1] == tablero[i][2] != '': # Verificar horizontalmente fila
      return True
    if tablero[0][i] == tablero[1][i] == tablero[2][i] != '': # Verificar verticalmente col
      return True
  if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
    return True
  if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
    return True
  return False

def verificar_empate():
  for fila in tablero:
    if '' in fila:
      return False
  return True

def mostrar_mensaje(mensaje):
  root = tk.Tk()
  root.withdraw()  # Ocultar la ventana principal de Tkinter
  messagebox.showinfo("Resultado del Juego", mensaje)
  root.destroy()

# Verificar en cada iteración las interacciones con un game_loop
while not game_over:
  reloj.tick(30) # Para que se quede en 30FPS en todos los casos
  # Eventos dentro del juego
  for event in pygame.event.get(): #Captura los eventos de interación anterior
    if event.type == pygame.QUIT:
      game_over = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouseX, mouseY = event.pos
      if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50) and (mouseY < 425):
        fila = (mouseY - 50) // 125
        columna = (mouseX - 40) // 125
        if tablero[fila][columna] == '':
          tablero[fila][columna] = turno
          fin_juego = verificar_ganador()
          if fin_juego:
            mostrar_mensaje(f"El jugador {turno} ha ganado!")
            game_over = True
          elif verificar_empate():
            mostrar_mensaje("¡Es un empate!")
            game_over = True
          else:
            turno = 'O' if turno == 'X' else 'X'
  #Actualizar la pantalla(screen)
  graficar_board()
  pygame.display.update()

pygame.quit()